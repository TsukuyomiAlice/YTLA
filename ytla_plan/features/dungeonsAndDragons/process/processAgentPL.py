# encode = utf-8

import json

from ytla_ai.client import contentHandler
from ytla_plan.features.dungeonsAndDragons.dataset import datasetJsonPicker
from ytla_plan.features.dungeonsAndDragons.prompt import (
    promptGuideKeywordPicker,
    promptGuidePreAnswer,
    promptGuideMaskedKeywordTopics,
    promptGuideKeywordTopics,
    promptGuideKeywordList,
    promptGuideAnswer
)

def topic_word_list():
    topics = datasetJsonPicker.extract_topic_keys(datasetJsonPicker.get_data_file_list())
    return topics


def create_keyword_list(topic_list: dict[str: list]):
    keyword_list = {}
    return keyword_list


def create_article(topic_list: dict[str: list], keyword_list: dict[str: list]) -> str:
    article = ""
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

query("什么法术可以让释放了纠缠术的植物松开？")
