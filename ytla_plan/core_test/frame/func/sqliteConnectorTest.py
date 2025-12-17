# coding=utf-8
import os
import unittest
import sqlite3
from core.domain.area.frame.func import sqlite_cursor, database_root_specific, loggerConfig


class TestSQLiteConnector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Get test database path from config
        cls.db_path = database_root_specific("temp_test")

        # Initialize test schema
        init_sql = """CREATE TABLE IF NOT EXISTS test_table (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    value INTEGER)"""
        try:
            sqlite_cursor(cls.db_path, init_sql, ())
        except Exception as e:
            loggerConfig.db_error_logger.error(f"Test table initialization failed: {str(e)}")

    @classmethod
    def tearDownClass(cls):
        """Cleanup test database"""
        try:
            if os.path.exists(cls.db_path):
                os.remove(cls.db_path)
                loggerConfig.db_info_logger.info(f"Test database deleted: {cls.db_path}")
        except Exception as e:
            loggerConfig.db_error_logger.error(f"Test database cleanup failed: {str(e)}")

    def test_basic_crud(self):
        # Test INSERT operation
        insert_sql = "INSERT INTO test_table (name, value) VALUES (?, ?)"
        insert_params = ("test_item", 42)

        # Execute and validate insertion
        sqlite_cursor(self.db_path, insert_sql, insert_params)

        # Verify insertion
        select_sql = "SELECT * FROM test_table WHERE name = ?"
        result = sqlite_cursor(self.db_path, select_sql, ("test_item",))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], "test_item")
        self.assertEqual(result[0]['value'], 42)

        # Test UPDATE operation
        update_sql = "UPDATE test_table SET value = ? WHERE name = ?"
        sqlite_cursor(self.db_path, update_sql, (99, "test_item"))

        # Verify update
        updated = sqlite_cursor(self.db_path, select_sql, ("test_item",))
        self.assertEqual(updated[0]['value'], 99)

        # Test DELETE operation
        delete_sql = "DELETE FROM test_table WHERE name = ?"
        sqlite_cursor(self.db_path, delete_sql, ("test_item",))

        # Verify deletion
        after_delete = sqlite_cursor(self.db_path, select_sql, ("test_item",))
        self.assertEqual(len(after_delete), 0)

    def test_transaction_rollback(self):
        # Test transaction rollback
        insert_sql = "INSERT INTO test_table (name, value) VALUES (?, ?)"
        try:
            # Intentionally trigger primary key violation
            sqlite_cursor(self.db_path, insert_sql, (1, "force_error", 0))
        except sqlite3.Error:
            pass

        # Verify rollback
        check_sql = "SELECT * FROM test_table WHERE name = ?"
        result = sqlite_cursor(self.db_path, check_sql, ("force_error",))
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
