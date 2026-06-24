import cv2
import numpy as np


def read_image(
        path
):
    """
    读取图片文件

    作用:
        通过 OpenCV 的 imread 函数从磁盘加载图片。

    参数:
        path - 图片文件的完整路径或相对路径。

    返回:
        img - OpenCV 图像对象（numpy.ndarray），形状为 (H, W, 3)，
              通道顺序为 BGR。

    说明:
        OpenCV 默认以 BGR 色彩空间读取图片，这与常见的 RGB 顺序不同。
        如果文件不存在、路径错误或文件格式不支持，imread 会返回 None。
        本函数通过检查返回值为 None 来捕获读取失败的情况，并抛出异常，
        避免后续处理在空数据上运行导致难以追踪的错误。
    """
    img = cv2.imread(path)

    if img is None:
        raise FileNotFoundError(
            f"无法读取图片: {path}"
        )

    return img


def save_image(
        img,
        path
):
    """
    保存图片文件

    作用:
        通过 OpenCV 的 imwrite 函数将图像数据写入磁盘文件。

    参数:
        img  - 要保存的图像数据（numpy.ndarray）。
        path - 保存路径。文件扩展名决定输出格式，
               如 .jpg、.png、.bmp 等。

    说明:
        imwrite 根据 path 的后缀名自动选择编码器。
        保存 JPG 时可通过 cv2.IMWRITE_JPEG_QUALITY 参数控制质量，
        保存 PNG 时可通过 cv2.IMWRITE_PNG_COMPRESSION 控制压缩级别。
    """
    cv2.imwrite(
        path,
        img
    )


