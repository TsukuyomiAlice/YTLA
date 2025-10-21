# encode=utf-8

import os
import json


def get_data_file_list():
    # 获取当前文件所在目录
    current_dir = os.path.dirname(__file__)
    # 存储JSON文件名的列表
    json_files = []

    # 遍历目录下所有条目
    for entry in os.listdir(current_dir):
        # 拼接完整路径以检查是否为文件
        entry_path = os.path.join(current_dir, entry)
        # 检查是否为文件且以.json结尾（不区分大小写）
        if os.path.isfile(entry_path) and entry.lower().endswith('.json'):
            json_files.append(entry)  # 添加文件名到列表

    return json_files


def extract_topic_keys(json_filenames):
    """
    读取JSON文件列表，提取每个文件中`topic`字段的所有键，返回文件名与key列表的映射

    参数:
        json_filenames (list): JSON文件名列表（由get_json_filenames获取）

    返回:
        dict: 键为文件名，值为对应文件中`topic`字段的key列表（无key时为[]）
    """
    dataset_dir = os.path.dirname(__file__)
    all_topic_keys = {}  # 改为字典存储文件名与key列表的映射

    for filename in json_filenames:
        file_path = os.path.join(dataset_dir, filename)
        current_topic_keys = []  # 存储当前文件的topic key列表

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)

            topic = json_data.get('topics')
            if isinstance(topic, dict):
                current_topic_keys = list(topic.keys())  # 提取当前文件的key列表
            else:
                print(f"警告: {filename} 中'topics'不是字典类型，已记录空列表")

        except Exception as e:
            print(f"处理文件 {filename} 时出错: {str(e)}")
            # 出错时仍保留文件名，值为空列表

        # 无论是否成功，都添加当前文件的映射（空列表表示无有效key）
        all_topic_keys[current_topic_keys[0]] = current_topic_keys

    return all_topic_keys


def generate_file_list(json_filenames):
    dataset_dir = os.path.dirname(__file__)
    all_topic_keys = {}  # 改为字典存储文件名与key列表的映射

    for filename in json_filenames:
        file_path = os.path.join(dataset_dir, filename)
        current_topic_keys = []  # 存储当前文件的topic key列表

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)

            topic = json_data.get('topics')
            if isinstance(topic, dict):
                current_topic_keys = list(topic.keys())  # 提取当前文件的key列表
            else:
                print(f"警告: {filename} 中'topics'不是字典类型，已记录空列表")

        except Exception as e:
            print(f"处理文件 {filename} 时出错: {str(e)}")
            # 出错时仍保留文件名，值为空列表

        # 无论是否成功，都添加当前文件的映射（空列表表示无有效key）
        all_topic_keys[current_topic_keys[0]] = filename

    return all_topic_keys

print(generate_file_list(get_data_file_list()))