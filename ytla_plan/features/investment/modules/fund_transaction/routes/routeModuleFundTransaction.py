# coding=utf-8
from flask import Blueprint, jsonify, request
from core.classic.frame._type.func.loggerConfig import router_log
from features.investment.modules.fund_transaction.process import processModuleFundTransaction

fund_transaction_bp = Blueprint('fund_transaction', __name__)


@fund_transaction_bp.route('/fund_transaction/analysis', methods=['POST'])
@router_log
def get_transaction_analysis():
    """获取基金交易分析数据"""
    data = request.json
    code = data.get('code')
    if not code:
        return jsonify({'success': False, 'message': '基金代码不能为空'}), 400
    res = processModuleFundTransaction.get_transaction_analysis(code)
    return jsonify({'success': res.success, 'data': res.data, 'message': res.msg}), res.code
