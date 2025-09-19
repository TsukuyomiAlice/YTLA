# coding=utf-8

import os
import io
from typing import List, Dict, Any, Optional, Tuple, Union
from PIL import Image

import fitz  # PyMuPDF
from ytla_plan.core.frame.func import loggerConfig


class PDFProcessor:
    """
    PDF处理工具类，基于PyMuPDF实现各种PDF操作功能

    功能包括：
    - PDF文件读取与保存
    - 文本提取
    - 图像提取
    - 页面操作（旋转、裁剪、缩放等）
    - 文档合并与分割
    - 添加文本水印
    - 文档元数据操作
    """

    def __init__(self):
        """初始化PDF处理器"""
        self.info_logger = loggerConfig.db_info_logger
        self.error_logger = loggerConfig.db_error_logger
        self.current_document = None
        self.file_path = None

    def open_document(self, file_path: str) -> bool:
        """
        打开PDF文档

        :param file_path: PDF文件路径
        :return: 是否成功打开
        """
        try:
            if not os.path.exists(file_path):
                self.error_logger.error(f"PDF文件不存在: {file_path}")
                return False

            self.current_document = fitz.open(file_path)
            self.file_path = file_path
            self.info_logger.info(f"成功打开PDF文档: {file_path}，共 {len(self.current_document)} 页")
            return True

        except Exception as e:
            self.error_logger.error(f"打开PDF文档失败: {str(e)}")
            return False

    def close_document(self) -> None:
        """\关闭当前打开的PDF文档"""
        if self.current_document is not None:
            try:
                self.current_document.close()
                self.info_logger.info(f"成功关闭PDF文档: {self.file_path}")
            except Exception as e:
                self.error_logger.error(f"关闭PDF文档失败: {str(e)}")
            finally:
                self.current_document = None
                self.file_path = None

    def get_document_metadata(self) -> Dict[str, Any]:
        """
        获取文档元数据

        :return: 包含文档元数据的字典
        """
        if self.current_document is None:
            self.error_logger.error("没有打开的PDF文档")
            return {}

        try:
            metadata = dict(self.current_document.metadata)
            # 添加一些额外信息
            metadata['page_count'] = len(self.current_document)
            metadata['file_path'] = self.file_path
            metadata['file_size'] = os.path.getsize(self.file_path) if self.file_path and os.path.exists(
                self.file_path) else 0

            self.info_logger.info(f"成功获取PDF文档元数据")
            return metadata

        except Exception as e:
            self.error_logger.error(f"获取PDF文档元数据失败: {str(e)}")
            return {}

    def extract_text_from_page(self, page_num: int) -> str:
        """
        从指定页码提取文本

        :param page_num: 页码（从0开始）
        :return: 提取的文本
        """
        if self.current_document is None:
            self.error_logger.error("没有打开的PDF文档")
            return ""

        if page_num < 0 or page_num >= len(self.current_document):
            self.error_logger.error(f"页码超出范围: {page_num}，文档共有 {len(self.current_document)} 页")
            return ""

        try:
            page = self.current_document[page_num]
            text = page.get_text()
            self.info_logger.info(f"成功从页码 {page_num + 1} 提取文本")
            return text

        except Exception as e:
            self.error_logger.error(f"从页码 {page_num} 提取文本失败: {str(e)}")
            return ""

    def extract_text_from_all_pages(self) -> Dict[int, str]:
        """
        从所有页面提取文本

        :return: 字典，键为页码，值为提取的文本
        """
        if self.current_document is None:
            self.error_logger.error("没有打开的PDF文档")
            return {}

        try:
            result = {}
            for i in range(len(self.current_document)):
                result[i] = self.extract_text_from_page(i)

            self.info_logger.info(f"成功从所有 {len(self.current_document)} 页提取文本")
            return result

        except Exception as e:
            self.error_logger.error(f"从所有页面提取文本失败: {str(e)}")
            return {}

    def extract_images_from_page(self, page_num: int, output_folder: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        从指定页码提取图像

        :param page_num: 页码（从0开始）
        :param output_folder: 图像保存文件夹路径，为None时不保存
        :return: 包含图像信息的列表
        """
        if self.current_document is None:
            self.error_logger.error("没有打开的PDF文档")
            return []

        if page_num < 0 or page_num >= len(self.current_document):
            self.error_logger.error(f"页码超出范围: {page_num}，文档共有 {len(self.current_document)} 页")
            return []

        try:
            page = self.current_document[page_num]
            image_list = []

            # 确保输出文件夹存在
            if output_folder and not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # 提取图像
            for img_index, img in enumerate(page.get_images(full=True)):
                xref = img[0]
                base_image = self.current_document.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]

                # 创建图像对象
                image = Image.open(io.BytesIO(image_bytes))

                # 准备图像信息
                image_info = {
                    "index": img_index,
                    "xref": xref,
                    "ext": image_ext,
                    "width": image.width,
                    "height": image.height,
                    "size": len(image_bytes)
                }

                # 保存图像
                if output_folder:
                    img_filename = f"page_{page_num + 1}_img_{img_index}.{image_ext}"
                    img_path = os.path.join(output_folder, img_filename)
                    image.save(img_path)
                    image_info["path"] = img_path

                image_list.append(image_info)

            self.info_logger.info(f"成功从页码 {page_num + 1} 提取 {len(image_list)} 张图像")
            return image_list

        except Exception as e:
            self.error_logger.error(f"从页码 {page_num} 提取图像失败: {str(e)}")
            return []

    def extract_images_from_all_pages(self, output_folder: Optional[str] = None) -> Dict[int, List[Dict[str, Any]]]:
        """
        从所有页面提取图像

        :param output_folder: 图像保存文件夹路径，为None时不保存
        :return: 字典，键为页码，值为该页提取的图像信息列表
        """
        if self.current_document is None:
            self.error_logger.error("没有打开的PDF文档")
            return {}

        try:
            result = {}
            total_images = 0

            # 确保输出文件夹存在并为每个页面创建子文件夹
            page_folders = {}
            if output_folder:
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)

                for i in range(len(self.current_document)):
                    page_folder = os.path.join(output_folder, f"page_{i + 1}")
                    os.makedirs(page_folder, exist_ok=True)
                    page_folders[i] = page_folder

            # 从每个页面提取图像
            for i in range(len(self.current_document)):
                page_folder = page_folders.get(i) if output_folder else None
                images = self.extract_images_from_page(i, page_folder)
                result[i] = images
                total_images += len(images)

            self.info_logger.info(f"成功从所有 {len(self.current_document)} 页提取 {total_images} 张图像")
            return result

        except Exception as e:
            self.error_logger.error(f"从所有页面提取图像失败: {str(e)}")
            return {}

    def save_document(self, output_path: str) -> bool:
        """
        保存当前文档到指定路径

        :param output_path: 输出文件路径
        :return: 是否保存成功
        """
        if self.current_document is None:
            self.error_logger.error("没有打开的PDF文档")
            return False

        try:
            # 确保输出目录存在
            output_dir = os.path.dirname(output_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)

            self.current_document.save(output_path)
            self.info_logger.info(f"成功保存PDF文档到: {output_path}")
            return True

        except Exception as e:
            self.error_logger.error(f"保存PDF文档失败: {str(e)}")
            return False

    def rotate_page(self, page_num: int, angle: int) -> bool:
        """
        旋转指定页码

        :param page_num: 页码（从0开始）
        :param angle: 旋转角度，只能是90的倍数
        :return: 是否旋转成功
        """
        if self.current_document is None:
            self.error_logger.error("没有打开的PDF文档")
            return False

        if page_num < 0 or page_num >= len(self.current_document):
            self.error_logger.error(f"页码超出范围: {page_num}，文档共有 {len(self.current_document)} 页")
            return False

        if angle % 90 != 0:
            self.error_logger.error(f"旋转角度必须是90的倍数: {angle}")
            return False

        try:
            page = self.current_document[page_num]
            page.set_rotation(angle)
            self.info_logger.info(f"成功旋转页码 {page_num + 1} 至 {angle} 度")
            return True

        except Exception as e:
            self.error_logger.error(f"旋转页码 {page_num} 失败: {str(e)}")
            return False

    def add_text_watermark(self, text: str, output_path: str,
                           fontsize: int = 50, opacity: float = 0.3,
                           angle: int = 45) -> bool:
        """
        为文档添加文本水印

        :param text: 水印文本
        :param output_path: 输出文件路径
        :param fontsize: 字体大小
        :param opacity: 不透明度（0-1之间）
        :param angle: 旋转角度
        :return: 是否添加成功
        """
        if self.current_document is None:
            self.error_logger.error("没有打开的PDF文档")
            return False

        try:
            # 创建新文档副本以添加水印
            new_doc = fitz.open()

            for page_num in range(len(self.current_document)):
                # 复制原始页面
                src_page = self.current_document[page_num]
                new_page = new_doc.new_page(width=src_page.rect.width, height=src_page.rect.height)

                # 插入原始页面内容
                new_page.show_pdf_page(new_page.rect, self.current_document, page_num)

                # 计算水印位置和大小
                page_rect = new_page.rect
                text_length = fitz.get_text_length(text, fontsize=fontsize)

                # 添加多个水印以覆盖整个页面
                x_step = text_length * 1.5
                y_step = fontsize * 3

                for x in range(-int(x_step / 2), int(page_rect.width + x_step / 2), int(x_step)):
                    for y in range(-int(y_step / 2), int(page_rect.height + y_step / 2), int(y_step)):
                        # 在当前位置添加水印
                        new_page.insert_text(
                            (x, y),
                            text,
                            fontsize=fontsize,
                            rotate=angle,
                            opacity=opacity,
                            color=(0, 0, 0)
                        )

            # 保存新文档
            new_doc.save(output_path)
            new_doc.close()

            self.info_logger.info(f"成功为PDF文档添加水印并保存到: {output_path}")
            return True

        except Exception as e:
            self.error_logger.error(f"为PDF文档添加水印失败: {str(e)}")
            return False

    def split_document(self, output_folder: str, pages_per_file: int = 1) -> List[str]:
        """
        分割文档为多个小文件

        :param output_folder: 输出文件夹路径
        :param pages_per_file: 每个输出文件包含的页数
        :return: 生成的文件路径列表
        """
        if self.current_document is None:
            self.error_logger.error("没有打开的PDF文档")
            return []

        if pages_per_file <= 0:
            self.error_logger.error(f"每页文件页数必须大于0: {pages_per_file}")
            return []

        try:
            # 确保输出文件夹存在
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            base_name = os.path.basename(self.file_path) if self.file_path else "split_document"
            base_name = os.path.splitext(base_name)[0]

            created_files = []
            total_pages = len(self.current_document)

            # 分割文档
            for i in range(0, total_pages, pages_per_file):
                # 计算当前分割的起止页码
                start_page = i
                end_page = min(i + pages_per_file, total_pages)

                # 创建新文档
                new_doc = fitz.open()

                # 添加指定范围的页面
                for page_num in range(start_page, end_page):
                    new_doc.insert_pdf(self.current_document, from_page=page_num, to_page=page_num)

                # 保存新文档
                output_filename = f"{base_name}_pages_{start_page + 1}-{end_page}.pdf"
                output_path = os.path.join(output_folder, output_filename)
                new_doc.save(output_path)
                new_doc.close()

                created_files.append(output_path)

            self.info_logger.info(f"成功将PDF文档分割为 {len(created_files)} 个文件")
            return created_files

        except Exception as e:
            self.error_logger.error(f"分割PDF文档失败: {str(e)}")
            return []


# 便捷函数：不需要实例化类即可使用的功能

def merge_pdfs(pdf_files: List[str], output_path: str) -> bool:
    """
    合并多个PDF文件

    :param pdf_files: 要合并的PDF文件路径列表
    :param output_path: 输出文件路径
    :return: 是否合并成功
    """
    try:
        info_logger = loggerConfig.db_info_logger
        error_logger = loggerConfig.db_error_logger

        # 检查输入文件是否存在
        for pdf_file in pdf_files:
            if not os.path.exists(pdf_file):
                error_logger.error(f"PDF文件不存在: {pdf_file}")
                return False

        # 确保输出目录存在
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 创建新文档并合并所有文件
        merged_doc = fitz.open()

        for pdf_file in pdf_files:
            with fitz.open(pdf_file) as src_doc:
                merged_doc.insert_pdf(src_doc)

        # 保存合并后的文档
        merged_doc.save(output_path)
        merged_doc.close()

        info_logger.info(f"成功合并 {len(pdf_files)} 个PDF文件并保存到: {output_path}")
        return True

    except Exception as e:
        loggerConfig.db_error_logger.error(f"合并PDF文件失败: {str(e)}")
        return False


def extract_text(pdf_path: str, page_num: Optional[int] = None) -> Union[str, Dict[int, str]]:
    """
    从PDF文件提取文本

    :param pdf_path: PDF文件路径
    :param page_num: 页码（从0开始），为None时提取所有页面
    :return: 提取的文本或文本字典
    """
    processor = PDFProcessor()
    try:
        if not processor.open_document(pdf_path):
            return "" if page_num is not None else {}

        if page_num is not None:
            return processor.extract_text_from_page(page_num)
        else:
            return processor.extract_text_from_all_pages()

    finally:
        processor.close_document()


def extract_images(pdf_path: str, page_num: Optional[int] = None, output_folder: Optional[str] = None) -> Union[
    List[Dict[str, Any]], Dict[int, List[Dict[str, Any]]]]:
    """
    从PDF文件提取图像

    :param pdf_path: PDF文件路径
    :param page_num: 页码（从0开始），为None时提取所有页面
    :param output_folder: 图像保存文件夹路径
    :return: 图像信息列表或图像信息字典
    """
    processor = PDFProcessor()
    try:
        if not processor.open_document(pdf_path):
            return [] if page_num is not None else {}

        if page_num is not None:
            return processor.extract_images_from_page(page_num, output_folder)
        else:
            return processor.extract_images_from_all_pages(output_folder)

    finally:
        processor.close_document()


def add_watermark_to_pdf(pdf_path: str, watermark_text: str, output_path: str,
                         fontsize: int = 50, opacity: float = 0.3, angle: int = 45) -> bool:
    """
    为PDF文件添加文本水印

    :param pdf_path: 源PDF文件路径
    :param watermark_text: 水印文本
    :param output_path: 输出文件路径
    :param fontsize: 字体大小
    :param opacity: 不透明度（0-1之间）
    :param angle: 旋转角度
    :return: 是否添加成功
    """
    processor = PDFProcessor()
    try:
        if not processor.open_document(pdf_path):
            return False

        return processor.add_text_watermark(watermark_text, output_path, fontsize, opacity, angle)

    finally:
        processor.close_document()


def split_pdf(pdf_path: str, output_folder: str, pages_per_file: int = 1) -> List[str]:
    """
    分割PDF文件

    :param pdf_path: 源PDF文件路径
    :param output_folder: 输出文件夹路径
    :param pages_per_file: 每个输出文件包含的页数
    :return: 生成的文件路径列表
    """
    processor = PDFProcessor()
    try:
        if not processor.open_document(pdf_path):
            return []

        return processor.split_document(output_folder, pages_per_file)

    finally:
        processor.close_document()