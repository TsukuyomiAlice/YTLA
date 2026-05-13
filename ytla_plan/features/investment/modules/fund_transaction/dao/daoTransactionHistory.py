# coding=utf-8

from core.classic.frame.database.func import sqliteConnector

"""
（暂时）数据库路径指定在下方
如果有独立的数据库连接，可以在此处添加
"""
db_name = 'Transaction'
table_name = "TRANSACTION_HISTORY"


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
          f" TRANSACTION_ID integer," \
          f" CODE varchar(6) not null," \
          f" TRANSACTION_DATE date not null," \
          f" TRANSACTION_TYPE varchar(2) not null," \
          f" TOTAL_PRICE double," \
          f" SHARE double," \
          f" UNIT_PRICE double," \
          f" TRANSACTION_FEE double," \
          f" FUND_NAME varchar," \
          f" primary key (TRANSACTION_ID)" \
          f");"
    execute_cursor(sql)


"""
下方Instance方法
"""


class Instance:

    def __init__(self, transaction_id: int):
        self.transaction_id = transaction_id
        self.code: str = ''
        self.fund_name: str = ''
        self.transaction_date: str = ''
        self.transaction_type: str = ''
        self.amount: float = 0
        self.share: float = 0
        self.price: float = 0
        self.transaction_fee: float = 0

    def get_instance_by_pk(self):
        db_res = transaction_history_select_id(self.transaction_id)
        if len(db_res) == 1:
            self.code = db_res[0]['CODE']
            self.fund_name = db_res[0]['FUND_NAME']
            self.transaction_date = db_res[0]['TRANSACTION_DATE']
            self.transaction_type = db_res[0]['TRANSACTION_TYPE']
            self.amount = db_res[0]['TOTAL_PRICE']
            self.share = db_res[0]['SHARE']
            self.price = db_res[0]['UNIT_PRICE']
            self.transaction_fee = db_res[0]['TRANSACTION_FEE']


def instance_list(pk_list: list):
    res = []
    for i in pk_list:
        p = Instance(i)
        p.get_instance_by_pk()
        res.append(p)
    return res


def instance_list_by_code(code: str):
    pk_list = get_transaction_list(code)
    if len(pk_list) > 0:
        for i in range(len(pk_list)):
            pk_list[i] = pk_list[i]['TRANSACTION_ID']
    return instance_list(pk_list)


"""
下方DAO方法
"""


def transaction_history_generate_id():
    """
    生成交易ID
    """
    sql = f"SELECT TRANSACTION_ID FROM {table_name} ORDER BY TRANSACTION_ID DESC LIMIT 1"
    res = execute_cursor(sql)
    transaction_id = 1 if len(res) == 0 else res[0]['TRANSACTION_ID'] + 1
    return transaction_id


def transaction_history_new_insert(code, transaction_date, transaction_type, total_price, share):
    """
    新建交易
    :param code:
    :param transaction_date:
    :param transaction_type:
    :param total_price:
    :param share:
    :return:
    """
    transaction_id = transaction_history_generate_id()
    sql = f"INSERT INTO TRANSACTION_HISTORY(TRANSACTION_ID, CODE, TRANSACTION_DATE, TRANSACTION_TYPE, TOTAL_PRICE, " \
          f"SHARE, UNIT_PRICE, TRANSACTION_FEE) VALUES " \
          f"({str(transaction_id)}, '{code}', '{transaction_date}', '{transaction_type}', {str(total_price)}, " \
          f"{str(share)}, 0, 0)"
    res = execute_cursor(sql)
    return res


def transaction_history_select_id(transaction_id):
    """
    抽取交易(指定交易编号)
    :param transaction_id:
    :return:
    """
    sql = f"SELECT TRANSACTION_ID, CODE, FUND_NAME, TRANSACTION_DATE, TRANSACTION_TYPE, TOTAL_PRICE, " \
          f"SHARE, UNIT_PRICE, TRANSACTION_FEE FROM TRANSACTION_HISTORY WHERE TRANSACTION_ID = {str(transaction_id)}"
    res = execute_cursor(sql)
    return res


