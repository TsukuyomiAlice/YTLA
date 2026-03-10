# encode=utf-8

import ast
import json
import os

def get_data_file_list():
    """
    获取当前目录下所有PY文件的文件名（不包含路径）

    返回:
        list: 所有PY文件的文件名列表（不包含路径）
    """
    # 获取当前文件所在目录
    current_dir = os.path.dirname(__file__)
    # 存储PY文件名的列表
    py_files = []

    # 遍历目录下所有条目
    for entry in os.listdir(current_dir):
        # 拼接完整路径以检查是否为文件
        entry_path = os.path.join(current_dir, entry)
        # 检查是否为文件且以.py结尾（不区分大小写）
        if (os.path.isfile(entry_path) and entry.lower().endswith('.py')
                and entry not in ['__init__.py', 'datasetJsonPicker.py', 'datasetPyToJson.py']):
            py_files.append(entry)  # 添加文件名到列表

    return py_files


def extract_topics_and_articles(py_file_path):
    """从每个字符串常量中同时提取topics和articles（键名关联）"""
    topics = {}  # 存储topics字典：{主题标题: [主题行列表]}
    articles = {}  # 存储articles字典：{主题标题: 常量内容}

    with open(py_file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=py_file_path)

    # 遍历所有字符串常量节点
    for node in ast.walk(tree):
        if isinstance(node, ast.Str):
            str_content = node.s.strip()  # 当前字符串常量内容
            if not str_content:
                continue  # 跳过空字符串

            # 步骤1：提取当前常量中的主题行（# ... 格式）
            all_lines = str_content.split('\n')
            topic_lines = [line[2:].strip() for line in all_lines if line.startswith("# ")]
            if not topic_lines:
                continue  # 非主题常量，跳过

            # 步骤2：生成topic键（首个主题行）和值（所有主题行）
            topic_key = topic_lines[0]  # 主题标题 = 首个主题行内容
            topics[topic_key] = topic_lines  # 添加到topics

            # 步骤3：生成article键（与topic键一致）和值（常量完整内容）
            articles[topic_key] = str_content  # 添加到articles（键与topic_key完全一致）

    return topics, articles  # 同时返回关联的topics和articles


def convert_to_json(py_file_path):
    # 关键：同时提取topics和articles，确保键名一一对应
    topics, articles = extract_topics_and_articles(py_file_path)

    # 构建JSON数据结构（topics先于articles写入）
    json_data = {
        "topics": topics,  # 先写入topics
        "articles": articles  # 后写入articles（键与topics完全对应）
    }

    # 写入JSON文件
    json_file_path = os.path.splitext(py_file_path)[0] + ".json"
    with open(json_file_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    print(f"转换完成，JSON文件已保存至: {json_file_path}")
    print(f"关联结果：topics键数量={len(topics)}, articles键数量={len(articles)}")


if __name__ == "__main__":
    files = get_data_file_list()
    for file in files:
        convert_to_json(file)
