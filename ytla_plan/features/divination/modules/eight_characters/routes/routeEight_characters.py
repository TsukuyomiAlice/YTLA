# encode = utf-8

from flask import Blueprint, request, jsonify
from core.classic.frame._type.func.loggerConfig import router_log
from features.divination.modules.eight_characters.process import processEightCharacters

eight_characters_bp = Blueprint('eight_characters', __name__)


@eight_characters_bp.route('/eight_characters_analyze', methods=['POST'])
@router_log
def eight_characters_analyze():
    """
    分析八字
    入参: { "eight_characters": "癸酉辛酉壬申己丑", "luck_cycle": "丁巳", "fleet_year": "丙午" }
    """
    params = request.json
    eight_characters = params.get("eight_characters", "")
    luck_cycle = params.get("luck_cycle", "")
    fleet_year = params.get("fleet_year", "")
    res = processEightCharacters.analyze(eight_characters, luck_cycle, fleet_year)
    return jsonify({"success": res.success, "data": res.data, "msg": res.msg}), res.code


@eight_characters_bp.route('/eight_characters_history_save', methods=['POST'])
@router_log
def eight_characters_history_save():
    """
    保存八字分析结果到历史记录
    入参: { "plan_id": 1, "module_id": 1, "birthday": "2024-01-01", ... }
    """
    params = request.json
    plan_id = params.get("plan_id", 0)
    module_id = params.get("module_id", 0)
    birthday = params.get("birthday", "")
    birth_time = params.get("birth_time", "")
    gender = params.get("gender", "")
    eight_characters = params.get("eight_characters", "")
    luck_cycle = params.get("luck_cycle", "")
    fleet_year = params.get("fleet_year", "")
    analysis_result = params.get("analysis_result", "")
    annotations = params.get("annotations", "")
    lunar_date = params.get("lunar_date", "")
    creator = params.get("creator", "")
    res = processEightCharacters.save_history(
        plan_id, module_id, birthday, birth_time, gender,
        eight_characters, luck_cycle, fleet_year,
        analysis_result, annotations, lunar_date, creator
    )
    return jsonify({"success": res.success, "data": res.data, "msg": res.msg}), res.code


@eight_characters_bp.route('/eight_characters_history_list', methods=['POST'])
@router_log
def eight_characters_history_list():
    """
    查询历史记录列表
    入参: { "plan_id": 1, "module_id": 1, "creator": "user1", "limit": 20, "offset": 0 }
    """
    params = request.json
    plan_id = params.get("plan_id", 0)
    module_id = params.get("module_id", 0)
    creator = params.get("creator", "")
    limit = params.get("limit", 20)
    offset = params.get("offset", 0)
    res = processEightCharacters.get_history_list(plan_id, module_id, creator, limit, offset)
    return jsonify({"success": res.success, "data": res.data, "msg": res.msg}), res.code


@eight_characters_bp.route('/eight_characters_history_detail', methods=['POST'])
@router_log
def eight_characters_history_detail():
    """
    查询单条历史记录详情
    入参: { "plan_id": 1, "module_id": 1, "eight_characters": "癸酉辛酉壬申己丑", "gender": "male" }
    """
    params = request.json
    plan_id = params.get("plan_id", 0)
    module_id = params.get("module_id", 0)
    eight_characters = params.get("eight_characters", "")
    gender = params.get("gender", "")
    res = processEightCharacters.get_history_detail(plan_id, module_id, eight_characters, gender)
    return jsonify({"success": res.success, "data": res.data, "msg": res.msg}), res.code


@eight_characters_bp.route('/eight_characters_convert', methods=['POST'])
@router_log
def eight_characters_convert():
    """
    公历日期转换为八字（四柱）
    入参: { "year": 2024, "month": 6, "day": 15, "hour_branch": "午", "gender": "male" }
    hour_branch 为时辰地支（可选），如 "子", "丑", ..., "亥"
    gender 为性别（可选），"male" 或 "female"，提供后返回大运表+流年表
    """
    params = request.json
    year = params.get("year", 0)
    month = params.get("month", 0)
    day = params.get("day", 0)
    hour_branch = params.get("hour_branch", "")
    gender = params.get("gender", "")
    res = processEightCharacters.convert_solar_to_bazi(year, month, day, hour_branch, gender)
    return jsonify({"success": res.success, "data": res.data, "msg": res.msg}), res.code


@eight_characters_bp.route('/eight_characters_history_delete', methods=['POST'])
@router_log
def eight_characters_history_delete():
    """
    逻辑删除历史记录
    入参: { "plan_id": 1, "module_id": 1, "eight_characters": "癸酉辛酉壬申己丑", "gender": "male" }
    """
    params = request.json
    plan_id = params.get("plan_id", 0)
    module_id = params.get("module_id", 0)
    eight_characters = params.get("eight_characters", "")
    gender = params.get("gender", "")
    res = processEightCharacters.delete_history(plan_id, module_id, eight_characters, gender)
    return jsonify({"success": res.success, "data": res.data, "msg": res.msg}), res.code
