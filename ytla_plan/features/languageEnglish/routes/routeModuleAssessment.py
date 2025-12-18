from flask import Blueprint, jsonify, request
from core.classic.frame.func.loggerConfig import router_log
from features.languageEnglish.process import processModuleAssessment

language_assessment_bp = Blueprint('language_assessment', __name__)

@language_assessment_bp.route('/language_assessment_start', methods=['POST'])
@router_log
def language_assessment_start():
    data = request.json
    res = processModuleAssessment.assessment_start(data['planId'], data['moduleId'], data['userName'])
    return jsonify({"success": res.success, "data": res.data}), res.code


@language_assessment_bp.route('/language_assessment_step_1a', methods=['POST'])
@router_log
def language_assessment_step1a():
    data = request.json
    res = processModuleAssessment.assessment_step_1(data['planId'], data['moduleId'], data['recordId'], data['step1aAnswer'])
    return jsonify({"success": res.success, "data": res.data}), res.code


@language_assessment_bp.route('/language_assessment_step_1b', methods=['POST'])
@router_log
def language_assessment_step1b():
    data = request.json
    res = processModuleAssessment.assessment_step_2(data['planId'], data['moduleId'], data['recordId'], data['step1bAnswer'])
    return jsonify({"success": res.success, "data": res.data}), res.code


@language_assessment_bp.route('/language_assessment_step_2', methods=['POST'])
@router_log
def language_assessment_step2():
    data = request.json
    res = processModuleAssessment.assessment_result(data['planId'], data['moduleId'], data['recordId'], data['step2Answer'])
    return jsonify({"success": res.success, "data": res.data}), res.code
