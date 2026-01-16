import unittest
import json
from core.classic.modules.dao.daoModulePersistence import DBConnector, Instance, get_content, insert_content, update_content


class TestDaoModulePersistence(unittest.TestCase):
    def setUp(self):
        """Initialize test environment"""
        self.plan_id = 999  # Fixed test plan ID
        self.module_id = 1  # Fixed test module ID
        self.test_user = "test_user"

        # Create test instance
        self.test_instance = Instance()
        self.test_instance.content = json.dumps({"test": "data"})
        self.test_instance.creator = self.test_user
        self.test_instance.updater = self.test_user

        # Insert test data
        self.record_id = insert_content(self.plan_id, self.module_id, self.test_instance)

    def tearDown(self):
        """Clean up test data"""
        # Drop the test table
        db = DBConnector(self.plan_id, self.module_id)
        db.drop_table()

    def test_1_insert_content(self):
        """Test inserting new content"""
        # Verify the insert was successful
        res = get_content(self.plan_id, self.module_id, self.record_id)
        self.assertEqual(len(res), 1)
        self.assertEqual(json.loads(res[0]['CONTENT']), {"test": "data"})

    def test_2_get_content(self):
        """Test retrieving content"""
        # Test get by record_id
        res = get_content(self.plan_id, self.module_id, self.record_id)
        self.assertEqual(len(res), 1)

        # Test get all
        res_all = get_content(self.plan_id, self.module_id)
        self.assertGreaterEqual(len(res_all), 1)

    def test_3_get_last_content(self):
        """Test getting last content by user"""
        from core.classic.modules.dao.daoModulePersistence import get_last_content

        # Should return our test data
        content = get_last_content(self.plan_id, self.module_id, self.test_user)
        self.assertEqual(content, {"test": "data"})

    def test_4_update_content(self):
        """Test updating content"""
        # Create updated instance
        updated_instance = Instance(self.record_id)
        updated_instance.content = json.dumps({"test": "updated"})
        updated_instance.updater = "updated_user"

        # Perform update
        update_content(self.plan_id, self.module_id, updated_instance)

        # Verify update
        res = get_content(self.plan_id, self.module_id, self.record_id)
        self.assertEqual(json.loads(res[0]['CONTENT']), {"test": "updated"})
        self.assertEqual(res[0]['UPDATER'], "updated_user")

    def test_5_delete_content(self):
        """Test soft deletion of content"""
        from core.classic.modules.dao.daoModulePersistence import delete_content

        # Perform soft delete
        delete_instance = Instance(self.record_id)
        delete_content(self.plan_id, self.module_id, delete_instance)

        # Verify deletion
        res = get_content(self.plan_id, self.module_id, self.record_id)
        self.assertEqual(len(res), 0)  # Should not return soft-deleted records


if __name__ == '__main__':
    unittest.main()
