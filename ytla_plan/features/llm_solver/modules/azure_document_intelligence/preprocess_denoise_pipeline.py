"""
预处理 + 二值图降噪管线

将 form_processing_demp 的自适应阈值二值化
与 image_processing_demo 的降噪方法串联使用。

流程:
  1. 读取原始图片
  2. 自适应阈值二值化 (THRESH_BINARY_INV)，得到白底黑字的二值图
  3. 对二值图应用选定的降噪方法，去除噪点
"""

import cv2
import numpy as np

# 从同目录导入两个模块
from form_processing_demp import (
    preprocess_image,
    read_image,
    save_image,
)
from image_processing_demo import (
    denoise,
    to_gray,
    resize,
)


# ─── 可用操作列表（供用户参考）─────────────────────

AVAILABLE_OPS = {
    # 预处理
    "preprocess": "自适应阈值二值化（文字/表格线为白色）",
    # 降噪方法（对二值图操作）
    "morph_open":  "开运算：去白底上的小黑点",
    "morph_close": "闭运算：去黑底上的小白点",
    "median":      "中值滤波：去孤立噪点",
    "area":        "连通域面积过滤：保线去点",
    "gaussian":    "高斯降噪（平滑二值图边缘）",
    "bilateral":   "双边滤波",
    "nlm":         "非局部均值降噪",
    "dct":         "DCT 频域降噪",
    # 后处理
    "gray":        "转为灰度图",
    "resize":      "缩放 50%",
}


def demo(input_path, operations, output_dir="."):
    """
    预处理 + 二值图降噪演示

    流程:
        preprocess 必须为第一个操作，后续降噪在其结果上执行。

    参数:
        input_path - 输入图片路径。
        operations - 操作列表，如 ['preprocess', 'area', 'morph_close']。
        output_dir - 输出目录。

    示例:
        # 二值化后用 area 去噪 + morph_close 补小白点
        demo("table.jpg", ["preprocess", "area", "morph_close"])

        # 对比多种降噪效果
        demo("table.jpg", ["preprocess", "area", "median", "morph_open"])
    """

    # ── 读取原始图片 ──
    img = read_image(input_path)

    print(f"输入图片: {input_path} (尺寸: {img.shape[1]}x{img.shape[0]})")
    print(f"执行操作: {operations}")
    print()

    # ── 强制 preprocess 为第一个操作 ──
    if not operations or operations[0] != "preprocess":
        operations = ["preprocess"] + list(operations)
        print("  ℹ 已自动在开头插入 'preprocess'")
        print()

    # 当前处理的图像
    current = img.copy()

    for op in operations:

        if op == "preprocess":
            """
            自适应阈值二值化（反色）。
            输出: 白色文字/表格线 + 黑色背景。
            """

            current = preprocess_image(current)

            save_image(current, f"{output_dir}/preprocess.png")
            print(f"  ✓ preprocess → {output_dir}/preprocess.png")

        elif op in (
            "gaussian", "nlm", "median",
            "morph_open", "morph_close", "bilateral",
            "area", "dct",
        ):
            """
            降噪类操作。
            对当前二值图应用降噪，默认 strength=5
            因为二值图只有 0/255 两个值，核不宜太大。
            """

            result = denoise(current, method=op, strength=5)

            # denoise 返回三通道时转回单通道二值图
            if len(result.shape) == 3:
                result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

            # 重新二值化，确保输出仍为纯 0/255 二值图
            _, result = cv2.threshold(
                result, 127, 255, cv2.THRESH_BINARY
            )

            current = result

            save_image(current, f"{output_dir}/{op}.png")
            print(f"  ✓ {op} → {output_dir}/{op}.png")

        elif op == "gray":

            gray = to_gray(current)

            save_image(gray, f"{output_dir}/gray.png")
            print(f"  ✓ gray → {output_dir}/gray.png")

        elif op == "resize":

            resized = resize(current, scale=0.5)

            save_image(resized, f"{output_dir}/resize_half.png")
            print(f"  ✓ resize → {output_dir}/resize_half.png")

        else:
            print(f"  ✗ 未知操作: '{op}'，已跳过")
            continue

        print()

    print("全部操作完成。")


def print_available_ops():
    """打印可用操作列表"""
    print("可用操作:")
    for key, desc in AVAILABLE_OPS.items():
        print(f"  {key:15s} - {desc}")


if __name__ == "__main__":
    # ============================================
    # 在这里修改 operations 列表
    # ============================================
    ops = [
        "preprocess",
        "area",
        "morph_close",
    ]

    print_available_ops()
    print(f"\n当前执行: {ops}\n")

    demo(
        input_path="./test1.jpeg",
        operations=ops,
        output_dir=".",
    )
