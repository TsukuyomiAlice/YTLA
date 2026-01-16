# coding=utf-8
import unittest
from unittest.mock import patch

from core.classic.frame import utilConfigs


class TestUtilConfigs(unittest.TestCase):
    """Unit tests for configuration utilities"""

    def test_proxy_settings(self):
        """Verify proxy configuration structure"""
        self.assertEqual(utilConfigs.proxies['http'], 'http://192.168.71.118:20172')
        self.assertEqual(utilConfigs.proxies['https'], utilConfigs.proxies['http'])  # Ensure https uses same proxy

    @patch('os.name', 'nt')
    def test_windows_paths(self):
        """Validate Windows path generation"""
        self.assertIn('YTLA_DATA', utilConfigs.get_db_folder_path())
        self.assertTrue(utilConfigs.get_log_folder_path().startswith('D:\\'))

    @patch('os.name', 'posix')
    def test_unix_paths(self):
        """Check POSIX-compliant path formatting"""
        self.assertTrue(utilConfigs.get_db_folder_path().startswith('/YTLA_DATAS'))
        self.assertIn('/logs', utilConfigs.get_log_folder_path())

    def test_database_files(self):
        """Confirm database file mappings"""
        required_keys = {'temp_test', 'ytla_user', 'life_plan'}
        self.assertTrue(required_keys.issubset(utilConfigs.db_files.keys()))
        self.assertEqual(utilConfigs.db_files['language_dictionary_oxford'], 'Oxford 8th.db')

    def test_log_level_constants(self):
        """Ensure log level constants match logging module"""
        self.assertEqual(utilConfigs.log_level_info, utilConfigs.logging.INFO)
        self.assertEqual(utilConfigs.log_level_critical, utilConfigs.logging.CRITICAL)


if __name__ == '__main__':
    unittest.main()
