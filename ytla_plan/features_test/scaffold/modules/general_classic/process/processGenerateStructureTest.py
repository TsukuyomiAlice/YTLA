# encode = utf-8

from ytla_plan.features.scaffold.modules.general_classic.process import processGenerateStructure

"""
Test case 1
generate the specified modules
"""
"""
processGenerateStructure.process_generate_structure('n', 'test', 'modules', '', False)
processGenerateStructure.process_generate_structure('n', 'test', 'modules', 'test1', False)
processGenerateStructure.process_generate_structure('n', 'test', 'modules', 'test2', True)
"""

"""
Test case 2
generate the scaffold structure itself
"""

"""
processGenerateStructure.process_generate_structure('n', 'scaffold', 'modules', '', False)
processGenerateStructure.process_generate_structure('n', 'scaffold', 'modules', 'backend_python_flask', True)
processGenerateStructure.process_generate_structure('n', 'scaffold', 'modules', 'frontend_vue3', True)
processGenerateStructure.process_generate_structure('n', 'scaffold', 'modules', 'general_classic', True)
"""

processGenerateStructure.process_generate_structure('y','classic', 'cards', 'sideCard', False)