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

"""
Test case 3: classic_vue3 - sidecard type (_type)
"""
# processGenerateStructure.process_generate_structure(False, 'test_classic', 'cards', '', True, True)

"""
Test case 4: classic_vue3 - sidecard (specific implementation)
"""
# processGenerateStructure.process_generate_structure(False, 'test_classic', 'cards', 'test_sidecard', True, True)

"""
Test case 5: classic_vue3 - module type (_type)
"""
# processGenerateStructure.process_generate_structure(False, 'test_classic', 'modules', '', True, True)

"""
Test case 6: classic_vue3 - module (specific implementation)
"""
# processGenerateStructure.process_generate_structure(False, 'test_classic', 'modules', 'test_module', True, True)

"""
Original test case
"""
processGenerateStructure.process_generate_structure(False, 'scaffold', 'modules', 'create_card', False, True)