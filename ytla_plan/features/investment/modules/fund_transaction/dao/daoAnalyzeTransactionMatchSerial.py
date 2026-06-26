# coding=utf-8

from core.classic.frame.database.func import sqliteConnector

"""
数据库路径: {base}/plan_{plan_id}/module_{module_id}/analyze_transaction.db
"""
table_name = "ANALYZE_TRANSACTION_MATCH_SERIAL"


class DBConnector:
    """Database connector for analyze transaction match serial (plan+module scoped)."""

    def __init__(self, plan_id: int, module_id: int):
        self.plan_id = plan_id
        self.module_id = module_id
        self.table_name = table_name
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
        res = sqliteConnector.execute_cursor_plan_module(self.plan_id, self.module_id, 'analyze_transaction', sql, params)
        return res

    def create_table(self):
        """
        数据库的默认创建方法
        :return:
        """
        sql = (f"CREATE TABLE IF NOT EXISTS {self.table_name}( "
               f" CODE varchar(6) not null,"
               f" NAME varchar,"
               f" TRN_DATE date not null,"
               f" TRN_TYPE varchar,"
               f" TRN_PRICE double,"
               f" TRN_SHARE double,"
               f" TRN_AMOUNT double,"
               f" TRN_REMAIN_SHARE double,"
               f" TRN_GAINED_AMOUNT double,"
               f" LABEL integer not null,"
               f" FIRST_TRN_ID integer not null,"
               f" FIRST_TRN_DATE date not null,"
               f" TRN_ID integer not null,"
               f" STATUS varchar,"
               f" constraint CODE_BUY_SELL primary key (CODE, LABEL, FIRST_TRN_ID, TRN_ID)"
               f");")
        self.execute_cursor(sql)

    def drop_table(self):
        """
        数据库的默认销毁方法
        :return:
        """
        sql = f"DROP TABLE {self.table_name}"
        self.execute_cursor(sql)

    def truncate_table(self):
        """
        数据库的默认清空方法
        :return:
        """
        sql1 = f"DELETE FROM {self.table_name} where 1 = 1"
        self.execute_cursor(sql1)
        sql2 = "VACUUM"
        self.execute_cursor(sql2)


"""
下方DAO方法
"""


def clear_records(plan_id: int, module_id: int, code):
    con = DBConnector(plan_id, module_id)
    sql = f"DELETE FROM {con.table_name} WHERE CODE = '{code}'"
    con.execute_cursor(sql)


def get_latest_label(plan_id: int, module_id: int, code):
    con = DBConnector(plan_id, module_id)
    sql = f"SELECT LABEL FROM {con.table_name} WHERE CODE = '{code}' ORDER BY LABEL DESC LIMIT 1"
    res = con.execute_cursor(sql)
    if len(res) > 0:
        return res[0][0]
    else:
        return 0


def insert_record(plan_id: int, module_id: int, code, name,
                  transaction_date, transaction_type, transaction_price, transaction_share, transaction_amount,
                  transaction_remain_share, transaction_gained_amount,
                  label, first_transaction_id, first_transaction_date, transaction_id, status):
    con = DBConnector(plan_id, module_id)
    sql = (f"INSERT INTO {con.table_name} ("
           f"CODE, NAME, "
           f"TRN_DATE, TRN_TYPE, TRN_PRICE, TRN_SHARE, TRN_AMOUNT, "
           f"TRN_REMAIN_SHARE, TRN_GAINED_AMOUNT, "
           f"LABEL, FIRST_TRN_ID, FIRST_TRN_DATE, TRN_ID, STATUS) VALUES ("
           f"'{code}', '{name}', "
           f"'{transaction_date}', '{transaction_type}', "
           f"{str(transaction_price)}, {str(transaction_share)}, {str(transaction_amount)}, "
           f"{str(transaction_remain_share)}, {str(transaction_gained_amount)}, "
           f"{str(label)}, {str(first_transaction_id)}, '{first_transaction_date}', "
           f"{str(transaction_id)}, '{status}')")
    con.execute_cursor(sql)


def match_transaction_amount(plan_id: int, module_id: int, code, amount, status):
    con = DBConnector(plan_id, module_id)
    sql = (f"SELECT LABEL, TRN_ID, FIRST_TRN_ID, FIRST_TRN_DATE, "
           f"TRN_TYPE, TRN_SHARE, TRN_REMAIN_SHARE, TRN_GAINED_AMOUNT FROM {con.table_name} "
           f"WHERE CODE = '{code}' AND TRN_AMOUNT = {str(amount)} "
           f"AND TRN_TYPE IN ('AMOUNT_SELL', 'SHARE_SELL') AND STATUS IN ({status}) "
           f"ORDER BY STATUS ASC, TRN_DATE ASC LIMIT 1")
    res = con.execute_cursor(sql)
    return res


def match_transaction_amount_remain(plan_id: int, module_id: int, code, amount, status):
    con = DBConnector(plan_id, module_id)
    sql = (f"SELECT LABEL, TRN_ID, FIRST_TRN_ID, FIRST_TRN_DATE, "
           f"TRN_TYPE, TRN_SHARE, TRN_REMAIN_SHARE, TRN_GAINED_AMOUNT FROM {con.table_name} "
           f"WHERE CODE = '{code}' AND TRN_GAINED_AMOUNT =  {str(amount)} "
           f"AND TRN_TYPE IN ('AMOUNT_SELL', 'SHARE_SELL') AND STATUS IN ({status}) "
           f"ORDER BY STATUS ASC, TRN_DATE ASC LIMIT 1")
    res = con.execute_cursor(sql)
    return res


