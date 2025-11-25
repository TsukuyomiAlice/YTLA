# encode = utf-8

from ytla_ai.client import contentHandler

from ytla_plan.features.learningAzureAI102.dataset import questionSet_AI_102
from ytla_plan.features.learningAzureAI102.prompt import promptAnalyzeFieldAI102, promptFigureSimilarQuestion, promptAnswerCheck
from ytla_plan.features.learningAzureAI102.process import processExerciseAnalyze

def analyze_domain(question: str):
    system_prompt = promptAnalyzeFieldAI102.prompt
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.chat(message_list, question, temperature=0.0)
    caller = message_list[2].get('content')
    print(caller)


def analyze_similarity(question: str):
    question_set = processExerciseAnalyze.analyzer()[1]
    system_prompt = promptFigureSimilarQuestion.prompt
    for q in question_set:
        system_prompt = system_prompt + '\n' + q
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.chat(message_list, question, temperature=0.0)
    caller = message_list[2].get('content')
    print(caller)


def judge_answer_for_single_question(question: str):
    # 准备输出内容
    separator = '=' * 50

    # 控制台输出
    print(separator)
    print(question)

    # 获取AI回复
    system_prompt = promptAnswerCheck.prompt
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.chat(message_list, question, temperature=0.0)
    caller = message_list[2].get('content')

    # 输出AI回复到控制台
    print(caller)


def judge_answer(output_file=None):
    # 如果指定了输出文件，打开文件进行写入
    file = None
    if output_file:
        file = open(output_file, 'w', encoding='utf-8')

    try:
        for attr_name in dir(questionSet_AI_102):
            if attr_name.startswith('question_09') or attr_name.startswith('question_1'):
                question = getattr(questionSet_AI_102, attr_name)

                # 准备输出内容
                separator = '=' * 50
                output_lines = [
                    separator,
                    attr_name,
                    question
                ]

                # 控制台输出
                print(separator)
                print(attr_name)
                print(question)

                # 文件输出（如果指定了文件）
                if file:
                    for line in output_lines:
                        file.write(line + '\n')

                # 获取AI回复
                system_prompt = promptAnswerCheck.prompt
                message_list = contentHandler.add_system_message([], system_prompt)
                message_list = contentHandler.chat(message_list, question, temperature=0.0)
                caller = message_list[2].get('content')

                # 输出AI回复到控制台
                print(caller)

                # 输出AI回复到文件（如果指定了文件）
                if file:
                    file.write(caller + '\n' + '\n')
    finally:
        # 确保文件被正确关闭
        if file:
            file.close()



def process_figure_question_domain():
    for attr_name in dir(questionSet_AI_102):
        if attr_name.startswith('question_'):
            question = getattr(questionSet_AI_102, attr_name)
            print(question)
            analyze_domain(question)
            analyze_similarity(question)


# judge_answer('D:\\answers_output.txt')
judge_answer_for_single_question(questionSet_AI_102.question_03_69)