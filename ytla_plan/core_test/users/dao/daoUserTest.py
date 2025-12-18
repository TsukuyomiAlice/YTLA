# coding=utf-8
import unittest
import os
from core.classic.users.dao import daoUser
from core.classic.frame import utilConfigs


class TestUserDAO(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 使用临时测试数据库
        utilConfigs.db_files['ytla_user'] = 'test_ytla_user.db'
        daoUser.create_table()

    @classmethod
    def tearDownClass(cls):
        # 清理测试数据库
        db_path = os.path.join(utilConfigs.db_folder_path, 'test_ytla_user.db')
        if os.path.exists(db_path):
            os.remove(db_path)

    def setUp(self):
        self.test_user = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'Test@1234',
            'phone_country_code': '86',
            'phone_number': '13800138000'
        }

    def test_1_create_user(self):
        result = daoUser.create_user(self.test_user)
        self.assertTrue(result['success'])
        self.assertIsInstance(result['user_id'], int)

    def test_2_get_user_by_username(self):
        user = daoUser.get_user_by('username', 'test_user')
        print(user)
        self.assertEqual(user['username'], 'test_user')
        self.assertEqual(user['email'], 'test@example.com')

    def test_3_update_user_info(self):
        update_data = {
            'username': 'updated_user',
            'email': 'updated@example.com',
            'password': 'New@1234'
        }
        result = daoUser.update_user_info(1000000001, update_data)
        self.assertTrue(result['success'])

    def test_4_check_permission(self):
        # 先分配角色
        daoUser.assign_role(1, 'admin')
        result = daoUser.check_permission(1, 1)
        self.assertTrue(result['success'])

    def test_5_unique_check(self):
        # 测试用户名唯一性检查
        result = daoUser.check_unique('username', 'test_user')
        self.assertFalse(result)

    def test_6_soft_delete_user(self):
        result = daoUser.soft_delete_user(1)
        self.assertTrue(result)

    def test_7_login_history(self):
        daoUser.update_last_login(1, '127.0.0.1')
        history = daoUser.get_login_history(1)
        self.assertGreaterEqual(len(history), 1)


if __name__ == '__main__':
    unittest.main()