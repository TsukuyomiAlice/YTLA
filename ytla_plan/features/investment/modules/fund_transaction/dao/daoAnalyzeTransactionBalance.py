# coding=utf-8

from core.classic.frame.database.func import sqliteConnector

"""
（暂时）数据库路径指定在下方
如果有独立的数据库连接，可以在此处添加
"""
db_name = 'AnalyzeTransaction'
table_name = "ANALYZE_TRANSACTION_BALANCE"


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
    sql = (f"CREATE TABLE IF NOT EXISTS {table_name} ("
           f" CODE varchar,"
           f" NAME varchar,"
           f" CUR_PRICE double,"
           f" CUR_AMOUNT double,"
           f" HOLDING_SHARE double,"
           f" HOLDING_AVG_PRICE double,"
           f" MATCH_SHARE_PROFIT double,"
           f" MATCH_AMOUNT_PROFIT double,"
           f" MATCH_SHARE_HOLD double,"
           f" MATCH_AMOUNT_PAID double,"
           f" MATCH_SHARE_SOLD double,"
           f" MATCH_AMOUNT_HOLD double,"
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


def clear_records(code):
    sql = f"DELETE FROM {table_name} WHERE CODE = '{code}'"
    execute_cursor(sql)


def insert(code, name, cur_price, cur_amount, holding_share, holding_avg_price,
           match_share_profit, match_amount_profit,
           match_share_hold, match_amount_paid, match_share_sold, match_amount_hold):
    sql = (f"INSERT INTO {table_name} (CODE, NAME, CUR_PRICE, CUR_AMOUNT, HOLDING_SHARE, HOLDING_AVG_PRICE, "
           f"MATCH_SHARE_PROFIT, MATCH_AMOUNT_PROFIT, "
           f"MATCH_SHARE_HOLD, MATCH_AMOUNT_PAID, MATCH_SHARE_SOLD, MATCH_AMOUNT_HOLD) VALUES ("
           f"'{code}', '{name}', {str(cur_price)}, {str(cur_amount)}, {str(holding_share)}, {str(holding_avg_price)}, "
           f"{str(match_share_profit)}, {str(match_amount_profit)}, "
           f"{str(match_share_hold)}, {str(match_amount_paid)}, {str(match_share_sold)}, {str(match_amount_hold)}"
           f")")
    execute_cursor(sql)


def select_current_holding(code):
    sql = f"SELECT NAME, HOLDING_SHARE, CUR_AMOUNT FROM {table_name} WHERE CODE = '{code}'"
    res = execute_cursor(sql)
    return res
