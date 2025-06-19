from core.frame.process import processGlobalPersistence


def get_global_persistence_test():
    res = processGlobalPersistence.get_global_persistence()
    print(res.data)


def update_global_persistence_layout_test():
    processGlobalPersistence.update_global_persistence('layout_swapped', True)
    processGlobalPersistence.update_global_persistence('layout_sidebar_visible', False)
    processGlobalPersistence.update_global_persistence('layout_user_language', 'en')
    processGlobalPersistence.update_global_persistence('layout_has_plan', False)
    get_global_persistence_test()

def update_global_persistence_card_test():
    processGlobalPersistence.update_card_global_persistence('sideCard_pinned', True, 2)
    processGlobalPersistence.update_card_global_persistence('sideCard_expanded', False, 4)
    processGlobalPersistence.update_card_global_persistence('planCard_pinned', False, 6)
    processGlobalPersistence.update_card_global_persistence('planCard_order', [1, 2, 3, 4, 5, 6])
    get_global_persistence_test()

def get_plan_current_module_id_test():
    res = processGlobalPersistence.get_plan_current_module_id('plan_1')
    print(res.success)

def update_plan_current_module_id_test():
    processGlobalPersistence.update_plan_current_module_id('plan_1', '2')
    get_plan_current_module_id_test()

def delete_plan_current_module_id_test():
    processGlobalPersistence.delete_plan('plan_1')
    get_plan_current_module_id_test()

