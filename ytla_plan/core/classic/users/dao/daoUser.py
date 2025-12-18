# encode = utf-8
from core.classic.frame.func import sqliteConnector

db_name = 'YTLA_USER'

"""
Documentation:
daoUser is a separate database for storing user information.
The entire database should be treated as independent of the current system.

Each user points to an independent directory (named by user id) where all user data is stored.
In multi-user interaction mode, it will read the corresponding db from the plan creator's directory.
If the logged-in user is not the creator, it will create an empty plan_db recording the creator's id,
and point to the creator's plan_db (for data interaction handling).
"""


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
    """Drop all user-related tables from the database."""
    sql = 'DROP TABLE users'
    execute_cursor(sql)
    sql = 'DROP TABLE user_roles'
    execute_cursor(sql)
    sql = 'DROP TABLE user_permissions'
    execute_cursor(sql)
    sql = 'DROP TABLE user_login_history'
    execute_cursor(sql)


def create_table():
    """Create all user-related tables in the database."""
    sql = '''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        phone_country_code TEXT,
        phone_number TEXT UNIQUE,
        password_hash TEXT NOT NULL,

        -- 权限相关
        role TEXT NOT NULL CHECK(role IN ('user', 'admin', 'super_admin')) DEFAULT 'user',
        permissions TEXT,  -- JSON存储细粒度权限

        -- 状态管理
        is_email_verified BOOLEAN DEFAULT 0,
        is_phone_verified BOOLEAN DEFAULT 0,
        is_active BOOLEAN DEFAULT 1,
        is_deleted BOOLEAN DEFAULT 0,

        -- 安全审计
        failed_login_attempts INTEGER DEFAULT 0,
        last_login_at DATETIME,
        last_login_ip TEXT,

        -- 用户偏好
        preferred_language TEXT DEFAULT 'zh',
        timezone TEXT DEFAULT 'Asia/Shanghai',

        -- 元数据
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    '''
    execute_cursor(sql)
    sql = 'CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);'
    execute_cursor(sql)
    sql = 'CREATE INDEX IF NOT EXISTS idx_users_phone ON users(phone_country_code, phone_number);'

    execute_cursor(sql)

    sql = '''
    CREATE TABLE IF NOT EXISTS user_roles (
        role_id INTEGER PRIMARY KEY,
        role_name TEXT NOT NULL UNIQUE,
        description TEXT
    );
    '''
    execute_cursor(sql)
    sql = '''
    CREATE TABLE IF NOT EXISTS user_permissions (
        user_id INTEGER,
        role_id INTEGER,
        granted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(user_id),
        FOREIGN KEY(role_id) REFERENCES user_roles(role_id),
        PRIMARY KEY (user_id, role_id)
    );
    '''
    execute_cursor(sql)
    sql = '''
    CREATE TABLE IF NOT EXISTS user_login_history (
        log_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        login_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        ip_address TEXT,
        device_type TEXT,
        user_agent TEXT,
        success BOOLEAN,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    );
    '''
    execute_cursor(sql)


def get_max_user_id() -> int:
    """
    Get the current maximum user ID.

    Returns:
        int: Current maximum user_id, returns 0 if no records exist
    """
    sql = "SELECT MAX(user_id) FROM users"
    result = execute_cursor(sql)[0]
    return result['MAX(user_id)'] if result and result['MAX(user_id)'] is not None else 0


def generate_user_id() -> int:
    """
    Generate a new user ID following the rules.

    Rules: Minimum is 1000000001, subsequent IDs increment from current maximum.

    Returns:
        int: Newly generated user ID
    """
    current_max = get_max_user_id()
    return 1000000001 if current_max < 1000000001 or current_max is None else current_max + 1


def create_user(user_data: dict) -> dict:
    """
    Create a new user (includes password encryption).

    Args:
        user_data (dict): Dictionary containing user data

    Returns:
        dict: {'success': bool, 'user_id': int, 'error': str}
    """
    try:
        import bcrypt
        hashed_pw = bcrypt.hashpw(user_data['password'].encode('utf-8'), bcrypt.gensalt())

        user_id = generate_user_id()

        sql = '''INSERT INTO users 
                (user_id, username, email, phone_country_code, phone_number, password_hash) 
                VALUES (?, ?, ?, ?, ?, ?)'''

        cursor = execute_cursor(sql, (
            user_id,
            user_data['username'],
            user_data['email'],
            user_data.get('phone_country_code'),
            user_data.get('phone_number'),
            hashed_pw.decode('utf-8')
        ))
        return {'success': True, 'user_id': user_id}
    except Exception as e:
        return {'success': False, 'error': str(e)}


def get_user_by(identifier: str, value: str) -> dict:
    """
    Generic user query method (supports ID/username/email/phone).

    Args:
        identifier (str): 'id'/'username'/'email'/'phone'
        value (str): Corresponding value

    Returns:
        dict: User object dictionary (excluding sensitive fields)
    """
    valid_identifiers = ['id', 'username', 'email', 'phone']
    if identifier not in valid_identifiers:
        return {'success': False, 'error': 'Invalid identifier'}

    field_map = {
        'id': 'user_id',
        'phone': '(phone_country_code, phone_number)'
    }
    field = field_map.get(identifier, identifier)

    sql = f"""SELECT 
            user_id, username, email, phone_country_code, phone_number,
            role, permissions, preferred_language, timezone 
            FROM users 
            WHERE {field}=? AND is_deleted='0'"""
    res = execute_cursor(sql, (value,))
    return res[0] if res else {}


