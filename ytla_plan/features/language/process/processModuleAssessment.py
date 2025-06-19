"""
词汇量评估的流程

一阶段测试的思路
https://preply.com/en/learn/english/test-your-vocab
参考文章
https://zhuanlan.zhihu.com/p/43989109

测试词源
https://englishprofile.org


测试过程

测试之前
告知测试者不要因测试结果产生压力，同时需要保持诚信
只需要知道该单词的任何一个含义就标记为“认识”

第一阶段 - 1
自举模式，40个单词 难度范围如下
如果没有做过任何先前的测试
5/5/10/10/5/5
如果有做过测试：根据上一次的核定评级
当前评级 - 10，当前评级 + 1等级 - 10，其它评级 - 5
第一阶段 - 2
自举模式，100个单词 难度范围如下
30/30/20/10/5/5 (当前评级，当前评级+1，当前评级-1，当前评级+2，当前评级-2，当前评级+3）
举例:
如果当前评级为C1,那么就是C1-C2-B2-B1-A2-A1
如果当前评级为B1,那么就是B1-B2-A2-C1-A1-C2

评定
结合历史记录做判定（初始认为全部认识）
该评级范围内的词汇掌握量 = 该评级上测试过的词汇中被标记为“认识”或“确实认识”的词汇总数 / 该级别上在全部测试中测试过的词汇总数 * 该级别上的词汇总数
评定包含第二阶段测试过的词汇


第二阶段
初始的测试评级为第一阶段里掌握率超过50%的最高评级
置信度为二阶段测试准确率/一阶段掌握率
置信度需要达到80%该阶段的一阶段的词汇掌握量的百分数才为可信
举例：
如果有人在第一次测试时选择全部都认识
那么在第二阶段时，他必须在所有词汇且各评级范围均达到80%的一阶段掌握量才行

如果二阶段的正确率在一阶段描述的掌握率的80%或以上，但是没触发升级情况
那么评判该等级词汇掌握率 = （第二阶段测试的准确率 + 第一阶段得出的词汇掌握量的百分数） / 2

如果第二阶段的正确率低于第一阶段后的词汇掌握量的百分数的50%，或高于80%，并且一阶段乱选，
那么评判该等级词汇掌握率 = （第二阶段测试的准确率 * 3 + 第一阶段得出的词汇掌握量的百分数） / 4

其它情况则为
那么评判该等级词汇掌握率 = （第二阶段测试的准确率 * 2 + 第一阶段得出的词汇掌握量的百分数） / 3

二阶段的测试词汇个数
一阶段结果后，评级等级范围的词汇 10个
正确率在50%-80%则立刻结束

正确率超过80% +1等级 10个
如果失败没有惩罚
如果依然超过80% 再+1等级
直到正确率低于80%

正确率低于50% -1等级 10个
如果依然低于50% 再-1等级
并且作废一阶段的测试结果
直到正确率达到50%

对于未被测试到的等级
根据基础的结果进行偏差计算
例如极端情况
有人在一阶段乱选全部认识，二阶段最后被降级到了B1
那么剩下的两个阶段A2和A1就分别是B1的结果乘以1.1和1.2，但不会超过100%
或者
有人在一阶段乱选全部不认识，二阶段最后被升级到了C1
那么剩下的C2阶段的结果应该是C1的结果乘以0.7

最终评判结果

"""
import json
import random

from core.modules.dao import daoModulePersistence, daoModules
from core.frame.func.loggerConfig import process_log
from core.frame.instance.instanceProcessToRoutes import Response
from features.language.dao import daoModuleAssessmentCefr

