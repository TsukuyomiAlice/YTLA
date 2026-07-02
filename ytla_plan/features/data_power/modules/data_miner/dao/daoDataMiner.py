# coding=utf-8

import sqlite3

import pandas as pd

from core.classic.frame.database.func import sqliteConnector

# pandas dtype 到 sqlite 类型映射
DTYPE_TO_SQLITE = {
    'int64': 'INTEGER',
    'int32': 'INTEGER',
    'int16': 'INTEGER',
    'int8': 'INTEGER',
    'Int64': 'INTEGER',
    'Int32': 'INTEGER',
    'Int16': 'INTEGER',
    'Int8': 'INTEGER',
    'uint64': 'INTEGER',
    'uint32': 'INTEGER',
    'uint16': 'INTEGER',
    'uint8': 'INTEGER',
    'UInt64': 'INTEGER',
    'UInt32': 'INTEGER',
    'UInt16': 'INTEGER',
    'UInt8': 'INTEGER',
    'float64': 'REAL',
    'float32': 'REAL',
    'Float64': 'REAL',
    'Float32': 'REAL',
    'object': 'TEXT',
    'string': 'TEXT',
    'str': 'TEXT',
    'bool': 'INTEGER',
    'boolean': 'INTEGER',
    'datetime64[ns]': 'TEXT',
    'datetime64[ns, UTC]': 'TEXT',
    'category': 'TEXT',
}


def _pandas_dtype_to_sqlite(dtype) -> str:
    """
    将 pandas 数据类型映射为 sqlite 列类型

    :param dtype: pandas dtype 对象或字符串
    :return: str - sqlite 类型名
    """
    dtype_str = str(dtype)
    return DTYPE_TO_SQLITE.get(dtype_str, 'TEXT')


def create_table_from_dataframe(db_path: str, df: pd.DataFrame, table_name: str):
    """
    从 pandas DataFrame 动态创建 sqlite 表并写入数据

    根据 DataFrame 的 dtypes 自动推断 sqlite 列类型，
    并使用参数化查询批量插入数据。

    :param db_path: str - .db 文件的完整路径
    :param df: pd.DataFrame - 要写入的数据
    :param table_name: str - 目标表名
    """
    # 构建 CREATE TABLE 语句
    columns = []
    for col_name, dtype in df.dtypes.items():
        sql_type = _pandas_dtype_to_sqlite(dtype)
        columns.append(f'"{col_name}" {sql_type}')
    columns_def = ', '.join(columns)
    create_sql = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({columns_def})'

    # 构建参数化 INSERT 语句
    col_names = [f'"{c}"' for c in df.columns]
    placeholders = ', '.join(['?' for _ in df.columns])
    insert_sql = f'INSERT INTO "{table_name}" ({", ".join(col_names)}) VALUES ({placeholders})'

    conn = sqlite3.connect(db_path)
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute(create_sql)

            # 批量插入
            # 将 DataFrame 转换为参数列表，处理 NaN 为 None
            params_list = []
            for _, row in df.iterrows():
                params = [None if pd.isna(v) else v for v in row]
                params_list.append(params)
            cursor.executemany(insert_sql, params_list)
    finally:
        conn.close()


def execute_cursor(db_name: str, sql: str, params=None):
    """
    通用参数化查询执行方法

    通过 sqliteConnector.execute_cursor 执行，
    适用于已注册的数据库名称。

    :param db_name: str - 数据库标识名（在配置中注册的名称）
    :param sql: str - SQL 语句（使用 ? 作为参数占位符）
    :param params: list/tuple - 参数值列表，默认为 None
    :return: list[dict] - 查询结果（SELECT 返回行列表，非 SELECT 返回空列表）
    """
    if params is None:
        params = []
    res = sqliteConnector.execute_cursor(db_name, sql, params)
    return res


def drop_table(db_name: str, table_name: str):
    """
    删除指定表

    :param db_name: str - 数据库标识名
    :param table_name: str - 要删除的表名
    """
    sql = f'DROP TABLE IF EXISTS "{table_name}"'
    execute_cursor(db_name, sql)


def get_table_info(db_path: str, table_name: str):
    """
    获取表结构信息（列名、类型等）

    使用原生 sqlite3 连接查询 PRAGMA table_info。

    :param db_path: str - .db 文件的完整路径
    :param table_name: str - 目标表名
    :return: list[dict] - 表结构信息列表，每项包含 cid, name, type, notnull, dflt_value, pk
    """
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        cursor.execute(f'PRAGMA table_info("{table_name}")')
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        res = [dict(zip(columns, row)) for row in rows]
        return res
    finally:
        conn.close()


def query_table_data(db_path: str, table_name: str):
    """
    查询指定表的所有数据

    使用原生 sqlite3 连接查询指定表的所有行，
    将 None 值统一保留为 None 返回。

    :param db_path: str - .db 文件的完整路径
    :param table_name: str - 目标表名
    :return: dict - {"columns": list[str], "rows": list[list]}
    """
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM "{table_name}"')
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        # 将每行数据转为 list，None 值保持不变
        rows_list = [list(row) for row in rows]
        return {
            'columns': columns,
            'rows': rows_list
        }
    finally:
        conn.close()
