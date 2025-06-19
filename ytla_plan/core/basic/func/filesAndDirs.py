# coding=utf-8
import json
import os


# 判断操作系统类型的方法
def slash():
    s = '/'
    if os.name == 'posix':
        s = '/'
    if os.name == 'nt':
        s = '\\'
    return s


def locate_project_path() -> str:
    # 可按实际路径进行更改
    path = os.path.abspath("").split('YTLA')[0] + 'YTLA'
    return path


def json_file_load(file_path):
    f = open(file_path, 'r')
    content = f.read()
    dic = json.loads(content)
    return dic


def load_file(file_path):
    f = open(file_path, 'r')
    content = f.read()
    return content


def write_to_file(file_name, line_list):
    with open(file_name, 'w') as f:
        for line in line_list:
            f.write(line + '\n')
        f.close()