def denoise(
        img,
        method="gaussian",
        strength=20
):
    """
    图片降噪处理

    作用:
        对输入图像进行降噪，去除图像中的随机噪声或高频噪点，
        使图像更平滑、清晰。

    参数:
        img      - 输入图像（numpy.ndarray）。
        method   - 降噪方法，可选:
            "gaussian"   - 高斯降噪：高斯核卷积，适合高斯噪声。
            "nlm"        - 非局部均值降噪：搜索相似块加权平均，
                           保留边缘效果好。
            "median"     - 中值滤波：取邻域中位数，**最适合去除
                           孤立小点（椒盐噪声）**。
            "morph_open" - 形态学开运算：先腐蚀后膨胀，去除白色
                           前景上的孤立小点。
            "morph_close"- 形态学闭运算：先膨胀后腐蚀，填充黑色
                           区域上的小空洞/小点。
            "bilateral"  - 双边滤波：同时考虑空间距离和像素值差异，
                           去噪同时保边。
            "area"       - **连通域面积过滤**：找出所有黑色连通区域，
                           去掉面积小于 strength 的孤立黑点。
                           最适合白底黑字/表格图去小黑点，
                           不会伤害细线条和文字笔画。
            "dct"        - **DCT 频域降噪**：将图像变换到频域
                           （离散余弦变换），去除高频噪声分量
                           再逆变换回空域。对文字图效果干净，
                           需要安装 opencv-contrib-python。
        strength - 对大多数方法为核大小/强度，默认 15。
                   对 "area" 表示**最小保留面积**（像素数），
                   建议从 5 开始试，如 strength=5 去极小黑点。

    返回:
        降噪处理后的图像（numpy.ndarray）。
    """

    if method == "gaussian":
        """
        高斯降噪的核心原理:

        用一个奇数尺寸的高斯核（权重符合二维高斯分布）在图像上滑动，
        对核覆盖区域的像素做加权平均，用平均值替换中心像素。
        由于噪声通常是高频信号（像素值突变），而高斯核相当于一个
        低通滤波器，能有效抑制高频噪声。

        cv2.GaussianBlur 的参数:
        - (ksize, ksize): 高斯核的宽度和高度，必须为正奇数。
        - sigmaX = 0: 让 OpenCV 根据核大小自动计算标准差。
        """

        return cv2.GaussianBlur(
            img,
            (
                strength if strength % 2 == 1 else strength + 1,
                strength if strength % 2 == 1 else strength + 1
            ),
            0
        )

    elif method == "nlm":
        """
        非局部均值降噪的核心原理:

        对于图像中某个像素点 p，不只看它周围的局部邻域，而是在
        整幅图像中搜索所有与 p 邻域相似的块（包括自身）。这些块
        的像素值通过权重（相似度）进行加权平均，从而得到 p 的
        新值。因为噪声是随机的，通过大量相似块的平均可以抵消噪声，
        同时非局部搜索能更好地保留重复纹理和边缘。

        cv2.fastNlMeansDenoisingColored 的参数:
        - None: 输出图像，None 表示由函数自动创建。
        - strength: 亮度分量（h）的降噪强度。
        - strength: 色彩分量（hColor）的降噪强度。
        - 7: templateWindowSize，用于比较的像素块大小。
        - 21: searchWindowSize，搜索窗口大小。
        """

        return cv2.fastNlMeansDenoisingColored(
            img,
            None,
            strength,
            strength,
            7,
            21
        )

    elif method == "median":
        """
        中值滤波的核心原理:

        将核覆盖区域内所有像素的灰度值排序，取中间值代替中心像素。
        对于椒盐噪声（孤立的小白点/小黑点），这些噪点的像素值
        在邻域中属于极端值，排序后必然落在两端，永远不会被选为
        中位数，因此能被完美去除，同时不会像均值滤波那样模糊边缘。

        cv2.medianBlur:
        - ksize: 核大小，必须为奇数。值越大，去噪越强，图像越平滑。
        """

        ksize = strength if strength % 2 == 1 else strength + 1

        return cv2.medianBlur(
            img,
            ksize
        )

    elif method == "morph_open":
        """
        形态学开运算的核心原理:

        先腐蚀（erode）再膨胀（dilate）。
        - 腐蚀：用核扫描图像，核覆盖区域全为 1 时中心才保留 1，
                否则变 0。效果是"收缩"白色区域，消除孤立的白点。
        - 膨胀：腐蚀后，核覆盖区域有至少一个 1 时中心变 1。
                效果是"恢复"白色区域到接近原来的大小。

        综合效果：去除白色前景上的孤立小点，同时保持较大物体
        的形状和大小基本不变。
        """

        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (strength, strength)
        )

        return cv2.morphologyEx(
            img,
            cv2.MORPH_OPEN,
            kernel
        )

    elif method == "morph_close":
        """
        形态学闭运算的核心原理:

        先膨胀（dilate）再腐蚀（erode），与开运算顺序相反。
        - 膨胀：白色区域扩张，填补黑色空洞/小点。
        - 腐蚀：膨胀后收缩回接近原来的大小。

        综合效果：填充黑色区域上的小空洞/小点，同时保持较大
        物体的形状基本不变。
        """

        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (strength, strength)
        )

        return cv2.morphologyEx(
            img,
            cv2.MORPH_CLOSE,
            kernel
        )

    elif method == "bilateral":
        """
        双边滤波的核心原理:

        在滤波时同时考虑两个权重:
        1. 空间距离权重（高斯分布）：离中心越近的像素权重越大。
        2. 像素值差异权重（高斯分布）：与中心像素值越接近，
           权重越大。

        因此在平滑平坦区域（像素值接近）时效果好，而在边缘处
        （像素值突变），像素值差异权重让边缘像素的贡献很小，
        从而保留边缘清晰度。

        cv2.bilateralFilter 的参数:
        - d:       邻域直径。
        - sigmaColor: 颜色空间的标准差，值越大表示更远的颜色
                      也会互相影响。
        - sigmaSpace: 空间距离的标准差，值越大表示更远的像素
                      也会互相影响。
        """

        return cv2.bilateralFilter(
            img,
            d=strength,
            sigmaColor=max(
                strength * 5,
                50
            ),
            sigmaSpace=max(
                strength * 5,
                50
            )
        )

    elif method == "area":
        """
        连通域面积过滤的核心原理:

        先将灰度图取反（黑变白、白变黑），然后用
        cv2.connectedComponentsWithStats 找出所有白色连通区域，
        计算每个区域的像素面积。只保留大于等于 strength 的
        面积较大的区域（对应文字和表格线），去掉小于 strength
        的孤立小点（对应噪点），最后再取反回来。
        
        ### Connected Component Area Filtering (method="area")
        What it does:

        It removes isolated black dots (noise) from a white-background image while preserving thin lines and small text characters.

        How it works — step by step:

        1. Invert the grayscale image ( 255 - gray ). Black text/table lines become white, white background becomes black. Noise dots also become white.
        2. Find all connected components using cv2.connectedComponentsWithStats(..., connectivity=8) . Each white blob (a character, a table line segment, or a noise dot) is assigned a unique label. 8-connectivity means pixels are considered connected if they touch at any of their 8 neighbors (including diagonals).
        3. Calculate the area (in pixels) of each component via stats[i, CC_STAT_AREA] .
        4. Filter by area threshold ( strength parameter). Components with area ≥ strength are kept (they are real content — text, table lines). Components with area < strength are discarded (they are noise).
        5. Invert back to restore the original black-on-white appearance.

        cv2.connectedComponentsWithStats 返回:
        - num_labels: 连通区域总数（含背景）。
        - labels: 每个像素所属的连通区域编号。
        - stats: 每个区域的外接矩形和面积信息，
                 stats[i, CC_STAT_AREA] 为区域面积。
        """

        if len(
                img.shape
        ) == 3:
            gray = cv2.cvtColor(
                img,
                cv2.COLOR_BGR2GRAY
            )
        else:
            gray = img

        # 取反：黑变白、白变黑
        inv = 255 - gray

        num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(
            inv,
            connectivity=8
        )

        # 创建纯黑背景，只保留面积 >= strength 的区域
        mask = np.zeros_like(
            inv
        )

        for i in range(
                1,
                num_labels
        ):
            if stats[
                i,
                cv2.CC_STAT_AREA
            ] >= strength:
                mask[
                    labels == i
                    ] = 255

        # 再取反，恢复黑白原色
        return 255 - mask

    elif method == "dct":
        """
        DCT 频域降噪的核心原理:

        1. 将图像从空域（像素值）通过离散余弦变换转换到频域。
        2. 在频域中，图像细节和噪声对应高频分量，图像主体
           对应低频分量。
        3. DCT 降噪通过对高频系数做软阈值处理，抑制噪声分量。
        4. 再通过逆 DCT 变换回空域，得到干净图像。

        相比空域滤波（高斯、中值等），频域方法能更精确地
        区分"噪声"和"边缘"——因为边缘虽然也是高频，但幅度
        远大于噪声，阈值处理后边缘得以保留。

        cv2.xphoto.dctDenoising 的参数:
        - sigma: 噪声标准差估计值。值越大，去噪越强。
                 建议范围 5-30，默认 10。
        - psize: DCT 块大小，必须为偶数。默认 16。
                 块越小，去噪越精细但可能产生块效应；
                 块越大，频域分辨率越高但局部细节可能丢失。
        """

        if len(
            img.shape
        ) == 3:
            gray = cv2.cvtColor(
                img,
                cv2.COLOR_BGR2GRAY
            )
        else:
            gray = img

        # cv2.xphoto.dctDenoising(src, dst, sigma, psize)
        # 预分配输出数组，函数写入 dst 并返回 None
        dst = np.empty_like(
            gray
        )
        cv2.xphoto.dctDenoising(
            gray,
            dst,
            strength,
            16
        )
        return dst

    else:

        raise ValueError(
            f"不支持的降噪方法: {method}，"
            f"请使用 'gaussian'、'nlm'、'median'、"
            f"'morph_open'、'morph_close'、'bilateral'、"
            f"'area' 或 'dct'"
        )


