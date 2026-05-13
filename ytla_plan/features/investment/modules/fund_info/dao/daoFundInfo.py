# coding=utf-8

from core.classic.frame.database.func import sqliteConnector

"""
（暂时）数据库路径指定在下方
如果有独立的数据库连接，可以在此处添加
"""
db_name = 'fund'
table_name = "FUND_INFO"


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
    sql = f"CREATE TABLE IF NOT EXISTS {table_name}(" \
          f" CODE varchar(6), " \
          f" NAME varchar(255), " \
          f" FUND_TYPE varchar(12), " \
          f" RATIO double, " \
          f" SHARE_ACCURACY int, " \
          f" FEE_FREE_LIMIT int, " \
          f" primary key (CODE)" \
          f");"
    execute_cursor(sql)


"""
下方Instance方法
"""


class Instance:

    def __init__(self, code: str):
        self.code: str = code
        self.fund_name: str = ''
        self.fund_type: str = ''
        self.ratio: float = 0
        self.share_accuracy: int = 0
        self.fee_free_limit: int = 0

    def get_instance_by_pk(self):
        db_res = fund_info_select(self.code)
        if len(db_res) == 1:
            self.fund_name = db_res[0]['NAME']
            self.fund_type = db_res[0]['FUND_TYPE']
            self.ratio = db_res[0]['RATIO']
            self.share_accuracy = db_res[0]['SHARE_ACCURACY']
            self.fee_free_limit = db_res[0]['FEE_FREE_LIMIT']


def instance_list(pk_list: list):
    res = []
    for i in pk_list:
        p = Instance(i)
        p.get_instance_by_pk()
        res.append(p)
    return res


"""
下方DAO方法
"""


def fund_info_select(code):
    """
    返回res元素读取:LIST-TUPLE
    :param code:
    :return:
    """
    sql = f"SELECT CODE, NAME, FUND_TYPE, RATIO, SHARE_ACCURACY, FEE_FREE_LIMIT FROM {table_name} WHERE CODE = '{code}'"
    res = execute_cursor(sql)
    return res


def fund_info_insert(code, name):
    """
    主插入
    :param code:
    :param name:
    :return:
    """
    sql = f"INSERT INTO {table_name} (CODE, NAME, RATIO, SHARE_ACCURACY, FEE_FREE_LIMIT) VALUES (" \
          f"'{code}', '{name}', 1, 2, 0)"
    res = execute_cursor(sql)
    return res


def fund_info_update(code, name):
    """
    更新基金名称
    :param code:
    :param name:
    :return:
    """
    sql = f"UPDATE {table_name} SET NAME = '{name}' WHERE CODE = '{code}'"
    res = execute_cursor(sql)
    return res


def fund_info_insert_full(code, name, fund_type, ratio, share_accuracy, fee_free_limit):
    """
    主插入
    :param code:
    :param name:
    :param fund_type:
    :param ratio:
    :param share_accuracy:
    :return:
    """
    sql = f"INSERT INTO {table_name} (CODE, NAME, FUND_TYPE, RATIO, SHARE_ACCURACY, FEE_FREE_LIMIT) VALUES (" \
          f"'{code}', '{name}', '{fund_type}', {str(ratio)}, {str(share_accuracy)}, {str(fee_free_limit)})"
    res = execute_cursor(sql)
    return res


def fund_info_update_ratio(code, ratio):
    """
    更新 单价倍率
    :param code:
    :param ratio:
    :return:
    """
    sql = f"UPDATE {table_name} SET RATIO = {ratio} WHERE CODE = '{code}'"
    res = execute_cursor(sql)
    return res


def fund_info_update_accuracy(code, accuracy):
    """
    更新 份额精度
    :param code:
    :param accuracy:
    :return:
    """
    sql = f"UPDATE {table_name} SET SHARE_ACCURACY = {accuracy} WHERE CODE = '{code}'"
    res = execute_cursor(sql)
    return res
