# coding=utf-8

from core.classic.frame.database.func import sqliteConnector

"""
数据库路径: {base}/plan_{plan_id}/module_{module_id}/eight_characters.db
"""
db_name = 'eight_characters'
table_name = "EIGHT_CHARACTERS_HISTORY"


class DBConnector:
    """Database connector for eight characters history (plan+module scoped)."""

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
        res = sqliteConnector.execute_cursor_plan_module(self.plan_id, self.module_id, db_name, sql, params)
        return res

    def create_table(self):
        """
        创建 EIGHT_CHARACTERS_HISTORY 表
        :return:
        """
        sql = (f"CREATE TABLE IF NOT EXISTS {self.table_name}("
               f" RECORD_ID INTEGER PRIMARY KEY AUTOINCREMENT,"
               f" BIRTHDAY TEXT,"
               f" LUNAR_DATE TEXT,"
               f" BIRTH_TIME TEXT,"
               f" GENDER TEXT,"
               f" EIGHT_CHARACTERS TEXT,"
               f" LUCK_CYCLE TEXT,"
               f" FLEET_YEAR TEXT,"
               f" TEN_GODS_RATIO TEXT,"
               f" ANALYSIS_RESULT TEXT,"
               f" ANNOTATIONS TEXT,"
               f" CREATOR TEXT,"
               f" UPDATER TEXT,"
               f" UPDATE_DATETIME TEXT DEFAULT (datetime('now','localtime')),"
               f" DELETE_FLG TEXT DEFAULT '0'"
               f");")
        self.execute_cursor(sql)

    def drop_table(self):
        """
        删除表
        :return:
        """
        sql = f"DROP TABLE {self.table_name}"
        self.execute_cursor(sql)

    def truncate_table(self):
        """
        清空表
        :return:
        """
        sql1 = f"DELETE FROM {self.table_name} where 1 = 1"
        self.execute_cursor(sql1)
        sql2 = "VACUUM"
        self.execute_cursor(sql2)


"""
下方DAO方法
"""


def insert_history(plan_id: int, module_id: int, data_dict: dict) -> int:
    """
    插入历史记录
    :param plan_id: 计划ID
    :param module_id: 模块ID
    :param data_dict: 包含字段 BIRTHDAY, LUNAR_DATE, BIRTH_TIME, GENDER,
                      EIGHT_CHARACTERS, LUCK_CYCLE, FLEET_YEAR,
                      TEN_GODS_RATIO, ANALYSIS_RESULT, ANNOTATIONS, CREATOR
    :return: RECORD_ID
    """
    con = DBConnector(plan_id, module_id)
    fields = ["BIRTHDAY", "LUNAR_DATE", "BIRTH_TIME", "GENDER",
              "EIGHT_CHARACTERS", "LUCK_CYCLE", "FLEET_YEAR",
              "TEN_GODS_RATIO", "ANALYSIS_RESULT", "ANNOTATIONS",
              "CREATOR", "UPDATER"]
    values = []
    for f in fields:
        values.append(data_dict.get(f, ""))
    placeholders = ", ".join(["?" for _ in fields])
    field_names = ", ".join(fields)
    sql = (f"INSERT INTO {con.table_name}({field_names}) "
           f"VALUES ({placeholders})")
    con.execute_cursor(sql, values)
    # 获取刚插入的 RECORD_ID
    sql_id = f"SELECT last_insert_rowid() AS RID"
    res = con.execute_cursor(sql_id)
    return res[0]["RID"] if res else 0


def select_history_list(plan_id: int, module_id: int, creator: str = "", limit: int = 20, offset: int = 0) -> list:
    """
    查询历史记录列表（仅有效记录）
    :param plan_id: 计划ID
    :param module_id: 模块ID
    :param creator: 创建者用户名（可选，用于筛选）
    :param limit: 每页条数
    :param offset: 偏移量
    :return: 记录列表
    """
    con = DBConnector(plan_id, module_id)
    if creator:
        sql = (f"SELECT * FROM {con.table_name} "
               f"WHERE DELETE_FLG = '0' AND CREATOR = ? "
               f"ORDER BY UPDATE_DATETIME DESC "
               f"LIMIT ? OFFSET ?")
        params = [creator, limit, offset]
    else:
        sql = (f"SELECT * FROM {con.table_name} "
               f"WHERE DELETE_FLG = '0' "
               f"ORDER BY UPDATE_DATETIME DESC "
               f"LIMIT ? OFFSET ?")
        params = [limit, offset]
    res = con.execute_cursor(sql, params)
    return res


