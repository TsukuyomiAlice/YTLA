"""
DeepSeek API configuration constants.
This module contains all constant values used for interacting with DeepSeek API.
"""

# API base URL configuration
BASE_URL = "https://api.deepseek.com"
"""
The base URL endpoint for DeepSeek API requests.
This is the primary entry point for all DeepSeek API calls.
"""

# Supported models configuration
SUPPORTED_MODELS = ["deepseek-chat", "deepseek-reasoner"]
"""
List of supported DeepSeek model identifiers.
- deepseek-chat: General purpose chat model
- deepseek-reasoner: Reasoning-focused model with thought chain capabilities
"""

# Default model configuration
DEFAULT_MODEL = "deepseek-chat"
"""
The default model to use when no specific model is specified.
DeepSeek-chat is recommended for most general use cases.
"""

# Default parameters configuration
DEFAULT_TEMPERATURE = 0.0
"""
Default temperature parameter for model generation.
Lower values (0.0) produce more deterministic and focused outputs.
Higher values (e.g., 1.0) produce more creative and varied outputs.
"""

DEFAULT_MAX_TOKENS = 2000
"""
Default maximum token limit for model responses.
Controls the maximum length of the generated response in tokens.
"""

DEFAULT_TOP_P = 1.0
"""
Default top-p (nucleus) sampling parameter.
Limits token selection to the top probability mass summing to this value.
1.0 means no filtering (all tokens considered).
"""

DEFAULT_FREQUENCY_PENALTY = 0.0
"""
Default frequency penalty parameter.
Reduces repetition of the same token sequences.
Range: -2.0 to 2.0, positive values reduce repetition.
"""

DEFAULT_PRESENCE_PENALTY = 0.0
"""
Default presence penalty parameter.
Increases diversity by encouraging new topics.
Range: -2.0 to 2.0, positive values encourage new topics.
"""

# Call mode configuration
CALL_MODE_HTTP = "http"
"""
HTTP call mode for direct API requests using HTTP libraries.
Provides low-level control over the API interaction.
"""

CALL_MODE_OPENAI = "openai"
"""
OpenAI SDK call mode using OpenAI compatible client.
Recommended for ease of use and compatibility.
"""

DEFAULT_CALL_MODE = "openai"
"""
Default call mode to use when no specific mode is specified.
OpenAI SDK mode is the recommended default for most use cases.
"""