def rotate(
        img,
        angle
):
    """
    旋转图片（任意角度，保持完整显示）

    作用:
        将图像绕其中心旋转指定的角度，并自动调整画布大小，
        确保旋转后的内容完全可见，不会被裁剪。

    参数:
        img   - 输入图像（numpy.ndarray）。
        angle - 旋转角度（度），正值为逆时针，负值为顺时针。

    返回:
        旋转后的图像（numpy.ndarray），尺寸已自动扩展。

    说明:
        旋转的核心步骤:
        1. 获取图像中心坐标 (w/2, h/2)，作为旋转的中心点。
        2. 调用 cv2.getRotationMatrix2D 生成 2x3 的仿射变换矩阵 M。
           该矩阵包含 cos/sin 旋转分量和中心平移分量。
        3. 从矩阵 M 中提取 cos 和 sin 的绝对值，计算旋转后图像
           的新边界尺寸:
           - 新宽度 = h * sin + w * cos
           - 新高度 = h * cos + w * sin
           这样可以保证旋转后的四个角都在画布内。
        4. 调整 M 中的平移分量 (M[0,2], M[1,2])，使旋转后的
           图像居中显示（因为旋转中心从旧中心移到了新画布的中心）。
        5. 用 cv2.warpAffine 执行实际仿射变换，使用三次插值
           (INTER_CUBIC) 保证质量，BORDER_REPLICATE 填充边缘。
    """

    # 1. 获取原始图像的高度和宽度（shape[:2] 前两个元素）
    h, w = img.shape[:2]

    # 2. 计算图像中心坐标
    center = (
        w / 2,
        h / 2
    )

    # 3. 生成旋转矩阵 M（2x3 仿射变换矩阵）
    #    M = [cos, -sin, tx]
    #        [sin,  cos, ty]
    #    其中 (tx, ty) 是平移量，保证旋转后图像居中
    M = cv2.getRotationMatrix2D(
        center,
        angle,
        1.0  # 缩放因子，1.0 表示旋转时不缩放
    )

    # 4. 提取旋转矩阵中的 cos 和 sin 值（取绝对值）
    #    因为角度可以是负的，绝对值保证新尺寸计算正确
    cos = abs(
        M[0, 0]
    )

    sin = abs(
        M[0, 1]
    )

    # 5. 计算旋转后图像的新边界尺寸
    #    将原始图像的四个角点分别旋转，取最远的 x、y 坐标作为新尺寸
    new_w = int(
        h * sin + w * cos
    )

    new_h = int(
        h * cos + w * sin
    )

    # 6. 调整平移量，使旋转后的图像在新画布中居中
    #    旧中心在旋转后偏移了，需要加回偏移量让它回到新画布中心
    M[0, 2] += (
            new_w / 2 - center[0]
    )

    M[1, 2] += (
            new_h / 2 - center[1]
    )

    # 7. 执行仿射变换，生成旋转后的图像
    #    INTER_CUBIC: 双三次插值，放大时质量较好
    #    BORDER_REPLICATE: 边缘像素复制填充，避免黑色边框
    return cv2.warpAffine(
        img,
        M,
        (new_w, new_h),
        flags=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_REPLICATE
    )