def match_transaction_share(plan_id: int, module_id: int, code, share, status):
    con = DBConnector(plan_id, module_id)
    sql = (f"SELECT LABEL, TRN_ID, FIRST_TRN_ID, FIRST_TRN_DATE, "
           f"TRN_TYPE, TRN_AMOUNT, TRN_REMAIN_SHARE, TRN_GAINED_AMOUNT FROM {con.table_name} "
           f"WHERE CODE = '{code}' AND TRN_SHARE = {str(share)} "
           f"AND TRN_TYPE IN ('AMOUNT_BUY', 'SHARE_BUY') AND STATUS IN ({status}) "
           f"ORDER BY STATUS ASC, TRN_DATE ASC LIMIT 1")
    res = con.execute_cursor(sql)
    return res


def match_transaction_share_remain(plan_id: int, module_id: int, code, share, status):
    con = DBConnector(plan_id, module_id)
    sql = (f"SELECT LABEL, TRN_ID, FIRST_TRN_ID, FIRST_TRN_DATE, "
           f"TRN_TYPE, TRN_AMOUNT, TRN_REMAIN_SHARE, TRN_GAINED_AMOUNT FROM {con.table_name} "
           f"WHERE CODE = '{code}' AND TRN_REMAIN_SHARE = {str(share)} "
           f"AND TRN_TYPE IN ('AMOUNT_BUY', 'SHARE_BUY') AND STATUS IN ({status}) "
           f"ORDER BY STATUS ASC, TRN_DATE ASC LIMIT 1")
    res = con.execute_cursor(sql)
    return res


def check_transaction_type(plan_id: int, module_id: int, code, first_transaction_id):
    con = DBConnector(plan_id, module_id)
    sql = (f"SELECT TRN_TYPE, TRN_REMAIN_SHARE, TRN_GAINED_AMOUNT FROM {con.table_name} "
           f"WHERE CODE = '{code}' AND FIRST_TRN_ID = {str(first_transaction_id)} ORDER BY LABEL DESC LIMIT 1")
    res = con.execute_cursor(sql)
    return res


def update_status_by_label(plan_id: int, module_id: int, code, label, status):
    con = DBConnector(plan_id, module_id)
    sql = (f"UPDATE {con.table_name} SET STATUS = '{status}' WHERE "
           f"CODE = '{code}' AND LABEL = {str(label)}")
    con.execute_cursor(sql)


def update_status_by_first_transaction_id(plan_id: int, module_id: int, code, transaction_id, status):
    con = DBConnector(plan_id, module_id)
    sql = (f"UPDATE {con.table_name} SET STATUS = '{status}' WHERE "
           f"CODE = '{code}' AND TRN_ID = {str(transaction_id)}")
    con.execute_cursor(sql)

    sql = (f"UPDATE {con.table_name} SET STATUS = '20' "
           f"WHERE CODE = '{code}' AND FIRST_TRN_ID = {str(transaction_id)} "
           f"AND STATUS = '01'")
    con.execute_cursor(sql)


def select_active_transactions(plan_id: int, module_id: int, code, transaction_date):
    con = DBConnector(plan_id, module_id)
    sql = (f"SELECT TRN_DATE, TRN_TYPE, TRN_SHARE, TRN_AMOUNT, "
           f"TRN_REMAIN_SHARE, TRN_GAINED_AMOUNT, "
           f"LABEL, FIRST_TRN_ID, FIRST_TRN_DATE, TRN_ID, STATUS FROM {con.table_name} "
           f"WHERE CODE = '{code}' AND TRN_DATE < '{transaction_date}' AND STATUS IN ('00', '01') "
           f"ORDER BY TRN_DATE ASC")
    res = con.execute_cursor(sql)
    return res


def select_first_transaction(plan_id: int, module_id: int, code, first_trn_id):
    con = DBConnector(plan_id, module_id)
    sql = (f"SELECT TRN_DATE, TRN_TYPE, TRN_SHARE, TRN_AMOUNT, "
           f"TRN_REMAIN_SHARE, TRN_GAINED_AMOUNT, "
           f"LABEL, FIRST_TRN_ID, FIRST_TRN_DATE, TRN_ID, STATUS FROM {con.table_name} "
           f"WHERE CODE = '{code}' AND FIRST_TRN_ID = {str(first_trn_id)} AND STATUS = '10' "
           f"ORDER BY LABEL ASC LIMIT 1")
    res = con.execute_cursor(sql)
    return res


def select_sum_profit(plan_id: int, module_id: int, code):
    con = DBConnector(plan_id, module_id)
    sql = (f"SELECT SUM(TRN_REMAIN_SHARE), SUM(TRN_GAINED_AMOUNT) FROM {con.table_name} WHERE "
           f"CODE = '{code}' AND STATUS = '99'")
    res = con.execute_cursor(sql)[0]
    result = [0, 0]
    if res[0] is not None:
        result[0] = res[0]
    if res[1] is not None:
        result[1] = res[1]
    return result