def get_transaction_list(code):
    sql = (f"SELECT TRANSACTION_ID FROM {table_name} WHERE CODE = '{code}' "
           f"ORDER BY TRANSACTION_DATE ASC, TRANSACTION_TYPE DESC")
    res = execute_cursor(sql)
    return res


def transaction_history_new_full_insert(
        code, transaction_date, transaction_type, total_price, share, unit_price, transaction_fee, fund_name):
    """
    插入完整交易
    :param code:
    :param transaction_date:
    :param transaction_type:
    :param total_price:
    :param share:
    :param unit_price:
    :param transaction_fee:
    :param fund_name:
    :return:
    """
    transaction_id = transaction_history_generate_id()
    sql = f"INSERT INTO TRANSACTION_HISTORY(TRANSACTION_ID, CODE, TRANSACTION_DATE, TRANSACTION_TYPE, TOTAL_PRICE, " \
          f"SHARE, UNIT_PRICE, TRANSACTION_FEE, FUND_NAME) VALUES " \
          f"({str(transaction_id)}, '{code}', '{transaction_date}', '{transaction_type}', {str(total_price)}, " \
          f"{str(share)}, {str(unit_price)}, {str(transaction_fee)}, '{fund_name}')"
    res = execute_cursor(sql)
    return res


def transaction_history_select(code):
    """
    抽取交易(按交易日期降序)
    :param code:
    :return:
    """
    sql = f"SELECT * FROM TRANSACTION_HISTORY WHERE CODE = '{code}' " \
          f"ORDER BY TRANSACTION_DATE DESC, TRANSACTION_TYPE DESC, TRANSACTION_ID ASC"
    res = execute_cursor(sql)
    return res


def transaction_history_select_asc(code):
    """
    抽取交易(按交易日期升序)
    :param code:
    :return:
    """
    sql = f"SELECT * FROM TRANSACTION_HISTORY WHERE CODE = '{code}' " \
          f"ORDER BY TRANSACTION_DATE ASC, TRANSACTION_TYPE DESC, TRANSACTION_ID ASC"
    res = execute_cursor(sql)
    return res


def transaction_history_select_after_date_asc(code, transaction_date):
    """
    抽取交易(按交易日期升序)
    :param code:
    :param transaction_date:
    :return:
    """
    sql = f"SELECT * FROM TRANSACTION_HISTORY WHERE CODE = '{code}' " \
          f"AND TRANSACTION_DATE > '{transaction_date}' " \
          f"ORDER BY TRANSACTION_DATE ASC, TRANSACTION_TYPE DESC"
    res = execute_cursor(sql)
    return res


def transaction_history_select_multi_id(transaction_ids):
    """
    抽取交易(多比交易)
    :param transaction_ids:
    :return:
    """
    sql = f"SELECT TRANSACTION_ID, CODE, FUND_NAME, TRANSACTION_DATE, TRANSACTION_TYPE, TOTAL_PRICE, " \
          f"SHARE, UNIT_PRICE, TRANSACTION_FEE FROM TRANSACTION_HISTORY WHERE TRANSACTION_ID in {transaction_ids}"
    res = execute_cursor(sql)
    return res


def transaction_history_update(transaction_id, transaction_type, total_price, share, unit_price, transaction_fee):
    """
    更新交易情报
    :param transaction_id:
    :param transaction_type:
    :param total_price:
    :param share:
    :param unit_price:
    :param transaction_fee:
    :return:
    """
    sql = f"UPDATE TRANSACTION_HISTORY " \
          f"SET TRANSACTION_TYPE = '{transaction_type}', " \
          f"TOTAL_PRICE = {str(total_price)}, " \
          f"SHARE = {str(share)}, " \
          f"UNIT_PRICE = {str(unit_price)}, " \
          f"TRANSACTION_FEE = {str(transaction_fee)} " \
          f"WHERE ID = {str(transaction_id)}"
    res = execute_cursor(sql)
    return res


def transaction_history_delete(transaction_id):
    """
    删除不正确的交易内容
    :param transaction_id:
    :return:
    """
    sql = f"DELETE FROM TRANSACTION_HISTORY WHERE TRANSACTION_ID = {str(transaction_id)}"
    res = execute_cursor(sql)
    return res


