# coding=utf-8

from core.classic.frame.database.func import sqliteConnector

"""
（暂时）数据库路径指定在下方
如果有独立的数据库连接，可以在此处添加
"""
db_name = 'AnalyzeTransaction'
table_name = "ANALYZE_TRANSACTION_MATCH_QUANTITATIVE"


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


def create_table():
    """
    数据库的默认创建方法
    :return:
    """
    sql = (f"CREATE TABLE IF NOT EXISTS {table_name}( "
           f" CODE varchar(6) not null,"
           f" NAME varchar,"
           f" FEE_FREE_LIMIT integer,"
           f" HOLDING_SHARE double,"
           f" FEE_FREE_SHARE double,"
           f" HOLDING_AMOUNT double,"
           f" SHOWN_AMOUNT double,"
           f" DAILY_SHARE double,"
           f" DAILY_AMOUNT double,"
           f" primary key (CODE)"
           f");")
    execute_cursor(sql)


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


"""
下方DAO方法
"""


def insert_new(code, name, holding_share, holding_amount, shown_amount):
    sql = (f"INSERT INTO {table_name} (CODE, NAME, FEE_FREE_LIMIT, "
           f"HOLDING_SHARE, FEE_FREE_SHARE, HOLDING_AMOUNT, SHOWN_AMOUNT, "
           f"DAILY_SHARE, DAILY_AMOUNT) VALUES ("
           f"'{code}', '{name}', 0, {str(holding_share)}, 0, {str(holding_amount)},  {str(shown_amount)}, 0, 0)")
    execute_cursor(sql)


def update_daily_quantity(code, holding_share, fee_free_share, holding_amount, shown_amount, daily_share, daily_amount):
    sql = (f"UPDATE {table_name} SET "
           f"HOLDING_SHARE = {str(holding_share)}, "
           f"FEE_FREE_SHARE = {str(fee_free_share)}, "
           f"HOLDING_AMOUNT = {str(holding_amount)}, "
           f"SHOWN_AMOUNT = {str(shown_amount)}, "
           f"DAILY_SHARE = {str(daily_share)}, DAILY_AMOUNT = {str(daily_amount)} WHERE "
           f"CODE = '{code}'")
    execute_cursor(sql)


def select_quantity_info(code):
    sql = (f"SELECT FEE_FREE_LIMIT, DAILY_SHARE, DAILY_AMOUNT FROM {table_name} "
           f"WHERE CODE = '{code}'")
    res = execute_cursor(sql)
    return res


def select_code_priority_list():
    sql = f"SELECT DISTINCT CODE FROM {table_name} ORDER BY DAILY_AMOUNT DESC, HOLDING_AMOUNT DESC"
    res = execute_cursor(sql)
    return res

