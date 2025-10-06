# encode = utf-8

import json
from ytla_ai.client import contentHandler
from ytla_plan.features.dungeonsAndDragons.dataset import (
    dnd_5e_player_000_prologue,
    dnd_5e_player_001_character,
    dnd_5e_player_002_races,
    dnd_5e_player_003_classes,
    dnd_5e_player_004_personalityAndBackground,
    dnd_5e_player_005_equipment,
    dnd_5e_player_006_customize,
    dnd_5e_player_007_ability_score,
    dnd_5e_player_008_adventuring,
    dnd_5e_player_009_combat,
    dnd_5e_player_010_spellcasting,
    dnd_5e_player_011_spells,
    dnd_5e_player_012_conditions,
    dnd_5e_player_013_godsOfMultiverse,
    dnd_5e_player_014_planesOfExistence,
    dnd_5e_player_015_creatureStatistics,
    dnd_5e_player_016_inspirationalReadings)

topic_word_list = {
    "prologue": [
        "Preface", "Introduction", "game_rule", "adventure_description", ],
    "character": [
        "build_character", ],
    "races": [
        "race_select", "Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half_Elf", "Half_Orc",
        "Tiefling", ],
    "classes": [
        "class_select", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue",
        "Sorcerer", "Warlock", "Wizard", ],
    "personality_and_background": [
        "Character_detail", "Inspiration", "Background", "Acolyte", "Charlatan", "Criminal",
        "Entertainer", "Folk_hero", "Guild_artisan", "Hermit", "Noble", "Outlander", "Sage",
        "Sailor", "Soldier", "Urchin", ],
    "equipment": [
        "Wealth", "Armor", "Weapon", "Adventure_gear", "Tool", "Mounts_vehicles", "Trade_goods", "Expenses",
        "Trinkets", ],
    "customize": [
        "Multiclassing", "Feats", ],
    "ability_score": [
        "Ability", "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma",
        "Saving_throws", ],
    "adventuring": [
        "time", "movement", "environment", "social_interaction", "resting", "between_adventure", ],
    "combat": [
        "The_order_of_combat", "Movement_and_position", "Action_in_combat", "Making_an_attack", "Cover",
        "Damage_and_healing", "Mounted_combat", "Underwater_Combat", ],
    "spellcasting": [
        "spell_description", "cast_spell", ],
    "spells": [
        "Bard_spells", "Cleric_spells", "Druid_spells", "Paladin_Spells", "Ranger_spells", "Sorcerer_spells",
        "Warlock_spells", "Wizard_spells", ],
    "conditions": [
        "conditions", ],
    "gods_of_multiverse": [
        "DND_Pantheons", "Fantasy_historical_pantheons", ],
    "planes_of_existence": [
        "the_material_plane", "beyond_the_material_plane", ],
    "creature_statistics": [
        "creature_statistics", ],
    "inspirational_readings": [
        "inspirational_readings"],
}


def create_keyword_list(topic_list: dict[str: list]):
    keyword_list = {}
    for key in topic_list.keys():
        if key == 'prologue':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_000_prologue.prologue_keyword_list[item]})
        if key == 'character':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_001_character.character_keyword_list[item]})
        if key == 'races':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_002_races.race_keyword_list[item]})
        if key == 'classes':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_003_classes.class_keyword_list[item]})
        if key == 'personality_and_background':
            for item in topic_list[key]:
                keyword_list.update(
                    {item: dnd_5e_player_004_personalityAndBackground.personality_background_keyword_list[item]})
        if key == 'equipment':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_005_equipment.equipment_keyword_list[item]})
        if key == 'customize':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_006_customize.customize_keyword_list[item]})
        if key == 'ability_score':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_007_ability_score.ability_keyword_list[item]})
        if key == 'adventuring':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_008_adventuring.adventuring_keyword_list[item]})
        if key == 'combat':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_009_combat.combat_keyword_list[item]})
        if key == 'spellcasting':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_010_spellcasting.spellcasting_keyword_list[item]})
        if key == 'spells':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_011_spells.spells_keyword_list[item]})
        if key == 'conditions':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_012_conditions.conditions_keyword_list[item]})
        if key == 'gods_of_multiverse':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_013_godsOfMultiverse.gods_of_multiverse_keyword_list[item]})
        if key == 'planes_of_existence':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_014_planesOfExistence.planes_of_existence_keyword_list[item]})
        if key == 'creature_statistics':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_015_creatureStatistics.creature_statistics_keyword_list[item]})
        if key == 'inspirational_readings':
            for item in topic_list[key]:
                keyword_list.update(
                    {item: dnd_5e_player_016_inspirationalReadings.inspirationalReadings_keyword_list[item]})
    return keyword_list