assessment_sheet = {
    "record_id": 0,
    "step_1_a_words": {
        "A1": {"words": [], "checked": [], "knowledge": 0, "knowledge_rate": 0},
        "A2": {"words": [], "checked": [], "knowledge": 0, "knowledge_rate": 0},
        "B1": {"words": [], "checked": [], "knowledge": 0, "knowledge_rate": 0},
        "B2": {"words": [], "checked": [], "knowledge": 0, "knowledge_rate": 0},
        "C1": {"words": [], "checked": [], "knowledge": 0, "knowledge_rate": 0},
        "C2": {"words": [], "checked": [], "knowledge": 0, "knowledge_rate": 0},
    },
    "step_1_b_words": {
        "A1": {"words": [], "checked": [], "knowledge": 0, "knowledge_rate": 0},
        "A2": {"words": [], "checked": [], "knowledge": 0, "knowledge_rate": 0},
        "B1": {"words": [], "checked": [], "knowledge": 0, "knowledge_rate": 0},
        "B2": {"words": [], "checked": [], "knowledge": 0, "knowledge_rate": 0},
        "C1": {"words": [], "checked": [], "knowledge": 0, "knowledge_rate": 0},
        "C2": {"words": [], "checked": [], "knowledge": 0, "knowledge_rate": 0},
    },
    "base_level": "",
    "step_1_adjusted_rate": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    "step_1_result": "",
    "step_2_words": {

    },
    "step_2_adjusted_rate": [1.01, 1.01, 1.01, 1.01, 1.01, 1.01],
    "step_2_result": "",
    "final_estimated": "",
    "final_result": "",
}

# adjust table: for those levels are not tested in step 2, and the final evaluation level is not as the same with step 1

adjust_table = {
    "A1": [0.5, 0.2, 0.1, 0.1, 0.1, 0.05],
    "A2": [0.8, 0.5, 0.2, 0.1, 0.1, 0.05],
    "B1": [0.9, 0.8, 0.5, 0.2, 0.1, 0.1],
    "B2": [1.0, 0.9, 0.8, 0.5, 0.2, 0.1],
    "C1": [1.0, 1.0, 0.9, 0.8, 0.5, 0.2],
    "C2": [1.0, 1.0, 1.0, 0.9, 0.8, 0.5],
}

level_list = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
level_word_count_base = [645, 1081, 1881, 2562, 1506, 2084]
level_word_count_sum = [645, 1726, 3607, 6169, 7675, 9759]
# level_word_count_pass: 1x, 1x, 1x, 0.9x 0.8x, 0.5x
level_word_count_pass = [0, 1057, 2386, 4404, 6222, 8160]


def check_last_level(record: dict) -> str:
    """Check the user's last assessment level from previous record.

    Args:
        record: Previous assessment record dictionary

    Returns:
        str: Default 'B1' if no record exists, otherwise returns the last level
    """
    if record is None or 'final_result' not in record.keys():
        return 'B1'
    if record['final_result'] not in level_list:
        return 'B1'
    return record['final_result']


def pick_words(word_level: str, word_amount: int) -> list:
    """Select words for assessment from database.

    Args:
        word_level: CEFR level (A1-C2)
        word_amount: Number of words to select

    Returns:
        list: Selected words
    """
    word_list = daoModuleAssessmentCefr.pick_step_1_words(word_level, word_amount)
    return word_list


@process_log
def generate_step_1_a_words(sheet, base_level) -> tuple:
    """Generate words for first stage (part A) of assessment.

    Args:
        sheet: Assessment sheet dictionary
        base_level: Starting CEFR level

    Returns:
        tuple: Updated sheet and word list
    """
    amount_list = [5, 5, 5, 5, 5, 5]
    if base_level == 'C2':
        amount_list = [5, 5, 5, 5, 10, 10]
    else:
        amount_list[level_list.index(base_level)] = 10
        amount_list[level_list.index(base_level) + 1] = 10
    word_list = []
    for i in range(0, len(level_list)):
        new_word_list = pick_words(level_list[i], amount_list[i])
        word_list = word_list + new_word_list
        sheet["step_1_a_words"][level_list[i]]["words"] = new_word_list
    return sheet, word_list


