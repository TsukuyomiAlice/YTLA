# encode = utf-8

from ytla_ai.client import contentHandler

from ytla_plan.features.learningAzureAI102.dataset import questionSet_AI_102
from ytla_plan.features.learningAzureAI102.prompt import promptAnalyzeFieldAI102, promptFigureSimilarQuestion
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


def process_figure_question_domain():
    for attr_name in dir(questionSet_AI_102):
        if attr_name.startswith('question_'):
            question = getattr(questionSet_AI_102, attr_name)
            print(question)
            analyze_domain(question)
            analyze_similarity(question)


process_figure_question_domain()