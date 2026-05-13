# coding=utf-8

from core.classic.frame.database.func import sqliteConnector

"""
（暂时）数据库路径指定在下方
如果有独立的数据库连接，可以在此处添加
"""
db_name = 'fund'
table_name = "FUND_HISTORY"


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
    sql = f"CREATE TABLE IF NOT EXISTS {table_name}( " \
          f" CODE varchar(6) not null," \
          f" TRANSACTION_DATE date not null," \
          f" CURRENT_PRICE double," \
          f" ORIGIN_PRICE double," \
          f" FLUCTUATION double," \
          f" SHARE_CHANGE_RATIO double," \
          f" SHARE_CHANGE_NOTE varchar(99)," \
          f" constraint CODE_DATE primary key (CODE, TRANSACTION_DATE)" \
          f");"
    execute_cursor(sql)


"""
下方Instance方法
"""


class Instance:

    def __init__(self, code: str, transaction_date: str):
        self.code: str = code
        self.transaction_date: str = transaction_date
        self.current_price: float = 0
        self.original_price: float = 0
        self.fluctuation: float = 0
        self.share_change_ratio: float = 0
        self.share_change_note: str = ''

    def get_instance_by_pk(self):
        db_res = fund_history_select(self.code, self.transaction_date)
        if len(db_res) == 1:
            self.current_price = db_res[0][2]
            self.original_price = db_res[0][3]
            self.fluctuation = db_res[0][4]
            self.share_change_ratio = db_res[0][5]
            self.share_change_note = db_res[0][6]


def instance_list(code: str, pk_list: list):
    res = []
    for i in pk_list:
        p = Instance(code, i)
        p.get_instance_by_pk()
        res.append(p)
    return res


"""
下方DAO方法
"""


def fund_history_insert(code, date, p1, p2, f, sc, note):
    """
    插入数据
    :param code:
    :param date:
    :param p1:
    :param p2:
    :param f:
    :param sc:
    :param note:
    :return:
    """
    sql = f"INSERT INTO FUND_HISTORY " \
          f"(CODE, TRANSACTION_DATE, CURRENT_PRICE, ORIGIN_PRICE, FLUCTUATION, " \
          f"SHARE_CHANGE_RATIO, SHARE_CHANGE_NOTE) " \
          f"VALUES ('{code}', '{date}', {str(p1)}, {str(p2)}, {str(f)}, {str(sc)}, '{note}') "
    res = execute_cursor(sql)
    return res


def fund_history_select(code, transaction_date):
    sql = (f"SELECT CODE, TRANSACTION_DATE, CURRENT_PRICE, ORIGIN_PRICE, FLUCTUATION, "
           f"SHARE_CHANGE_RATIO, SHARE_CHANGE_NOTE FROM {table_name} WHERE "
           f"CODE = '{code}' AND TRANSACTION_DATE = '{transaction_date}'")
    res = execute_cursor(sql)
    return res


def fund_history_get_latest_price(code, transaction_date):
    """
    查询指定日期基金的净值
    :param code:
    :param transaction_date:
    :return:
    """
    sql = f"SELECT CURRENT_PRICE FROM FUND_HISTORY WHERE CODE = '{code}' AND TRANSACTION_DATE = '{transaction_date}'"
    res = execute_cursor(sql)
    if len(res) > 0:
        return res[0]['CURRENT_PRICE']
    else:
        return 0


def fund_history_select_latest_date(code):
    """
    查询最新数据日期
    :param code:
    :return:
    """
    sql = f"SELECT TRANSACTION_DATE FROM FUND_HISTORY WHERE CODE = '{code}' ORDER BY TRANSACTION_DATE DESC LIMIT 1"
    res = execute_cursor(sql)
    return res


def fund_history_select_latest_price(code):
    """
    查询最新基金净值
    :param code:
    :return:
    """
    sql = f"SELECT CURRENT_PRICE, ORIGIN_PRICE FROM FUND_HISTORY " \
          f"WHERE CODE = '{code}' ORDER BY TRANSACTION_DATE DESC LIMIT 1"
    res = execute_cursor(sql)
    return res