def search_keywords_simply(keywords: list[str]):
    pass


def create_article(topic_list: dict[str: list]) -> str:
    article = ""
    for key in topic_list.keys():
        if key == 'prologue':
            for item in topic_list[key]:
                article = article + dnd_5e_player_000_prologue.prologue_article[item]
        if key == 'character':
            for item in topic_list[key]:
                article = article + dnd_5e_player_001_character.character_article[item]
        if key == 'races':
            for item in topic_list[key]:
                article = article + dnd_5e_player_002_races.race_article[item]
        if key == 'classes':
            for item in topic_list[key]:
                article = article + dnd_5e_player_003_classes.class_article[item]
        if key == 'personality_and_background':
            for item in topic_list[key]:
                article = article + dnd_5e_player_004_personalityAndBackground.personality_background_article[item]
        if key == 'equipment':
            for item in topic_list[key]:
                article = article + dnd_5e_player_005_equipment.equipment_article[item]
        if key == 'customize':
            for item in topic_list[key]:
                article = article + dnd_5e_player_006_customize.customize_article[item]
        if key == 'ability_score':
            for item in topic_list[key]:
                article = article + dnd_5e_player_007_ability_score.ability_article[item]
        if key == 'adventuring':
            for item in topic_list[key]:
                article = article + dnd_5e_player_008_adventuring.adventuring_article[item]
        if key == 'combat':
            for item in topic_list[key]:
                article = article + dnd_5e_player_009_combat.combat_article[item]
        if key == 'spellcasting':
            for item in topic_list[key]:
                article = article + dnd_5e_player_010_spellcasting.spellcasting_article[item]
        if key == 'spells':
            article = article + dnd_5e_player_011_spells.spell_description_prompt
        if key == 'conditions':
            for item in topic_list[key]:
                article = article + dnd_5e_player_012_conditions.conditions_article[item]
        if key == 'gods_of_multiverse':
            for item in topic_list[key]:
                article = article + dnd_5e_player_013_godsOfMultiverse.gods_of_multiverse_article[item]
        if key == 'planes_of_existence':
            for item in topic_list[key]:
                article = article + dnd_5e_player_014_planesOfExistence.planes_of_existence_article[item]
        if key == 'creature_statistics':
            for item in topic_list[key]:
                article = article + dnd_5e_player_015_creatureStatistics.creature_statistics_article[item]
        if key == 'inspirational_readings':
            for item in topic_list[key]:
                article = article + dnd_5e_player_016_inspirationalReadings.inspirational_readings_articles[item]
    return article


def question_keyword_picker(request_prompt: str, temperature=0.1) -> str:
    system_prompt = f"""
# Prompt开始：
你是一个龙与地下城（Dungeons & Dragons）游戏的资深玩家，精通所有官方设定和规则（如第五版规则）。
你的任务是：当用户提出任何关于D&D的问题时，不直接回答问题内容，而是先分析用户的问题，提炼出问题的核心组成部分。
分析后，你需要返回两个列表：
    “asked”列表：包含问题中直接提到的具体D&D实体、概念或对象（如“战士”、“火球术”）。这些关键词应基于官方设定，代表被讨论的核心项目。
    “wanted”列表：包含用户寻求的信息类型、行动意图或查询目标（如“创建方法”、“规则解释”、“列表”或“比较”）。这些关键词应描述用户想要获取的知识或操作。
关键词必须基于D&D官方设定，简洁、具体，且避免主观解释。
响应格式要求：
    始终以两个列表的形式输出，格式为：
    {{"asked": ["关键词1", "关键词2", ...], "wanted": ["关键词1", "关键词2", ...]}}。
    每个列表中的关键词应按照问题主题的相关性排序，从最核心到次要。
    如果问题涉及多个独立方面，请用关键词覆盖所有内容。
    如果问题模糊或无关D&D，返回空列表：{{"asked": [], "wanted": []}}。
示例：
    用户问题："如何创建一名战士角色？"
    输出：{{"asked": ["战士", "职业"], "wanted": ["角色创建", "方法"]}}
    用户问题："解释一下火球术的伤害计算？"
    输出：{{"asked": ["火球术", "法术"], "wanted": ["伤害计算", "规则解释"]}}
    用户问题："战士和法师哪个更适合新手？"
    输出：{{"asked": ["战士", "法师", "职业"], "wanted": ["职业比较", "适合性"]}}
    用户问题："能通过自身获取工匠套装的职业和背景"
    输出：{{"asked": ["工匠工具"], "wanted": ["职业", "背景"]}}
现在，请根据这个设定处理用户的D&D相关问题。
# Prompt结束。
    """
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.chat(message_list, request_prompt, temperature=temperature)
    caller = message_list[2].get('content')
    print("=" * 21, "提问方向", "=" * 21)
    print(caller)
    return caller


