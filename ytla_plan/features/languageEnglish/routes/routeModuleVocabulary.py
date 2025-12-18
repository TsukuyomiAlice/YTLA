from flask import Blueprint, jsonify, request
from core.classic.frame.func.loggerConfig import router_log
from features.languageEnglish.process import processModuleVocabulary

language_vocabulary_bp = Blueprint('language_vocabulary', __name__)


@language_vocabulary_bp.route('/language_vocabulary_new', methods=['POST'])
@router_log
def language_vocabulary_create():
    data = request.json
    res = processModuleVocabulary.create_new_vocabulary_book(data['planId'], data['moduleId'], 'Ann', [])
    return jsonify({"success": res.success}), res.code


@language_vocabulary_bp.route('/language_vocabulary_get_all', methods=['POST'])
@router_log
def language_vocabulary_get_all():
    data = request.json
    res = processModuleVocabulary.get_vocabulary_book_by_creator(data['planId'], data['moduleId'], 'Ann')
    return jsonify({"success": res.success, "data": res.data}), res.code


@language_vocabulary_bp.route('/language_vocabulary_update_word_list', methods=['POST'])
@router_log
def language_vocabulary_update_word_list():
    data = request.json
    res = processModuleVocabulary.update_vocabulary_book_word_list(data['planId'], data['moduleId'], data['record_id'], data['word_list'])
    return jsonify({"success": res.success}), res.code


@language_vocabulary_bp.route('/language_vocabulary_update_book_name', methods=['POST'])
@router_log
def language_vocabulary_update_book_name():
    data = request.json
    res = processModuleVocabulary.update_vocabulary_book_name(data['planId'], data['moduleId'], data['record_id'], data['book_name'])
    return jsonify({"success": res.success}), res.code