@process_log
def generate_step_1_b_words(sheet, step_1_result) -> tuple:
    """Generate words for first stage (partB) of assessment.

    Args:
        sheet: Assessment sheet dictionary
        step_1_result: The answer of the 1 - A stage

    Returns:
        tuple: Updated sheet and word list
    """
    amount_list = [5, 5, 5, 5, 5, 5]
    if step_1_result == 'C2':
        amount_list = [5, 5, 15, 15, 30, 30]
    if step_1_result == 'C1':
        amount_list = [5, 5, 15, 15, 30, 30]
    if step_1_result == 'B2':
        amount_list = [5, 5, 15, 30, 30, 15]
    if step_1_result == 'B1':
        amount_list = [5, 15, 30, 30, 15, 5]
    if step_1_result == 'A2':
        amount_list = [15, 30, 30, 15, 5, 5]
    if step_1_result == 'A1':
        amount_list = [30, 30, 15, 15, 5, 5]
    word_list = []
    for i in range(0, len(level_list)):
        new_word_list = pick_words(level_list[i], amount_list[i])
        word_list = word_list + new_word_list
        sheet["step_1_b_words"][level_list[i]]["words"] = new_word_list
    return sheet, word_list


@process_log
def generate_step_2_words(sheet, level):
    prepared_words = daoModuleAssessmentCefr.pick_step_2_words(level)
    groups = []
    question_group = []
    for _ in prepared_words:
        question_group.append(_)
        if len(question_group) == 4:
            groups.append(question_group)
            question_group = []
    answers = [random.randint(0, 3) for _ in range(10)]
    # returned questions
    question_list = []
    for i in range(10):
        question_list.append({groups[i][answers[i]]['GUIDE_WORD']: [groups[i][0]['BASE_WORD'],
                                                                    groups[i][1]['BASE_WORD'],
                                                                    groups[i][2]['BASE_WORD'],
                                                                    groups[i][3]['BASE_WORD']]})
    sheet["step_2_words"].update({level: {"groups": groups, "answers": answers}})
    return sheet, question_list


@process_log
def assessment_start(plan_id, module_id, user_name):
    """Initialize vocabulary assessment process.

        Args:
            plan_id: ID of the learning plan
            module_id: ID of assessment module
            user_name: Name of user taking assessment

        Returns:
            Response: Contains record ID and initial word list
    """
    last_record = daoModulePersistence.get_last_content(plan_id, module_id, user_name)
    base_level = check_last_level(last_record)
    sheet = assessment_sheet.copy()
    sheet["base_level"] = base_level
    instance = daoModulePersistence.Instance()
    instance.creator = user_name
    instance.updater = user_name
    instance.content = '{}'
    new_record_id = daoModulePersistence.insert_content(plan_id, module_id, instance)
    instance.record_id = new_record_id
    sheet["record_id"] = new_record_id
    sheet, word_list = generate_step_1_a_words(sheet, base_level)
    instance.content = str(json.dumps(sheet))
    daoModulePersistence.update_content(plan_id, module_id, instance)
    response = Response()
    response.data = {
        "record_id": new_record_id,
        "word_list": word_list
    }
    return response


@process_log
def assessment_step_1(plan_id, module_id, record_id, answer_list: list):
    """Process first stage (part A) assessment results.

        Args:
            plan_id: ID of the learning plan
            module_id: ID of assessment module
            record_id: Assessment record ID
            answer_list: User's answers for known words

        Returns:
            Response: Contains record ID and next word list
        """
    response = Response()
    instance = daoModulePersistence.Instance(record_id)
    instance.load_persistence(plan_id, module_id)
    sheet = json.loads(instance.content)
    if len(answer_list) > 40:
        response.success = False
        response.code = 400
        response.message = 'answer_list length is illegal'
        return response
    # statistic
    for level in level_list:
        for word in sheet["step_1_a_words"][level]["words"]:
            if word in answer_list:
                sheet["step_1_a_words"][level]["checked"].append(word)
                sheet["step_1_a_words"][level]["knowledge"] += 1
    for level in level_list:
        sheet["step_1_a_words"][level]["knowledge_rate"] = round(
            sheet["step_1_a_words"][level]["knowledge"] / len(sheet["step_1_a_words"][level]["words"]), 2)
    # step_1_level_result
    step_1_result = "C2"
    for level in level_list:
        if sheet["step_1_a_words"][level]["knowledge_rate"] >= 0.5:
            step_1_result = level
    # step_1_b
    sheet, word_list = generate_step_1_b_words(sheet, step_1_result)
    instance.content = str(json.dumps(sheet))
    daoModulePersistence.update_content(plan_id, module_id, instance)
    response = Response()
    response.data = {
        "record_id": record_id,
        "word_list": word_list
    }
    return response


