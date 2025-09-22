# coding=utf-8

"""
D&D 内容查询示例脚本

用于演示如何查询已嵌入到 ChromaDB 中的 D&D 玩家手册内容
"""

import time
from typing import Dict, Any, List, Set

# 导入自定义模块
from ytla_plan.core.frame.func import chromaDBConnector, loggerConfig


class DnDQueryTool:
    """D&D 内容查询工具类"""

    def __init__(self):
        """初始化查询工具"""
        # 设置日志记录器
        self.info_logger = loggerConfig.db_info_logger
        self.error_logger = loggerConfig.db_error_logger

        # 设置数据库和集合名称（与嵌入时使用的名称一致）
        self.db_name = "dnd_5e_db"
        self.collection_name = "phb_content"

        # 初始化时检查集合是否存在
        try:
            count = chromaDBConnector.chroma_count(self.db_name, self.collection_name)
            self.info_logger.info(f"集合 {self.collection_name} 中包含 {count} 条记录")
        except Exception as e:
            self.error_logger.error(f"无法访问集合: {str(e)}")
            raise

    def similarity_search(self, query_text: str, n_results: int = 5, distance_threshold: float = None) -> Dict[str, List]:
        """
        基于相似度进行搜索

        :param query_text: 搜索查询文本
        :param n_results: 返回的结果数量
        :param distance_threshold: 距离阈值，小于此值的结果才会返回（值越小相似度越高）
        :return: 搜索结果字典
        """
        try:
            self.info_logger.info(f"执行相似度搜索: '{query_text}'")
            start_time = time.time()

            # 使用 chroma_query 函数进行相似度搜索
            results = chromaDBConnector.chroma_query(
                db_name=self.db_name,
                collection_name=self.collection_name,
                query_texts=[query_text],  # 注意：这里需要传入列表形式的查询文本
                n_results=n_results,
                include=["metadatas", "documents", "distances"]
            )

            # 应用距离阈值过滤
            if distance_threshold is not None:
                filtered_ids = []
                filtered_metadatas = []
                filtered_documents = []
                filtered_distances = []

                for i, distance in enumerate(results["distances"][0]):
                    if distance < distance_threshold:
                        filtered_ids.append(results["ids"][0][i])
                        filtered_metadatas.append(results["metadatas"][0][i])
                        filtered_documents.append(results["documents"][0][i])
                        filtered_distances.append(distance)

                results = {
                    "ids": [filtered_ids],
                    "metadatas": [filtered_metadatas],
                    "documents": [filtered_documents],
                    "distances": [filtered_distances]
                }

            end_time = time.time()
            self.info_logger.info(f"搜索完成，耗时: {end_time - start_time:.4f}秒，返回 {len(results['ids'][0])} 条结果")

            return results
        except Exception as e:
            self.error_logger.error(f"相似度搜索失败: {str(e)}")
            raise

    def search_with_content_filter(self, query_text: str, content_keywords: List[str], n_results: int = 5) -> Dict[
        str, List]:
        """
        结合相似度搜索和内容关键词过滤

        :param query_text: 搜索查询文本
        :param content_keywords: 文档内容必须包含的关键词列表
        :param n_results: 返回的结果数量
        :return: 搜索结果字典
        """
        try:
            self.info_logger.info(f"执行带内容过滤的相似度搜索: '{query_text}'，关键词: {content_keywords}")

            # 构建内容过滤条件
            # 注意：ChromaDB的where_document目前只支持简单的contains操作
            # 这里我们先进行相似度搜索，然后在Python层面进行内容过滤
            results = self.similarity_search(query_text, n_results=n_results * 2)  # 获取更多结果用于过滤

            # 在Python层面进行内容关键词过滤
            filtered_ids = []
            filtered_metadatas = []
            filtered_documents = []
            filtered_distances = []

            for i, document in enumerate(results["documents"][0]):
                # 检查文档是否包含所有关键词
                contains_all_keywords = all(keyword.lower() in document.lower() for keyword in content_keywords)

                if contains_all_keywords:
                    filtered_ids.append(results["ids"][0][i])
                    filtered_metadatas.append(results["metadatas"][0][i])
                    filtered_documents.append(document)
                    if "distances" in results:
                        filtered_distances.append(results["distances"][0][i])

            filtered_results = {
                "ids": [filtered_ids],
                "metadatas": [filtered_metadatas],
                "documents": [filtered_documents]
            }

            if filtered_distances:
                filtered_results["distances"] = [filtered_distances]

            # 限制结果数量
            if len(filtered_ids) > n_results:
                for key in filtered_results:
                    filtered_results[key][0] = filtered_results[key][0][:n_results]

            self.info_logger.info(f"内容过滤搜索完成，返回 {len(filtered_results['ids'][0])} 条结果")
            return filtered_results
        except Exception as e:
            self.error_logger.error(f"内容过滤搜索失败: {str(e)}")
            raise

    def hybrid_search(self, query_text: str, metadata_filter: Dict[str, Any] = None,
                      content_keywords: List[str] = None, n_results: int = 5,
                      distance_threshold: float = None) -> Dict[str, List]:
        """
        混合搜索方法，结合相似度、元数据和内容过滤

        :param query_text: 搜索查询文本
        :param metadata_filter: 元数据过滤条件
        :param content_keywords: 文档内容必须包含的关键词列表
        :param n_results: 返回的结果数量
        :param distance_threshold: 距离阈值
        :return: 搜索结果字典
        """
        try:
            self.info_logger.info(f"执行混合搜索: '{query_text}'")

            # 第一步：基于相似度和元数据过滤进行搜索
            results = chromaDBConnector.chroma_query(
                db_name=self.db_name,
                collection_name=self.collection_name,
                query_texts=[query_text],
                n_results=n_results * 3,  # 获取更多结果用于后续过滤
                where=metadata_filter,
                include=["metadatas", "documents", "distances"]
            )

            # 第二步：应用距离阈值过滤
            filtered_ids = []
            filtered_metadatas = []
            filtered_documents = []
            filtered_distances = []

            for i, distance in enumerate(results["distances"][0]):
                # 检查距离阈值
                if distance_threshold is None or distance < distance_threshold:
                    document = results["documents"][0][i]
                    metadata = results["metadatas"][0][i]

                    # 第三步：应用内容关键词过滤
                    if content_keywords is None or \
                            all(keyword.lower() in document.lower() for keyword in content_keywords):
                        filtered_ids.append(results["ids"][0][i])
                        filtered_metadatas.append(metadata)
                        filtered_documents.append(document)
                        filtered_distances.append(distance)

            # 构建最终结果
            final_results = {
                "ids": [filtered_ids[:n_results]],
                "metadatas": [filtered_metadatas[:n_results]],
                "documents": [filtered_documents[:n_results]],
                "distances": [filtered_distances[:n_results]]
            }

            self.info_logger.info(f"混合搜索完成，返回 {len(final_results['ids'][0])} 条结果")
            return final_results
        except Exception as e:
            self.error_logger.error(f"混合搜索失败: {str(e)}")
            raise

    def search_by_metadata(self, metadata_filter: Dict[str, Any], n_results: int = 10) -> Dict[str, List]:
        """
        基于元数据进行筛选搜索

        :param metadata_filter: 元数据过滤条件
        :param n_results: 返回的结果数量
        :return: 搜索结果字典
        """
        try:
            self.info_logger.info(f"执行元数据搜索: {metadata_filter}")

            # 使用 chroma_query 函数，传入 where 参数进行元数据过滤
            results = chromaDBConnector.chroma_query(
                db_name=self.db_name,
                collection_name=self.collection_name,
                query_texts=[""],  # 空文本作为查询，主要依靠元数据过滤
                n_results=n_results,
                where=metadata_filter,
                include=["metadatas", "documents"]
            )

            return results
        except Exception as e:
            self.error_logger.error(f"元数据搜索失败: {str(e)}")
            raise

    def get_by_ids(self, ids: List[str]) -> Dict[str, List]:
        """
        根据 ID 获取特定记录

        :param ids: 文档 ID 列表
        :return: 查询结果字典
        """
        try:
            self.info_logger.info(f"根据ID获取记录，ID数量: {len(ids)}")

            # 使用 chroma_get 函数根据 ID 获取记录
            results = chromaDBConnector.chroma_get(
                db_name=self.db_name,
                collection_name=self.collection_name,
                ids=ids,
                include=["metadatas", "documents"]
            )

            return results
        except Exception as e:
            self.error_logger.error(f"根据ID获取记录失败: {str(e)}")
            raise

    def get_collection_stats(self) -> Dict[str, Any]:
        """
        获取集合统计信息

        :return: 包含统计信息的字典
        """
        try:
            # 获取文档数量
            count = chromaDBConnector.chroma_count(self.db_name, self.collection_name)

            # 获取集合中的所有文档ID（用于统计）
            all_docs = chromaDBConnector.chroma_get(
                db_name=self.db_name,
                collection_name=self.collection_name,
                include=["metadatas"],
                where={"source": "DnD 5e 玩家手册"}  # 过滤来源
            )

            # 计算页数分布
            page_count = {}
            if "metadatas" in all_docs:
                for metadata in all_docs["metadatas"]:
                    if "page_number" in metadata:
                        page_num = metadata["page_number"]
                        page_count[page_num] = page_count.get(page_num, 0) + 1

            stats = {
                "total_documents": count,
                "unique_pages": len(page_count),
                "pages_with_content": [page for page, count in page_count.items() if count > 0]
            }

            self.info_logger.info(f"集合统计信息: {stats}")
            return stats
        except Exception as e:
            self.error_logger.error(f"获取集合统计信息失败: {str(e)}")
            raise

    def pretty_print_results(self, results: Dict[str, List], query_text: str = None,
                             sort_by: str = "distance", deduplicate: bool = False) -> None:
        """
        美观打印搜索结果，支持排序和去重

        :param results: 搜索结果字典
        :param query_text: 原始查询文本（可选）
        :param sort_by: 排序方式，可选值："distance"（默认，按相似度）或 "page_number"（按页码）
        :param deduplicate: 是否去重，去除相似度过高的重复内容
        """
        if query_text:
            print(f"\n===== 搜索结果: '{query_text}' =====\n")

        if "ids" in results and results["ids"] and results["ids"][0]:
            # 准备结果列表以便排序和去重
            result_items = []
            for i in range(len(results["ids"][0])):
                doc_id = results["ids"][0][i]
                document = results["documents"][0][i]
                metadata = results["metadatas"][0][i]
                distance = results["distances"][0][i] if "distances" in results and results["distances"] else 0

                result_items.append({
                    "id": doc_id,
                    "document": document,
                    "metadata": metadata,
                    "distance": distance,
                    "index": i
                })

            # 排序结果
            if sort_by == "page_number":
                result_items.sort(key=lambda x: x["metadata"].get("page_number", float('inf')))
            else:  # 默认按距离排序（相似度）
                result_items.sort(key=lambda x: x["distance"])

            # 去重处理
            if deduplicate:
                unique_items = []
                seen_content = set()

                for item in result_items:
                    # 使用内容的前100个字符作为去重标识
                    content_signature = item["document"][:100].lower()

                    if content_signature not in seen_content:
                        seen_content.add(content_signature)
                        unique_items.append(item)

                result_items = unique_items

            # 打印结果
            for i, item in enumerate(result_items):
                print(f"结果 #{i + 1}:")
                print(f"ID: {item['id']}")
                print(f"页码: {item['metadata'].get('page_number', '未知')}")
                print(f"来源: {item['metadata'].get('source', '未知')}")
                print(
                    f"块索引: {item['metadata'].get('chunk_index', '未知')}/{item['metadata'].get('total_chunks', '未知')}")

                # 打印部分内容，避免输出过长
                content_preview = item['document']
                print(f"内容预览: {content_preview}")

                # 如果有距离信息（相似度），也打印出来
                if "distances" in results and results["distances"]:
                    # 计算相似度得分（距离越小，相似度越高）
                    similarity_score = max(0, min(1, 1 - item['distance']))
                    print(f"相似度: {similarity_score:.4f}")

                print("=" * 50)

    def search_by_page_range(self, min_page: int, max_page: int, n_results: int = 10) -> Dict[str, List]:
        """
        通过页码范围搜索内容

        :param min_page: 最小页码
        :param max_page: 最大页码
        :param n_results: 返回的结果数量
        :return: 搜索结果字典
        """
        try:
            self.info_logger.info(f"执行页码范围搜索: 页码 {min_page} 到 {max_page}")

            # 因为ChromaDB不支持在同一字段上同时使用多个操作符，我们需要先获取所有文档
            # 然后在Python层面进行筛选
            all_docs = chromaDBConnector.chroma_get(
                db_name=self.db_name,
                collection_name=self.collection_name,
                include=["metadatas", "documents"],
                where={"source": "DnD 5e 玩家手册"}  # 过滤来源
            )

            # 在Python中筛选页码范围
            filtered_ids = []
            filtered_metadatas = []
            filtered_documents = []

            if "ids" in all_docs and "metadatas" in all_docs and "documents" in all_docs:
                for i, metadata in enumerate(all_docs["metadatas"]):
                    page_num = metadata.get("page_number", 0)
                    if min_page <= page_num <= max_page:
                        filtered_ids.append(all_docs["ids"][i])
                        filtered_metadatas.append(metadata)
                        filtered_documents.append(all_docs["documents"][i])

            # 限制结果数量
            if len(filtered_ids) > n_results:
                filtered_ids = filtered_ids[:n_results]
                filtered_metadatas = filtered_metadatas[:n_results]
                filtered_documents = filtered_documents[:n_results]

            # 构建结果字典，保持与chroma_query相同的格式
            results = {
                "ids": [filtered_ids],
                "metadatas": [filtered_metadatas],
                "documents": [filtered_documents]
            }

            self.info_logger.info(f"页码范围搜索完成，找到 {len(filtered_ids)} 条记录")
            return results
        except Exception as e:
            self.error_logger.error(f"页码范围搜索失败: {str(e)}")
            raise


