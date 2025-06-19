from flask import Blueprint, jsonify, request
from core.frame.func.loggerConfig import router_log
from core.cards.process import processCards
from core.cards.dao import daoCards

cards_bp = Blueprint('card', __name__)

@cards_bp.route('/get_cards')
@router_log
def get_cards():
    try:
        cards = processCards.get_cards()
        return jsonify({'success': True, 'cards': cards})
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'error': str(e)}), 500


@cards_bp.route('/add_card', methods=['POST'])
@router_log
def add_card():
    data = request.json
    return processCards.card_router(data, 'add')


@cards_bp.route('/update_card_detail/<int:card_id>', methods=['POST'])
@router_log
def update_card_detail(card_id):
    data = request.json
    return processCards.card_router(data, 'update', card_id=card_id)


@cards_bp.route('/card_action/<int:card_id>/<action>', methods=['POST'])
@router_log
def handle_card_action(card_id, action):
    try:
        result = processCards.soft_update_card(card_id, action)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@cards_bp.route('/update_card/<int:card_id>', methods=['POST'])
@router_log
def update_card(card_id):
    try:
        data = request.json

        # 调用处理逻辑
        success = processCards.update_card(card_id, data)
        return jsonify({'success': success})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@cards_bp.route('/update_card/<int:card_id>/tags', methods=['POST', 'DELETE'])
@router_log
def update_card_tags(card_id):
    try:
        data = request.json

        # 调用处理逻辑
        success = processCards.update_card(card_id, data)
        return jsonify({'success': success})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@cards_bp.route('/delete_card/<int:card_id>', methods=['POST'])
@router_log
def delete_card(card_id):
    try:
        # 检查卡片是否存在
        if not daoCards.get_card_name_by_card_id(card_id):
            return jsonify({'success': False, 'error': '卡片不存在'}), 404

        processCards.soft_delete_card(card_id)
        # 验证删除操作
        if daoCards.check_card_delete_status(card_id) == '1':
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': '删除操作未生效'}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@cards_bp.route('/deactivate_card/<int:card_id>', methods=['POST'])
@router_log
def deactivate_card(card_id):
    try:
        # 检查卡片是否存在
        if not daoCards.get_card_name_by_card_id(card_id):
            return jsonify({'success': False, 'error': '卡片不存在'}), 404

        processCards.deactivate_card(card_id)
        # 验证删除操作
        if daoCards.check_card_active_status(card_id) == '0':
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': '删除操作未生效'}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
