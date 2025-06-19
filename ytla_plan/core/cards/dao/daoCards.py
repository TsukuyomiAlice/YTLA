# coding=utf-8

import json
from core.frame.func import sqliteConnector

"""
(Temporary) Database path is specified below.
If there's an independent database connection, it can be added here.
"""
db_name = 'life_plan'
table_name = "CARDS"


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
    """Drop the CARDS table from the database."""
    sql = f"DROP TABLE {table_name}"
    execute_cursor(sql)


def truncate_table():
    """
    Clear all data from the table and reclaim storage space.

    Performs DELETE operation followed by VACUUM to optimize database.
    """
    sql1 = f"DELETE FROM {table_name} where 1 = 1"
    execute_cursor(sql1)
    sql2 = "VACUUM"
    execute_cursor(sql2)


def create_table():
    """
    Create the CARDS table with default schema if not exists.

    Table structure includes:
    - Primary key (auto-increment)
    - Card metadata fields
    - Status flags (active/deleted)
    """
    sql = (f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
            CARD_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            CARD_TYPE TEXT NOT NULL,
            CARD_SUB_TYPE TEXT,
            TAGS TEXT,
            DESCRIPTION TEXT,
            ICON_PATH TEXT,
            BACKGROUND_PATH TEXT,
            DETAIL_PARAMS TEXT NOT NULL, 
            ACTIVE_FLAG TEXT DEFAULT '1',
            DELETE_FLAG TEXT DEFAULT '0'
        )
    ''')
    execute_cursor(sql)


"""
Instance methods for card object manipulation
"""


class Instance:
    """
    A class representing a card instance with database persistence.

    This class provides an object-oriented interface to the CARDS table,
    allowing for easy manipulation of card data while maintaining database
    consistency.

    Attributes:
        card_id: The unique identifier for the card (0 for new cards)
        name: The display name of the card
        card_type: The type classification of the card
        card_sub_type: Optional subtype classification
        tags: Comma-separated tags for categorization
        description: Detailed description of the card
        icon_path: Filesystem path to the card's icon image
        background_path: Filesystem path to the card's background image
        detail_params: JSON string containing card-specific parameters
        active_flag: '1' if active, '0' if inactive
        delete_flag: '1' if deleted, '0' if active
    """

    def __init__(self, name: str, card_type: str, **kwargs):
        """Initialize card instance with basic attributes."""
        if 'card_id' in kwargs:
            self.card_id: int = kwargs['card_id']
        else:
            self.card_id: int = 0
        self.name = name
        self.card_type = card_type
        self.card_sub_type = ''
        self.tags: str = ''
        self.description: str = ''
        self.icon_path: str = ''
        self.background_path: str = ''
        self.detail_params: str = '{}'
        self.active_flag: str = ''
        self.delete_flag: str = ''

    def get_instance_by_pk(self) -> dict:
        """
        Retrieve card record from database by primary key.

        Returns:
            dict: Card data if found, empty dict otherwise
        """
        if self.card_id != 0:
            db_record = select_all_by_pk(self.name, card_id=self.card_id)
        else:
            db_record = select_all_by_pk(self.name)
        return db_record[0] if db_record else {}

    def set_instance(self, db_res: dict) -> None:
        """Populate instance attributes from database record."""
        if len(db_res) != 11:
            return
        self.card_id = db_res['CARD_ID']
        self.name = db_res['NAME']
        self.card_type = db_res['CARD_TYPE']
        self.card_sub_type = db_res['CARD_SUB_TYPE']
        self.tags = db_res['TAGS']
        self.description = db_res['DESCRIPTION']
        self.icon_path = db_res['ICON_PATH']
        self.background_path = db_res['BACKGROUND_PATH']
        self.detail_params = db_res['DETAIL_PARAMS']
        self.active_flag = db_res['ACTIVE_FLAG']
        self.delete_flag = db_res['DELETE_FLAG']


def instance_list(pk_list: list) -> list:
    """
    Create list of card instances from primary key list.

    Args:
        pk_list: List of (name, card_type) tuples

    Returns:
        list: List of initialized card instances
    """
    res = []
    for i in pk_list:
        p = Instance(i[0], i[1])
        p.set_instance(p.get_instance_by_pk())
        res.append(p)
    return res


def select_all_by_pk(name, **kwargs) -> list:
    """
    Query card by name and optional card_id.

    Args:
        name: Card name to search for
        **kwargs: Optional card_id parameter

    Returns:
        list: Matching card records
    """
    card_id_phrase = "CARD_ID = ? AND " if 'card_id' in kwargs else ''
    params = (kwargs.get('card_id'), name) if 'card_id' in kwargs else (name,)
    sql = (f"SELECT CARD_ID, NAME, CARD_TYPE, CARD_SUB_TYPE, TAGS, DESCRIPTION, "
           f"ICON_PATH, BACKGROUND_PATH, DETAIL_PARAMS, ACTIVE_FLAG, DELETE_FLAG "
           f"FROM {table_name} WHERE {card_id_phrase} NAME = ?")
    res = execute_cursor(sql, params)
    return res


"""
DAO methods for card management
"""


def add_card(card_type: str, card_sub_type: str, card: dict) -> None:
    """
    Add a new card record to the database.

    Args:
        card_type: The primary type classification of the card
        card_sub_type: The secondary type classification (optional)
        card: Dictionary containing card attributes including:
            - name: The display name (required)
            - tags: Comma-separated tags (optional)
            - description: Detailed description (optional)
            - icon_path: Path to icon image (optional)
            - background_path: Path to background image (optional)

    """
    detail_json = json.dumps(card, ensure_ascii=False)
    sql = (f'''
        INSERT INTO {table_name} (
            NAME, CARD_TYPE, CARD_SUB_TYPE, TAGS, DESCRIPTION, 
            ICON_PATH, BACKGROUND_PATH, DETAIL_PARAMS
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''')
    params = (card['name'], card_type, card_sub_type, card['tags'],
              card['description'], card['icon_path'],
              card['background_path'], detail_json)
    execute_cursor(sql, params)


def get_card_type_info(card_id: int) -> tuple:
    """
    Retrieve card type and subtype information by card ID.

    Args:
        card_id: The unique identifier of the card

    Returns:
        tuple: (card_type, card_sub_type) if found, (None, None) otherwise
    """
    sql = f'SELECT CARD_TYPE, CARD_SUB_TYPE FROM {table_name} WHERE CARD_ID = ?'
    res = execute_cursor(sql, (card_id,))
    if res:
        return res[0]['CARD_TYPE'], res[0]['CARD_SUB_TYPE']
    return (None, None)


def get_card_name_by_card_id(card_id: int) -> str:
    """
    Retrieve card name by its ID.

    Args:
        card_id: ID of the card

    Returns:
        str: Card name if found, None otherwise
    """
    sql = f'SELECT NAME FROM {table_name} WHERE CARD_ID = ?'
    res = execute_cursor(sql, (card_id,))
    return res[0]['NAME'] if res else None


def get_cards_from_db(**kwargs) -> list:
    """
    Query cards from database with optional filters.

    Args:
        **kwargs: Optional filters including:
            - card_type (str|list): Filter by single card type or list of types

    Returns:
        list[dict]: List of card records where each record is a dictionary
        with column names as keys.

    Raises:
        DatabaseError: If there is an error executing the query

    Example:
        >>> get_cards_from_db()  # Get all active cards
        >>> get_cards_from_db(card_type='task')  # Filter by type
        >>> get_cards_from_db(card_type=['task', 'note'])  # Multiple types
    """
    card_type_phrase = f"AND CARD_TYPE in (?)" if 'card_type' in kwargs else ""
    sql = (f'SELECT DISTINCT CARD_ID, NAME, CARD_TYPE, CARD_SUB_TYPE, TAGS, '
           f'DESCRIPTION, ICON_PATH, BACKGROUND_PATH, DETAIL_PARAMS, '
           f'ACTIVE_FLAG, DELETE_FLAG FROM {table_name} '
           f'WHERE DELETE_FLAG = 0 {card_type_phrase}')
    res = execute_cursor(sql, card_type_phrase)
    return res


def get_cards(**kwargs) -> list:
    """
    Retrieve cards from the database with optional filtering.

    Args:
        **kwargs: Optional filters including:
            - card_type: Filter by card type

    Returns:
        A list of dictionaries where each dictionary represents a complete card,
        including parsed detail_params as a nested dictionary.

    Example:
        >>> get_cards()
        [{'card_id': 1, 'name': 'Sample', ...}]

        >>> get_cards(card_type='task')
        [{'card_id': 2, 'name': 'Task 1', ...}]
    """
    card_list = get_cards_from_db(**kwargs)
    cards = []
    for card in card_list:
        ins = Instance(card['NAME'], card['CARD_TYPE'], card_id=card['CARD_ID'])
        ins.set_instance(card)
        card_dict = convert_to_dict(ins)
        cards.append(card_dict)
    return cards


def convert_to_dict(card: Instance) -> dict:
    """
    Convert card instance to dictionary format.

    Args:
        card: Card instance to convert

    Returns:
        dict: Dictionary representation of card
    """
    return {
        "card_id": card.card_id,
        "name": card.name,
        "card_type": card.card_type,
        "card_sub_type": card.card_sub_type,
        "tags": card.tags,
        "description": card.description,
        "icon_path": card.icon_path,
        "background_path": card.background_path,
        "detail_params": json.loads(card.detail_params),
        "delete_flag": card.delete_flag,
        "active_flag": card.active_flag
    }


def soft_delete_card(card_id: int) -> None:
    """Mark card as deleted without physical removal.

    Args:
        card_id (int): ID of the card to check
    """
    sql = f"UPDATE {table_name} SET DELETE_FLAG = '1' WHERE CARD_ID = ?"
    execute_cursor(sql, (card_id,))


def check_card_delete_status(card_id: int) -> int:
    """Check if card is marked as deleted.

    Args:
        card_id (int): ID of the card to check

    Returns:
        str: '1' if deleted, '0' if not, '1' if card not found
    """
    sql = f'SELECT DELETE_FLAG FROM {table_name} WHERE CARD_ID = ?'
    res = execute_cursor(sql, (card_id,))
    return res[0]['DELETE_FLAG'] if res else 1


def deactivate_card(card_id: int) -> None:
    """Deactivate card by setting active_flag to 0.

    Args:
        card_id (int): ID of the card to check
    """
    sql = f"UPDATE {table_name} SET ACTIVE_FLAG = '0' WHERE CARD_ID = ?"
    execute_cursor(sql, (card_id,))


def check_card_active_status(card_id: int) -> int:
    """Check if card is active.

    Args:
        card_id (int): ID of the card to check

    Returns:
        str: '1' if active, '0' if not, '0' if card not found
    """
    sql = f'SELECT ACTIVE_FLAG FROM {table_name} WHERE CARD_ID = ?'
    res = execute_cursor(sql, (card_id,))
    return res[0]['ACTIVE_FLAG'] if res else 0


def update_card_detail(card: Instance) -> None:
    """Update card details in database.

    Args:
        card: Instance object containing updated card data

    """
    sql = (f'UPDATE {table_name} SET NAME = ?, CARD_SUB_TYPE = ?, TAGS = ?, '
           f'DESCRIPTION =?, ICON_PATH = ?, BACKGROUND_PATH = ?, '
           f'DETAIL_PARAMS = ? WHERE CARD_ID = ?')
    params = (card.name, card.card_sub_type, card.tags, card.description,
              card.icon_path, card.background_path, card.detail_params,
              card.card_id)
    execute_cursor(sql, params)