def question_pre_answer(request_prompt: str, temperature=0.2) -> str:
    system_prompt = f"""
# Prompt开始：
你是一个龙与地下城（Dungeons & Dragons）游戏的资深玩家，精通所有官方设定和规则（如第五版规则）。
你的任务是：
当用户提出关于D&D的问题时，直接给出答案。答案必须基于官方第五版规则集（如《玩家手册》）。
在回答问题前，你会收到一个分析结果，格式为：{{"asked": ["关键词列表"], "wanted": ["关键词列表"]}}，这是从用户问题中提炼出的核心组成部分。
请基于这个分析结果生成答案。
答案必须是一个列表，包含问题所询问的具体游戏内元素（如职业、种族、专长、背景、法术、物品的名称）。
列表应直接对应分析结果中的"wanted"关键词和"asked"实体，仅列出官方名称，不添加任何解释。
响应格式要求：
    始终以列表形式输出，格式为：["名称1", "名称2", ...]。
    列表内容应完整覆盖分析结果所指示的查询维度（如"wanted"中的信息类型）和实体（如"asked"中的对象）。
    仅使用官方第五版规则中的术语，确保名称准确（例如，背景名称用"工会工匠"而非"工会工匠背景"）。
    如果问题模糊或无法根据官方规则回答，返回空列表[]。
示例：
    用户问题："战士有哪些核心能力？"
    分析结果：{{"asked": ["战士", "职业"], "wanted": ["核心能力"]}}
    输出：["战斗风格", "动作涌潮", "额外攻击", "不屈"]
    用户问题："哪些职业能使用重甲？"
    分析结果：{{"asked": ["重甲"], "wanted": ["职业"]}}
    输出：["战士", "圣武士", "牧师"]
    用户问题："能在游戏内获得工匠套装的职业或背景？"
    分析结果：{{"asked": ["工匠工具"], "wanted": ["职业", "背景"]}}
    输出：["战士", "武僧", "工会工匠", "平民英雄"]
现在，请根据这个设定处理用户的D&D相关问题。
# Prompt结束。
    """
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.chat(message_list, request_prompt, temperature=temperature)
    caller = message_list[2].get('content')
    print("=" * 21, "预回答结果", "=" * 21)
    print(caller)
    return caller


def masked_keyword_topics(request_prompt: str, temperature=0.0) -> str:
    system_prompt = f"""
# Prompt开始：
你是一个龙与地下城（Dungeons & Dragons）游戏的资深玩家，精通所有官方设定和规则（如第五版规则）。
你的任务是：当用户提供一系列D&D术语时，判断这些术语的父类别是什么。
父类别必须是龙与地下城游戏中的标准分类（如"职业"、"种族"、"法术学派"、"装备类型"等）。
对于每个术语，确定其最直接相关的父类别。
如果多个术语共享同一父类别，只需列出一次。

响应格式要求：
    始终以列表形式输出，格式为：["父类别1", "父类别2", "父类别3", ...]。
    父类别应按相关度从高到低排序，最相关的父类别排在前面。
    仅使用龙与地下城第五版官方规则集中的标准分类术语。
    如果用户提供的术语与龙与地下城游戏无关，返回一个空列表[]。
示例：
    用户输入：["战士", "法师", "游侠"] → 输出：["职业"]
    用户输入：["火球术", "治疗术", "隐形术"] → 输出：["法术"]
    用户输入：["长剑", "盾牌", "链甲"] → 输出：["装备"]
    用户输入：["精灵", "矮人", "半身人"] → 输出：["种族"]
    用户输入：["工匠", "艺人", "战士", "游侠"] → 输出：["职业", "背景"]
    用户输入：["战士", "长剑", "精灵"] → 输出：["职业", "装备", "种族"]
现在，请根据这个设定处理用户的D&D术语分类请求。
# Prompt结束。
"""
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.chat(message_list, request_prompt, temperature=temperature)
    caller = message_list[2].get('content')
    print("=" * 20, "问题大类分析结果", "=" * 20)
    print(caller)
    return caller


