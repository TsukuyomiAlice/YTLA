import unittest
from core.modules.dao import daoModules
from core.modules.dao.daoModules import Instance, add_module, update_module_detail, soft_delete_module


class TestDaoModules(unittest.TestCase):
    def setUp(self):
        """Initialize test environment"""
        self.test_module = Instance("Test Module", "test_type")
        self.test_module.detail_params = '{}'
        add_module("test_type", "", {
            'belong_plan_id': 0,
            'name': "Test Module",
            'tags': "",
            'description': "",
            'icon_path': "",
            'background_path': ""
        })
        # Get the last inserted module ID
        sql = "SELECT MODULE_ID FROM MODULES WHERE NAME = ? ORDER BY MODULE_ID DESC LIMIT 1"
        res = daoModules.execute_cursor(sql, ("Test Module",))
        self.module_id = res[0]['MODULE_ID']

    def tearDown(self):
        """Clean up test data"""
        soft_delete_module(self.module_id)

    def test_1_add_module(self):
        """Test adding a new module"""
        new_module = Instance("New Test Module", "new_type")
        add_module("new_type", "", {
            'belong_plan_id': 0,
            'name': "New Test Module",
            'tags': "",
            'description': "",
            'icon_path': "",
            'background_path': ""
        })

        # Verify the new module was added
        sql = "SELECT MODULE_ID FROM MODULES WHERE NAME = ?"
        res = daoModules.execute_cursor(sql, ("New Test Module",))
        self.assertGreater(len(res), 0)

    def test_2_update_module_detail(self):
        """Test updating module details"""
        updated_module = Instance("Updated Module", "updated_type", module_id=self.module_id)
        updated_module.description = "Updated description"
        update_module_detail(updated_module)

        # Verify the update
        sql = "SELECT DESCRIPTION FROM MODULES WHERE MODULE_ID = ?"
        res = daoModules.execute_cursor(sql, (self.module_id,))
        self.assertEqual(res[0]['DESCRIPTION'], "Updated description")

    def test_3_activate_deactivate(self):
        """Test module activation/deactivation workflow"""
        from core.modules.dao.daoModules import deactivate_module, activate_module, check_module_active_status

        deactivate_module(self.module_id)
        self.assertEqual(check_module_active_status(self.module_id), '0')

        activate_module(self.module_id)
        self.assertEqual(check_module_active_status(self.module_id), '1')

    def test_4_soft_delete(self):
        """Test soft deletion of module"""
        soft_delete_module(self.module_id)

        # Verify soft delete
        sql = "SELECT DELETE_FLAG FROM MODULES WHERE MODULE_ID = ?"
        res = daoModules.execute_cursor(sql, (self.module_id,))
        self.assertEqual(res[0]['DELETE_FLAG'], '1')


if __name__ == '__main__':
    unittest.main()