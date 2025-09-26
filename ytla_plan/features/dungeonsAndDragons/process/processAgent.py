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
    "prologue": ["Preface", "Introduction", "game_rule", "adventure_description",],
    "character": ["build_character", ],
    "races": ["race_select", "Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half_Elf", "Half_Orc", "Tiefling",],
    "classes": ["class_select", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", ],
    "personality_and_background": ["Character_detail", "Inspiration", "Background", "Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk_hero", "Guild_artisan", "Hermit", "Noble", "Outlander", "Sage", "Sailor", "Soldier", "Urchin",],
    "equipment": ["Wealth", "Armor", "Weapon", "Adventure_gear", "Tool", "Mounts_vehicles", "Trade_goods", "Expenses", "Trinkets",],
    "customize": ["Multiclassing", "Feats", ],
    "ability_score": ["Ability", "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma", "Saving_throws",],
    "adventuring": ["time", "movement", "environment", "social_interaction", "resting", "between_adventure",],
    "combat": ["The_order_of_combat", "Movement_and_position", "Action_in_combat", "Making_an_attack", "Cover", "Damage_and_healing", "Mounted_combat", "Underwater_Combat",],
    "spellcasting": ["spell_description", "cast_spell", ],
    "spells": ["Bard_spells", "Cleric_spells", "Druid_spells", "Paladin_Spells", "Ranger_spells", "Sorcerer_spells", "Warlock_spells", "Wizard_spells", ],
    "conditions": ["conditions", ],
    "gods_of_multiverse": ["DND_Pantheons", "Fantasy_historical_pantheons",],
    "planes_of_existence": ["the_material_plane", "beyond_the_material_plane",],
    "creature_statistics": ["creature_statistics",],
    "inspirational_readings": ["inspirational_readings"],
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
                keyword_list.update({item: dnd_5e_player_004_personalityAndBackground.personality_background_keyword_list[item]})
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
                keyword_list.update({item: dnd_5e_player_016_inspirationalReadings.inspirationalReadings_keyword_list[item]})
    return keyword_list


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


def select_keyword_topics(request_prompt: str) -> str:
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
把你认为有关的应当检索的内容尽可能多地回答给我。
你必须确保你的回答中，类别名与关键词的关系与类别关键词列表中一致。

## 如果你认为没有有关的内容，回复:
{{}}
"""
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.chat(message_list, request_prompt)
    caller = message_list[2].get('content')
    print("=" * 20, "问题大类筛选结果", "=" * 20 )
    print(caller)
    return caller


def select_keyword_list(topic_list: list, request_prompt: str) -> str:
    keyword_list = create_keyword_list(topic_list)
    system_prompt = """
# 提示词
## 你是一个忠于游戏设定的龙与地下城游戏设定的信息检索员。
## 稍后有一份游戏规则的主题列表。

## 主题列表的格式是这样的。这是一份符合<键>: <值>数据格式的数据文档。
{ <章节名1>: [<关键词1>, <关键词2>, <关键词3>...],
  <章节名2>: [<关键词1>, <关键词2>, <关键词3>...], 
 ... }
你需要根据用户发送的信息来判断应该检索哪些章节的内容以获取正确答案。

## 回答的格式如下：
## 如果有你认为应该检索的内容，按以下格式回复：
[
{ <章节1>： [<关键词1>, <关键词2>, ...] }, 
{ <章节2>： [<关键词3>, <关键词4>, ...] }, 
...
]
把你认为有关的应当检索的内容尽可能多地回答给我。
回答必须与主题列表内容完全一致。
回答必须与主题列表内容完全一致。
回答必须与主题列表内容完全一致。

## 如果你认为没有有关的内容，回复:
[]
"""
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.add_system_message(message_list, str(json.dumps(keyword_list, ensure_ascii=False)))
    message_list = contentHandler.chat(message_list, request_prompt)
    caller = message_list[3].get('content')
    print("=" * 20, "问题子类筛选结果", "=" * 20 )
    print(caller)
    return caller


def guide_answer(topic_chat, keyword_chat, request_prompt: str):
    article = create_article(topic_chat)
    system_prompt = f"""
# 提示词
## 你是一个忠于游戏设定的龙与地下城游戏设定的信息检索员。
## 稍后有一份玩家手册的原版片段。

你需要根据用户提出的问题，忠于原文内容，给出正确的回答。
你可以把注意力放在以下章节里：
{keyword_chat}

## 你的回答应当附上原文，并做出解释说明。
## 你不需要做出超过玩家提问的额外回答内容。
    """
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.add_system_message(message_list, article)
    message_list = contentHandler.chat(message_list, request_prompt)
    caller = message_list[3].get('content')
    print("=" * 20, "最终回答", "=" * 20 )
    print(caller)
    return caller


def query(chat):
    topic_chat = select_keyword_topics(chat)
    print("=" * 55)
    keyword_chat = select_keyword_list(eval(topic_chat), chat)
    print("=" * 55)
    guide_chat = guide_answer(eval(topic_chat), keyword_chat, chat)
    print("=" * 55)


query("""
可以获取工匠套组的角色或职业
""")