def select_keyword_topics(request_prompt: str, temperature=0.0) -> str:
    system_prompt = f"""
# 提示词
## 你是一个忠于游戏设定的龙与地下城游戏设定的信息检索员。
你需要根据客户发送的信息来判断，用户提的是属于什么类别的问题。
以下是你可以用于回答的类别关键词列表
{str(json.dumps(topic_word_list, ensure_ascii=False))}
## 回答的格式如下:
## 如果有你认为应该检索的内容，按以下格式回复：
{{
   <类别名1>： [<关键词1>, <关键词2>, ...],
   <类别名2>： [<关键词3>, <关键词4>, ...],
...
}}
你需要依靠你已有的知识，反推答案可能存在于哪些类别和关键词下。
把你认为可能有关的、应当检索的内容尽可能多地回答给我。
你必须确保你的回答中，类别名与关键词的关系与类别关键词列表中一致。

## 如果你认为没有有关的内容，回复:
{{}}
"""
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.chat(message_list, request_prompt, temperature=temperature)
    caller = message_list[2].get('content')
    print("=" * 20, "问题大类筛选结果", "=" * 20)
    print(caller)
    return caller


def select_keyword_list(topic_list: list, request_prompt: str, temperature=0.0) -> str:
    keyword_list = create_keyword_list(topic_list)
    system_prompt = """
# 提示词
## 你是一个忠于游戏设定的龙与地下城游戏设定的信息检索员。
## 稍后有一份游戏规则的主题列表。

## 主题列表的格式是这样的。这是一份符合<键>: <值>数据格式的数据文档。
{ <章节名1>: [<关键词1>, <关键词2>, <关键词3>...],
  <章节名2>: [<关键词1>, <关键词2>, <关键词3>...], 
 ... }
你需要根据用户发送的信息来判断应该检索哪些章节的内容以获取正确答案。rrrrrrrrrrrrrrrrrrr

## 回答的格式如下：
## 如果有你认为应该检索的内容，按以下格式回复：
[
{ <章节1>： [<关键词1>, <关键词2>, ...] }, 
{ <章节2>： [<关键词3>, <关键词4>, ...] }, 
...
]
把你认为可能有关的、应当检索的内容尽可能多地回答给我。
回答必须与主题列表内容完全一致。
不要遗漏基本的关键词。
不要给出过于果断的回答。

## 如果你认为没有有关的内容，回复:
[]
"""
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.add_system_message(message_list, str(json.dumps(keyword_list, ensure_ascii=False)))
    message_list = contentHandler.chat(message_list, request_prompt, temperature=temperature)
    caller = message_list[3].get('content')
    print("=" * 20, "问题子类筛选结果", "=" * 20)
    print(caller)
    return caller


def guide_answer(topic_chat, keyword_chat, request_prompt: str, temperature=0.0) -> str:
    article = create_article(topic_chat)
    system_prompt = f"""
# 提示词
## 你是一个忠于游戏设定的龙与地下城游戏设定的信息检索员。
## 稍后有一份玩家手册的原版片段。

你需要根据用户提出的问题，忠于原文内容，给出正确的回答。
你需要根据用户发送的信息来判断，用户提出的问题中有哪些DND术语关键词。
你需要联想用户的问题和DND术语之间的关系。
你可以把注意力放在以下章节里：
{keyword_chat}

## 你的回答应当附上原文，并做出解释说明。
## 你不需要做出超过玩家提问的额外回答内容。
    """
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.add_system_message(message_list, article)
    message_list = contentHandler.chat(message_list, request_prompt, temperature=temperature)
    caller = message_list[3].get('content')
    print("=" * 23, "最终回答", "=" * 23)
    print(caller)
    return caller


def query(chat):
    question_keywords = question_keyword_picker(chat)
    chat_a = chat + '\n' + '分析结果:' + question_keywords
    pre_answer = question_pre_answer(chat_a)
    masked_keyword_topics_picker = masked_keyword_topics(pre_answer)
    print("=" * 55)
    additional_prompt = ('分析结果:' + question_keywords + '\n' +
                         '问题大类分析结果' + masked_keyword_topics_picker + '\n' +
                         '预回答结果' + pre_answer)
    chat = chat + '\n' + '附加提示词:' + '\n' + additional_prompt
    topic_chat = select_keyword_topics(chat)
    print("=" * 55)
    keyword_chat = select_keyword_list(eval(topic_chat), chat)
    print("=" * 55)
    guide_chat = guide_answer(eval(topic_chat), keyword_chat, chat)
    print("=" * 55)


query("能说龙裔语的种族和职业")