def to_gray(
        img
):
    """
    将图片转为灰度图

    作用:
        将彩色图像（3 通道 BGR）转换为单通道灰度图像。
        灰度图像只包含亮度信息，不含色彩，常用于简化后续处理
        （如边缘检测、OCR 识别等），也能减少数据量。

    参数:
        img - 输入彩色图像（numpy.ndarray），形状为 (H, W, 3)。

    返回:
        灰度图像（numpy.ndarray），形状为 (H, W)，数据类型 uint8，
        值域 [0, 255]，0 为纯黑，255 为纯白。

    说明:
        cv2.cvtColor 用于色彩空间转换。
        cv2.COLOR_BGR2GRAY 表示将 BGR 格式转换为灰度。
        转换公式为标准亮度公式:
            Gray = 0.299 * R + 0.587 * G + 0.114 * B
        人眼对绿色最敏感（权重 0.587），对蓝色最不敏感（权重 0.114），
        因此灰度转换时各通道的权重不同。
    """

    return cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )


def resize(
        img,
        scale=None,
        width=None,
        height=None
):
    """
    缩放图片

    作用:
        改变图像的尺寸，可以按比例缩放，也可以缩放到指定的宽高。

    参数:
        img    - 输入图像（numpy.ndarray）。
        scale  - 缩放比例。小于 1 缩小，大于 1 放大。
                 例如 0.5 表示宽高都缩小为原来的一半。
        width  - 目标宽度（像素）。需要与 height 同时指定。
        height - 目标高度（像素）。需要与 width 同时指定。

    返回:
        缩放后的图像（numpy.ndarray）。

    说明:
        - 两种用法二选一:
          1. 按比例: resize(img, scale=0.5)
          2. 按尺寸: resize(img, width=800, height=600)
          不能同时使用两种方式，否则会抛出异常。

        - cv2.resize 的 interpolation 参数决定了插值方式:
          INTER_NEAREST - 最近邻插值（速度最快，质量最差）
          INTER_LINEAR  - 双线性插值（默认，速度与质量的平衡）
          INTER_CUBIC   - 双三次插值（放大时质量好，速度稍慢）
          INTER_LANCZOS4 - Lanczos 插值（质量最高，速度最慢）

        - 本函数使用 INTER_LINEAR，适用于大多数场景。
    """

    if scale is not None:
        """
        按比例缩放:
        用原始宽高乘以缩放比例得到新尺寸。
        img.shape[1] 是宽度（列数），
        img.shape[0] 是高度（行数）。
        """

        new_w = int(
            img.shape[1] * scale
        )

        new_h = int(
            img.shape[0] * scale
        )

    elif width is not None and height is not None:
        """
        按指定尺寸缩放:
        直接将目标宽高赋给新尺寸。
        注意：这种方式可能会改变图像的宽高比，
        导致图像被拉伸或压缩。
        """

        new_w = width
        new_h = height

    else:

        raise ValueError(
            "请指定 scale（缩放比例）或 width + height（目标尺寸）"
        )

    return cv2.resize(
        img,
        (new_w, new_h),
        interpolation=cv2.INTER_LINEAR
    )