# 演示用例
if __name__ == "__main__":
    try:
        # 创建查询工具实例
        query_tool = DnDQueryTool()

        print("\n===== D&D 玩家手册数据库查询演示 =====\n")

        # 1. 获取集合统计信息
        print("1. 获取集合统计信息:")
        stats = query_tool.get_collection_stats()
        print(f"   总文档数: {stats['total_documents']}")
        print(f"   包含内容的页数: {len(stats['pages_with_content'])}")

        # 2. 相似度搜索示例
        print("\n2. 相似度搜索示例 - '牧师':")
        results = query_tool.similarity_search("牧师", n_results=3)
        query_tool.pretty_print_results(results, "牧师")

        # 3. 另一个相似度搜索示例
        print("\n3. 相似度搜索示例 - '法术列表':")
        results = query_tool.similarity_search("法术", n_results=3)
        query_tool.pretty_print_results(results, "法术")

        # 4. 元数据过滤搜索示例 - 单一条件
        print("\n4. 元数据过滤搜索示例 - 特定页码:")
        # 使用单一条件来避免多操作符错误
        metadata_filter = {"page_number": 100}
        results = query_tool.search_by_metadata(metadata_filter, n_results=3)
        if "ids" in results and results["ids"] and results["ids"][0]:
            print(f"   找到 {len(results['ids'][0])} 条匹配记录")
            for i in range(len(results['ids'][0])):
                page_num = results['metadatas'][0][i].get('page_number', '未知')
                content_preview = results['documents'][0][i][:100] + "..." if len(results['documents'][0][i]) > 100 else \
                    results['documents'][0][i]
                print(f"   页码 {page_num}: {content_preview}")

        # 5. 页码范围搜索示例 - 使用新方法
        print("\n5. 页码范围搜索示例 - 第95-105页的内容:")
        results = query_tool.search_by_page_range(95, 105, n_results=3)
        if "ids" in results and results["ids"] and results["ids"][0]:
            print(f"   找到 {len(results['ids'][0])} 条匹配记录")
            for i in range(len(results['ids'][0])):
                page_num = results['metadatas'][0][i].get('page_number', '未知')
                content_preview = results['documents'][0][i][:100] + "..." if len(results['documents'][0][i]) > 100 else \
                    results['documents'][0][i]
                print(f"   页码 {page_num}: {content_preview}")

        # 6. 使用距离阈值的相似度搜索
        print("\n6. 使用距离阈值的相似度搜索示例 - '战士职业'（仅保留高相似度结果）:")
        results = query_tool.similarity_search("战士", n_results=5, distance_threshold=0.5)
        query_tool.pretty_print_results(results, "战士")

        # 7. 带内容过滤的搜索
        print("\n7. 带内容过滤的搜索示例 - '法师' 包含关键词 '法术':")
        results = query_tool.search_with_content_filter("法师", ["法术"], n_results=3)
        query_tool.pretty_print_results(results, "法师")

        # 8. 混合搜索示例 - 查找第100页附近与'战斗'相关的内容
        print("\n8. 混合搜索示例 - 第100页附近与'战斗'相关的内容:")
        metadata_filter = {"source": "DnD 5e 玩家手册"}
        results = query_tool.hybrid_search(
            "战斗",
            metadata_filter=metadata_filter,
            content_keywords=["战斗"],
            n_results=3,
            distance_threshold=0.6
        )
        query_tool.pretty_print_results(results, "战斗", sort_by="page_number")

        # 9. 搜索结果去重示例
        print("\n9. 搜索结果去重示例 - '角色创建'（去除相似内容）:")
        results = query_tool.similarity_search("角色创建", n_results=10)
        query_tool.pretty_print_results(results, "角色创建", deduplicate=True)

    except Exception as e:
        print(f"演示过程中出错: {str(e)}")