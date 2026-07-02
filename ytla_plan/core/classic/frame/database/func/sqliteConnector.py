# coding=utf-8

import os
import sqlite3

from core.classic.frame._type.func import loggerConfig


def _slash():
    """Get OS-appropriate path separator."""
    return '/' if os.name == 'posix' else '\\'


def database_root(db_name):
    """
    Get predefined database path from configuration (structured layout)

    New path structure:
        {base}/{feature_type}/{feature_subtype}/{filename}

    Example:
        >>> database_root('life_plan')
        'D:\\\\YTLA_DATA\\\\ytla_plan\\\\plans\\\\plan\\\\life_plan.db'

    :param db_name: str - Predefined database identifier in config
    :return: str - Full database file path with .db extension
    """
    from core.classic.frame.database.process.processDatabaseSqlite import get_db_files, db_folder_path
    s = _slash()
    db_files = get_db_files()
    entry = db_files.get(db_name)
    if entry is None:
        raise KeyError(f"Database '{db_name}' not found in configuration")
    if isinstance(entry, str):
        # 兼容旧版简单字符串映射
        return f'{db_folder_path}{s}{entry}'
    return f'{db_folder_path}{s}{entry["feature_type"]}{s}{entry["feature_subtype"]}{s}{entry["filename"]}'


def database_root_specific(db_name):
    """
    Generate direct database path for immediate use

    Use case:
        - Temporary databases
        - Non-configured database files

    Example:
        >>> database_root_specific('temp_data')
        'path/from/config/temp_data.db'

    :param db_name: str - Direct database name (without extension)
    :return: str - Full database path with automatic .db suffix
    """
    from core.classic.frame.database.process.processDatabaseSqlite import db_folder_path
    s = _slash()
    return f'{db_folder_path}{s}{db_name}.db'


def database_root_plan(plan_id: int) -> str:
    """
    Get database path for plan-specific database.

    Path: {base}/plan_{plan_id}/plan_{plan_id}.db

    Example:
        >>> database_root_plan(1)
        'D:\\\\YTLA_DATA\\\\ytla_plan\\\\plan_1\\\\plan_1.db'

    :param plan_id: int - Plan ID
    :return: str - Full database file path
    """
    from core.classic.frame.database.process.processDatabaseSqlite import db_folder_path
    s = _slash()
    return f'{db_folder_path}{s}plan_{plan_id}{s}plan_{plan_id}.db'


def database_root_plan_module(plan_id: int, module_id: int, db_filename: str) -> str:
    """
    Get database path for plan+module-specific database.

    Path: {base}/plan_{plan_id}/module_{module_id}/{db_filename}.db

    Example:
        >>> database_root_plan_module(1, 5, 'transactions')
        'D:\\\\YTLA_DATA\\\\ytla_plan\\\\plan_1\\\\module_5\\\\transactions.db'

    :param plan_id: int - Plan ID
    :param module_id: int - Module ID
    :param db_filename: str - Database filename (without extension)
    :return: str - Full database file path
    """
    from core.classic.frame.database.process.processDatabaseSqlite import db_folder_path
    s = _slash()
    return f'{db_folder_path}{s}plan_{plan_id}{s}module_{module_id}{s}{db_filename}.db'


def sqlite_cursor(database_path, sql, params):
    """
    Secure method for executing parameterized SQL queries

    Features:
    - Establishes database connection and creates cursor
    - Automatic transaction commit/rollback handling
    - Auto-creates parent directories and database file if not exists
    - Ensures resource cleanup (connection/cursor closure)
    - Error logging and exception handling

    :param database_path: str - Absolute path to database file
    :param sql: str - SQL statement with ? placeholders
    :param params: Tuple/List - Parameter values for SQL injection prevention
    :return: List[Dict] - Query results as list of dictionaries (empty list for non-SELECT)
    :raises sqlite3.Error: Propagates exceptions after logging
    """
    db_dir = os.path.dirname(database_path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
    conn = sqlite3.connect(database_path)
    res = []
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            if cursor.description:
                columns = [col[0] for col in cursor.description]
                rows = cursor.fetchall()
                res = [dict(zip(columns, row)) for row in rows]
            else:
                res = cursor.fetchall()

            loggerConfig.db_info_logger.info(f"\nSQL Executed: {sql}\nParams: {params}\n")

    except sqlite3.Error as e:
        loggerConfig.db_error_logger.error(f"\nSQL Failed: {sql}\nParams: {params}\nDetails: {str(e)}\n")
        raise
    finally:
        conn.close()

    return res


def execute_cursor(db, sql, params):
    """
    Universal DB operation method using predefined database mappings

    Example:
    >>> execute_cursor('main_db', 'SELECT * FROM users WHERE id=?', (1,))

    :param db: str - Database identifier from config
    :param sql: str - SQL statement with placeholders
    :param params: Tuple/List - Query parameters
    :return: List[Dict] - Query results
    """
    path = database_root(db)
    return sqlite_cursor(path, sql, params)


def execute_cursor_with_db(db, sql, params):
    """
    Direct database file operation method

    Example:
    >>> execute_cursor_with_db('custom_db', 'INSERT INTO logs VALUES (?,?)', ('error', 500))

    :param db: str - Direct database filename (without extension)
    :param sql: str - SQL statement with placeholders
    :param params: Tuple/List - Query parameters
    :return: List[Dict] - Query results
    """
    path = database_root_specific(db)
    return sqlite_cursor(path, sql, params)


def execute_cursor_plan(plan_id: int, sql, params):
    """
    Database operation for plan-specific database.

    Uses database_root_plan() to locate the database file.

    Example:
    >>> execute_cursor_plan(1, 'SELECT * FROM MODULE_5 WHERE RECORD_ID=?', (1,))

    :param plan_id: int - Plan ID
    :param sql: str - SQL statement with placeholders
    :param params: Tuple/List - Query parameters
    :return: List[Dict] - Query results
    """
    path = database_root_plan(plan_id)
    return sqlite_cursor(path, sql, params)


def execute_cursor_plan_module(plan_id: int, module_id: int, db_filename: str, sql, params):
    """
    Database operation for plan+module-specific database.

    Uses database_root_plan_module() to locate the database file.

    Example:
    >>> execute_cursor_plan_module(1, 5, 'transactions', 'SELECT * FROM ...', ())

    :param plan_id: int - Plan ID
    :param module_id: int - Module ID
    :param db_filename: str - Database filename (without extension)
    :param sql: str - SQL statement with placeholders
    :param params: Tuple/List - Query parameters
    :return: List[Dict] - Query results
    """
    path = database_root_plan_module(plan_id, module_id, db_filename)
    return sqlite_cursor(path, sql, params)
