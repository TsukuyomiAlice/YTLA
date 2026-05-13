# coding=utf-8

from core.classic.frame.database.func import sqliteConnector

"""
（暂时）数据库路径指定在下方
如果有独立的数据库连接，可以在此处添加
"""
db_name = 'AnalyzeTransaction'
table_name = "ANALYZE_TRANSACTION_ORIGINAL_SERIAL"


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


'''
STATUS
0: LATEST RECORD
1: EARLIER RECORD
'''


def create_table():
    """
    数据库的默认创建方法
    :return:
    """
    sql = (f"CREATE TABLE IF NOT EXISTS {table_name}( "
           f" CODE varchar(6) not null,"
           f" NAME varchar,"
           f" TRN_DATE date not null,"
           f" TRN_TYPE varchar,"
           f" TRN_PRICE double,"
           f" TRN_SHARE double,"
           f" TRN_AMOUNT double,"
           f" TRN_EFFECTIVE_SHARE double,"
           f" TRN_EFFECTIVE_AMOUNT double,"
           f" TRN_REMAIN_SHARE double,"
           f" TRN_GAINED_AMOUNT double,"
           f" LABEL integer not null,"
           f" TRN_BUY_IN_ID integer not null,"
           f" TRN_BUY_IN_DATE date not null,"
           f" TRN_ID integer not null,"
           f" STATUS varchar,"
           f" constraint CODE_BUY_SELL primary key (CODE, TRN_BUY_IN_ID, TRN_ID)"
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


def get_latest_label(code):
    sql = f"SELECT LABEL FROM {table_name} WHERE CODE = '{code}' ORDER BY LABEL DESC LIMIT 1"
    res = execute_cursor(sql)
    if len(res) > 0:
        return res[0][0]
    else:
        return 0


def insert_record(code, name,
                  transaction_date, transaction_type, transaction_price, transaction_share, transaction_amount,
                  transaction_effective_share, transaction_effective_amount,
                  transaction_remained_share, transaction_gained_amount,
                  label, transaction_buy_in_id, transaction_buy_in_date, transaction_id, status):
    sql = (f"INSERT INTO {table_name} ("
           f"CODE, NAME, "
           f"TRN_DATE, TRN_TYPE, TRN_PRICE, TRN_SHARE, TRN_AMOUNT, "
           f"TRN_EFFECTIVE_SHARE, TRN_EFFECTIVE_AMOUNT, "
           f"TRN_REMAIN_SHARE, TRN_GAINED_AMOUNT, "
           f"LABEL, TRN_BUY_IN_ID, TRN_BUY_IN_DATE, TRN_ID, STATUS) VALUES ("
           f"'{code}', '{name}', "
           f"'{transaction_date}', '{transaction_type}', "
           f"{str(transaction_price)}, {str(transaction_share)}, {str(transaction_amount)}, "
           f"{str(transaction_effective_share)}, {str(transaction_effective_amount)}, "
           f"{str(transaction_remained_share)}, {str(transaction_gained_amount)}, "
           f"{str(label)}, {str(transaction_buy_in_id)}, '{transaction_buy_in_date}', "
           f"{str(transaction_id)}, '{status}')")
    execute_cursor(sql)


def get_open_transactions(code):
    sql = (f"SELECT LABEL, TRN_BUY_IN_ID, TRN_BUY_IN_DATE, "
           f"TRN_REMAIN_SHARE, TRN_GAINED_AMOUNT "
           f"FROM {table_name} WHERE CODE = '{code}' AND STATUS = '0' "
           f"ORDER BY TRN_BUY_IN_DATE ASC")
    res = execute_cursor(sql)
    return res


def update_status(code, label, status):
    sql = f"UPDATE {table_name} SET STATUS = '{status}' WHERE CODE = '{code}' AND LABEL = {str(label)}"
    execute_cursor(sql)


def get_transaction_price(code, transaction_id):
    sql = f"SELECT TRN_PRICE FROM {table_name} WHERE CODE = '{code}' AND TRN_ID = {str(transaction_id)}"
    res = execute_cursor(sql)[0][0]
    return res


def get_sum_remain_share(code, date_before):
    sql = (f"SELECT SUM(TRN_REMAIN_SHARE) FROM {table_name} "
           f"WHERE CODE = '{code}' AND TRN_BUY_IN_DATE <= '{date_before}' AND STATUS = '0'")
    res = execute_cursor(sql)[0][0]
    if res is None:
        res = 0
    return res
