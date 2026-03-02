# encode = utf-8

from ytla_plan.features.scaffold.modules.general_classic.process import processGenerateStructure

processGenerateStructure.process_generate_structure('n', 'test', 'modules', '', False)
processGenerateStructure.process_generate_structure('n', 'test', 'modules', 'test1', False)
processGenerateStructure.process_generate_structure('n', 'test', 'modules', 'test2', True)
