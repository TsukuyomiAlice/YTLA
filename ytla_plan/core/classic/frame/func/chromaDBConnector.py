# coding=utf-8

import os
from typing import List, Dict, Any, Optional

import chromadb
from chromadb.utils import embedding_functions  # 导入嵌入函数工具
from core.classic.frame.func import loggerConfig
from core.classic.frame.func import utilConfigs


class ChromaDBConnector:
    """
    ChromaDB 数据库连接器类

    提供与 ChromaDB 向量数据库交互的统一接口，包括：
    - 集合(collection)管理
    - 向量数据的增删改查
    - 相似度搜索
    - 日志记录与异常处理
    """

    _instances = {}
    _lock = False

    def __new__(cls, db_name: str):
        """单例模式，相同数据库名共享一个连接实例"""
        if db_name not in cls._instances:
            cls._instances[db_name] = super(ChromaDBConnector, cls).__new__(cls)
            cls._instances[db_name]._init_connection(db_name)
        return cls._instances[db_name]

    def _init_connection(self, db_name: str):
        """初始化 ChromaDB 连接"""
        self.db_name = db_name
        self.db_path = self._get_db_path(db_name)

        try:
            # 确保数据库目录存在
            db_dir = os.path.dirname(self.db_path)
            if not os.path.exists(db_dir):
                os.makedirs(db_dir)

            # 使用新版本的 ChromaDB 客户端构建方式
            import chromadb
            self.client = chromadb.PersistentClient(path=self.db_path)

            loggerConfig.db_info_logger.info(f"成功连接到 ChromaDB: {self.db_path}")

        except Exception as e:
            loggerConfig.db_error_logger.error(f"连接 ChromaDB 失败: {str(e)}")
            raise

    def _get_db_path(self, db_name: str) -> str:
        """
        获取 ChromaDB 数据库存储路径

        :param db_name: 数据库名称
        :return: 完整的数据库存储路径
        """
        slash = '/' if os.name == 'posix' else '\\'
        db_folder_path = utilConfigs.db_folder_path
        return f"{db_folder_path}{slash}chroma_{db_name}"

    def get_or_create_collection(self, collection_name: str, embedding_function=None) -> chromadb.Collection:
        """
        获取或创建一个集合

        :param collection_name: 集合名称
        :param embedding_function: 可选的嵌入函数
        :return: ChromaDB 集合对象
        """
        try:
            # 如果没有提供嵌入函数，使用默认的嵌入函数
            if embedding_function is None:
                # 使用 ChromaDB 内置的 all-MiniLM-L6-v2 嵌入函数
                embedding_function = embedding_functions.DefaultEmbeddingFunction()
                loggerConfig.db_info_logger.info("使用默认嵌入函数: all-MiniLM-L6-v2")

            collection = self.client.get_or_create_collection(
                name=collection_name,
                embedding_function=embedding_function
            )
            loggerConfig.db_info_logger.info(f"获取/创建集合成功: {collection_name}")
            return collection
        except Exception as e:
            loggerConfig.db_error_logger.error(f"获取/创建集合失败: {collection_name}, 错误: {str(e)}")
            raise

    def get_collection(self, collection_name: str) -> chromadb.Collection:
        """
        获取一个已存在的集合

        :param collection_name: 集合名称
        :return: ChromaDB 集合对象
        """
        try:
            collection = self.client.get_collection(name=collection_name)
            loggerConfig.db_info_logger.info(f"获取集合成功: {collection_name}")
            return collection
        except Exception as e:
            loggerConfig.db_error_logger.error(f"获取集合失败: {collection_name}, 错误: {str(e)}")
            raise

    def delete_collection(self, collection_name: str) -> None:
        """
        删除一个集合

        :param collection_name: 集合名称
        """
        try:
            self.client.delete_collection(name=collection_name)
            loggerConfig.db_info_logger.info(f"删除集合成功: {collection_name}")
        except Exception as e:
            loggerConfig.db_error_logger.error(f"删除集合失败: {collection_name}, 错误: {str(e)}")
            raise

    def list_collections(self) -> List[Dict[str, str]]:
        """
        列出所有集合

        :return: 集合列表，每个元素包含集合名称和ID
        """
        try:
            collections = self.client.list_collections()
            result = [{'name': col.name, 'id': col.id} for col in collections]
            loggerConfig.db_info_logger.info(f"列出集合成功，共 {len(result)} 个集合")
            return result
        except Exception as e:
            loggerConfig.db_error_logger.error(f"列出集合失败: {str(e)}")
            raise