@process_log
def assessment_step_2(plan_id, module_id, record_id, answer_list: list):
    """Process first stage (part B) assessment results.

        Args:
            plan_id: ID of the learning plan
            module_id: ID of assessment module
            record_id: Assessment record ID
            answer_list: User's answers for known words

        Returns:
            Response: Contains record ID and next step data
        """
    response = Response()
    instance = daoModulePersistence.Instance(record_id)
    instance.load_persistence(plan_id, module_id)
    sheet = json.loads(instance.content)
    if len(answer_list) > 100:
        response.success = False
        response.code = 400
        response.message = 'answer_list length is illegal'
        return response
    # statistic
    for level in level_list:
        for word in sheet["step_1_b_words"][level]["words"]:
            if word in answer_list:
                sheet["step_1_b_words"][level]["checked"].append(word)
                sheet["step_1_b_words"][level]["knowledge"] += 1
    i = 0
    for level in level_list:
        sheet["step_1_b_words"][level]["knowledge_rate"] = round(
            sheet["step_1_b_words"][level]["knowledge"] / len(sheet["step_1_b_words"][level]["words"]), 2)
        sheet["step_1_adjusted_rate"][i] = round(
            (sheet["step_1_a_words"][level]["knowledge"] + sheet["step_1_b_words"][level]["knowledge"]) / (
                    len(sheet["step_1_a_words"][level]["words"]) + len(sheet["step_1_b_words"][level]["words"])), 2)
        i += 1
    # step_1_level_result
    step_1_result = "A1"
    for i in range(6):
        if sheet["step_1_adjusted_rate"][i] >= 0.5:
            step_1_result = level_list[i]
    sheet["step_1_result"] = step_1_result
    sheet["step_2_result"] = step_1_result
    # step_2
    sheet, question_list = generate_step_2_words(sheet, step_1_result)
    instance.content = str(json.dumps(sheet))
    daoModulePersistence.update_content(plan_id, module_id, instance)
    response = Response()
    response.data = {
        "record_id": record_id,
        "is_step_2": True,
        "question_list": question_list,
        "final_result": ''
    }
    return response


def collect_vocabulary(plan_id, vocabulary_module_id, sheet):
    """Collect unknown words from assessment to create vocabulary list.

       Args:
           plan_id: ID of the learning plan
           vocabulary_module_id: ID of vocabulary module
           sheet: Assessment sheet dictionary
    """
    vocabulary = []

    # Collect unknown words from stage 1A
    for level in level_list:
        known_words = set(sheet["step_1_a_words"][level]["checked"])
        all_words = set(sheet["step_1_a_words"][level]["words"])
        vocabulary.extend(list(all_words - known_words))

    # Collect unknown words from stage 1B
    for level in level_list:
        known_words = set(sheet["step_1_b_words"][level]["checked"])
        all_words = set(sheet["step_1_b_words"][level]["words"])
        vocabulary.extend(list(all_words - known_words))

    # Remove duplicates
    vocabulary = list(set(vocabulary))

    # Calling processModuleVocabulary
    if vocabulary:
        from features.language.process import processModuleVocabulary
        processModuleVocabulary.create_new_vocabulary_book(plan_id, vocabulary_module_id, 'Ann', vocabulary)


