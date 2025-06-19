import unittest
import tempfile
import os
import json
from unittest.mock import patch
from core.basic.func.crossProjectMessageMailer import Message, send_message, receive_message, slash


class TestSlashFunction(unittest.TestCase):
    """Test path separator detection functionality"""

    @patch('os.name', 'nt')
    def test_windows_separator(self):
        """Should return backslash for Windows systems"""
        self.assertEqual(slash(), '\\')

    @patch('os.name', 'posix')
    def test_unix_separator(self):
        """Should return forward slash for Unix-like systems"""
        self.assertEqual(slash(), '/')


class TestMessageClass(unittest.TestCase):
    """Verify message object initialization"""

    def test_message_creation(self):
        """Should correctly initialize message attributes"""
        test_msg = Message("test_message")
        self.assertEqual(test_msg.message_name, "test_message")
        self.assertEqual(test_msg.message_type, ' ')
        self.assertEqual(test_msg.message_time, '')
        self.assertEqual(test_msg.message, {})


class TestSendMessage(unittest.TestCase):
    """Validate message serialization and storage"""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        global receiver_folder_position
        receiver_folder_position = self.temp_dir.name

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_file_creation(self):
        """Should generate valid JSON file with expected naming format"""
        msg = Message("urgent_alert")
        msg.message_type = "priority"
        msg.message_time = "2024-01-01"
        msg.message = {"content": "system failure"}

        send_message(msg)

        expected_file = os.path.join(
            receiver_folder_position,
            f"_priority_2024-01-01_urgent_alert.json"
        )
        self.assertTrue(os.path.exists(expected_file))

        with open(expected_file, 'r') as f:
            content = json.load(f)
            self.assertEqual(content["message_type"], "priority")


class TestReceiveMessage(unittest.TestCase):
    """Check message retrieval functionality"""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        global receiver_folder_position
        receiver_folder_position = self.temp_dir.name
        # Create sample test files
        with open(os.path.join(self.temp_dir.name, "test1.json"), 'w') as f:
            f.write("test_content")
        with open(os.path.join(self.temp_dir.name, "test2.json"), 'w') as f:
            f.write("test_content")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_file_listing(self):
        """Should return all files in target directory"""
        files = receive_message()
        self.assertEqual(len(files), 2)
        self.assertIn("test1.json", files)
        self.assertIn("test2.json", files)


if __name__ == '__main__':
    unittest.main()