def chroma_insert(
        db_name: str,
        collection_name: str,
        documents: Optional[List[str]] = None,
        metadatas: Optional[List[Dict]] = None,
        ids: List[str] = None,
        embeddings: Optional[List[List[float]]] = None
) -> None:
    """
    向 ChromaDB 集合中插入数据

    :param db_name: 数据库名称
    :param collection_name: 集合名称
    :param documents: 文档内容列表
    :param metadatas: 元数据列表
    :param ids: 文档ID列表，必需
    :param embeddings: 向量嵌入列表
    """
    try:
        connector = ChromaDBConnector(db_name)
        collection = connector.get_or_create_collection(collection_name)

        # 如果没有数据要插入，直接返回
        if not ids:
            loggerConfig.db_info_logger.info("没有数据需要插入")
            return

        # 确定批次大小（设置为小于最大限制的值）
        batch_size = 5000  # 小于5461的安全值
        total_docs = len(ids)

        # 如果数据量小于批次大小，直接插入
        if total_docs <= batch_size:
            collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids,
                embeddings=embeddings
            )
            loggerConfig.db_info_logger.info(f"向集合 {collection_name} 插入数据成功，共 {total_docs} 条")
        else:
            # 分批插入数据
            loggerConfig.db_info_logger.info(f"数据量较大，将分批次插入，共 {total_docs} 条数据，每批 {batch_size} 条")

            for i in range(0, total_docs, batch_size):
                end_idx = min(i + batch_size, total_docs)

                # 准备当前批次的数据
                batch_ids = ids[i:end_idx]
                batch_docs = documents[i:end_idx] if documents else None
                batch_metadatas = metadatas[i:end_idx] if metadatas else None
                batch_embeddings = embeddings[i:end_idx] if embeddings else None

                # 插入当前批次
                collection.add(
                    documents=batch_docs,
                    metadatas=batch_metadatas,
                    ids=batch_ids,
                    embeddings=batch_embeddings
                )

                loggerConfig.db_info_logger.info(
                    f"批次 {i // batch_size + 1} 插入成功，插入 {end_idx - i} 条数据，累计 {end_idx} 条")

            loggerConfig.db_info_logger.info(f"所有批次插入完成，共向集合 {collection_name} 插入 {total_docs} 条数据")

    except Exception as e:
        loggerConfig.db_error_logger.error(f"向集合 {collection_name} 插入数据失败: {str(e)}")
        raise


def chroma_query(
        db_name: str,
        collection_name: str,
        query_texts: Optional[List[str]] = None,
        query_embeddings: Optional[List[List[float]]] = None,
        n_results: int = 10,
        where: Optional[Dict[str, Any]] = None,
        where_document: Optional[Dict[str, Any]] = None,
        include: List[str] = ["metadatas", "documents", "distances"]
) -> Dict[str, List]:
    """
    在 ChromaDB 集合中进行相似度查询

    :param db_name: 数据库名称
    :param collection_name: 集合名称
    :param query_texts: 查询文本列表
    :param query_embeddings: 查询向量列表
    :param n_results: 返回结果数量
    :param where: 元数据过滤条件
    :param where_document: 文档内容过滤条件
    :param include: 结果包含的内容，可选值：metadatas, documents, distances, embeddings
    :return: 查询结果字典
    """
    try:
        connector = ChromaDBConnector(db_name)
        collection = connector.get_collection(collection_name)

        results = collection.query(
            query_texts=query_texts,
            query_embeddings=query_embeddings,
            n_results=n_results,
            where=where,
            where_document=where_document,
            include=include
        )

        loggerConfig.db_info_logger.info(f"在集合 {collection_name} 中查询成功，返回 {n_results} 条结果")
        return results

    except Exception as e:
        loggerConfig.db_error_logger.error(f"在集合 {collection_name} 中查询失败: {str(e)}")
        raise


def chroma_get(
        db_name: str,
        collection_name: str,
        ids: Optional[List[str]] = None,
        where: Optional[Dict[str, Any]] = None,
        where_document: Optional[Dict[str, Any]] = None,
        include: List[str] = ["metadatas", "documents"]
) -> Dict[str, List]:
    """
    从 ChromaDB 集合中获取数据

    :param db_name: 数据库名称
    :param collection_name: 集合名称
    :param ids: 文档ID列表
    :param where: 元数据过滤条件
    :param where_document: 文档内容过滤条件
    :param include: 结果包含的内容
    :return: 查询结果字典
    """
    try:
        connector = ChromaDBConnector(db_name)
        collection = connector.get_collection(collection_name)

        results = collection.get(
            ids=ids,
            where=where,
            where_document=where_document,
            include=include
        )

        loggerConfig.db_info_logger.info(f"从集合 {collection_name} 中获取数据成功")
        return results

    except Exception as e:
        loggerConfig.db_error_logger.error(f"从集合 {collection_name} 中获取数据失败: {str(e)}")
        raise


