# encode = utf-8

import random
from ytla_plan.features.learningAzureAI102.script import scriptTextParaClipper
from ytla_plan.features.learningAzureAI102.dataset import questionSet_AI_102

def question_picker():
    merged_questions = {}

    for attr_name in dir(questionSet_AI_102):
        if attr_name.startswith('question_'):
            question = getattr(questionSet_AI_102, attr_name)
            question_type = question.split('\n')[1]
            records = scriptTextParaClipper.clipper(
                question,
                {'question': question_type, 'answer': '# Correct Answer', 'reference': '# Reference'},
                question_type
            )

            for record in records:
                q = record.get('question', '')
                a = record.get('answer', '')
                r = record.get('reference', '')

                if not q in merged_questions:
                    merged_questions[q] = {
                        'question_id': attr_name,
                        'question': q,
                        'answer': a,
                        'reference': r,
                    }

    return merged_questions


def mock_exerciser():
    """
    随机显示问题，按回车显示答案和参考资料，直到输入q退出
    """
    questions = list(question_picker().values())
    if not questions:
        print("没有找到问题，请检查数据源")
        return

    print("欢迎使用Azure AI 102练习器！")
    print("按回车键显示问题，再次按回车键显示答案，输入q退出")

    current_question = None
    while True:
        user_input = input().strip().lower()

        if user_input == 'q':
            print("感谢使用，再见！")
            break

        if not user_input:  # 用户按了回车
            if current_question is None:  # 显示新问题
                current_question = random.choice(questions)
                print("\n" + "=" * 50)
                print(current_question['question_id'])
                print("问题:")
                print(current_question['question'].strip())
                print("\n按回车键查看答案...")
            else:  # 显示答案和参考资料
                print("\n答案:")
                print(current_question['answer'].strip())
                print("\n参考资料:")
                print(current_question['reference'].strip())
                print("=" * 50)
                current_question = None  # 重置，准备下一个问题
                print("\n按回车键显示下一个问题，输入q退出...")


# 调用新的mock_exerciser方法
mock_exerciser()