def fund_history_get_share_change_ratio(code, transaction_date):
    """
    获取最近的基金份额变动比率
    :param code:
    :param transaction_date:
    :return:
    """
    sql = f"SELECT SHARE_CHANGE_RATIO from FUND_HISTORY " \
          f"where code = '{code}' and TRANSACTION_DATE <= '{transaction_date}' " \
          f"and SHARE_CHANGE_RATIO > 0 order by TRANSACTION_DATE desc limit 1"
    res = execute_cursor(sql)
    if len(res) > 0:
        return res[0]['SHARE_CHANGE_RATIO']
    else:
        return 1


def fund_history_get_share_change_ratio_list(code, transaction_date):
    """
    获取最近的基金份额变动比率
    :param code:
    :param transaction_date:
    :return:
    """
    sql = f"SELECT SHARE_CHANGE_RATIO from FUND_HISTORY " \
          f"where code = '{code}' and TRANSACTION_DATE <= '{transaction_date}' " \
          f"and SHARE_CHANGE_RATIO > 0 order by TRANSACTION_DATE desc limit 1"
    res = execute_cursor(sql)
    return res


def get_fund_history_list(code, transaction_date):
    sql = f"SELECT TRANSACTION_DATE, CURRENT_PRICE, ORIGIN_PRICE, " \
          f"FLUCTUATION, SHARE_CHANGE_RATIO, SHARE_CHANGE_NOTE FROM " \
          f"FUND_HISTORY WHERE " \
          f"CODE = '{code}' AND TRANSACTION_DATE > '{transaction_date}' ORDER BY TRANSACTION_DATE ASC"
    res = execute_cursor(sql)
    return res


def get_fund_history_full_list(code):
    sql = f"SELECT TRANSACTION_DATE, CURRENT_PRICE, ORIGIN_PRICE, " \
          f"FLUCTUATION, SHARE_CHANGE_RATIO, SHARE_CHANGE_NOTE FROM " \
          f"FUND_HISTORY WHERE " \
          f"CODE = '{code}' ORDER BY TRANSACTION_DATE ASC"
    res = execute_cursor(sql)
    return res


def get_fund_moving_average(code, transaction_date, limits):
    sql_1 = f"SELECT COUNT(*) AS COUNT FROM FUND_HISTORY WHERE " \
            f"CODE = '{code}' AND TRANSACTION_DATE <= '{transaction_date}' " \
            f"ORDER BY TRANSACTION_DATE DESC LIMIT {str(limits)}"
    res_1 = execute_cursor(sql_1)
    sql_2 = f"SELECT SUM(CURRENT_PRICE) AS SUM_CURRENT_PRICE, SUM(ORIGIN_PRICE) AS SUM_ORIGIN_PRICE FROM " \
            f"(SELECT CURRENT_PRICE, ORIGIN_PRICE FROM FUND_HISTORY WHERE " \
            f"CODE = '{code}' AND TRANSACTION_DATE <= '{transaction_date}' " \
            f"ORDER BY TRANSACTION_DATE DESC LIMIT {str(limits)})"
    res_2 = execute_cursor(sql_2)
    if len(res_1) > 0:
        return [res_1[0]['COUNT'], res_2[0]['SUM_CURRENT_PRICE'], res_2[0]['SUM_ORIGIN_PRICE']]
    else:
        return [0, 0, 0]


def fund_history_get_share_change_history_list(code):
    """
    获取单个基金的基金份额变动比率列表
    :param code:
    :return:
    """
    sql = f"SELECT TRANSACTION_DATE, SHARE_CHANGE_RATIO from FUND_HISTORY " \
          f"where code = '{code}'  " \
          f"and SHARE_CHANGE_RATIO > 0  and SHARE_CHANGE_NOTE like '每份基金份额%' order by TRANSACTION_DATE asc"
    res = execute_cursor(sql)
    return res


def fund_history_get_latest_history_list(code, limits):
    sql = f"SELECT * FROM (" \
          f"SELECT TRANSACTION_DATE, CURRENT_PRICE, FLUCTUATION, SHARE_CHANGE_RATIO, SHARE_CHANGE_NOTE FROM " \
          f"FUND_HISTORY WHERE CODE = '{code}' ORDER BY TRANSACTION_DATE DESC LIMIT {str(limits)}) " \
          f"ORDER BY TRANSACTION_DATE ASC"
    res = execute_cursor(sql)
    return res
