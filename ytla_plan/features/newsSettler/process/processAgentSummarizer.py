# encode = utf-8

from ytla_ai.client import contentHandler

def news_summarizer(news_time, news: str) -> dict:
    system_prompt = """
    # prompt开始
    你是一个有着专业素养的新闻从业人员。你的主要任务是对新闻进行总结。
    接下来你会收到一条微博内容，可能是新闻，但也可能并不是新闻。
    你要根据新闻六要素，仅针对微博内提到的内容，结合微博发布的时间进行提炼。
    严格返回以下的格式的结果。
    不要添加其它任何内容。不要视作为json。
    {
        "origin_source": "<新闻来源>",
        "who": [<列举所有提到的主要人物、组织、机构、团体等>],
        "what": "<简要描述事件>",
        "when": "<事件发生的时间，以yyyy-mm-dd hh:mm:ss的格式返回>",
        "where": "<事件发生的地点>",
        "why": "<事件的原因>",
        "how": "<事件的具体内容>",
        "credibility_level": <"A": 是时事新闻, "B": 是报道、不是时事新闻, "C": 不是重要内容、不是新闻内容>
        "credibility_score": <根据提炼内容相较于原文表述得到的置信度，评分为0-100的整数>
    }
    如果有无法总结，或者未明确提到的内容，该区域留空。尤其是时间。
    # prompt结束
    """

    messages = contentHandler.add_system_message([], system_prompt)
    message = contentHandler.chat(messages, f'新闻时间：{news_time}\n新闻内容：{news}')
    caller = message[2].get('content')

    print(eval(caller))
    return eval(caller)

if __name__ == '__main__':
    news_time = '2025-10-10 12:00:00'
    p = """
    【[话筒]#对抑郁症患者多理解多倾听#】抑郁症≠抑郁情绪，不是仅靠自我振奋就能好转的。多理解倾听、多关心配合、不盲目建议、不指责……#与抑郁症患者相处试试这些方法#↓↓今天是#世界精神卫生日#，转发了解。
    """
    news_summarizer(news_time, p)
