# coding=utf-8

from core.classic.frame.database.func import sqliteConnector

"""
数据库路径: {base}/plan_{plan_id}/module_{module_id}/analyze_transaction.db
"""
table_name = "ANALYZE_TRANSACTION_MATCH_QUANTITATIVE"


class DBConnector:
    """Database connector for analyze transaction match quantitative (plan+module scoped)."""

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
               f" FEE_FREE_LIMIT integer,"
               f" HOLDING_SHARE double,"
               f" FEE_FREE_SHARE double,"
               f" HOLDING_AMOUNT double,"
               f" SHOWN_AMOUNT double,"
               f" DAILY_SHARE double,"
               f" DAILY_AMOUNT double,"
               f" primary key (CODE)"
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


def insert_new(plan_id: int, module_id: int, code, name, holding_share, holding_amount, shown_amount):
    con = DBConnector(plan_id, module_id)
    sql = (f"INSERT INTO {con.table_name} (CODE, NAME, FEE_FREE_LIMIT, "
           f"HOLDING_SHARE, FEE_FREE_SHARE, HOLDING_AMOUNT, SHOWN_AMOUNT, "
           f"DAILY_SHARE, DAILY_AMOUNT) VALUES ("
           f"'{code}', '{name}', 0, {str(holding_share)}, 0, {str(holding_amount)},  {str(shown_amount)}, 0, 0)")
    con.execute_cursor(sql)


def update_daily_quantity(plan_id: int, module_id: int, code, holding_share, fee_free_share, holding_amount, shown_amount, daily_share, daily_amount):
    con = DBConnector(plan_id, module_id)
    sql = (f"UPDATE {con.table_name} SET "
           f"HOLDING_SHARE = {str(holding_share)}, "
           f"FEE_FREE_SHARE = {str(fee_free_share)}, "
           f"HOLDING_AMOUNT = {str(holding_amount)}, "
           f"SHOWN_AMOUNT = {str(shown_amount)}, "
           f"DAILY_SHARE = {str(daily_share)}, DAILY_AMOUNT = {str(daily_amount)} WHERE "
           f"CODE = '{code}'")
    con.execute_cursor(sql)


def select_quantity_info(plan_id: int, module_id: int, code):
    con = DBConnector(plan_id, module_id)
    sql = (f"SELECT FEE_FREE_LIMIT, DAILY_SHARE, DAILY_AMOUNT FROM {con.table_name} "
           f"WHERE CODE = '{code}'")
    res = con.execute_cursor(sql)
    return res


def select_code_priority_list(plan_id: int, module_id: int):
    con = DBConnector(plan_id, module_id)
    sql = f"SELECT DISTINCT CODE FROM {con.table_name} ORDER BY DAILY_AMOUNT DESC, HOLDING_AMOUNT DESC"
    res = con.execute_cursor(sql)
    return res
