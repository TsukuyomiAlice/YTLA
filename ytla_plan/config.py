import os

"""
" Flask configuration
"""

UPLOAD_FOLDER = os.path.abspath('D:\\YTLA_DATA\\ytla_plan')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'ico'}
MAX_CONTENT_LENGTH = 5 * 1024 * 1024 * 1024