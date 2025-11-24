# encode = utf-8

from ytla_plan.features.learningAzureAI102.script import scriptTextParaClipper
from ytla_plan.features.learningAzureAI102.dataset import questionSet_AI_102

def question_picker():
    merged_questions = {}

    for attr_name in dir(questionSet_AI_102):
        if attr_name.startswith('question_'):
            question = getattr(questionSet_AI_102, attr_name)
            records = scriptTextParaClipper.clipper(
                question,
                {'question': '# ', 'answer': '# Correct Answer:', 'reference': '# Reference:'},
                '# '
            )

            for record in records:
                q = record.get('question', '')
                a = record.get('answer', '')
                r = record.get('reference', '')

                if not q in merged_questions:
                    merged_questions[q] = {
                        'question': q,
                        'answer': a,
                        'reference': r,
                    }

    print(merged_questions)

    return merged_questions


question_picker()