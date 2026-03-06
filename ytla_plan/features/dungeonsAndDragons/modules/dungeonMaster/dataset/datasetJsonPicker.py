# encode=utf-8

import os
import json

"""
获取文件列表
"""

def get_data_file_list():
    """
    获取当前目录下所有JSON文件的文件名（不包含路径）

    返回:
        list: 所有JSON文件的文件名列表（不包含路径）
    """
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

"""
获取指定json文件的全部的索引
"""

def extract_file_index(json_filename):
    """
    从JSON文件中提取topics的键名（主题标题）

    参数:
        json_filename (str): JSON文件名（包含.json扩展名）

    返回:
        list: topics字典中的所有键名（主题标题列表），如果'topics'不存在或不是字典，返回空列表
    """
    dataset_dir = os.path.dirname(__file__)
    file_path = os.path.join(dataset_dir, json_filename)
    current_topic_keys = []
    topics, articles = {}, {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        topics = json_data.get('topics')
        articles = json_data.get('articles')
        if isinstance(topics, dict):
            current_topic_keys = list(topics.keys())
        else:
            print(f"警告: {json_filename} 中'topics'不是字典类型，已记录空列表")

    except Exception as e:
        print(f"处理文件 {json_filename} 时出错: {str(e)}")

    return current_topic_keys, topics, articles


def generate_topic_key_list():
    """
    从所有JSON文件中提取所有topics的键名（主题标题），并生成一个字典，键为主题标题，值为对应的JSON文件名

    返回:
        dict: 键为主题标题（topics字典中的第一个键），值为该主题标题所在的JSON文件名
    """
    json_filenames = get_data_file_list()
    all_topic_keys = {}

    for filename in json_filenames:
        current_topic_keys = extract_file_index(filename)[0]
        all_topic_keys[current_topic_keys[0]] = current_topic_keys

    return all_topic_keys


def generate_topic_file_list():
    """
    从所有JSON文件中提取所有topics的键名（主题标题），并生成一个字典，键为主题标题，值为对应的JSON文件名

    返回:
        dict: 键为主题标题（topics字典中的第一个键），值为该主题标题所在的JSON文件名
    """
    json_filenames = get_data_file_list()
    all_topic_keys = {}

    for filename in json_filenames:
        current_topic_keys = extract_file_index(filename)[0]
        all_topic_keys[current_topic_keys[0]] = filename

    return all_topic_keys


def generate_topic_keyword_list(topic_list: dict[str: list]):
    file_menu = generate_topic_file_list()
    keyword_list = {}
    for index in topic_list.keys():
        topics_list = extract_file_index(file_menu[index])[1]
        topic_key_list = {}
        for topic in topic_list[index]:
            topic_key_list[topic] = topics_list[topic]
        keyword_list[index] = topic_key_list
    return keyword_list


def generate_article_part(keyword_list: dict[str: list]):
    file_menu = generate_topic_file_list()
    articles = ""
    for index in keyword_list.keys():
        articles_list = extract_file_index(file_menu[index])[2]
        for topic in keyword_list[index]:
            articles = articles + articles_list[topic] + '\n'
    return articles


def generate_article_part_by_whole_search(keyword, article: str):
    file_menu = generate_topic_file_list()
    for topic in file_menu.keys():
        articles_list = extract_file_index(file_menu[topic])[2]
        for article_topic in articles_list.keys():
            if keyword in articles_list[article_topic] and article_topic not in article:
                article = article + articles_list[article_topic] + '\n'
    return article
