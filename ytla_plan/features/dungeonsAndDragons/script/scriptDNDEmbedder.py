# coding=utf-8

import os
import time
import hashlib
from typing import List, Dict, Optional, Tuple

# 导入自定义模块
from core.domain.area.frame.func import pdfProcessor, chromaDBConnector, loggerConfig


class DNDEmbedder:
    """
    D&D 内容嵌入器，用于将 D&D 玩家手册内容嵌入到 ChromaDB
    """

    def __init__(self, pdf_paths: Optional[List[str]] = None):
        """初始化 D&D 嵌入器"""
        self.info_logger = loggerConfig.db_info_logger
        self.error_logger = loggerConfig.db_error_logger
        self.pdf_processor = pdfProcessor.PDFProcessor()

        # 设置数据库和集合名称
        self.db_name = "dnd_5e_db"
        self.collection_name = "phb_content"

        # 设置PDF文件路径
        if pdf_paths:
            self.pdf_paths = pdf_paths
        else:
            # 默认只包含玩家手册
            self.pdf_paths = [
                r"D:\YTLA\ytla_plan\features\dungeonsAndDragons\dataset\DND_5E_玩家手册PHB-中译v1.72-配图v1.2.pdf"]

        # 检查所有PDF文件是否存在
        for pdf_path in self.pdf_paths:
            if not os.path.exists(pdf_path):
                self.error_logger.error(f"PDF文件不存在: {pdf_path}")
                raise FileNotFoundError(f"PDF文件不存在: {pdf_path}")

    def generate_id(self, content: str, page_num: int, source_file: str) -> str:
        """
        生成内容的唯一ID

        :param content: 文本内容
        :param page_num: 页码
        :param source_file: 源文件名称
        :return: 唯一ID字符串
        """
        # 组合源文件、页码和内容的哈希值作为ID，确保跨文件唯一性
        file_identifier = os.path.basename(source_file).split('.')[0][:10]  # 获取文件名前10个字符作为标识
        content_hash = hashlib.md5(content.encode('utf-8')).hexdigest()[:8]
        return f"dnd_{file_identifier}_page_{page_num}_{content_hash}"

    def chunk_text(self, text: str, chunk_size: int = 300, overlap: int = 50,
                  preserve_sentences: bool = True) -> List[str]:
        """
        将文本分割成适当大小的块，支持句子级别的分割

        :param text: 原始文本
        :param chunk_size: 块大小，默认减小为300字符以提高精细度
        :param overlap: 重叠大小，默认50字符
        :param preserve_sentences: 是否保留句子完整性
        :return: 文本块列表
        """
        if not preserve_sentences:
            # 基于字符计数的简单分割，但块大小减小
            chunks = []
            start = 0
            text_length = len(text)

            while start < text_length:
                end = min(start + chunk_size, text_length)
                chunk = text[start:end]
                chunks.append(chunk)

                # 如果未到文本末尾，则移动起始位置
                if end < text_length:
                    # 确保不会跳过内容，重叠部分至少为1
                    start += max(1, chunk_size - overlap)
                else:
                    break

            return chunks
        else:
            # 基于句子的分割（在下一个方法中实现）
            return self._chunk_by_sentences(text, chunk_size, overlap)

    def _chunk_by_sentences(self, text: str, chunk_size: int = 512, overlap: int = 20) -> List[str]:
        """
        基于句子边界分割文本，保留句子完整性

        :param text: 原始文本
        :param chunk_size: 目标块大小
        :param overlap: 重叠大小
        :return: 文本块列表
        """
        # 简单的句子分割，使用常见的中文和英文句子分隔符
        sentences = []
        current_sentence = ""
        separators = ['.', '。', '!', '！', '?', '？', ';', '；']

        for char in text:
            if char != '\n':
                current_sentence += char
                if char in separators:
                    # 确保句子有一定长度
                    if len(current_sentence.strip()) > 10:
                        sentences.append(current_sentence)
                        current_sentence = ""


        # 添加最后一个句子（如果有）
        if current_sentence.strip():
            sentences.append(current_sentence)

        # 现在根据句子构建块
        chunks = []
        current_chunk = ""

        for sentence in sentences:
            # 检查添加当前句子后是否超过块大小
            if len(current_chunk) + len(sentence) <= chunk_size:
                current_chunk += sentence
            else:
                # 如果当前块不为空，先保存它
                if current_chunk:
                    chunks.append(current_chunk)

                    # 添加重叠部分
                    # 找到当前块中最后几个句子作为重叠
                    overlap_text = ""
                    temp_sentences = []
                    temp_length = 0

                    # 从当前块的最后开始，向前寻找重叠部分
                    chunk_sentences = self._split_into_sentences(current_chunk)
                    for sent in reversed(chunk_sentences):
                        if temp_length + len(sent) <= overlap:
                            temp_sentences.insert(0, sent)
                            temp_length += len(sent)
                        else:
                            break

                    current_chunk = "".join(temp_sentences)

                # 添加当前句子
                if len(sentence) > chunk_size:
                    # 如果句子太长，需要进一步分割
                    sub_chunks = self.chunk_text(sentence, chunk_size, overlap, False)
                    chunks.extend(sub_chunks[:-1])
                    current_chunk = sub_chunks[-1] if sub_chunks else ""
                else:
                    current_chunk += sentence

        # 添加最后一个块
        if current_chunk:
            chunks.append(current_chunk)

        return chunks

    def _split_into_sentences(self, text: str) -> List[str]:
        """
        将文本分割成句子列表（辅助方法）

        :param text: 原始文本
        :return: 句子列表
        """
        sentences = []
        current_sentence = ""
        separators = ['.', '。', '!', '！', '?', '？', ';', '；']

        for char in text:
            current_sentence += char
            if char in separators:
                sentences.append(current_sentence)
                current_sentence = ""

        if current_sentence.strip():
            sentences.append(current_sentence)

        return sentences


    def extract_content_from_pdf(self) -> Dict[str, Dict[int, str]]:
        """
        从所有PDF中提取内容

        :return: 源文件到（页码到内容的映射）的映射
        """
        all_content = {}
        try:
            self.info_logger.info(f"开始从 {len(self.pdf_paths)} 个PDF文件中提取内容")
            total_start_time = time.time()

            for pdf_path in self.pdf_paths:
                file_name = os.path.basename(pdf_path)
                self.info_logger.info(f"开始处理文件: {file_name}")
                start_time = time.time()

                # 打开PDF文档
                if not self.pdf_processor.open_document(pdf_path):
                    raise Exception(f"打开PDF文档失败: {file_name}")

                # 获取文档元数据
                metadata = self.pdf_processor.get_document_metadata()
                self.info_logger.info(f"PDF文档信息: {metadata}")

                # 提取所有页面的文本
                file_content = self.pdf_processor.extract_text_from_all_pages()
                all_content[file_name] = file_content

                # 关闭文档
                self.pdf_processor.close_document()

                end_time = time.time()
                self.info_logger.info(f"成功提取 {file_name} 内容，耗时: {end_time - start_time:.2f}秒，共提取 {len(file_content)} 页内容")

            total_end_time = time.time()
            self.info_logger.info(f"所有PDF文件内容提取完成，总耗时: {total_end_time - total_start_time:.2f}秒")

            return all_content

        except Exception as e:
            self.error_logger.error(f"提取PDF内容失败: {str(e)}")
            # 确保文档被关闭
            self.pdf_processor.close_document()
            raise

    def prepare_embedding_data(self, content_dict: Dict[str, Dict[int, str]],
                               chunk_size: int = 300, overlap: int = 50,
                               preserve_sentences: bool = True) -> Tuple[List[str], List[Dict], List[str]]:
        """
        准备嵌入数据

        :param content_dict: 源文件到（页码到内容的映射）的映射
        :param chunk_size: 文本块大小
        :param overlap: 重叠大小
        :param preserve_sentences: 是否保留句子完整性
        :return: (文档列表, 元数据列表, ID列表)
        """
        documents = []
        metadatas = []
        ids = []

        try:
            self.info_logger.info("开始准备嵌入数据")

            for file_name, page_dict in content_dict.items():
                for page_num, text in page_dict.items():
                    # 过滤空白页面
                    if not text.strip():
                        continue

                    # 将页面文本分割成块
                    chunks = self.chunk_text(text, chunk_size, overlap, preserve_sentences)

                    # 提取页面的标题或章节信息
                    page_title = self._extract_page_title(text)

                    # 获取段落信息
                    paragraphs = self._split_into_paragraphs(text)
                    total_paragraphs = len(paragraphs)

                    # 为每个块确定其在页面中的位置和上下文
                    for chunk_idx, chunk in enumerate(chunks):
                        # 生成唯一ID
                        chunk_id = self.generate_id(chunk, page_num, file_name)

                        # 确定块在页面中的位置百分比
                        chunk_start_pos = text.find(chunk)
                        chunk_end_pos = chunk_start_pos + len(chunk)
                        page_length = len(text)
                        position_percent = (chunk_start_pos / page_length) * 100 if page_length > 0 else 0

                        # 确定块包含哪些段落
                        paragraph_indices = []
                        for i, para in enumerate(paragraphs):
                            para_start = text.find(para)
                            para_end = para_start + len(para)
                            if not (para_end < chunk_start_pos or para_start > chunk_end_pos):
                                paragraph_indices.append(i)

                        # 准备增强的元数据
                        metadata = {
                            "source": "DnD 5e 资料",
                            "source_file": file_name,
                            "page_number": page_num + 1,  # 页码从1开始显示
                            "chunk_index": chunk_idx,
                            "total_chunks": len(chunks),
                            "original_file": file_name,
                            "embedding_time": time.strftime("%Y-%m-%d %H:%M:%S"),
                            "position_percent": round(position_percent, 2),
                            "content_length": len(chunk),
                            "paragraph_indices": ",".join(map(str, paragraph_indices)),  # 将列表转换为逗号分隔的字符串
                            "total_paragraphs": total_paragraphs
                        }

                        # 如果有页面标题，添加到元数据
                        if page_title:
                            metadata["page_title"] = page_title

                        # 添加到列表
                        documents.append(chunk)
                        metadatas.append(metadata)
                        ids.append(chunk_id)

            self.info_logger.info(f"嵌入数据准备完成，共 {len(documents)} 个文本块")

            return documents, metadatas, ids

        except Exception as e:
            self.error_logger.error(f"准备嵌入数据失败: {str(e)}")
            raise

    def _extract_page_title(self, text: str) -> Optional[str]:
        """
        尝试从页面文本中提取标题

        :param text: 页面文本
        :return: 提取的标题（如果有）
        """
        try:
            # 简单的标题提取逻辑：查找文本的前几行中的可能标题
            lines = text.split('\n')

            # 检查前3行，寻找可能的标题
            for i in range(min(3, len(lines))):
                line = lines[i].strip()
                if line and len(line) < 50 and ('\t' not in line):
                    # 标题通常较短且不包含制表符
                    # 检查是否有多个连续大写字母（可能是章节标题）
                    if sum(1 for c in line if c.isupper()) >= len(line) * 0.5:
                        return line

                    # 检查是否以数字或特殊字符开头（可能是列表项或章节号）
                    if line and (line[0].isdigit() or line[0] in ['•', '◆', '■', '□', '►']):
                        return line

            # 如果没有找到明显的标题，返回None
            return None
        except Exception:
            # 出错时返回None，不影响主流程
            return None

    def _split_into_paragraphs(self, text: str) -> List[str]:
        """
        将文本分割成段落

        :param text: 原始文本
        :return: 段落列表
        """
        # 简单的段落分割逻辑：基于空行
        paragraphs = []
        current_para = ""

        for line in text.split('\n'):
            line = line.strip()
            if line:
                current_para += line + "\n"
            else:
                if current_para.strip():
                    paragraphs.append(current_para.strip())
                    current_para = ""

        # 添加最后一个段落
        if current_para.strip():
            paragraphs.append(current_para.strip())

        return paragraphs


    def embed_into_chroma(self, documents: List[str], metadatas: List[Dict], ids: List[str]) -> None:
        """
        将数据嵌入到ChromaDB

        :param documents: 文档列表
        :param metadatas: 元数据列表
        :param ids: ID列表
        """
        try:
            self.info_logger.info(f"开始将内容嵌入到ChromaDB，数据库: {self.db_name}，集合: {self.collection_name}")
            start_time = time.time()

            # 使用chroma_insert函数插入数据
            chromaDBConnector.chroma_insert(
                db_name=self.db_name,
                collection_name=self.collection_name,
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )

            end_time = time.time()
            self.info_logger.info(f"内容嵌入完成，耗时: {end_time - start_time:.2f}秒")

            # 验证嵌入结果
            count = chromaDBConnector.chroma_count(self.db_name, self.collection_name)
            self.info_logger.info(f"集合 {self.collection_name} 中当前共有 {count} 条记录")

        except Exception as e:
            self.error_logger.error(f"嵌入内容到ChromaDB失败: {str(e)}")
            raise

    def create_index_if_not_exists(self) -> None:
        """\创建索引（如果不存在）"""
        try:
            # 尝试获取集合，如果不存在则创建
            connector = chromaDBConnector.ChromaDBConnector(self.db_name)
            connector.get_or_create_collection(self.collection_name)
            self.info_logger.info(f"确保集合 {self.collection_name} 存在")
        except Exception as e:
            self.error_logger.error(f"创建或获取集合失败: {str(e)}")
            raise

    def clear_collection(self) -> None:
        """清空集合中的所有内容"""
        try:
            self.info_logger.info(f"准备清空集合 {self.collection_name} 中的所有内容")

            # 使用空的where条件删除所有内容
            chromaDBConnector.chroma_delete(
                db_name=self.db_name,
                collection_name=self.collection_name,
                where={}
            )

            self.info_logger.info(f"集合 {self.collection_name} 内容已清空")
        except Exception as e:
            self.error_logger.error(f"清空集合内容失败: {str(e)}")
            raise

    def run_full_embedding_process(self, clear_existing: bool = True,
                                   chunk_size: int = 300, overlap: int = 50,
                                   preserve_sentences: bool = True) -> None:
        """
        运行完整的嵌入流程

        :param clear_existing: 是否清除现有的集合内容
        :param chunk_size: 文本块大小
        :param overlap: 重叠大小
        :param preserve_sentences: 是否保留句子完整性
        """
        try:
            self.info_logger.info("开始运行完整的嵌入流程")

            # 确保集合存在（这是新增的关键代码）
            self.create_index_if_not_exists()

            # 如果需要清除现有内容
            if clear_existing:
                self.clear_collection()

            # 从PDF提取内容
            content_dict = self.extract_content_from_pdf()

            # 准备嵌入数据，传入分割参数
            documents, metadatas, ids = self.prepare_embedding_data(
                content_dict, chunk_size, overlap, preserve_sentences
            )

            # 嵌入到ChromaDB
            self.embed_into_chroma(documents, metadatas, ids)

            self.info_logger.info("完整的嵌入流程运行完成")

        except Exception as e:
            self.error_logger.error(f"运行完整嵌入流程失败: {str(e)}")
            raise


# 主函数，用于直接运行脚本
if __name__ == "__main__":
    try:
        # 添加所有需要嵌入的PDF文件路径
        pdf_files = [
            r"D:\YTLA\ytla_plan\features\dungeonsAndDragons\dataset\DND_5E_玩家手册PHB-中译v1.72-配图v1.2.pdf",
            # 添加第二本PDF文件路径
            r"D:\YTLA\ytla_plan\features\dungeonsAndDragons\dataset\DND_5E_城主指南CN.pdf",
            # 添加第三本PDF文件路径
            r"D:\YTLA\ytla_plan\features\dungeonsAndDragons\dataset\DND_5E_怪物图鉴CN.pdf"
        ]

        # 创建嵌入器实例，传入PDF文件列表
        embedder = DNDEmbedder(pdf_files)

        # 运行完整的嵌入流程，使用更精细的分割设置
        embedder.run_full_embedding_process(
            clear_existing=True,
            chunk_size=512,
            overlap=20,
            preserve_sentences=True
        )

    except Exception as e:
        print(f"嵌入过程中出错: {str(e)}")