# 可用操作列表（供用户参考）
AVAILABLE_OPS = {
    # 降噪方法
    "gaussian": "高斯降噪",
    "nlm": "非局部均值降噪",
    "median": "中值滤波（去孤立小点）",
    "morph_open": "形态学开运算（去白色小点）",
    "morph_close": "形态学闭运算（去黑色小点）",
    "bilateral": "双边滤波",
    "area": "连通域面积过滤（保线去点）",
    "dct": "DCT 频域降噪",
    # 其他操作
    "rotate": "旋转 45 度",
    "gray": "转为灰度图",
    "resize": "缩放 50%",
}


def demo(
        input_path,
        operations,
        output_dir="."
):
    """
    演示函数（按需选择操作）

    作用:
        读取图片后，仅执行 operations 列表中指定的操作，
        每步结果分别保存到输出目录。

    参数:
        input_path - 输入图片的路径。
        operations - 要执行的操作名称列表，例如:
                     ['median', 'rotate', 'gray']
                     可选值见 AVAILABLE_OPS 的 key。
        output_dir - 输出目录，默认为当前目录。

    示例:
        # 只做中值滤波 + 灰度
        demo("input.jpg", ["median", "gray"])

        # 只做旋转 + 缩放
        demo("input.jpg", ["rotate", "resize"])

        # 做所有降噪方法对比
        demo("input.jpg", [
            "gaussian", "nlm", "median",
            "morph_open", "morph_close", "bilateral"
        ])
    """

    # 读取原始图片
    img = read_image(
        input_path
    )

    for op in operations:

        if op in (
                "gaussian", "nlm", "median",
                "morph_open", "morph_close", "bilateral",
                "area", "dct"
        ):
            # 降噪类操作
            result = denoise(
                img,
                method=op,
                strength=15
            )

            save_image(
                result,
                f"{output_dir}/{op}.jpg"
            )

            print(
                f"  ✓ {op} → {output_dir}/{op}.jpg"
            )

        elif op == "rotate":
            # 旋转 45 度（顺时针）
            result = rotate(
                img,
                -45
            )

            save_image(
                result,
                f"{output_dir}/rotate_45.jpg"
            )

            print(
                f"  ✓ rotate → {output_dir}/rotate_45.jpg"
            )

        elif op == "gray":
            # 转为灰度图
            result = to_gray(
                img
            )

            save_image(
                result,
                f"{output_dir}/gray.jpg"
            )

            print(
                f"  ✓ gray → {output_dir}/gray.jpg"
            )

        elif op == "resize":
            # 缩放为原始尺寸的 50%
            result = resize(
                img,
                scale=0.5
            )

            save_image(
                result,
                f"{output_dir}/resize_half.jpg"
            )

            print(
                f"  ✓ resize → {output_dir}/resize_half.jpg"
            )

        else:

            print(
                f"  ✗ 未知操作: {op}，已跳过"
            )

    print(
        "演示完成"
    )


def print_available_ops():
    print(
        "可用操作:"
    )

    for key, desc in AVAILABLE_OPS.items():
        print(
            f"  {key:15s} - {desc}"
        )


if __name__ == "__main__":
    # ============================================
    # 在这里修改 operations 列表来选择要执行的操作
    # ============================================
    ops = [
        "area",
    ]

    print_available_ops()

    print(
        f"\n当前执行: {ops}\n"
    )

    demo(
        input_path="./test2_a.jpg",
        operations=ops,
        output_dir="."
    )