@process_log
def assessment_result(plan_id, module_id, record_id, answer_list: list):
    """Calculate and return final assessment results.

        Args:
            plan_id: ID of the learning plan
            module_id: ID of assessment module
            record_id: Assessment record ID
            answer_list: User's answers for final questions

        Returns:
            Response: Contains final assessment result
    """
    response = Response()
    instance = daoModulePersistence.Instance(record_id)
    instance.load_persistence(plan_id, module_id)
    sheet = json.loads(instance.content)
    if len(answer_list) != 10:
        response.success = False
        response.code = 400
        response.message = 'answer_list length is illegal'
        return response
    # statistic
    pass_rate = round(sheet["step_1_adjusted_rate"][level_list.index(sheet["step_1_result"])] * 0.8, 2)
    upgrade_rate = 0.8
    sheet["step_2_words"][sheet["step_2_result"]]["answered"] = answer_list
    correct_answer = sheet["step_2_words"][sheet["step_2_result"]]["answers"]
    correct_count = 0
    for i in range(10):
        if answer_list[i] == correct_answer[i]:
            correct_count += 1
    correct_rate = round(correct_count / 10, 2)
    # calculate

    # downgrade
    if correct_rate < pass_rate:
        sheet["step_2_adjusted_rate"][level_list.index(sheet["step_2_result"])] = round(
            (correct_rate * 3 + sheet["step_1_adjusted_rate"][level_list.index(sheet["step_1_result"])]) / 4, 2)
        if sheet["step_2_result"] != 'A1' and sheet["step_2_adjusted_rate"][
            level_list.index(sheet["step_2_result"]) - 1] == 1.01:
            sheet["step_2_result"] = level_list[level_list.index(sheet["step_2_result"]) - 1]
            level = sheet["step_2_result"]
            sheet, question_list = generate_step_2_words(sheet, level)
            instance.content = str(json.dumps(sheet))
            daoModulePersistence.update_content(plan_id, module_id, instance)
            response = Response()
            response.data = {
                "record_id": record_id,
                "is_step_2": True,
                "question_list": question_list,
                "final_result": ''
            }
            return response
    # upgrade
    if correct_rate >= upgrade_rate:
        sheet["step_2_adjusted_rate"][level_list.index(sheet["step_2_result"])] = round(
            (correct_rate * 3 + sheet["step_1_adjusted_rate"][level_list.index(sheet["step_1_result"])]) / 4, 2)
        if sheet["step_2_result"] != 'C2' and sheet["step_2_adjusted_rate"][
            level_list.index(sheet["step_2_result"]) + 1] == 1.01:
            sheet["step_2_result"] = level_list[level_list.index(sheet["step_2_result"]) + 1]
            level = sheet["step_2_result"]
            sheet, question_list = generate_step_2_words(sheet, level)
            instance.content = str(json.dumps(sheet))
            daoModulePersistence.update_content(plan_id, module_id, instance)
            response = Response()
            response.data = {
                "record_id": record_id,
                "is_step_2": True,
                "question_list": question_list,
                "final_result": ''
            }
            return response

    # final
    sheet["final_result"] = sheet["step_2_result"]
    sheet["step_2_adjusted_rate"][level_list.index(sheet["step_2_result"])] = round(
        (correct_rate * 2 + sheet["step_1_adjusted_rate"][level_list.index(sheet["step_1_result"])]) / 3, 2)
    for i in range(6):
        if sheet["step_2_adjusted_rate"][i] == 1.01:
            if level_list.index(sheet["final_result"]) > i:
                sheet["step_2_adjusted_rate"][i] = round(adjust_table[sheet["final_result"]][i], 2)
            if level_list.index(sheet["final_result"]) < i:
                sheet["step_2_adjusted_rate"][i] = round(
                    adjust_table[sheet["final_result"]][i] * sheet["step_1_adjusted_rate"][i], 2)
    estimate_amount = 0
    for i in range(6):
        estimate_amount += round(sheet["step_2_adjusted_rate"][i] * level_word_count_base[i], 0)
    sheet["final_estimated"] = estimate_amount
    for i in range(6):
        if estimate_amount >= level_word_count_pass[i]:
            sheet["final_result"] = level_list[i]

    instance.content = str(json.dumps(sheet))
    daoModulePersistence.update_content(plan_id, module_id, instance)
    response = Response()
    response.data = {
        "record_id": record_id,
        "is_step_2": False,
        "question_list": [],
        "final_result": sheet["final_result"]
    }
    vocabulary_module_id = daoModules.if_exist_specific_module(plan_id, 'language', 'vocabulary')
    if vocabulary_module_id:
        collect_vocabulary(plan_id, vocabulary_module_id, sheet)
    return response
