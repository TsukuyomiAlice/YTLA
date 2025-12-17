# coding=utf-8

from core.domain.area.frame.func import sqliteConnector

"""
（暂时）数据库路径指定在下方
如果有独立的数据库连接，可以在此处添加
"""
db_name = 'life_plan'
table_name = "GLOBAL_PERSISTENCE"


def execute_cursor(sql, params=None):
    """
    数据库参数化查询执行方法（安全版本）

    使用参数化查询执行 SQL 语句，适用于包含用户输入或动态参数的场景，
    能有效防止 SQL 注入。主要用于 INSERT/UPDATE 等含动态值的 DML 语句。

    :param sql: str - 带有占位符的 SQL 语句（例如使用 ? 作为参数占位符）
    :param params: Tuple/List - 与 SQL 语句中占位符对应的参数值
    :return: sqlite3.Cursor 对象 - 包含执行结果的光标对象，
             可通过 fetchall()/fetchone() 获取查询结果，
             或通过 rowcount 获取受影响行数
    """
    if params is None:
        params = []
    res = sqliteConnector.execute_cursor(db_name, sql, params)
    return res


def drop_table():
    """
    数据库的默认销毁方法
    :return:
    """
    sql = f"DROP TABLE {table_name}"
    execute_cursor(sql)


def truncate_table():
    """
    数据库的默认清空方法
    :return:
    """
    sql1 = f"DELETE FROM {table_name} where 1 = 1"
    execute_cursor(sql1)
    sql2 = "VACUUM"
    execute_cursor(sql2)


def create_table():
    """
    数据库的默认创建方法
    :return:
    """
    sql = (f"CREATE TABLE IF NOT EXISTS {table_name}("
           f"PERSISTENCE_KEY varchar, "
           f"PERSISTENCE_VALUE varchar, "
           f"DELETE_FLAG varchar, "
           f"PRIMARY KEY (PERSISTENCE_KEY));")
    execute_cursor(sql)


"""
下方Instance方法
"""


class Instance:

    def __init__(self, persistence_key: str):
        self.persistence_key = persistence_key
        self.persistence_value: str = ''
        self.delete_flag: str = '0'

    def load_persistence(self):
        db_res = select_all_by_pk(self.persistence_key)
        if len(db_res) == 1:
            return db_res[0]
        else:
            return []

    def set_instance(self, db_res: dict):
        if len(db_res) != 3:
            return
        self.persistence_value = db_res['PERSISTENCE_VALUE']
        self.delete_flag = db_res['DELETE_FLAG']


def instance_list(pk_list: list):
    res = []
    for i in pk_list:
        p = Instance(i)
        p.set_instance(p.load_persistence())
        res.append(p)
    return res


def select_all_by_pk(pk: str):
    sql = f"SELECT PERSISTENCE_KEY, PERSISTENCE_VALUE, DELETE_FLAG FROM {table_name} WHERE PERSISTENCE_KEY = ?"
    res = execute_cursor(sql, [pk])
    return res


"""
下方DAO方法
"""
def load_full_persistence():
    sql =  f"SELECT PERSISTENCE_KEY, PERSISTENCE_VALUE FROM {table_name} WHERE DELETE_FLAG = '0'"
    res = execute_cursor(sql)
    return res


def save_persistence(persistence: Instance):
    sql = f"INSERT OR REPLACE INTO {table_name} (PERSISTENCE_KEY, PERSISTENCE_VALUE, DELETE_FLAG) VALUES (?, ?, ?)"
    params = (persistence.persistence_key, persistence.persistence_value, persistence.delete_flag)
    execute_cursor(sql, params)


def delete_persistence(persistence: Instance):
    sql = f"UPDATE {table_name} SET DELETE_FLAG = '1' WHERE PERSISTENCE_KEY = ?"
    params = (persistence.persistence_key,)
    execute_cursor(sql, params)

