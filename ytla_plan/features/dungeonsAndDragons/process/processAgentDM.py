# encode = utf-8

import json

from ytla_ai.client import contentHandler

def process_agent_dm_dungeon_maker(demand: str, temperature: float = 0.0):
    json_file = json.load(open(r'D:/YTLA/ytla_plan/features/dungeonsAndDragons/dataset/dnd_5e_dmguide_010_random_dungeons.json', 'r', encoding='utf-8'))
    articles = json_file['articles']
    rules = ""
    for article in articles.keys():
        if article[0] != 'd':
            rules += articles[article] + "\n"
    system_prompt = f"""
# prompt开始
你是一个 dungeons and dragons 5e 游戏的 Dungeon Maker。
你将依照玩家的需求，生成符合要求的随机地下城。
随机地下城的生成规则: {str(rules)}
你可以选择模拟掷骰，也可以直接选择适合的要素生成地下城元素和内容。
你需要挑选一个合适的数据结构，返回你的生成结果。
# prompt结束
"""

    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.chat(message_list, demand)
    caller = message_list[2].get('content')
    print(caller)


def process_agent_dm_story_teller(story_teller: str, temperature: float = 0.0):
    pass

process_agent_dm_dungeon_maker('生成一个包含5个房间的地下城。')
