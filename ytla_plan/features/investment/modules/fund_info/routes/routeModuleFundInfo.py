# coding=utf-8
from flask import Blueprint, jsonify, request
from core.classic.frame._type.func.loggerConfig import router_log
from features.investment.modules.fund_info.process import processModuleFundInfo

fund_info_bp = Blueprint('fund_info', __name__)


@fund_info_bp.route('/fund_info/get', methods=['POST'])
@router_log
def get_fund_info():
    """获取基金基本信息"""
    data = request.json
    code = data.get('code')
    if not code:
        return jsonify({'success': False, 'message': '基金代码不能为空'}), 400
    res = processModuleFundInfo.get_fund_info(code)
    return jsonify({'success': res.success, 'data': res.data, 'message': res.msg}), res.code


@fund_info_bp.route('/fund_info/history', methods=['POST'])
@router_log
def get_fund_history():
    """获取基金历史净值数据"""
    data = request.json
    code = data.get('code')
    if not code:
        return jsonify({'success': False, 'message': '基金代码不能为空'}), 400
    res = processModuleFundInfo.get_fund_history(code)
    return jsonify({'success': res.success, 'data': res.data, 'message': res.msg}), res.code


@fund_info_bp.route('/fund_info/latest_price', methods=['POST'])
@router_log
def get_fund_latest_price():
    """获取基金最新净值"""
    data = request.json
    code = data.get('code')
    if not code:
        return jsonify({'success': False, 'message': '基金代码不能为空'}), 400
    res = processModuleFundInfo.get_fund_latest_price(code)
    return jsonify({'success': res.success, 'data': res.data, 'message': res.msg}), res.code