def transaction_history_get_id(code):
    """
    获取最近的交易
    :param code:
    :return:
    """
    sql = f"SELECT TRANSACTION_ID FROM TRANSACTION_HISTORY WHERE CODE = '{code}' ORDER BY TRANSACTION_ID DESC LIMIT 1"
    res = execute_cursor(sql)
    return res


def transaction_history_get_id_all(code):
    """
    获取最近的交易
    :param code:
    :return:
    """
    sql = f"SELECT TRANSACTION_ID FROM TRANSACTION_HISTORY WHERE CODE = '{code}' " \
          f"AND TRANSACTION_TYPE IN ('01', '11', '21', '31', '41') " \
          f"ORDER BY TRANSACTION_DATE"
    res = execute_cursor(sql)
    return res


def transaction_fund_code_get():
    """
    获取所有存在的交易的交易记录
    """
    sql = f"SELECT DISTINCT CODE FROM {table_name}"
    res = execute_cursor(sql)
    return res


def check_share_change_records(code, transaction_date, transaction_id):
    sql = f"SELECT COUNT(*) AS COUNT FROM TRANSACTION_HISTORY WHERE " \
          f"CODE = '{code}' AND TRANSACTION_TYPE = '28' AND " \
          f"TRANSACTION_DATE = '{transaction_date}' and transaction_id < {transaction_id}"
    res = execute_cursor(sql)[0]['COUNT']
    return res


def select_appointed_transactions(code):
    sql = f"SELECT TRANSACTION_ID, TRANSACTION_TYPE, TOTAL_PRICE, SHARE FROM TRANSACTION_HISTORY WHERE " \
          f"CODE = '{code}' AND TRANSACTION_TYPE IN ('01', '11')"
    res = execute_cursor(sql)
    return res


def select_plain_fund_name_list():
    sql = f"SELECT DISTINCT CODE FROM {table_name} WHERE FUND_NAME = ''"
    res = execute_cursor(sql)
    return res


def update_fund_name(code, fund_name):
    sql = f"UPDATE TRANSACTION_HISTORY SET FUND_NAME = '{fund_name}' WHERE CODE = '{code}'"
    execute_cursor(sql)


def transaction_sum(code, transaction_type):
    sql = (f"SELECT SUM(SHARE), SUM(TOTAL_PRICE) FROM {table_name} "
           f"WHERE CODE = '{code}' AND TRANSACTION_TYPE IN ({transaction_type})")
    res = execute_cursor(sql)[0]
    result = [0, 0]
    if res[0] is not None:
        result[0] = res[0]
    if res[1] is not None:
        result[1] = res[1]
    return result


def maintain_get_transaction_list():
    sql = f"SELECT TRANSACTION_ID FROM {table_name} ORDER BY TRANSACTION_DATE ASC, TRANSACTION_ID ASC"
    res = execute_cursor(sql)
    return res


def maintain_update_transaction_list(old_transaction_id, new_transaction_id):
    sql = (f"UPDATE {table_name} SET "
           f"TRANSACTION_ID = {str(new_transaction_id)} WHERE TRANSACTION_ID = {str(old_transaction_id)}")
    execute_cursor(sql)


def update_transactions_to_confirmed():
    sql = f"UPDATE {table_name} SET TRANSACTION_TYPE = '09' WHERE TRANSACTION_TYPE = '01'"
    execute_cursor(sql)
    sql = f"UPDATE {table_name} SET TRANSACTION_TYPE = '19' WHERE TRANSACTION_TYPE = '11'"
    execute_cursor(sql)
    sql = f"UPDATE {table_name} SET TRANSACTION_TYPE = '29' WHERE TRANSACTION_TYPE = '21'"
    execute_cursor(sql)
    sql = f"UPDATE {table_name} SET TRANSACTION_TYPE = '39' WHERE TRANSACTION_TYPE = '31'"
    execute_cursor(sql)
    sql = f"UPDATE {table_name} SET TRANSACTION_TYPE = '49' WHERE TRANSACTION_TYPE = '41'"
    execute_cursor(sql)