def verify_credentials(email: str, password: str) -> dict:
    """
    Verify user credentials (includes login failure recording).

    Args:
        email (str): User email
        password (str): User password

    Returns:
        dict: {success: bool, user: dict, error: str}
    """
    try:
        import bcrypt
        sql = "SELECT user_id, password_hash, failed_login_attempts FROM users WHERE email=?"
        user = execute_cursor(sql, (email,))[0]

        if not user:
            return {'success': False, 'error': 'The User does not exist'}

        if user[0]['failed_login_attempts'] >= 5:
            return {'success': False, 'error': 'The User has been locked'}

        if bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):

            execute_cursor("UPDATE users SET failed_login_attempts=0 WHERE user_id=?", (user['user_id'],))
            return {'success': True, 'user': get_user_by('id', user['user_id'])}
        else:
            execute_cursor("UPDATE users SET failed_login_attempts=failed_login_attempts+1 WHERE user_id=?",
                           (user['user_id'],))
            return {'success': False, 'error': 'Incorrect password'}
    except Exception as e:
        return {'success': False, 'error': str(e)}


def update_last_login(user_id: int, ip: str) -> None:
    """
    Update last login information.

    Args:
        user_id (int): User ID
        ip (str): IP address of login
    """
    execute_cursor(
        "UPDATE users SET last_login_at=CURRENT_TIMESTAMP, last_login_ip=? WHERE user_id=?",
        (ip, user_id)
    )
    execute_cursor('''INSERT INTO user_login_history 
                    (user_id, ip_address, success) 
                    VALUES (?, ?, 1)''',
                   (user_id, ip))


def update_user_info(user_id: int, user_data: dict) -> dict:
    """
    Update user information.

    Args:
        user_id (int): User ID to update
        user_data (dict): Dictionary containing updated user data

    Returns:
        dict: {'success': bool, 'user_id': int, 'error': str}
    """
    try:
        execute_cursor(
            'UPDATE users SET username=?, email=?, phone_country_code=?, phone_number=?, password_hash=? WHERE user_id=?',
            (user_data['username'], user_data['email'], user_data.get('phone_country_code'),
             user_data.get('phone_number'), user_data['password'], user_id)
        )
        return {'success': True, 'user_id': user_id}
    except Exception as e:
        return {'success': False, 'error': str(e)}


def assign_role(user_id: int, role_name: str) -> dict:
    """
    Assign a role to a user.

    Args:
        user_id (int): User ID
        role_name (str): Role name to assign

    Returns:
        dict: {'success': bool, 'error': str}
    """
    try:
        role_id = execute_cursor(
            "SELECT role_id FROM user_roles WHERE role_name=?",
            (role_name,)
        )[0]['role_id']

        execute_cursor('''INSERT INTO user_permissions (user_id, role_id) 
                        VALUES (?, ?)''',
                       (user_id, role_id))
        return {'success': True}
    except Exception as e:
        return {'success': False, 'error': str(e)}


def get_user_permissions(user_id: int) -> list:
    """
    Get complete set of user permissions.

    Args:
        user_id (int): User ID

    Returns:
        list: List of permission records
    """
    sql = '''SELECT r.role_name, u.permissions 
            FROM user_permissions p
            JOIN user_roles r ON p.role_id = r.role_id
            JOIN users u ON p.user_id = u.user_id
            WHERE p.user_id=?'''
    return execute_cursor(sql, (user_id,))


def check_permission(user_id: int, role_id: int) -> dict:
    """
    Check if user has specific permission.

    Args:
        user_id (int): User ID
        role_id (int): Role ID to check

    Returns:
        dict: {'success': bool, 'user_id': int, 'error': str}
    """
    try:
        execute_cursor(
            'SELECT * FROM user_permissions WHERE user_id=? AND role_id=?',
            (user_id, role_id)
        )
        return {'success': True, 'user_id': user_id}
    except Exception as e:
        return {'success': False, 'error': str(e)}


def update_role_info(user_id: int, role_id: int) -> dict:
    """
    Update user's role information.

    Args:
        user_id (int): User ID
        role_id (int): New role ID

    Returns:
        dict: {'success': bool, 'user_id': int, 'error': str}
    """
    try:
        execute_cursor(
            'UPDATE user_permissions SET role_id=? WHERE user_id=?',
            (role_id, user_id)
        )
        return {'success': True, 'user_id': user_id}
    except Exception as e:
        return {'success': False, 'error': str(e)}


def get_login_history(user_id: int, limit: int = 30) -> list:
    """
    Get recent login history for a user.

    Args:
        user_id (int): User ID
        limit (int): Maximum number of records to return (default 30)

    Returns:
        list: List of login history records
    """
    sql = '''SELECT login_at, ip_address, device_type, success 
            FROM user_login_history 
            WHERE user_id=? 
            ORDER BY login_at DESC 
            LIMIT ?'''
    return execute_cursor(sql, (user_id, limit))


def check_unique(field: str, value: str) -> bool:
    """
    Check if username/email/phone number is unique.

    Args:
        field (str): Field to check ('username', 'email', 'phone_number')
        value (str): Value to check

    Returns:
        bool: True if unique, False if not
    """
    allowed_fields = ['username', 'email', 'phone_number']
    if field not in allowed_fields:
        return False
    sql = f"SELECT 1 FROM users WHERE {field}=? AND is_deleted=0"
    return bool(len(execute_cursor(sql, (value,))))


def soft_delete_user(user_id: int) -> bool:
    """
    Soft delete a user (mark as deleted without removing record).

    Args:
        user_id (int): User ID to delete

    Returns:
        bool: True if successful
    """
    execute_cursor("UPDATE users SET is_deleted=1 WHERE user_id=?", (user_id,))
    return True


def deactivate_user(user_id: int) -> bool:
    """
    Deactivate a user account.

    Args:
        user_id (int): User ID to deactivate

    Returns:
        bool: True if successful
    """
    execute_cursor("UPDATE users SET is_active=0 WHERE user_id=?", (user_id,))
    return True
