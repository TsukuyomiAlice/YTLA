# coding=utf-8

from core.classic.frame.database.func import sqliteConnector

"""
数据库路径: {base}/plan_{plan_id}/module_{module_id}/analyze_transaction.db
"""
table_name = "ANALYZE_TRANSACTION_BALANCE"


class DBConnector:
    """Database connector for analyze transaction balance (plan+module scoped)."""

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
        sql = (f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
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


def insert(plan_id: int, module_id: int, code, name, cur_price, cur_amount, holding_share, holding_avg_price,
           match_share_profit, match_amount_profit,
           match_share_hold, match_amount_paid, match_share_sold, match_amount_hold):
    con = DBConnector(plan_id, module_id)
    sql = (f"INSERT INTO {con.table_name} (CODE, NAME, CUR_PRICE, CUR_AMOUNT, HOLDING_SHARE, HOLDING_AVG_PRICE, "
           f"MATCH_SHARE_PROFIT, MATCH_AMOUNT_PROFIT, "
           f"MATCH_SHARE_HOLD, MATCH_AMOUNT_PAID, MATCH_SHARE_SOLD, MATCH_AMOUNT_HOLD) VALUES ("
           f"'{code}', '{name}', {str(cur_price)}, {str(cur_amount)}, {str(holding_share)}, {str(holding_avg_price)}, "
           f"{str(match_share_profit)}, {str(match_amount_profit)}, "
           f"{str(match_share_hold)}, {str(match_amount_paid)}, {str(match_share_sold)}, {str(match_amount_hold)}"
           f")")
    con.execute_cursor(sql)


def select_current_holding(plan_id: int, module_id: int, code):
    con = DBConnector(plan_id, module_id)
    sql = f"SELECT NAME, HOLDING_SHARE, CUR_AMOUNT FROM {con.table_name} WHERE CODE = '{code}'"
    res = con.execute_cursor(sql)
    return res