def chroma_update(
        db_name: str,
        collection_name: str,
        ids: List[str],
        documents: Optional[List[str]] = None,
        metadatas: Optional[List[Dict]] = None,
        embeddings: Optional[List[List[float]]] = None
) -> None:
    """
    更新 ChromaDB 集合中的数据

    :param db_name: 数据库名称
    :param collection_name: 集合名称
    :param ids: 文档ID列表，必需
    :param documents: 更新后的文档内容列表
    :param metadatas: 更新后的元数据列表
    :param embeddings: 更新后的向量嵌入列表
    """
    try:
        connector = ChromaDBConnector(db_name)
        collection = connector.get_collection(collection_name)

        collection.update(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings
        )

        loggerConfig.db_info_logger.info(f"更新集合 {collection_name} 中的数据成功，共 {len(ids)} 条")

    except Exception as e:
        loggerConfig.db_error_logger.error(f"更新集合 {collection_name} 中的数据失败: {str(e)}")
        raise


def chroma_delete(
        db_name: str,
        collection_name: str,
        ids: Optional[List[str]] = None,
        where: Optional[Dict[str, Any]] = None,
        where_document: Optional[Dict[str, Any]] = None
) -> None:
    """
    从 ChromaDB 集合中删除数据

    :param db_name: 数据库名称
    :param collection_name: 集合名称
    :param ids: 要删除的文档ID列表
    :param where: 元数据过滤条件
    :param where_document: 文档内容过滤条件
    """
    try:
        connector = ChromaDBConnector(db_name)
        collection = connector.get_collection(collection_name)

        # 检查是否提供了任何有效的过滤条件
        has_valid_filter = (ids is not None and len(ids) > 0) or \
                           (where is not None and where != {}) or \
                           (where_document is not None and where_document != {})

        # 如果没有提供有效的过滤条件，我们需要获取所有文档ID来删除
        if not has_valid_filter:
            # 获取集合中所有文档的ID
            try:
                # 尝试获取所有文档的ID，但不获取实际内容以提高效率
                all_docs = collection.get(include=[], limit=10000)  # 限制为10000条，可根据实际情况调整
                if "ids" in all_docs and len(all_docs["ids"]) > 0:
                    # 使用ID列表来删除所有文档
                    collection.delete(ids=all_docs["ids"])
                    loggerConfig.db_info_logger.info(
                        f"从集合 {collection_name} 中删除所有数据成功，共删除 {len(all_docs['ids'])} 条记录")
                    return
                else:
                    # 集合为空，不需要删除
                    loggerConfig.db_info_logger.info(f"集合 {collection_name} 为空，无需删除操作")
                    return
            except Exception as inner_e:
                # 如果获取所有ID失败，提供一个默认的安全where条件
                # 使用一个一定能匹配到所有文档的条件
                where = {"$exists": "source"}  # 假设所有文档都有source字段
                loggerConfig.db_info_logger.warning(f"获取所有文档ID失败，使用备用条件: {str(inner_e)}")

        # 创建参数字典
        delete_kwargs = {}
        if ids is not None and len(ids) > 0:
            delete_kwargs['ids'] = ids
        if where is not None and where != {}:
            delete_kwargs['where'] = where
        if where_document is not None and where_document != {}:
            delete_kwargs['where_document'] = where_document

        # 执行删除操作
        collection.delete(**delete_kwargs)

        loggerConfig.db_info_logger.info(f"从集合 {collection_name} 中删除数据成功")

    except Exception as e:
        loggerConfig.db_error_logger.error(f"从集合 {collection_name} 中删除数据失败: {str(e)}")
        raise


def chroma_count(db_name: str, collection_name: str) -> int:
    """
    获取 ChromaDB 集合中的文档数量

    :param db_name: 数据库名称
    :param collection_name: 集合名称
    :return: 文档数量
    """
    try:
        connector = ChromaDBConnector(db_name)
        collection = connector.get_collection(collection_name)

        count = collection.count()
        loggerConfig.db_info_logger.info(f"获取集合 {collection_name} 中的文档数量成功: {count}")
        return count

    except Exception as e:
        loggerConfig.db_error_logger.error(f"获取集合 {collection_name} 中的文档数量失败: {str(e)}")
        raise


def execute_chroma_operation(
        db_name: str,
        operation: str,
        collection_name: str,
        **kwargs
) -> Any:
    """
    统一的 ChromaDB 操作执行函数

    :param db_name: 数据库名称
    :param operation: 操作类型，可选值：insert, query, get, update, delete, count, list_collections
    :param collection_name: 集合名称
    :param kwargs: 操作的其他参数
    :return: 操作结果
    """
    operation_map = {
        'insert': chroma_insert,
        'query': chroma_query,
        'get': chroma_get,
        'update': chroma_update,
        'delete': chroma_delete,
        'count': chroma_count
    }

    if operation == 'list_collections':
        connector = ChromaDBConnector(db_name)
        return connector.list_collections()

    if operation not in operation_map:
        error_msg = f"不支持的操作类型: {operation}"
        loggerConfig.db_error_logger.error(error_msg)
        raise ValueError(error_msg)

    return operation_map[operation](db_name, collection_name, **kwargs)
