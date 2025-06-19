# coding=utf-8
import unittest
from unittest.mock import patch


class TestUtilConfigs(unittest.TestCase):
    """Unit tests for configuration utilities"""

    def test_proxy_settings(self):
        """Verify proxy configuration structure"""
        self.assertEqual(proxies['http'], 'http://192.168.71.118:20172')
        self.assertEqual(proxies['https'], proxies['http'])  # Ensure https uses same proxy

    @patch('os.name', 'nt')
    def test_windows_paths(self):
        """Validate Windows path generation"""
        self.assertIn('YTLA_DATA', get_db_folder_path())
        self.assertTrue(get_log_folder_path().startswith('D:\\'))

    @patch('os.name', 'posix')
    def test_unix_paths(self):
        """Check POSIX-compliant path formatting"""
        self.assertTrue(get_db_folder_path().startswith('/YTLA_DATAS'))
        self.assertIn('/logs', get_log_folder_path())

    def test_database_files(self):
        """Confirm database file mappings"""
        required_keys = {'temp_test', 'ytla_user', 'life_plan'}
        self.assertTrue(required_keys.issubset(db_files.keys()))
        self.assertEqual(db_files['language_dictionary_oxford'], 'Oxford 8th.db')

    def test_log_level_constants(self):
        """Ensure log level constants match logging module"""
        self.assertEqual(log_level_info, logging.INFO)
        self.assertEqual(log_level_critical, logging.CRITICAL)


if __name__ == '__main__':
    unittest.main()
