# encode = utf-8

from core.domain.area.frame.func import sqliteConnector

"""
（暂时）数据库路径指定在下方
如果有独立的数据库连接，可以在此处添加
"""
db_name = 'language_cefr'
table_name = "VOCABULARY_LIST"


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
    sql = (f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
            BASE_WORD TEXT NOT NULL,
            GUIDE_WORD TEXT,
            LEVEL TEXT NOT NULL,
            PARD_OF_SPEECH TEXT,
            TOPIC TEXT
        )
    ''')
    execute_cursor(sql)


"""
下方DAO方法
"""
def insert_data(data):
    sql = f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?)"
    execute_cursor(sql, data)

def pick_step_1_words(level: str, amount: int):
    level_exclude = {
        "A1" : "''",
        "A2" : "'A1'",
        "B1" : "'A1', 'A2'",
        "B2" : "'A1', 'A2', 'B1'",
        "C1" : "'A1', 'A2', 'B1', 'B2'",
        "C2" : "'A1', 'A2', 'B1', 'B2', 'C1'",
    }
    sql = f"select distinct BASE_WORD from (select distinct BASE_WORD from {table_name} where LEVEL = ? AND GUIDE_WORD = '' AND BASE_WORD NOT IN (SELECT BASE_WORD FROM {table_name} WHERE LEVEL IN ({level_exclude[level]}))) ORDER BY RANDOM() LIMIT ?"
    res = execute_cursor(sql, [level, amount])
    ret = []
    for row in res:
        ret.append(row['BASE_WORD'])
    return ret


def pick_step_2_words(level: str):
    sql = (f"select distinct BASE_WORD, GUIDE_WORD from {table_name} where "
           f"LEVEL = ? and GUIDE_WORD NOT IN ('', 'IDIOM' ) "
           f"GROUP BY GUIDE_WORD ORDER BY random() limit 40")
    res = execute_cursor(sql, [level])
    return res


def get_pure_new_words(level_count:str):
    level_exclude = {
        'A1': '',
        'A2': 'A1',
        'B1': 'A1, A2',
        'B2': 'A1, A2, B1',
        'C1': 'A1, A2, B1, B2',
        'C2': 'A1, A2, B1, B2, C1',
    }
    sql = (f"select count(*) from (select distinct BASE_WORD from {table_name} where "
           f"LEVEL = ? "
           f"AND BASE_WORD NOT IN (SELECT BASE_WORD FROM {table_name} WHERE LEVEL IN (?)))")
    res = execute_cursor(sql, [level_count, level_exclude[level_count]])
    return res