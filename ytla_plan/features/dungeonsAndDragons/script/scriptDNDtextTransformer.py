# encode = utf-8

from ytla_plan.features.dungeonsAndDragons.script import scriptDNDtext

def changer():
    # 简单的句子分割，使用常见的中文和英文句子分隔符
    sentences = []
    current_sentence = ""
    separators = ['.', '。', '!', '！', '?', '？', ';', '；', '：']

    last_char = ""
    for char in scriptDNDtext.original_text:
        if last_char in separators:
            if char != '\n':
                current_sentence += char
            else:
                # 确保句子有一定长度
                if len(current_sentence.strip()) > 10:
                    sentences.append(current_sentence)
                    current_sentence = ""
        else:
            if char != '\n':
                current_sentence += char
        last_char = char

    # 添加最后一个句子（如果有）
    if current_sentence.strip():
        sentences.append(current_sentence)
    for sentence in sentences:
        print(sentence)

changer()