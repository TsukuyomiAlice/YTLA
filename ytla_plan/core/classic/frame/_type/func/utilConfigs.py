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
