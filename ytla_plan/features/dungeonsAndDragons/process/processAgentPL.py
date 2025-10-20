# encode = utf-8

import json

from ytla_ai.client import contentHandler
from ytla_plan.features.dungeonsAndDragons.dataset import (
    dnd_5e_player_000_preface,
    dnd_5e_player_001_step_by_step_characters,
    dnd_5e_player_002_races,
    dnd_5e_player_003_classes,
    dnd_5e_player_004_personality_and_background,
    dnd_5e_player_005_equipment,
    dnd_5e_player_006_customization_options,
    dnd_5e_player_007_using_ability_scores,
    dnd_5e_player_008_adventuring,
    dnd_5e_player_009_combat,
    dnd_5e_player_010_spellcasting,
    dnd_5e_player_011_spells,
    dnd_5e_player_012_conditions,
    dnd_5e_player_013_gods_of_multiverse,
    dnd_5e_player_014_planes_of_existence,
    dnd_5e_player_015_creature_statistics,
    dnd_5e_player_016_inspirational_readings)
from ytla_plan.features.dungeonsAndDragons.prompt import (
    promptGuideKeywordPicker,
    promptGuidePreAnswer,
    promptGuideMaskedKeywordTopics,
    promptGuideKeywordTopics,
    promptGuideKeywordList,
    promptGuideAnswer
)

def topic_word_list():
    topics = {}
    topics.update(dnd_5e_player_000_preface.topics)
    topics.update(dnd_5e_player_001_step_by_step_characters.topics)
    topics.update(dnd_5e_player_002_races.topics)
    topics.update(dnd_5e_player_003_classes.topics)
    topics.update(dnd_5e_player_004_personality_and_background.topics)
    topics.update(dnd_5e_player_005_equipment.topics)
    topics.update(dnd_5e_player_006_customization_options.topics)
    topics.update(dnd_5e_player_007_using_ability_scores.topics)
    topics.update(dnd_5e_player_008_adventuring.topics)
    topics.update(dnd_5e_player_009_combat.topics)
    topics.update(dnd_5e_player_010_spellcasting.topics)
    topics.update(dnd_5e_player_011_spells.topics)
    topics.update(dnd_5e_player_012_conditions.topics)
    topics.update(dnd_5e_player_013_gods_of_multiverse.topics)
    topics.update(dnd_5e_player_014_planes_of_existence.topics)
    topics.update(dnd_5e_player_015_creature_statistics.topics)
    topics.update(dnd_5e_player_016_inspirational_readings.topics)
    return topics


def create_keyword_list(topic_list: dict[str: list]):
    keyword_list = {}
    for key in topic_list.keys():
        if key == 'preface':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_000_preface.keyword_list[item]})
        if key == 'step_by_step_characters':
            for item in topic_list[key]:
                keyword_list.update(
                    {item: dnd_5e_player_001_step_by_step_characters.keyword_list[item]})
        if key == 'races':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_002_races.keyword_list[item]})
        if key == 'classes':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_003_classes.keyword_list[item]})
        if key == 'personality_and_background':
            for item in topic_list[key]:
                keyword_list.update(
                    {item: dnd_5e_player_004_personality_and_background.keyword_list[item]})
        if key == 'equipment':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_005_equipment.keyword_list[item]})
        if key == 'customize':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_006_customization_options.keyword_list[item]})
        if key == 'using_ability_scores':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_007_using_ability_scores.keyword_list[item]})
        if key == 'adventuring':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_008_adventuring.keyword_list[item]})
        if key == 'combat':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_009_combat.keyword_list[item]})
        if key == 'spellcasting':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_010_spellcasting.keyword_list[item]})
        if key == 'spells':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_011_spells.keyword_list[item]})
        if key == 'conditions':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_012_conditions.keyword_list[item]})
        if key == 'gods_of_multiverse':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_013_gods_of_multiverse.keyword_list[item]})
        if key == 'planes_of_existence':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_014_planes_of_existence.keyword_list[item]})
        if key == 'creature_statistics':
            for item in topic_list[key]:
                keyword_list.update({item: dnd_5e_player_015_creature_statistics.keyword_list[item]})
        if key == 'inspirational_readings':
            for item in topic_list[key]:
                keyword_list.update(
                    {item: dnd_5e_player_016_inspirational_readings.keyword_list[item]})
    return keyword_list


