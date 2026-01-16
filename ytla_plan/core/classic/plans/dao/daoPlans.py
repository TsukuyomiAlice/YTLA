# coding=utf-8

import json
from core.classic.frame.func import sqliteConnector

"""
(Temporary) Database path is specified below.
If there's an independent database connection, it can be added here.
"""
DB_NAME = 'life_plan'
TABLE_NAME = "PLANS"


def execute_cursor(sql, params=None) -> list[dict]:
    """
    Execute parameterized database query (secure version).

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
    res = sqliteConnector.execute_cursor(DB_NAME, sql, params)
    return res


def drop_table():
    """Drop the table from the database."""
    sql = f"DROP TABLE {TABLE_NAME}"
    execute_cursor(sql)


def truncate_table():
    """
    Clear all data from the table and vacuum the database.

    This performs a DELETE operation followed by VACUUM to reclaim storage space.
    """
    sql1 = f"DELETE FROM {TABLE_NAME} where 1 = 1"
    execute_cursor(sql1)
    sql2 = "VACUUM"
    execute_cursor(sql2)


def create_table():
    """
    Create the table if it doesn't exist.

    The table structure includes:
    - PLAN_ID: Primary key, auto-incrementing integer
    - NAME: Required text field
    - TAGS: Optional text field
    - MODULE_GROUPS: Text field for module groups
    - DESCRIPTION: Optional text field
    - ICON_PATH: Path to icon image
    - BACKGROUND_PATH: Path to background image
    - DETAIL_PARAMS: JSON parameters
    - ACTIVE_FLAG: Default '1' (active)
    - DELETE_FLAG: Default '0' (not deleted)
    """
    sql = f'''
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            PLAN_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            TAGS TEXT,
            MODULE_GROUPS TEXT,
            DESCRIPTION TEXT,
            ICON_PATH TEXT,
            BACKGROUND_PATH TEXT,
            DETAIL_PARAMS TEXT,
            ACTIVE_FLAG TEXT DEFAULT '1',
            DELETE_FLAG TEXT DEFAULT '0'
        )
    '''
    execute_cursor(sql)


"""
Instance methods below
"""


class Instance:
    """Represents a plan instance with all its attributes."""

    def __init__(self, name: str, **kwargs):
        """
        Initialize a plan instance.

        Args:
            name (str): Name of the plan
            **kwargs: Additional parameters including:
                - plan_id (int): ID of the plan if it exists in database
        """
        if 'plan_id' in kwargs:
            self.plan_id: int = kwargs['plan_id']
        else:
            self.plan_id: int = 0
        self.name = name
        self.tags: str = ''
        self.module_groups: str = ''
        self.description: str = ''
        self.icon_path: str = ''
        self.background_path: str = ''
        self.detail_params: str = '{}'
        self.active_flag: str = ''
        self.delete_flag: str = ''

    def get_instance_by_pk(self) -> dict:
        """
        Retrieve plan instance from database by primary key.

        Returns:
            dict: Dictionary containing all plan attributes
        """
        if self.plan_id != 0:
            db_res = select_all_by_pk(self.name, plan_id=self.plan_id)
        else:
            db_res = select_all_by_pk(self.name)
        return db_res[0]

    def set_instance(self, db_res: dict) -> None:
        """
        Set instance attributes from database result.

        Args:
            db_res (dict): Dictionary containing plan attributes from database
        """
        if len(db_res) != 10:
            return
        self.plan_id = db_res['PLAN_ID']
        self.name = db_res['NAME']
        self.tags = db_res['TAGS']
        self.module_groups = db_res['MODULE_GROUPS']
        self.description = db_res['DESCRIPTION']
        self.icon_path = db_res['ICON_PATH']
        self.background_path = db_res['BACKGROUND_PATH']
        self.detail_params = db_res['DETAIL_PARAMS']
        self.active_flag = db_res['ACTIVE_FLAG']
        self.delete_flag = db_res['DELETE_FLAG']


def instance_list(pk_list: list) -> list:
    """
    Get a list of plan instances from a list of primary keys.

    Args:
        pk_list (list): List of primary keys

    Returns:
        list: List of plan instances
    """
    res = []
    for i in pk_list:
        p = Instance(i)
        p.set_instance(p.get_instance_by_pk())
        res.append(p)
    return res


def select_all_by_pk(name, **kwargs) -> list[dict]:
    """
    Select plan by primary key (name or name + plan_id).

    Args:
        name (str): Name of the plan
        **kwargs: Additional parameters including:
            - plan_id (int): ID of the plan

    Returns:
        list[dict]: List of matching plans
    """
    plan_id_phrase = "PLAN_ID = ? AND " if 'plan_id' in kwargs else ''
    params = (kwargs.get('plan_id'), name) if 'plan_id' in kwargs else (name,)
    sql = (f"SELECT PLAN_ID, NAME, TAGS, MODULE_GROUPS, DESCRIPTION, "
           f"ICON_PATH, BACKGROUND_PATH, DETAIL_PARAMS, ACTIVE_FLAG, DELETE_FLAG "
           f"FROM {TABLE_NAME} WHERE {plan_id_phrase} NAME = ?")
    res = execute_cursor(sql, params)
    return res


"""
DAO methods below
"""


def add_plan(plan: Instance) -> None:
    """
    Add a new plan to the database.

    Args:
        plan (Instance): Plan instance to be added
    """
    sql = f"""
           INSERT INTO {TABLE_NAME} (NAME, TAGS, MODULE_GROUPS, DESCRIPTION, 
           ICON_PATH, BACKGROUND_PATH, DETAIL_PARAMS, ACTIVE_FLAG, DELETE_FLAG) 
           VALUES (?, ?, ?, ?, ?, ?, ?, '1', '0')
            """
    execute_cursor(sql, (plan.name, plan.tags, plan.module_groups,
                         plan.description, plan.icon_path,
                         plan.background_path, plan.detail_params))


def get_plan_name_by_plan_id(plan_id: int) -> str:
    """
    Get plan name by plan ID.

    Args:
        plan_id (int): ID of the plan

    Returns:
        str: Name of the plan, or None if not found
    """
    sql = f'SELECT NAME FROM {TABLE_NAME} WHERE PLAN_ID = ?'
    res = execute_cursor(sql, (plan_id,))
    if len(res) > 0:
        return res[0]['NAME']
    else:
        return None


def get_plan_from_db() -> list[dict]:
    """
    Retrieve all active plans from database (not deleted).

    Returns:
        list[dict]: List of all active plans
    """
    sql = (f'SELECT DISTINCT PLAN_ID, NAME, TAGS, MODULE_GROUPS, DESCRIPTION, '
           f'ICON_PATH, BACKGROUND_PATH, DETAIL_PARAMS, ACTIVE_FLAG, DELETE_FLAG '
           f'FROM {TABLE_NAME} WHERE DELETE_FLAG = 0')
    res = execute_cursor(sql)
    return res


def get_plans() -> list[dict]:
    """
    Get all plans as dictionaries.

    Returns:
        list[dict]: List of plan dictionaries
    """
    plan_list = get_plan_from_db()
    plans = []
    for plan in plan_list:
        ins = Instance(plan['NAME'], plan_id=plan['PLAN_ID'])
        ins.set_instance(plan)
        plan_dict = convert_to_dict(ins)
        plans.append(plan_dict)
    return plans


def convert_to_dict(plan: Instance) -> dict:
    """
    Convert plan instance to dictionary.

    Args:
        plan (Instance): Plan instance to convert

    Returns:
        dict: Dictionary representation of the plan
    """
    plan_dict = {
        "plan_id": plan.plan_id,
        "name": plan.name,
        "tags": plan.tags,
        "module_groups": plan.module_groups,
        "description": plan.description,
        "icon_path": plan.icon_path,
        "background_path": plan.background_path,
        "detail_params": json.loads(plan.detail_params),
        "delete_flag": plan.delete_flag,
        "active_flag": plan.active_flag
    }
    return plan_dict


def soft_delete_plan(plan_id: int) -> None:
    """
    Mark a plan as deleted (soft delete).

    Args:
        plan_id (int): ID of the plan to delete
    """
    sql = f"UPDATE {TABLE_NAME} SET DELETE_FLAG = '1' WHERE PLAN_ID = ?"
    execute_cursor(sql, (plan_id,))


def check_plan_delete_status(plan_id: int) -> str:
    """
    Check if a plan is marked as deleted.

    Args:
        plan_id (int): ID of the plan to check

    Returns:
        str: '1' if deleted, '0' if not, '1' if plan not found
    """
    sql = f'SELECT DELETE_FLAG FROM {TABLE_NAME} WHERE PLAN_ID = ?'
    res = execute_cursor(sql, (plan_id,))
    if len(res) > 0:
        return res[0]['DELETE_FLAG']
    else:
        return '1'


def deactivate_plan(plan_id: int) -> None:
    """
    Deactivate a plan.

    Args:
        plan_id (int): ID of the plan to deactivate
    """
    sql = f"UPDATE {TABLE_NAME} SET ACTIVE_FLAG = '0' WHERE PLAN_ID = ?"
    execute_cursor(sql, (plan_id,))


def activate_plan(plan_id: int) -> None:
    """
    Activate a plan.

    Args:
        plan_id (int): ID of the plan to activate
    """
    sql = f"UPDATE {TABLE_NAME} SET ACTIVE_FLAG = '1' WHERE PLAN_ID = ?"
    execute_cursor(sql, (plan_id,))


def check_plan_active_status(plan_id: int) -> str:
    """
    Check if a plan is active.

    Args:
        plan_id (int): ID of the plan to check

    Returns:
        str: '1' if active, '0' if not, '0' if plan not found
    """
    sql = f'SELECT ACTIVE_FLAG FROM {TABLE_NAME} WHERE PLAN_ID = ?'
    res = execute_cursor(sql, (plan_id,))
    if len(res) > 0:
        return res[0]['ACTIVE_FLAG']
    else:
        return '0'


def update_plan_detail(plan: Instance) -> None:
    """
    Update plan details in the database.

    Args:
        plan (Instance): Plan instance with updated details
    """
    sql = (f"UPDATE {TABLE_NAME} SET NAME = ?, TAGS = ?, MODULE_GROUPS = ?, "
           f"DESCRIPTION =?, ICON_PATH = ?, BACKGROUND_PATH = ?, "
           f"DETAIL_PARAMS = ? WHERE PLAN_ID = ?")
    params = (plan.name, plan.tags, plan.module_groups, plan.description,
              plan.icon_path, plan.background_path, plan.detail_params,
              plan.plan_id)
    execute_cursor(sql, params)


def get_last_new_plan_id() -> int:
    """
    Get the ID of the most recently created empty plan.

    Returns:
        int: ID of the most recent empty plan
    """
    blank_bracket = '{}'
    sql = (f"SELECT PLAN_ID FROM {TABLE_NAME} "
           f"WHERE TAGS = '' AND DESCRIPTION = '' AND DETAIL_PARAMS = '{blank_bracket}' "
           f"AND ACTIVE_FLAG = '1' AND DELETE_FLAG = '0' "
           f"ORDER BY PLAN_ID DESC limit 1")
    res = execute_cursor(sql)
    return res[0]['PLAN_ID']
