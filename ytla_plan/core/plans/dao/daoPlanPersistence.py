# coding=utf-8

from core.frame.func import sqliteConnector

"""
（暂时）数据库路径指定在下方
如果有独立的数据库连接，可以在此处添加
"""
table_name = "PLAN_PERSISTENCE"


class DBConnector:

    def __init__(self, plan_id: int):
        self.db_name = f"plan_{str(plan_id)}"
        self.create_table()

    def execute_cursor(self, sql, params=None):
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
        res = sqliteConnector.execute_cursor_with_db(self.db_name, sql, params)
        return res

    def drop_table(self):
        """
        数据库的默认销毁方法
        :return:
        """
        sql = f"DROP TABLE {table_name}"
        self.execute_cursor(sql)

    def truncate_table(self):
        """
        数据库的默认清空方法
        :return:
        """
        sql1 = f"DELETE FROM {table_name} where 1 = 1"
        self.execute_cursor(sql1)
        sql2 = "VACUUM"
        self.execute_cursor(sql2)

    def create_table(self):
        """
        数据库的默认创建方法
        :return:
        """
        sql = (f"CREATE TABLE IF NOT EXISTS {table_name}("
               f"MODULE_ID int, "
               f"PERSISTENCE_KEY varchar, "
               f"PERSISTENCE_VALUE varchar, "
               f"DELETE_FLAG varchar, "
               f"CONSTRAINT K PRIMARY KEY (MODULE_ID, PERSISTENCE_KEY));")
        self.execute_cursor(sql)


"""
下方Instance方法
"""


class Instance:

    def __init__(self, module_id: int, persistence_key: str):
        self.module_id = module_id
        self.persistence_key = persistence_key
        self.persistence_value: str = ''
        self.delete_flag: str = ''

    def load_persistence(self, plan_id: int):
        db_res = select_all_by_pk(plan_id, self.module_id, self.persistence_key)
        return db_res

    def set_instance(self, db_res: list):
        if len(db_res) != 4:
            return
        self.persistence_value = db_res[2]
        self.delete_flag = db_res[3]


def instance_list(plan_id: int, pk_list: list):
    res = []
    for [module_id, persistence_key] in pk_list:
        p = Instance(module_id, persistence_key)
        p.set_instance(p.load_persistence(plan_id))
        res.append(p)
    return res


def select_all_by_pk(plan_id: int, module_id: int, persistence_key: str):
    con = DBConnector(plan_id)
    sql = f"SELECT MODULE_ID, PERSISTENCE_KEY, PERSISTENCE_VALUE, DELETE_FLAG FROM {table_name} WHERE MODULE_ID = ? AND PERSISTENCE_KEY = ?"
    res = con.execute_cursor(sql, [module_id, persistence_key])
    return res


"""
下方DAO方法
"""
def load_persistence_by_module_id(plan_id: int, module_id: int):
    con = DBConnector(plan_id)
    sql = f"SELECT MODULE_ID, PERSISTENCE_KEY, PERSISTENCE_VALUE FROM {table_name} WHERE MODULE_ID = ? AND DELETE_FLAG = '0'"
    res = con.execute_cursor(sql, [module_id])
    return res


def save_persistence_by_module_id(plan_id: int, persistence: Instance):
    con = DBConnector(plan_id)
    sql = f"INSERT OR REPLACE INTO {table_name} (MODULE_ID, PERSISTENCE_KEY, PERSISTENCE_VALUE, DELETE_FLAG) VALUES (?, ?, ?, '0')"
    params = (persistence.module_id, persistence.persistence_key, persistence.persistence_value)
    res = con.execute_cursor(sql, params)
    return res


def delete_persistence_by_module_id(plan_id: int, persistence: Instance):
    con = DBConnector(plan_id)
    sql = f"UPDATE {table_name} SET DELETE_FLAG = '1' WHERE MODULE_ID = ? AND PERSISTENCE_KEY = ?"
    params = (persistence.module_id, persistence.persistence_key)
    res = con.execute_cursor(sql, params)
    return res


def delete_all_persistence_by_module_id(plan_id: int, module_id: int):
    con = DBConnector(plan_id)
    sql = f"UPDATE {table_name} SET DELETE_FLAG = '1' WHERE MODULE_ID = ?"
    params = [module_id]
    res = con.execute_cursor(sql, params)
    return res
