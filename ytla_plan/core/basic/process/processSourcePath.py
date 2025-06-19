# coding=utf-8
import os


def access_local_directory(directory_path):
    try:
        if os.path.isdir(directory_path):
            items = os.listdir(directory_path)
            return items
        else:
            return "提供的路径不是一个有效的目录。"
    except Exception as e:
        return f"访问目录时出错: {str(e)}"

