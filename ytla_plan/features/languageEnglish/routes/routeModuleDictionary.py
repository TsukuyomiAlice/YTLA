from flask import Blueprint, jsonify, request
from core.frame.func.loggerConfig import router_log
from features.languageEnglish.process import processModuleDictionary

language_dictionary_bp = Blueprint('language_dictionary', __name__)


@language_dictionary_bp.route('/language_dictionary_search_word', methods=['POST'])
@router_log
def language_dictionary_search_word():
    data = request.json
    res = processModuleDictionary.search_word(data['word'])
    return jsonify({"success": res.success, "data": res.data}), res.code
