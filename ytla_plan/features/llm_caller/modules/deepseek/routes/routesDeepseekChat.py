"""
Flask routes for DeepSeek chat API.
This module provides HTTP endpoints for interacting with DeepSeek chat models.
"""

from flask import Blueprint, request, jsonify
from ..caller.callerDeepseekChat import chat
from ..instance.instanceDeepseekTypes import ChatMessage, dict_to_chat_messages

deepseek_chat_bp = Blueprint('deepseek_chat', __name__)


@deepseek_chat_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint for the DeepSeek chat API.
    
    Returns:
        JSON response with status 'ok' and 200 HTTP status code.
    """
    return jsonify({"status": "ok"}), 200


@deepseek_chat_bp.route('/chat', methods=['POST'])
def deepseek_chat():
    """
    Endpoint for sending chat requests to DeepSeek models.
    
    Request JSON parameters:
        messages (list): List of message dictionaries with 'role' and 'content' keys.
        model (str, optional): Model identifier to use. Defaults to None.
        temperature (float, optional): Sampling temperature. Defaults to None.
        max_tokens (int, optional): Maximum tokens in response. Defaults to None.
        call_mode (str, optional): Call mode to use (http or openai). Defaults to None.
    
    Returns:
        JSON response with 'success' (bool) and 'data' keys.
        On success: 200 HTTP status code with the model's response.
        On validation error: 400 HTTP status code with error message.
        On server error: 500 HTTP status code with error message.
    """
    try:
        request_data = request.get_json()

        if not request_data:
            return jsonify({
                "success": False,
                "data": "No JSON data provided"
            }), 400

        messages = request_data.get('messages')
        if not messages:
            return jsonify({
                "success": False,
                "data": "messages parameter is required"
            }), 400

        if not isinstance(messages, list):
            return jsonify({
                "success": False,
                "data": "messages must be a list"
            }), 400

        try:
            chat_messages = dict_to_chat_messages(messages)
        except ValueError as ve:
            return jsonify({
                "success": False,
                "data": str(ve)
            }), 400

        model = request_data.get('model')
        temperature = request_data.get('temperature')
        max_tokens = request_data.get('max_tokens')
        call_mode = request_data.get('call_mode')

        messages_dicts = [msg.to_dict() for msg in chat_messages]

        response = chat(
            messages=messages_dicts,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            call_mode=call_mode
        )

        return jsonify({
            "success": True,
            "data": response
        }), 200

    except ValueError as ve:
        return jsonify({
            "success": False,
            "data": str(ve)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "data": f"Server error: {str(e)}"
        }), 500
