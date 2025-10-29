# encode = utf-8

from ytla_ai.client import contentHandler

from ytla_plan.features.learningAzure.dataset import questionSet_AI_102
from ytla_plan.features.learningAzure.prompt import promptAnalyzeFieldAI102

def analyze():
    system_prompt = promptAnalyzeFieldAI102.prompt
    message_list = contentHandler.add_system_message([], system_prompt)
    message_list = contentHandler.chat(message_list, questionSet_AI_102.question_1_11, temperature=0.0)
    caller = message_list[2].get('content')
    print(caller)

analyze()
