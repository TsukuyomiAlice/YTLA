import cv2
import numpy as np


def preprocess_image(img):
    """
    自适应阈值二值化

    作用:
        将输入图像转为灰度图，再用自适应阈值二值化转为黑白图
        （反色：文字/表格线为白色，背景为黑色）。
        自适应阈值能处理光照不均的情况。

    参数:
        img - OpenCV 图像对象 (numpy.ndarray)。

    返回:
        binary - 二值化图像（白色前景，黑色背景）。
    """

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    binary = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )

    return binary

def repair_lines(binary_img):
    # 定义垂直/水平结构元素
    kernel_v = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 15))
    kernel_h = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 1))
    # 垂直方向膨胀修复断裂线
    repaired_v = cv2.dilate(binary_img, kernel_v, iterations=1)
    # 水平方向膨胀
    repaired = cv2.dilate(repaired_v, kernel_h, iterations=1)
    return repaired

def find_table_contours(binary_img):
    # 查找轮廓
    contours, _ = cv2.findContours(
        binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    # 筛选符合表格特征的轮廓
    table_contours = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = w / float(h)
        area = cv2.contourArea(cnt)
        # 筛选条件：长宽比>1.5，面积>图像面积的5%
        if (aspect_ratio > 1.5 and
            area > binary_img.size * 0.05):
            table_contours.append(cnt)
    return table_contours

def detect_table_lines(img):
    # Canny边缘检测
    edges = cv2.Canny(img, 50, 150, apertureSize=3)
    # 霍夫直线检测
    lines = cv2.HoughLinesP(
        edges, 1, np.pi/180, threshold=100,
        minLineLength=img.shape[1]*0.3,
        maxLineGap=10
    )
    # 分离水平和垂直线
    h_lines = []
    v_lines = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        if abs(y2 - y1) < abs(x2 - x1)*0.2:  # 水平线
            h_lines.append((x1, y1, x2, y2))
        else:  # 垂直线
            v_lines.append((x1, y1, x2, y2))
    return h_lines, v_lines

def get_intersection_points(h_lines, v_lines):
    points = []
    for h_line in h_lines:
        for v_line in v_lines:
            # 计算两条直线的交点
            x1, y1, x2, y2 = h_line
            x3, y3, x4, y4 = v_line
            denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
            if denom == 0:  # 平行线
                continue
            x = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denom
            y = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denom
            points.append((int(x), int(y)))
    return points

def merge_cells(points):
    # 使用DBSCAN聚类处理相近点
    from sklearn.cluster import DBSCAN
    points_arr = np.array(points)
    clustering = DBSCAN(eps=10, min_samples=1).fit(points_arr)
    # 获取聚类中心作为单元格顶点
    unique_points = []
    for label in set(clustering.labels_):
        if label == -1:  # 噪声点
            continue
        cluster_points = points_arr[clustering.labels_ == label]
        center = np.mean(cluster_points, axis=0)
        unique_points.append((int(center[0]), int(center[1])))
    return unique_points


# ─── 共用输入/输出方法 ─────────────────────────────

def read_image(path):
    """
    读取图片文件

    作用:
        通过 OpenCV 从磁盘加载图片。

    参数:
        path - 图片文件路径。

    返回:
        img - OpenCV 图像对象 (numpy.ndarray)。

    说明:
        如果文件不存在或无法解码，抛出 FileNotFoundError。
    """

    img = cv2.imread(path)

    if img is None:
        raise FileNotFoundError(
            f"无法读取图片: {path}，请检查文件是否存在或路径是否正确"
        )

    return img


def save_image(img, path):
    """
    保存图片文件

    作用:
        通过 OpenCV 的 imwrite 将图像数据写入磁盘。

    参数:
        img  - 要保存的图像数据 (numpy.ndarray)。
        path - 保存路径，扩展名决定格式（.jpg、.png 等）。

    说明:
        cv2.imwrite 在保存彩色图时默认使用 BGR 通道顺序，
        imread 读取时也是 BGR，所以直接保存无需通道转换。
    """

    cv2.imwrite(path, img)


# ─── 可用操作列表（供用户参考）─────────────────────

AVAILABLE_OPS = {
    "preprocess": "自适应阈值二值化（灰度→黑白）",
    "repair":     "膨胀修复断裂表格线",
    "contour":    "查找并绘制表格轮廓",
    "lines":      "霍夫检测水平/垂直线并绘制",
    "intersect":  "计算并绘制行列线交点",
    "merge":      "DBSCAN 聚类合并相近交点",
}


# ─── 演示函数 ───────────────────────────────────────

def demo(input_path, operations, output_dir="."):
    """
    表格处理演示函数（按需选择操作）

    作用:
        读取图片后，仅执行 operations 列表中指定的操作，
        每步结果分别保存到输出目录。

    参数:
        input_path - 输入图片的路径。
        operations - 要执行的操作名称列表，例如:
                     ['preprocess', 'repair', 'contour']
                     可选值见 AVAILABLE_OPS 的 key。
        output_dir - 输出目录，默认为当前目录。

    示例:
        # 完整表格检测流程
        demo("table.jpg", ["preprocess", "repair", "contour"])

        # 只看交点和合并结果
        demo("table.jpg", ["preprocess", "intersect", "merge"])
    """

    # 读取原始图片
    img = read_image(input_path)

    # 当前处理的图像（在管线中逐步更新）
    current = img.copy()

    # ── 自动补全依赖：后续操作需要 preprocess 的结果 ──
    dependent_ops = {
        "repair", "contour",
        "lines", "intersect", "merge"
    }

    if (
        not any(op == "preprocess" for op in operations)
        and dependent_ops.intersection(operations)
    ):
        operations = ["preprocess"] + list(operations)
        print("  ℹ 检测到依赖 preprocess 的操作，已自动插入 'preprocess'")

    print(
        f"输入图片: {input_path} (尺寸: {img.shape[1]}x{img.shape[0]})"
    )
    print(f"执行操作: {operations}")
    print()

    for op in operations:

        if op == "preprocess":
            """
            preprocess 将彩色/灰度图通过自适应阈值二值化
            转为黑白图（反色：文字/表格线为白色，背景为黑色）。
            这样后续的形态学、轮廓检测都在二值图上进行。
            """

            current = preprocess_image(current)

            save_image(current, f"{output_dir}/preprocess.png")

            print(
                f"  ✓ preprocess → {output_dir}/preprocess.png"
            )

        elif op == "repair":
            """
            repair 通过水平和垂直方向的膨胀操作，
            填补表格线中的断裂/缺口，确保后续轮廓
            检测能识别出完整的表格外框。
            """

            current = repair_lines(current)

            save_image(current, f"{output_dir}/repair.png")

            print(
                f"  ✓ repair → {output_dir}/repair.png"
            )

        elif op == "contour":
            """
            contour 在二值图上查找轮廓，筛选出符合
            表格特征（长宽比>1.5、面积>5%）的轮廓，
            并绘制在原图副本上。
            """

            contours = find_table_contours(current)

            vis = img.copy()

            cv2.drawContours(vis, contours, -1, (0, 255, 0), 2)

            save_image(vis, f"{output_dir}/contour.png")

            print(
                f"  ✓ contour → {output_dir}/contour.png"
                f" (找到 {len(contours)} 个表格轮廓)"
            )

        elif op == "lines":
            """
            lines 先用 Canny 边缘检测，再用霍夫变换
            检测直线，按角度分离为水平线和垂直线，
            并绘制在原图副本上（水平线绿色，垂直线红色）。
            """

            h_lines, v_lines = detect_table_lines(current)

            vis = img.copy()

            for x1, y1, x2, y2 in h_lines:
                cv2.line(vis, (x1, y1), (x2, y2), (0, 255, 0), 2)

            for x1, y1, x2, y2 in v_lines:
                cv2.line(vis, (x1, y1), (x2, y2), (0, 0, 255), 2)

            save_image(vis, f"{output_dir}/lines.png")

            print(
                f"  ✓ lines → {output_dir}/lines.png"
                f" (水平线 {len(h_lines)} 条，垂直线 {len(v_lines)} 条)"
            )

        elif op == "intersect":
            """
            intersect 计算所有水平线与垂直线的交点，
            并用蓝色圆点标记在原图副本上。
            这些交点就是表格单元格的候选顶点。
            """

            h_lines, v_lines = detect_table_lines(current)

            points = get_intersection_points(h_lines, v_lines)

            vis = img.copy()

            for x, y in points:
                cv2.circle(vis, (x, y), 3, (255, 0, 0), -1)

            save_image(vis, f"{output_dir}/intersect.png")

            print(
                f"  ✓ intersect → {output_dir}/intersect.png"
                f" (交点 {len(points)} 个)"
            )

        elif op == "merge":
            """
            merge 使用 DBSCAN 聚类，将相邻的相近交点
            合并为一个中心点。eps=10 表示距离在 10 像素
            以内的点会被归为同一簇。
            合并后的点用黄色圆点标记在原图副本上。
            """

            h_lines, v_lines = detect_table_lines(current)

            points = get_intersection_points(h_lines, v_lines)

            unique_points = merge_cells(points)

            vis = img.copy()

            for x, y in unique_points:
                cv2.circle(vis, (x, y), 4, (0, 255, 255), -1)

            save_image(vis, f"{output_dir}/merge.png")

            print(
                f"  ✓ merge → {output_dir}/merge.png"
                f" (合并前 {len(points)} 个交点 → 合并后 {len(unique_points)} 个)"
            )

        else:
            print(
                f"  ✗ 未知操作: '{op}'，可用操作: "
                f"{', '.join(AVAILABLE_OPS.keys())}"
            )
            continue

        print()

    print("全部操作完成。")


if __name__ == "__main__":
    # ─────────────────────────────────────────────────
    # 在这里修改输入图片路径和要执行的操作
    # ─────────────────────────────────────────────────

    demo(
        input_path="./test1.jpeg",
        operations=[
            "preprocess",
            "repair",
            "contour",
            "lines",
            "intersect",
            "merge",
        ],
        output_dir="."
    )