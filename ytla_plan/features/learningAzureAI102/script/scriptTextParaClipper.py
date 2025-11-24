# encode = utf-8

from ytla_plan.features.learningAzureAI102.script import scriptText

def clipper(rules: dict, starter, ender: str = '') -> list[dict]:
    """
    从scriptText.original_text中读取原文，按starter和ender分段，并根据rules进行内容分类

    Args:
        rules: 字典，key为分类标识，value为对应的行开头文本
        starter: 段落开始标识，以该行开头的内容为新段落的开始
        ender: 段落结束标识，以该行开头的内容为段落的结束

    Returns:
        list[dict]: 包含分段内容和分类信息的列表
    """
    paragraphs = []
    current_paragraph = None
    current_rule_key = None  # 记录当前正在收集的规则key

    # 读取原始文本并按行分割
    lines = scriptText.original_text.lstrip().split('\n')

    for line in lines:
        # 跳过完全空的行
        if not line.lstrip():
            continue

        line_stripped = line.lstrip()
        if line_stripped == '':
            continue

        # 检查是否是新段落的开始
        if line_stripped.startswith(starter):
            # 如果当前有未完成的段落，先添加到结果中
            if current_paragraph is not None:
                paragraphs.append(current_paragraph)

            # 创建新段落
            current_paragraph = {'raw_text': line + '\n'}

            # 初始化rules中定义的所有key
            for key in rules:
                current_paragraph[key] = ''

            # 检查并分类当前行，同时记录当前的规则key
            current_rule_key = None
            for key, value in rules.items():
                if line_stripped.lstrip().startswith(value):
                    current_paragraph[key] = line + '\n'
                    current_rule_key = key

        # 如果当前正在处理段落
        elif current_paragraph is not None:
            # 将当前行添加到段落的原始文本中
            current_paragraph['raw_text'] += line + '\n'

            # 检查当前行是否是新的规则关键词开始
            is_new_rule_start = False
            for key, value in rules.items():
                if line_stripped.lstrip().startswith(value):
                    # 如果是新的规则开始，更新current_rule_key
                    current_paragraph[key] += line + '\n'
                    current_rule_key = key
                    is_new_rule_start = True
                    break

            # 如果不是新的规则开始，且当前有正在收集的规则key，则将当前行添加到对应规则中
            if not is_new_rule_start and current_rule_key is not None:
                current_paragraph[current_rule_key] += line + '\n'

            # 检查是否是段落的结束
            if ender and line_stripped.lstrip().startswith(ender) and ender != '':
                paragraphs.append(current_paragraph)
                current_paragraph = None
                current_rule_key = None

    # 添加最后一个段落（如果有）
    if current_paragraph is not None:
        paragraphs.append(current_paragraph)


    return paragraphs
