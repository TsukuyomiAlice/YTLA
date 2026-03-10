#!/usr/bin/env python3
"""
Unit tests for DeepSeek chat module.
This test suite verifies the functionality of the DeepSeek chat caller implementation.
"""

import unittest
import sys
import os
from unittest.mock import patch, Mock
from typing import Dict, List

# Add project path to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from ytla_plan.features.llm_caller.modules.deepseek.const.constDeepseekConfig import (
    BASE_URL,
    SUPPORTED_MODELS,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    DEFAULT_MAX_TOKENS,
    DEFAULT_TOP_P,
    DEFAULT_FREQUENCY_PENALTY,
    DEFAULT_PRESENCE_PENALTY,
    CALL_MODE_HTTP,
    CALL_MODE_OPENAI,
    DEFAULT_CALL_MODE
)
from ytla_plan.features.llm_caller.modules.deepseek.instance.instanceDeepseekTypes import (
    ChatMessage,
    ChatRequest,
    ChatResponse,
    dict_to_chat_messages
)
from ytla_plan.features.llm_caller.modules.deepseek.func.funcDeepseekUtils import (
    validate_messages
)
from ytla_plan.features.llm_caller.modules.deepseek.api.apiDeepseekOpenai import chat_openai
from ytla_plan.features.llm_caller.modules.deepseek.api.apiDeepseekHttp import chat_http
from ytla_plan.features.llm_caller.modules.deepseek.process.processDeepseekChat import process_simple_chat


class TestDeepseekChat(unittest.TestCase):
    """
    Test suite for DeepSeek chat functionality.
    This class contains unit tests for constants, data types, utility functions, and API calls.
    """

    def test_constants(self):
        """
        Test that all required constants are properly defined with correct values.
        """
        self.assertEqual(BASE_URL, "https://api.deepseek.com")
        self.assertIsInstance(SUPPORTED_MODELS, list)
        self.assertIn("deepseek-chat", SUPPORTED_MODELS)
        self.assertIn("deepseek-reasoner", SUPPORTED_MODELS)
        self.assertEqual(DEFAULT_MODEL, "deepseek-chat")
        self.assertEqual(DEFAULT_TEMPERATURE, 0.0)
        self.assertEqual(DEFAULT_MAX_TOKENS, 2000)
        self.assertEqual(DEFAULT_TOP_P, 1.0)
        self.assertEqual(DEFAULT_FREQUENCY_PENALTY, 0.0)
        self.assertEqual(DEFAULT_PRESENCE_PENALTY, 0.0)
        self.assertEqual(CALL_MODE_HTTP, "http")
        self.assertEqual(CALL_MODE_OPENAI, "openai")
        self.assertEqual(DEFAULT_CALL_MODE, "openai")

    def test_chat_message(self):
        """
        Test ChatMessage data class initialization and to_dict method.
        """
        message = ChatMessage(role="user", content="Hello, World!")
        self.assertEqual(message.role, "user")
        self.assertEqual(message.content, "Hello, World!")
        
        message_dict = message.to_dict()
        self.assertIsInstance(message_dict, dict)
        self.assertEqual(message_dict['role'], "user")
        self.assertEqual(message_dict['content'], "Hello, World!")

    def test_dict_to_chat_messages(self):
        """
        Test conversion from dictionary list to ChatMessage list.
        """
        input_dicts = [
            {"role": "system", "content": "You are helpful."},
            {"role": "user", "content": "Hi!"}
        ]
        
        messages = dict_to_chat_messages(input_dicts)
        self.assertEqual(len(messages), 2)
        self.assertIsInstance(messages[0], ChatMessage)
        self.assertEqual(messages[0].role, "system")
        self.assertEqual(messages[0].content, "You are helpful.")
        self.assertEqual(messages[1].role, "user")
        self.assertEqual(messages[1].content, "Hi!")
        
        with self.assertRaises(ValueError):
            dict_to_chat_messages([{"role": "user"}])

    def test_validate_messages(self):
        """
        Test message validation function with various inputs.
        """
        valid_chat_messages = [
            ChatMessage(role="user", content="Hi"),
            ChatMessage(role="assistant", content="Hello")
        ]
        self.assertTrue(validate_messages(valid_chat_messages))
        
        valid_dicts = [
            {"role": "user", "content": "Hi"},
            {"role": "assistant", "content": "Hello"}
        ]
        self.assertTrue(validate_messages(valid_dicts))
        
        self.assertTrue(validate_messages([]))
        
        self.assertFalse(validate_messages("not a list"))
        
        invalid_mixed = [ChatMessage(role="user", content="Hi"), {"role": "user", "content": "Hi"}]
        self.assertFalse(validate_messages(invalid_mixed))
        
        invalid_dict_missing = [{"role": "user"}]
        self.assertFalse(validate_messages(invalid_dict_missing))

    @patch('ytla_plan.features.llm_caller.modules.deepseek.api.apiDeepseekOpenai.client')
    def test_chat_openai_mode(self, mock_client):
        """
        Test OpenAI SDK call mode with mocked client.
        """
        mock_response = Mock()
        mock_message = Mock()
        mock_message.content = "Test response from OpenAI mode"
        mock_response.choices = [Mock(message=mock_message)]
        mock_client.chat.completions.create.return_value = mock_response
        
        messages = [{"role": "user", "content": "Hi"}]
        result = chat_openai(messages)
        
        self.assertEqual(result.content, "Test response from OpenAI mode")
        mock_client.chat.completions.create.assert_called_once()

    @patch('ytla_plan.features.llm_caller.modules.deepseek.api.apiDeepseekHttp.requests.post')
    def test_chat_http_mode(self, mock_post):
        """
        Test HTTP call mode with mocked requests.
        """
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "Test response from HTTP mode"}}]
        }
        mock_post.return_value = mock_response
        
        messages = [{"role": "user", "content": "Hi"}]
        result = chat_http(messages)
        
        self.assertEqual(result, "Test response from HTTP mode")
        mock_post.assert_called_once()
        
        with self.assertRaises(ValueError):
            chat_http([])

    @patch('ytla_plan.features.llm_caller.modules.deepseek.process.processDeepseekChat.chat')
    def test_process_simple_chat(self, mock_chat):
        """
        Test simple chat interface with mocked underlying chat function.
        """
        mock_chat.return_value = "Hello, user!"
        
        result = process_simple_chat("Hi!")
        self.assertEqual(result, "Hello, user!")
        
        result_with_system = process_simple_chat("Hi!", system_prompt="You are helpful.")
        self.assertEqual(result_with_system, "Hello, user!")
        
        mock_chat.assert_called()


if __name__ == '__main__':
    unittest.main()
