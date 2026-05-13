# coding=utf-8

from core.classic.frame.database.func import sqliteConnector

"""
（暂时）数据库路径指定在下方
如果有独立的数据库连接，可以在此处添加
"""
db_name = 'AnalyzeTransaction'
table_name = "ANALYZE_TRANSACTION_MATCH_SERIAL_REMAIN"


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
    sql = (f"CREATE TABLE IF NOT EXISTS {table_name}("
           f" CODE varchar(6) not null,"
           f" NAME varchar,"
           f" CRN_PRICE double,"
           f" TRN_TYPE varchar,"
           f" TRN_PRICE double,"
           f" TRN_SHARE double,"
           f" TRN_AMOUNT double,"
           f" TRN_PROFIT double,"
           f" TRN_PROFIT_PCT double,"
           f" TRN_REMAIN_SHARE double,"
           f" TRN_GAINED_AMOUNT double,"
           f" FRS_TYPE varchar,"
           f" FRS_PRICE double,"
           f" FRS_SHARE double,"
           f" FRS_AMOUNT double,"
           f" FRS_PROFIT double,"
           f" FRS_PROFIT_PCT double,"
           f" TRN_DATE date not null,"
           f" FRS_DATE date,"
           f" TRN_ID integer,"
           f" TRN_PRIORITY integer,"
           f" constraint CODE_TRN_ID primary key (CODE, TRN_ID)"
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


def insert(code, name, crn_price,
           trn_type, trn_price, trn_share, trn_amount, trn_profit, trn_profit_pct,
           trn_remain_share, trn_gained_amount,
           frs_type, frs_price, frs_share, frs_amount, frs_profit, frs_profit_pct,
           trn_date, frs_date, trn_id):
    sql = (f"INSERT INTO {table_name} ("
           f"CODE, NAME, CRN_PRICE, "
           f"TRN_TYPE, TRN_PRICE, TRN_SHARE, TRN_AMOUNT, TRN_PROFIT, TRN_PROFIT_PCT, "
           f"TRN_REMAIN_SHARE, TRN_GAINED_AMOUNT, "
           f"FRS_TYPE, FRS_PRICE, FRS_SHARE, FRS_AMOUNT, FRS_PROFIT, FRS_PROFIT_PCT, "
           f"TRN_DATE, FRS_DATE, TRN_ID, TRN_PRIORITY) VALUES ("
           f"'{code}', '{name}', {str(crn_price)}, "
           f"'{trn_type}', '{str(trn_price)}', '{str(trn_share)}', '{str(trn_amount)}', "
           f"'{str(trn_profit)}', '{str(trn_profit_pct)}', "
           f"'{str(trn_remain_share)}', '{str(trn_gained_amount)}', "
           f"'{frs_type}', '{str(frs_price)}', '{str(frs_share)}', '{str(frs_amount)}', "
           f"'{str(frs_profit)}', '{str(frs_profit_pct)}', "
           f"'{trn_date}', '{frs_date}', {str(trn_id)}, 9999)")
    execute_cursor(sql)


def get_sum_share(code, and_condition):
    sql = (f"SELECT SUM(TRN_REMAIN_SHARE) FROM {table_name} WHERE "
           f"CODE = '{str(code)}' AND TRN_REMAIN_SHARE {and_condition} 0")
    res = execute_cursor(sql)[0][0]
    if res is None:
        res = 0
    return res


def get_sum_amount(code, and_condition):
    sql = (f"SELECT SUM(TRN_GAINED_AMOUNT) FROM {table_name} WHERE "
           f"CODE = '{str(code)}' AND TRN_GAINED_AMOUNT {and_condition} 0")
    res = execute_cursor(sql)[0][0]
    if res is None:
        res = 0
    return res


def update_transaction_priority(code, priority):
    sql = f"UPDATE {table_name} SET TRN_PRIORITY = {str(priority)} WHERE CODE = '{code}'"
    execute_cursor(sql)