def create_article(topic_list: dict[str: list], keyword_list: dict[str: list]) -> str:
    article = ""
    for key in topic_list.keys():
        if key == 'preface':
            for item in topic_list[key]:
                article = article + dnd_5e_player_000_preface.article[item]
        if key == 'step_by_step_characters':
            for item in topic_list[key]:
                article = article + dnd_5e_player_001_step_by_step_characters.article[item]
        if key == 'races':
            for item in topic_list[key]:
                article = article + dnd_5e_player_002_races.article[item]
        if key == 'classes':
            for item in topic_list[key]:
                article = article + dnd_5e_player_003_classes.article[item]
        if key == 'personality_and_background':
            for item in topic_list[key]:
                article = article + dnd_5e_player_004_personality_and_background.article[item]
        if key == 'equipment':
            for item in topic_list[key]:
                article = article + dnd_5e_player_005_equipment.article[item]
        if key == 'customize':
            for item in topic_list[key]:
                article = article + dnd_5e_player_006_customization_options.article[item]
        if key == 'using_ability_scores':
            for item in topic_list[key]:
                article = article + dnd_5e_player_007_using_ability_scores.article[item]
        if key == 'adventuring':
            for item in topic_list[key]:
                article = article + dnd_5e_player_008_adventuring.article[item]
        if key == 'combat':
            for item in topic_list[key]:
                article = article + dnd_5e_player_009_combat.article[item]
        if key == 'spellcasting':
            for item in topic_list[key]:
                article = article + dnd_5e_player_010_spellcasting.article[item]

        if key == 'spells':
            for group in topic_list[key]:
                if group in keyword_list.keys():
                    for item in keyword_list[group]:
                        article = article + dnd_5e_player_011_spells.spell_descriptions_list[item]

        if key == 'conditions':
            for item in topic_list[key]:
                article = article + dnd_5e_player_012_conditions.article[item]
        if key == 'gods_of_multiverse':
            for item in topic_list[key]:
                article = article + dnd_5e_player_013_gods_of_multiverse.article[item]
        if key == 'planes_of_existence':
            for item in topic_list[key]:
                article = article + dnd_5e_player_014_planes_of_existence.article[item]

        if key == 'creature_statistics':
            for group in topic_list[key]:
                if group in keyword_list.keys():
                    for item in keyword_list[group]:
                        article = article + dnd_5e_player_015_creature_statistics.creature_statistics_list[item]

        if key == 'inspirational_readings':
            for item in topic_list[key]:
                article = article + dnd_5e_player_016_inspirational_readings.article[item]
    return article


def question_keyword_picker(request_prompt: str, temperature=0.1) -> str:
    system_prompt = promptGuideKeywordPicker.prompt
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.chat(message_list, request_prompt, temperature=temperature)
    caller = message_list[2].get('content')
    print("=" * 21, "提问方向", "=" * 21)
    print(caller)
    return caller


def question_pre_answer(request_prompt: str, temperature=0.2) -> str:
    system_prompt = promptGuidePreAnswer.prompt
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.chat(message_list, request_prompt, temperature=temperature)
    caller = message_list[2].get('content')
    print("=" * 21, "预回答结果", "=" * 21)
    print(caller)
    return caller


def masked_keyword_topics(request_prompt: str, temperature=0.0) -> str:
    system_prompt = promptGuideMaskedKeywordTopics.prompt
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.chat(message_list, request_prompt, temperature=temperature)
    caller = message_list[2].get('content')
    print("=" * 20, "问题大类分析结果", "=" * 20)
    print(caller)
    return caller


def select_keyword_topics(request_prompt: str, temperature=0.0) -> str:
    system_prompt = promptGuideKeywordTopics.prompt_front + str(
        json.dumps(topic_word_list(), ensure_ascii=False)) + promptGuideKeywordTopics.prompt_back
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.chat(message_list, request_prompt, temperature=temperature)
    caller = message_list[2].get('content')
    print("=" * 20, "问题大类筛选结果", "=" * 20)
    print(caller)
    return caller


def select_keyword_list(topic_chat, request_prompt: str, temperature=0.0) -> str:
    keyword_list = create_keyword_list(eval(topic_chat))
    system_prompt = promptGuideKeywordList.prompt
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.add_system_message(message_list, str(json.dumps(keyword_list, ensure_ascii=False)))
    message_list = contentHandler.chat(message_list, request_prompt, temperature=temperature)
    caller = message_list[3].get('content')
    print("=" * 20, "问题子类筛选结果", "=" * 20)
    print(caller)
    return caller


def guide_answer(topic_chat, keyword_chat, request_prompt: str, temperature=0.0) -> str:
    article = create_article(eval(topic_chat), eval(keyword_chat))
    print(article)
    system_prompt = promptGuideAnswer.prompt_front + keyword_chat + promptGuideAnswer.prompt_back
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

    keyword_chat = select_keyword_list(topic_chat, chat)
    print("=" * 55)

    guide_chat = guide_answer(topic_chat, keyword_chat, chat)
    print("=" * 55)

query("我想创建一个新的角色。我现在需要一份标准的空白角色文档，能给我设计一份么")
