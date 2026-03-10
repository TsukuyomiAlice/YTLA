# encode = utf-8

from ytla_plan.features.scaffold.modules.general_classic.process import processGenerateStructure

"""
Test case 1
generate the specified modules
"""
"""
processGenerateStructure.process_generate_structure(False, 'test', 'modules', '', True, False)
processGenerateStructure.process_generate_structure(False, 'test', 'modules', 'test1', True, False)
processGenerateStructure.process_generate_structure(False, 'test', 'modules', 'test2', True, True)
"""

"""
Test case 2
generate the scaffold structure itself
"""

"""
processGenerateStructure.process_generate_structure(False, 'scaffold', 'modules', '', True, False)
processGenerateStructure.process_generate_structure(False, 'scaffold', 'modules', 'backend_python_flask', True, False)
processGenerateStructure.process_generate_structure(False, 'scaffold', 'modules', 'frontend_vue3', True, False)
processGenerateStructure.process_generate_structure(False, 'scaffold', 'modules', 'general_classic', True, False)
"""

processGenerateStructure.process_generate_structure(True, 'classic', 'users', '', True, False)