def select_history_by_eight_characters_and_gender(plan_id: int, module_id: int, eight_characters: str, gender: str) -> dict:
    """
    按八字+性别查询有效记录（用于去重 upsert）
    在同一 plan_id + module_id 范围内查找相同 EIGHT_CHARACTERS + GENDER 且未删除的记录
    :param plan_id: 计划ID
    :param module_id: 模块ID
    :param eight_characters: 八字字符串
    :param gender: 性别
    :return: 记录字典，未找到时返回 None
    """
    con = DBConnector(plan_id, module_id)
    sql = (f"SELECT * FROM {con.table_name} "
           f"WHERE DELETE_FLG = '0' AND EIGHT_CHARACTERS = ? AND GENDER = ? "
           f"ORDER BY UPDATE_DATETIME DESC LIMIT 1")
    res = con.execute_cursor(sql, [eight_characters, gender])
    return res[0] if res else None


def select_history_by_pk(plan_id: int, module_id: int, record_id: int) -> dict:
    """
    按主键查询单条记录（包含已删除记录）
    :param plan_id: 计划ID
    :param module_id: 模块ID
    :param record_id: 记录ID
    :return: 记录字典，未找到时返回 None
    """
    con = DBConnector(plan_id, module_id)
    sql = f"SELECT * FROM {con.table_name} WHERE RECORD_ID = ?"
    res = con.execute_cursor(sql, [record_id])
    return res[0] if res else None


def update_history(plan_id: int, module_id: int, record_id: int, data_dict: dict) -> bool:
    """
    更新历史记录
    :param plan_id: 计划ID
    :param module_id: 模块ID
    :param record_id: 记录ID
    :param data_dict: 需要更新的字段字典
    :return: 是否更新成功
    """
    con = DBConnector(plan_id, module_id)
    updatable_fields = ["BIRTHDAY", "LUNAR_DATE", "BIRTH_TIME", "GENDER",
                        "EIGHT_CHARACTERS", "LUCK_CYCLE", "FLEET_YEAR",
                        "TEN_GODS_RATIO", "ANALYSIS_RESULT", "ANNOTATIONS",
                        "UPDATER"]
    set_parts = []
    params = []
    for f in updatable_fields:
        if f in data_dict:
            set_parts.append(f"{f} = ?")
            params.append(data_dict[f])
    if not set_parts:
        return False
    # 自动更新 UPDATE_DATETIME
    set_parts.append("UPDATE_DATETIME = datetime('now','localtime')")
    params.append(record_id)
    sql = (f"UPDATE {con.table_name} "
           f"SET {', '.join(set_parts)} "
           f"WHERE RECORD_ID = ?")
    res = con.execute_cursor(sql, params)
    return res is not None


def soft_delete_history(plan_id: int, module_id: int, record_id: int) -> bool:
    """
    逻辑删除历史记录（按 RECORD_ID）
    :param plan_id: 计划ID
    :param module_id: 模块ID
    :param record_id: 记录ID
    :return: 是否删除成功
    """
    con = DBConnector(plan_id, module_id)
    sql = (f"UPDATE {con.table_name} "
           f"SET DELETE_FLG = '1', UPDATE_DATETIME = datetime('now','localtime') "
           f"WHERE RECORD_ID = ?")
    res = con.execute_cursor(sql, [record_id])
    return res is not None


def soft_delete_history_by_eight_characters_and_gender(plan_id: int, module_id: int, eight_characters: str, gender: str) -> bool:
    """
    逻辑删除历史记录（按 EIGHT_CHARACTERS + GENDER，用于统一检索 Key）
    :param plan_id: 计划ID
    :param module_id: 模块ID
    :param eight_characters: 八字字符串
    :param gender: 性别
    :return: 是否删除成功
    """
    con = DBConnector(plan_id, module_id)
    sql = (f"UPDATE {con.table_name} "
           f"SET DELETE_FLG = '1', UPDATE_DATETIME = datetime('now','localtime') "
           f"WHERE DELETE_FLG = '0' AND EIGHT_CHARACTERS = ? AND GENDER = ?")
    res = con.execute_cursor(sql, [eight_characters, gender])
    return res is not None
