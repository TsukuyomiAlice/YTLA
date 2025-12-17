# coding=utf-8

import json

from core.domain.area.frame.func import sqliteConnector

"""
(Temporary) Database path is specified below.
If there's an independent database connection, it can be added here.
"""
db_name = 'life_plan'
table_name = "MODULES"


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
    res = sqliteConnector.execute_cursor(db_name, sql, params)
    return res


def drop_table():
    """
    Default method to drop the module table from database.
    """
    sql = f"DROP TABLE {table_name}"
    execute_cursor(sql)


def truncate_table():
    """
    Default method to truncate the module table and vacuum the database.
    """
    sql1 = f"DELETE FROM {table_name} where 1 = 1"
    execute_cursor(sql1)
    sql2 = "VACUUM"
    execute_cursor(sql2)


def create_table():
    """
    Default method to create the module table if it doesn't exist.
    """
    sql = (f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
            MODULE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            BELONG_PLAN_ID INTEGER,
            BELONG_GROUP_NAME TEXT, 
            NAME TEXT NOT NULL,
            MODULE_TYPE TEXT NOT NULL,
            MODULE_SUB_TYPE TEXT,
            TAGS TEXT,
            DESCRIPTION TEXT,
            MESSAGE TEXT,
            ICON_PATH TEXT,
            BACKGROUND_PATH TEXT,
            DETAIL_PARAMS TEXT NOT NULL, 
            ACTIVE_FLAG TEXT DEFAULT '1',
            DELETE_FLAG TEXT DEFAULT '0'
        )
    ''')
    execute_cursor(sql)


"""
Module Instance methods
"""


class Instance:
    """
    Represents a module instance with all its attributes and database operations.
    """

    def __init__(self, name: str, module_type: str, **kwargs):
        """
        Initialize a module instance.

        Args:
            name (str): Name of the module
            module_type (str): Type of the module
            **kwargs: Additional parameters including:
                - module_id (int): ID of existing module (optional)
        """
        if 'module_id' in kwargs:
            self.module_id: int = kwargs['module_id']
        else:
            self.module_id: int = 0
        self.belong_plan_id: int = 0
        self.belong_group_name = ''
        self.name = name
        self.module_type = module_type
        self.module_sub_type = ''
        self.tags: str = ''
        self.description: str = ''
        self.message: str = ''
        self.icon_path: str = ''
        self.background_path: str = ''
        self.detail_params: str = '{}'
        self.active_flag: str = ''
        self.delete_flag: str = ''

    def get_instance_by_pk(self):
        """
        Retrieve module instance from database by primary key (name or module_id).

        Returns:
            dict: Module data from database
        """
        if self.module_id != 0:
            db_res = select_all_by_pk(self.name, module_id=self.module_id)
        else:
            db_res = select_all_by_pk(self.name)
        return db_res[0]

    def set_instance(self, db_res: dict):
        """
        Set instance attributes from database result.

        Args:
            db_res (dict): Database result containing module attributes
        """
        if len(db_res) != 14:
            return
        self.module_id = db_res['MODULE_ID']
        self.belong_plan_id = db_res['BELONG_PLAN_ID']
        self.belong_group_name = db_res['BELONG_GROUP_NAME']
        self.name = db_res['NAME']
        self.module_type = db_res['MODULE_TYPE']
        self.module_sub_type = db_res['MODULE_SUB_TYPE']
        self.tags = db_res['TAGS']
        self.description = db_res['DESCRIPTION']
        self.message = db_res['MESSAGE']
        self.icon_path = db_res['ICON_PATH']
        self.background_path = db_res['BACKGROUND_PATH']
        self.detail_params = db_res['DETAIL_PARAMS']
        self.active_flag = db_res['ACTIVE_FLAG']
        self.delete_flag = db_res['DELETE_FLAG']


def instance_list(pk_list: list):
    """
    Create a list of module instances from primary key list.

    Args:
        pk_list (list): List of tuples containing (name, module_type)

    Returns:
        list: List of module instances
    """
    res = []
    for i in pk_list:
        p = Instance(i[0], i[1])
        p.set_instance(p.get_instance_by_pk())
        res.append(p)
    return res


def select_all_by_pk(name, **kwargs):
    """
    Select module by primary key (name and optionally module_id).

    Args:
        name (str): Module name
        **kwargs: Additional parameters including:
            - module_id (int): Module ID (optional)

    Returns:
        list: Database results matching the query
    """
    module_id_phrase = f"MODULE_ID = '{kwargs['module_id']}' AND " if 'module_id' in kwargs else ''
    sql = (
        f"SELECT MODULE_ID, BELONG_PLAN_ID, BELONG_GROUP_NAME, NAME, MODULE_TYPE, MODULE_SUB_TYPE, TAGS, DESCRIPTION, "
        f"MESSAGE, ICON_PATH, BACKGROUND_PATH, DETAIL_PARAMS, ACTIVE_FLAG, DELETE_FLAG "
        f"FROM {table_name} WHERE {module_id_phrase} NAME = ?")
    res = execute_cursor(sql, (name,))
    return res


"""
Module DAO methods
"""


def add_module(module_type, module_sub_type, module):
    """
    Add a new module to the database.

    Args:
        module_type (str): Primary type of the module
        module_sub_type (str): Subtype of the module
        module (dict): Dictionary containing module attributes:
            - belong_plan_id (int): ID of the plan this module belongs to
            - name (str): Module name
            - tags (str): Comma-separated tags
            - description (str): Module description
            - icon_path (str): Path to icon image
            - background_path (str): Path to background image
    """
    detail_json = json.dumps(module, ensure_ascii=False)
    sql = (f'''
        INSERT INTO {table_name} (
            BELONG_PLAN_ID, NAME, 
            MODULE_TYPE, MODULE_SUB_TYPE, TAGS, DESCRIPTION, ICON_PATH, BACKGROUND_PATH, DETAIL_PARAMS, 
            BELONG_GROUP_NAME, MESSAGE
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, '', '')
    ''')
    params = (module['belong_plan_id'], module['name'],
              module_type, module_sub_type, module['tags'], module['description'],
              module['icon_path'], module['background_path'], detail_json)
    execute_cursor(sql, params)


def get_module_name_by_module_id(module_id):
    """
    Get module name by its ID.

    Args:
        module_id (int): ID of the module

    Returns:
        str: Module name if found, None otherwise
    """
    sql = f'SELECT NAME FROM {table_name} WHERE MODULE_ID = {str(module_id)}'
    res = execute_cursor(sql)
    if len(res) > 0:
        return res[0]['NAME']
    else:
        return None


def get_modules_from_db(**kwargs):
    """
    Query modules from database with optional filters.

    Args:
        **kwargs: Optional filters including:
            - module_type (str): Filter by module type
            - plan_id (int): Filter by plan ID

    Returns:
        list: Database results matching the query
    """
    and_where_phrase = ""
    if 'module_type' in kwargs:
        and_where_phrase = f"AND MODULE_TYPE in ('{kwargs['module_type']}')"
    if 'plan_id' in kwargs:
        and_where_phrase = f"AND BELONG_PLAN_ID in ('{kwargs['plan_id']}')"
    sql = (
        f'SELECT DISTINCT MODULE_ID, BELONG_PLAN_ID, BELONG_GROUP_NAME, NAME, MODULE_TYPE, MODULE_SUB_TYPE, TAGS, DESCRIPTION, '
        f'MESSAGE, ICON_PATH, BACKGROUND_PATH, DETAIL_PARAMS, ACTIVE_FLAG, DELETE_FLAG '
        f'FROM {table_name} WHERE DELETE_FLAG = 0 {and_where_phrase}')
    res = execute_cursor(sql)
    return res


def get_modules(**kwargs):
    """
    Get complete module data including parsed detail_params.

    Args:
        **kwargs: Optional filters including:
            - module_type (str): Filter by module type
            - plan_id (int): Filter by plan ID

    Returns:
        list: List of module dictionaries with parsed detail_params
    """
    if 'module_type' in kwargs:
        module_type = kwargs['module_type']
        module_name_list = get_modules_from_db(module_type=module_type)
    elif 'plan_id' in kwargs:
        plan_id = kwargs['plan_id']
        module_name_list = get_modules_from_db(plan_id=plan_id)
    else:
        module_name_list = get_modules_from_db()

    modules = []
    for module in module_name_list:
        ins = Instance(module['NAME'], module['MODULE_TYPE'], module_id=module['MODULE_ID'])
        ins.set_instance(module)
        module_dict = convert_to_dict(ins)
        modules.append(module_dict)
    return modules


def convert_to_dict(module: Instance):
    """
    Convert module instance to dictionary format.

    Args:
        module (Instance): Module instance to convert

    Returns:
        dict: Dictionary representation of the module
    """
    module_dict = {
        "module_id": module.module_id,
        "belong_plan_id": module.belong_plan_id,
        "belong_group_name": module.belong_group_name,
        "name": module.name,
        "module_type": module.module_type,
        "module_sub_type": module.module_sub_type,
        "tags": module.tags,
        "description": module.description,
        "message": module.message,
        "icon_path": module.icon_path,
        "background_path": module.background_path,
        "detail_params": json.loads(module.detail_params),
        "delete_flag": module.delete_flag,
        "active_flag": module.active_flag
    }
    return module_dict


def soft_delete_module(module_id):
    """
    Soft delete a module by setting its DELETE_FLAG to 1.

    Args:
        module_id (int): ID of module to softly delete
    """
    sql = f"UPDATE {table_name} SET DELETE_FLAG = '1' WHERE MODULE_ID = {str(module_id)}"
    execute_cursor(sql)


def check_module_delete_status(module_id):
    """
    Check if a module is softly deleted.

    Args:
        module_id (int): ID of module to check

    Returns:
        str: '1' if deleted, '0' if not, '1' if module not found
    """
    sql = f'SELECT DELETE_FLAG FROM {table_name} WHERE MODULE_ID = {module_id}'
    res = execute_cursor(sql)
    if len(res) > 0:
        return res[0]['DELETE_FLAG']
    else:
        return '1'


def deactivate_module(module_id):
    """
    Deactivate a module by setting its ACTIVE_FLAG to 0.

    Args:
        module_id (int): ID of module to deactivate
    """
    sql = f"UPDATE {table_name} SET ACTIVE_FLAG = '0' WHERE MODULE_ID = {str(module_id)}"
    execute_cursor(sql)


def activate_module(module_id):
    """
    Activate a module by setting its ACTIVE_FLAG to 1.

    Args:
        module_id (int): ID of module to activate
    """
    sql = f"UPDATE {table_name} SET ACTIVE_FLAG = '1' WHERE MODULE_ID = {str(module_id)}"
    execute_cursor(sql)


def check_module_active_status(module_id):
    """
    Check if a module is active.

    Args:
        module_id (int): ID of module to check

    Returns:
        str: '1' if active, '0' if not, '0' if module not found
    """
    sql = f'SELECT ACTIVE_FLAG FROM {table_name} WHERE MODULE_ID = {module_id}'
    res = execute_cursor(sql)
    if len(res) > 0:
        return res[0]['ACTIVE_FLAG']
    else:
        return '0'


def update_module_detail(module: Instance):
    """
    Update module details in database.

    Args:
        module (Instance): Module instance with updated details
    """
    sql = (f'UPDATE {table_name} SET BELONG_GROUP_NAME = ?,  NAME = ?, MODULE_SUB_TYPE = ?, TAGS = ?, DESCRIPTION =?,'
           f'ICON_PATH = ?, BACKGROUND_PATH = ?, DETAIL_PARAMS = ? WHERE MODULE_ID = ?')
    params = (module.belong_group_name, module.name, module.module_sub_type, module.tags, module.description,
              module.icon_path, module.background_path, module.detail_params,
              module.module_id)
    execute_cursor(sql, params)


def update_belong_group(module: Instance):
    """
    Update the group a module belongs to.

    Args:
        module (Instance): Module instance with updated group
    """
    sql = f'UPDATE {table_name} SET BELONG_GROUP_NAME =? WHERE MODULE_ID =?'
    params = (module.belong_group_name, module.module_id)
    execute_cursor(sql, params)


def update_module_belong_group(belong_plan_id, belong_group_name_old, belong_group_name_new):
    """
    Update group name for all modules in a plan.

    Args:
        belong_plan_id (int): ID of the plan
        belong_group_name_old (str): Current group name
        belong_group_name_new (str): New group name
    """
    sql = f"UPDATE {table_name} SET BELONG_GROUP_NAME = ? WHERE BELONG_PLAN_ID = ? AND BELONG_GROUP_NAME = ?"
    params = (belong_group_name_new, belong_plan_id, belong_group_name_old)
    execute_cursor(sql, params)


def delete_module_belong_group(belong_plan_id, belong_group_name):
    """
    Remove modules from a group by clearing their group name.

    Args:
        belong_plan_id (int): ID of the plan
        belong_group_name (str): Group name to clear
    """
    sql = f"UPDATE {table_name} SET BELONG_GROUP_NAME = '' WHERE BELONG_PLAN_ID = ? AND BELONG_GROUP_NAME = ?"
    params = (belong_plan_id, belong_group_name)
    execute_cursor(sql, params)


def if_exist_specific_module(belong_plan_id, module_type, module_sub_type):
    """
    Check if a specific module exists in a plan.

    Args:
        belong_plan_id (int): ID of the plan
        module_type (str): Module type to check
        module_sub_type (str): Module subtype to check

    Returns:
        int: Module ID if found, 0 otherwise
    """
    sql = f"SELECT MODULE_ID FROM {table_name} WHERE BELONG_PLAN_ID =? AND MODULE_TYPE =? AND MODULE_SUB_TYPE =? AND ACTIVE_FLAG = '1' AND DELETE_FLAG = '0'"
    params = (belong_plan_id, module_type, module_sub_type)
    res = execute_cursor(sql, params)
    if len(res) > 0:
        return res[0]['MODULE_ID']
    else:
        return 0
