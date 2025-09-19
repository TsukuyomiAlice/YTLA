# coding=utf-8

import os
import sqlite3

from ytla_plan.core.frame.func import loggerConfig, utilConfigs


def database_root(db_name):
    """
    Get predefined database path from configuration

    Handles:
    - Cross-platform path separators
    - Database name to filename mapping

    Example:
    >>> database_root('main_db')
    'path/from/config/main.db'

    :param db_name: str - Predefined database identifier in config
    :return: str - Full database file path with .db extension
    """
    slash = '/'
    if os.name == 'posix':
        slash = '/'
    if os.name == 'nt':
        slash = '\\'
    db_folder_path = utilConfigs.db_folder_path
    db_files = utilConfigs.db_files
    db_file_name = db_files.get(db_name)
    return f'{db_folder_path}{slash}{db_file_name}'


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
    slash = '/'
    if os.name == 'posix':
        slash = '/'
    if os.name == 'nt':
        slash = '\\'
    db_folder_path = utilConfigs.db_folder_path
    return f'{db_folder_path}{slash}{db_name}.db'


def sqlite_cursor(database_path, sql, params):
    """
    Secure method for executing parameterized SQL queries

    Features:
    - Establishes database connection and creates cursor
    - Automatic transaction commit/rollback handling
    - Ensures resource cleanup (connection/cursor closure)
    - Error logging and exception handling

    :param database_path: str - Absolute path to database file
    :param sql: str - SQL statement with ? placeholders
    :param params: Tuple/List - Parameter values for SQL injection prevention
    :return: List[Dict] - Query results as list of dictionaries (empty list for non-SELECT)
    :raises sqlite3.Error: Propagates exceptions after logging
    """
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
