from features.language.process import processModuleAssessment

plan_id = 4
module_id = 10
record_id = 1

def test_assessment_start():
    processModuleAssessment.assessment_start(plan_id, module_id, 'Ann')


ans_1 = ['eighteen', 'hotel', 'next week/year/Monday, etc.', "Don't worry (about sth)", 'half past one/two/three, etc.', 'square', 'silver', 'tyre', 'violin', 'a variety of sth/sb', 'have no doubt', 'cut up sth or cut sth up', 'facilities', 'the heart of sth', 'thriller', 'consider sb/sth (to be) sth', 'on offer', 'be the case', 'chase sb/sth away/off/out, etc.', 'innocently', 'overdo', 'put a stop to sth', 'in common with sb/sth', 'mansion', 'know what you are talking about', 'unthinkable', 'save sb (from) doing sth', 'purity', 'with a view to doing sth', 'distressed', 'at a loss for words', 'stern', 'cookie', 'in confidence', 'tactful', 'a display of affection/anger, etc.', 'so much for...', 'be glued to sth', 'go out of your way to do sth', 'be meant to do sth']
def test_assessment_step_1():
    processModuleAssessment.assessment_step_1(plan_id, module_id, record_id, ans_1)


ans_2 = ['the present', 'restaurant', 'son', 'homework', 'museum', 'cool', 'nurse', '(by) herself', 'comic', 'blonde', 'regarding', 'disease', 'family/private/sex, etc. life', 'at present', 'first-floor', 'nephew', 'give up (sth) or give (sth) up', 'of your own', 'cod', 'creature', 'likely', 'gun', 'dust', 'public transport', 'front', 'pint', 'look up to sb', 'dramatically', 'pass around/round sth or pass sth around/round', 'paperwork', 'theft', 'side by side', 'make sth into sth', 'suitably', 'for real', 'the whole thing', 'the trouble with sb/sth', 'accidental', 'rural', 'misleading', 'dock', 'selective', '(have) the best of both worlds', 'other than', 'the rear', 'smuggle', 'the unknown', 'underpaid', 'greed', 'ownership', 'in the light of sth', 'relate to sb/sth', 'multiple', 'gadget', 'have a high/low opinion of sb/sth', 'gene', 'build (sth) up or build up (sth)', 'be dead (set) against sth/doing sth', 'I trust (that)', 'a skeleton crew/staff/service', 'rarity', 'loneliness', "in sb's favour", 'magistrate', 'regardless of', 'scenic', 'transaction', 'all/just the same', 'injustice', 'unwanted', 'be led by sth', 'flick through sth', 'thread a needle', 'be wasted on sb', 'stereotypical', 'restructure', 'peculiar to sb/sth', 'crush', 'do sth to excess', 'once and for all', 'trudge along/through/up, etc.', 'deem', 'yet another/more, etc.', 'all the better/easier/more exciting, etc.', 'bear a/little/no, etc. resemblance to sth/sb', 'ruling', 'conscience', 'the globe', 'be at a premium', 'crumble', 'erupt', 'validity', 'output', 'cynical', 'commence', 'indefinitely', 'be beside yourself (with sth)', 'patch sth up', 'make allowances for sb/sth', 'a force to be reckoned with']
def test_assessment_step_2():
    processModuleAssessment.assessment_step_2(plan_id, module_id, record_id, ans_2)


ans_3 = [3, 3, 0, 0, 0, 2, 3, 3, 1, 3]
def test_assessment_result():
    processModuleAssessment.assessment_result(plan_id, module_id, record_id, ans_3)


test_assessment_step_2()