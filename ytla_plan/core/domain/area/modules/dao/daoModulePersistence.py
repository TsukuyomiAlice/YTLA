# coding=utf-8
import json

from core.domain.area.frame.func import sqliteConnector


class DBConnector:
    """Database connector class for module persistence operations.

    Handles all database operations for a specific module within a plan.
    """

    def __init__(self, plan_id: int, module_id: int):
        """Initialize the database connector for a specific module.

        Args:
            plan_id (int): ID of the plan
            module_id (int): ID of the module
        """
        self.db_name = f"plan_{str(plan_id)}"
        self.table_name = f"MODULE_{str(module_id)}"
        self.create_table()

    def execute_cursor(self, sql: str, params=None) -> list[dict]:
        """Execute parameterized database query (secure version).

        Uses parameterized queries to execute SQL statements, suitable for scenarios
        involving user input or dynamic parameters. Effectively prevents SQL injection.
        Mainly used for DML statements with dynamic values (INSERT/UPDATE etc.).

        Args:
            sql (str): SQL statement with placeholders (e.g. using ? as parameter placeholder)
            params (Tuple/List): Parameter values corresponding to placeholders in SQL

        Returns:
            list[dict]: List of dictionaries containing query results
        """
        if params is None:
            params = []
        res = sqliteConnector.execute_cursor_with_db(self.db_name, sql, params)
        return res

    def drop_table(self):
        """Drop the module table from the database."""
        sql = f"DROP TABLE {self.table_name}"
        self.execute_cursor(sql)

    def truncate_table(self):
        """Truncate the module table (delete all records and vacuum the database)."""
        sql1 = f"DELETE FROM {self.table_name} where 1 = 1"
        self.execute_cursor(sql1)
        sql2 = "VACUUM"
        self.execute_cursor(sql2)

    def create_table(self):
        """Create the module table if it doesn't exist.

        The table structure includes:
        - RECORD_ID: Primary key
        - CONTENT: Module content
        - CREATOR: Creator username
        - UPDATER: Updater username
        - UPDATE_DATETIME: Last update timestamp
        - DELETE_FLG: Deletion flag ('0' for active, '1' for deleted)
        """
        sql = (f"CREATE TABLE IF NOT EXISTS {self.table_name}("
               f"RECORD_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
               f"CONTENT varchar, "
               f"CREATOR varchar, "
               f"UPDATER varchar, "
               f"UPDATE_DATETIME varchar, "
               f"DELETE_FLG varchar)")
        self.execute_cursor(sql)


class Instance:
    """Data instance class representing a single module record."""

    def __init__(self, record_id: int = None):
        """Initialize a module instance.

        Args:
            record_id (int, optional): Database record ID. Defaults to None.
        """
        self.record_id = record_id
        self.content: str = '{}'
        self.creator: str = ''
        self.updater: str = ''
        self.update_datetime: str = ''
        self.delete_flag: str = ''

    def load_persistence(self, plan_id: int, module_id: int) -> dict:
        """Load instance data from database.

        Args:
            plan_id (int): Plan ID
            module_id (int): Module ID

        Returns:
            dict: Database record data
        """
        db_res = select_all_by_pk(plan_id, module_id, self.record_id)[0]
        self.set_instance(db_res)
        return db_res

    def set_instance(self, db_res: dict):
        """Set instance properties from database record.

        Args:
            db_res (dict): Database record data
        """
        if len(db_res) != 6:
            return
        self.content = db_res['CONTENT']
        self.creator = db_res['CREATOR']
        self.updater = db_res['UPDATER']
        self.update_datetime = db_res['UPDATE_DATETIME']
        self.delete_flag = db_res['DELETE_FLG']


def instance_list(plan_id: int, module_id: int, pk_list: list) -> list:
    """Get a list of module instances for given record IDs.

    Args:
        plan_id (int): Plan ID
        module_id (int): Module ID
        pk_list (list): List of record IDs

    Returns:
        list: List of Instance objects
    """
    res = []
    for record_id in pk_list:
        p = Instance(record_id)
        p.set_instance(p.load_persistence(plan_id, module_id))
        res.append(p)
    return res


def select_all_by_pk(plan_id: int, module_id: int, record_id: int) -> list:
    """Select a module record by its primary key.

    Args:
        plan_id (int): Plan ID
        module_id (int): Module ID
        record_id (int): Record ID

    Returns:
        list: List of matching records (should contain 0 or 1 record)
    """
    con = DBConnector(plan_id, module_id)
    sql = f"SELECT RECORD_ID, CONTENT, CREATOR, UPDATER, UPDATE_DATETIME, DELETE_FLG FROM {con.table_name} WHERE RECORD_ID = ?"
    res = con.execute_cursor(sql, [record_id])
    return res


