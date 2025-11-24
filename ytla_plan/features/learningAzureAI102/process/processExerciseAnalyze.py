# encode = utf-8

from ytla_plan.features.learningAzureAI102.script import scriptTextParaClipper, scriptText


def analyzer() -> [list[dict], list[str]]:
    """
    分析练习记录，处理问题、答案并统计答题情况

    Returns:
        list[dict]: 包含处理后问题和统计信息的列表
    """
    # 获取原始记录
    records = scriptTextParaClipper.clipper(
        scriptText.original_text,
        {'question': '问题 ', 'answer': '你的答案', 'correct_answer': '正确答案'},
        '问题 '
    )

    # 使用字典存储合并后的问题记录，键为处理后的问题文本
    merged_questions = {}

    for record in records:
        # 处理question：去掉第一行（以"问题"开始的文字行）
        question_lines = record.get('question', '').split('\n')
        processed_question = ''

        if question_lines:
            # 跳过第一行（通常是问题开头行）
            if len(question_lines) > 1:
                # 从第二行开始保留内容
                processed_question = '\n'.join(question_lines[1:]).strip()

        # 获取原始answer和correct_answer
        user_answer = record.get('answer', '')
        correct_answer = record.get('correct_answer', '')

        # 检查是否回答错误
        is_correct = '回答错误' not in user_answer

        # 合并相同问题的记录
        if processed_question in merged_questions:
            # 更新统计信息
            merged_questions[processed_question]['count_asked'] += 1
            if is_correct:
                merged_questions[processed_question]['count_correct'] += 1
            else:
                merged_questions[processed_question]['count_error'] += 1
        else:
            # 创建新的问题记录
            merged_questions[processed_question] = {
                'question': processed_question,
                'correct_answer': correct_answer,
                'count_asked': 1,
                'count_correct': 1 if is_correct else 0,
                'count_error': 0 if is_correct else 1
            }

    # 转换为列表格式返回
    result = list(merged_questions.values())
    questions = []

    for res in result:
        questions.append(res['question'])
    """
    for res in result:
        for k, v in res.items():
            print(f'{k}: \n{v}')
        print('\n')
    print(f'总问题类别数: {len(result)}')
    print(f'总问题回答数: {sum([res["count_asked"] for res in result])}')
    print(f'总问题回答正确数: {sum([res["count_correct"] for res in result])}')
    print(f'总问题回答错误数: {sum([res["count_error"] for res in result])}')
    print(questions)
    
    """

    return result, questions

analyzer()