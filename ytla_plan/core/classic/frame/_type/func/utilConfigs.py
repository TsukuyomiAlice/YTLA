# coding = utf-8
import logging
import os

"""
" ################
" YTLA CONFIG FILE
" ################
"""
"""
USEFUL LINKS FOR THIS PROJECT

"""

''' 
Proxy Configuration 
'''
# Proxy settings for external API access
proxies = {
    'http': 'http://192.168.71.118:20172',
    # https -> http
    'https': 'http://192.168.71.118:20172'
}

''' 
Database Configuration 
'''


def get_db_folder_path():
    """
    Retrieve the database directory path with system-appropriate separators

    Returns:
        str: Platform-dependent path using native filesystem separators
        - POSIX systems: Uses forward slashes (/)
        - Windows: Uses backslashes (\\)

    Note:
        The actual storage location differs by OS, but the relative
        path structure remains consistent
    """
    s = '/YTLA_DATAS'
    if os.name == 'posix':
        s = '/YTLA_DATAS/ytla_plan'
    if os.name == 'nt':
        s = 'D:\\YTLA_DATA\\ytla_plan'
    return s


db_folder_path = get_db_folder_path()

# Database file paths
db_files = {
    "temp_test": "temp_test.db",
    "ytla_user": "ytla_user.db",
    "life_plan": "life_plan.db",
    "language_cefr": "language_cefr.db",
    "language_dictionary_oxford": "Oxford 8th.db"
}

''' 
Logging Configuration 
'''


def get_log_folder_path():
    """
    Get log directory path with OS-correct separator

    Returns:
        str: Platform-formatted path ensuring:
        - POSIX compliance with forward slashes
        - Windows compliance with backslashes
    """
    s = '/YTLA_DATAS/ytla_plan/logs'
    if os.name == 'posix':
        s = '/YTLA_DATAS/ytla_plan/logs'
    if os.name == 'nt':
        s = 'D:\\YTLA_DATA\\ytla_plan\\logs'
    return s


log_folder_path = get_log_folder_path()

# Default log level
log_level_info = logging.INFO
log_level_warning = logging.WARNING
log_level_error = logging.ERROR
log_level_critical = logging.CRITICAL
