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
    plan_id = data.get('plan_id')
    module_id = data.get('module_id')
    code = data.get('code')
    if not plan_id or not module_id or not code:
        return jsonify({'success': False, 'message': '参数不完整'}), 400
    res = processModuleFundTransaction.get_transaction_analysis(plan_id, module_id, code)
    return jsonify({'success': res.success, 'data': res.data, 'message': res.msg}), res.code


@fund_transaction_bp.route('/fund_transaction/transactions', methods=['POST'])
@router_log
def get_transactions():
    data = request.json
    plan_id = data.get('plan_id')
    module_id = data.get('module_id')
    code = data.get('code')
    if not plan_id or not module_id or not code:
        return jsonify({'success': False, 'message': '参数不完整'}), 400
    res = processModuleFundTransaction.get_transactions(plan_id, module_id, code)
    return jsonify({'success': res.success, 'data': res.data, 'message': res.msg}), res.code


@fund_transaction_bp.route('/fund_transaction/transaction', methods=['POST'])
@router_log
def get_transaction():
    data = request.json
    plan_id = data.get('plan_id')
    module_id = data.get('module_id')
    transaction_id = data.get('transaction_id')
    if not plan_id or not module_id or not transaction_id:
        return jsonify({'success': False, 'message': '参数不完整'}), 400
    res = processModuleFundTransaction.get_transaction(plan_id, module_id, transaction_id)
    return jsonify({'success': res.success, 'data': res.data, 'message': res.msg}), res.code


@fund_transaction_bp.route('/fund_transaction/add', methods=['POST'])
@router_log
def add_transaction():
    data = request.json
    plan_id = data.get('plan_id')
    module_id = data.get('module_id')
    code = data.get('code')
    transaction_date = data.get('transaction_date')
    transaction_type = data.get('transaction_type')
    amount = data.get('amount', 0)
    share = data.get('share', 0)
    price = data.get('price', 0)
    transaction_fee = data.get('transaction_fee', 0)
    
    if not plan_id or not module_id or not code or not transaction_date or not transaction_type:
        return jsonify({'success': False, 'message': '必要参数不能为空'}), 400
    
    res = processModuleFundTransaction.add_transaction(
        plan_id, module_id, code, transaction_date, transaction_type, amount, share, price, transaction_fee
    )
    return jsonify({'success': res.success, 'data': res.data, 'message': res.msg}), res.code


@fund_transaction_bp.route('/fund_transaction/update', methods=['POST'])
@router_log
def update_transaction():
    data = request.json
    plan_id = data.get('plan_id')
    module_id = data.get('module_id')
    transaction_id = data.get('transaction_id')
    code = data.get('code')
    transaction_date = data.get('transaction_date')
    transaction_type = data.get('transaction_type')
    amount = data.get('amount', 0)
    share = data.get('share', 0)
    price = data.get('price', 0)
    transaction_fee = data.get('transaction_fee', 0)
    
    if not plan_id or not module_id or not transaction_id:
        return jsonify({'success': False, 'message': '必要参数不能为空'}), 400
    
    res = processModuleFundTransaction.update_transaction(
        plan_id, module_id, transaction_id, code, transaction_date, transaction_type, 
        amount, share, price, transaction_fee
    )
    return jsonify({'success': res.success, 'data': res.data, 'message': res.msg}), res.code


@fund_transaction_bp.route('/fund_transaction/delete', methods=['POST'])
@router_log
def delete_transaction():
    data = request.json
    plan_id = data.get('plan_id')
    module_id = data.get('module_id')
    transaction_id = data.get('transaction_id')
    if not plan_id or not module_id or not transaction_id:
        return jsonify({'success': False, 'message': '参数不完整'}), 400
    
    res = processModuleFundTransaction.delete_transaction(plan_id, module_id, transaction_id)
    return jsonify({'success': res.success, 'data': res.data, 'message': res.msg}), res.code