def get_content(plan_id: int, module_id: int, record_id: int = None) -> list:
    """Get module content from database.

    Args:
        plan_id (int): Plan ID
        module_id (int): Module ID
        record_id (int, optional): Specific record ID to retrieve. Defaults to None.

    Returns:
        list: List of matching records
    """
    con = DBConnector(plan_id, module_id)
    sql_param = ''
    if record_id is not None and isinstance(record_id, int):
        sql_param = f'AND RECORD_ID = {str(record_id)}'
    sql = f"SELECT RECORD_ID, CONTENT, CREATOR, UPDATER, UPDATE_DATETIME, DELETE_FLG FROM {con.table_name} WHERE DELETE_FLG = '0' {sql_param}"
    res = con.execute_cursor(sql)
    return res


def get_last_content(plan_id: int, module_id: int, user_name: str) -> dict:
    """Get the most recent content created by a specific user.

    Args:
        plan_id (int): Plan ID
        module_id (int): Module ID
        user_name (str): Creator username

    Returns:
        dict: Parsed JSON content, or None if no record found
    """
    con = DBConnector(plan_id, module_id)
    sql = f"SELECT CONTENT FROM {con.table_name} WHERE CREATOR = ? AND DELETE_FLG = '0' ORDER BY RECORD_ID DESC LIMIT 1"
    res = con.execute_cursor(sql, [user_name])
    if len(res) == 0:
        return None
    return json.loads(res[0]['CONTENT'])


def get_all_content(plan_id: int, module_id: int, user_name: str) -> list:
    """Get all content records created by a specific user.

    Args:
        plan_id (int): Plan ID
        module_id (int): Module ID
        user_name (str): Creator username

    Returns:
        list: List of parsed JSON content records
    """
    con = DBConnector(plan_id, module_id)
    sql = f"SELECT CONTENT FROM {con.table_name} WHERE CREATOR = ? AND DELETE_FLG = '0' ORDER BY RECORD_ID"
    res = con.execute_cursor(sql, [user_name])
    ret = []
    for _ in res:
        ret.append(json.loads(_['CONTENT']))
    return ret


def get_content_by_creator(plan_id: int, module_id: int, user_name: str) -> list:
    """Get all content records created by a specific user (alias of get_all_content).

    Args:
        plan_id (int): Plan ID
        module_id (int): Module ID
        user_name (str): Creator username

    Returns:
        list: List of parsed JSON content records
    """
    con = DBConnector(plan_id, module_id)
    sql = f"SELECT CONTENT FROM {con.table_name} WHERE CREATOR = ? AND DELETE_FLG = '0' ORDER BY RECORD_ID"
    res = con.execute_cursor(sql, [user_name])
    ret = []
    for _ in res:
        ret.append(json.loads(_['CONTENT']))
    return ret


def insert_content(plan_id: int, module_id: int, content: Instance) -> int:
    """Insert new content into the module.

    Args:
        plan_id (int): Plan ID
        module_id (int): Module ID
        content (Instance): Content instance to insert

    Returns:
        int: ID of the newly created record
    """
    con = DBConnector(plan_id, module_id)
    sql = f"INSERT INTO {con.table_name} (CONTENT, CREATOR, UPDATER, UPDATE_DATETIME, DELETE_FLG) VALUES (?,?,?,CURRENT_TIMESTAMP, '0')"
    params = (content.content, content.creator, content.creator)
    con.execute_cursor(sql, params)
    sql_ret = f"SELECT RECORD_ID FROM {con.table_name} WHERE CONTENT =? AND CREATOR =? AND UPDATER =? AND DELETE_FLG = '0' ORDER BY UPDATE_DATETIME DESC LIMIT 1"
    res = con.execute_cursor(sql_ret, params)[0]['RECORD_ID']
    return res


def update_content(plan_id: int, module_id: int, content: Instance) -> list:
    """Update existing content in the module.

    Args:
        plan_id (int): Plan ID
        module_id (int): Module ID
        content (Instance): Content instance to update

    Returns:
        list: Database execution result
    """
    con = DBConnector(plan_id, module_id)
    sql = f"UPDATE {con.table_name} SET CONTENT = ?, UPDATER = ?, UPDATE_DATETIME = CURRENT_TIMESTAMP WHERE RECORD_ID = ?"
    params = (content.content, content.updater, content.record_id)
    res = con.execute_cursor(sql, params)
    return res


def delete_content(plan_id: int, module_id: int, content: Instance) -> list:
    """Mark content as deleted in the module (soft delete).

    Args:
        plan_id (int): Plan ID
        module_id (int): Module ID
        content (Instance): Content instance to delete

    Returns:
        list: Database execution result
    """
    con = DBConnector(plan_id, module_id)
    sql = f"UPDATE {con.table_name} SET DELETE_FLG = '1' WHERE RECORD_ID = ?"
    res = con.execute_cursor(sql, [content.record_id])
    return res
