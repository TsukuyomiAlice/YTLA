from core.frame.func.loggerConfig import process_log
from core.frame.instance.instanceProcessToRoutes import Response
from features.language.dao import daoModuleDictionaryEntries
from bs4 import BeautifulSoup  # 新增HTML解析库


@process_log
def search_word(word):
    """
    搜索单词并解析HTML内容（保留<span>和<div>标签）
    :param word: 要搜索的单词
    :return: 处理后的释义内容
    """
    # 查找单词
    entries = daoModuleDictionaryEntries.query_data(word)
    meaning = ''  # 最终存储处理后的释义

    for entry in entries:
        # 跳过空条目
        if not entry['definition']:
            continue

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(entry['definition'], 'html.parser')

        # 保留所有<span>和<div>标签，移除其他标签
        # 1. 先提取所有需要保留的标签
        kept_tags = soup.find_all(['span', 'div'])
        # 2. 清除其他类型的标签（如<img>、<a>等）
        for tag in soup.find_all():
            if tag.name not in ['span', 'div']:
                tag.decompose()  # 移除标签及其内容

        # 保留原始换行符（通过获取处理后的文本+标签的混合内容）
        # 注意：这里直接使用str(soup)会保留标签和原始换行符结构
        processed_content = str(soup)

        # 拼接结果（如果有多个条目，用换行分隔）
        meaning += processed_content + '\n'

    response = Response()
    response.data = {
        'meaning': meaning,
    }
    return response
