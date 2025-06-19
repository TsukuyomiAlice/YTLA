import unittest
import tempfile
import shutil
import logging
import os
from core.frame.func import loggerConfig


class TestLoggerConfig(unittest.TestCase):
    """Test cases for logger configuration module"""

    def setUp(self):
        """Create temporary directory for log files"""
        self.temp_dir = tempfile.mkdtemp()
        loggerConfig.LOG_DIR = self.temp_dir  # Override log directory

    def tearDown(self):
        """Clean up temporary files"""
        shutil.rmtree(self.temp_dir)

    def test_file_creation(self):
        """Test if logger creates log file properly"""
        test_logger = loggerConfig.setup_logger("test_logger", "test_log")
        test_logger.info("Test message")

        log_file = os.path.join(self.temp_dir, "test_log.log")
        self.assertTrue(os.path.exists(log_file))

    def test_log_levels(self):
        """Verify log level filtering works correctly"""
        error_logger = loggerConfig.setup_logger("error_logger", "error_log",
                                                 level=logging.ERROR)
        error_logger.info("This should not appear")
        error_logger.error("This should appear")

        log_file = os.path.join(self.temp_dir, "error_log.log")
        with open(log_file, 'r') as f:
            content = f.read()
            self.assertNotIn("should not appear", content)
            self.assertIn("should appear", content)

    def test_process_decorator(self):
        """Test process log decorator functionality"""

        @loggerConfig.process_log
        def test_function(x, y):
            return x + y

        result = test_function(2, 3)
        log_file = os.path.join(self.temp_dir, "process_msg_info.log")
        with open(log_file, 'r') as f:
            content = f.read()
            self.assertIn("START   : test_function", content)
            self.assertIn("FINISHED: test_function", content)
            self.assertIn("RESULT  : 5", content)

    def test_rotation(self):
        """Test log rotation functionality"""
        rot_logger = loggerConfig.setup_logger("rotation_test", "rotation_log")

        # Write enough data to trigger rotation (32MB)
        # Note: This test might take time, consider mocking for CI environments
        large_msg = 'X' * 1024 * 1024  # 1MB per message
        for _ in range(33):
            rot_logger.info(large_msg)

        log_files = [f for f in os.listdir(self.temp_dir)
                     if f.startswith("rotation_log.log")]
        self.assertGreater(len(log_files), 1)

    def test_console_output(self):
        """Verify console output control works"""
        console_logger = loggerConfig.setup_logger("console_test", "console_log",
                                                   export_to_console=True)
        # Should test stream output, but we'll verify handler count here
        self.assertEqual(len(console_logger.handlers), 2)


if __name__ == '__main__':
    unittest.main()
