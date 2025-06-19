# encode = utf-8
# html_parser.py
from bs4 import BeautifulSoup
from lxml import etree
from typing import Dict, Tuple, Any
import json

"""
提示
本文件为DeepSeek预先生成的代码。
在test_parse()内直接贴入需要被解析的HTML代码，并将本文件上传至DeepSeek即可。
DeepSeek需要尽可能多地返回可提取的信息，并生成替换进 解析规则配置区 的代码
"""


class UniversalParser:
    """通用HTML解析框架"""
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, 'html.parser')
        self.lxml_tree = etree.HTML(html)
    
    def bs4_extract(self, rules: Dict[str, Tuple[str, str]]) -> Dict:
        """新版BeautifulSoup提取方法
        参数规则格式: {'字段名': (CSS选择器, '属性名/text')}
        """
        result = {}
        for key, (selector, attr) in rules.items():
            elements = self.soup.select(selector)
            if attr == 'text':
                result[key] = [el.get_text(strip=True) for el in elements]
            else:
                result[key] = [el.get(attr) for el in elements]
        return result
    
    def xpath_extract(self, rules: Dict) -> Dict:
        """XPath提取方法"""
        result = {}
        for key, path in rules.items():
            # 自动处理文本/属性提取
            if path.endswith('/text()'):
                result[key] = [el.strip() for el in self.lxml_tree.xpath(path)]
            elif path.startswith('@'):
                result[key] = self.lxml_tree.xpath(path)[0] if self.lxml_tree.xpath(path) else None
            else:
                result[key] = self.lxml_tree.xpath(path)
        return result


def execute(html_segment):
    # 解析规则配置区（由AI根据提供的HTML动态生成）
    # DeepSeek需要需要在对话中返回parse_rules
    parse_rules = {
        # BeautifulSoup规则
        'bs4_rules': {

        },
        
        # XPath规则
        'xpath_rules': {

        }
    }
    
    # 执行解析
    parser = UniversalParser(html_segment)
    
    # 组合两种解析方式的结果
    final_result = {
        **parser.bs4_extract(parse_rules['bs4_rules']),
        **parser.xpath_extract(parse_rules['xpath_rules'])
    }

    # 这里不是DeepSeek需要在对话中返回的内容
    return json.dumps(final_result, ensure_ascii=False, indent=2)


def test_parse():
    html_segment = '''
    '''
    print(execute(html_segment))


if __name__ == '__main__':
    test_parse()
