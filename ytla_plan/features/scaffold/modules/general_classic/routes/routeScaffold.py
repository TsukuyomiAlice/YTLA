# encode = utf-8

from flask import Blueprint, request, jsonify
from ..process.processGenerateScaffold import generate_scaffold

scaffold_bp = Blueprint('scaffold', __name__)


@scaffold_bp.route('/scaffold/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200


@scaffold_bp.route('/scaffold/generate', methods=['POST'])
def generate_scaffold_endpoint():
    try:
        request_data = request.get_json()

        if not request_data:
            return jsonify({
                "success": False,
                "message": "No JSON data provided"
            }), 400

        is_core = request_data.get('is_core')
        type_name = request_data.get('type_name')
        structure = request_data.get('structure')
        sub_type_name = request_data.get('sub_type_name')
        gen_backend = request_data.get('gen_backend')
        gen_frontend = request_data.get('gen_frontend')

        if type_name is None:
            return jsonify({
                "success": False,
                "message": "type_name parameter is required"
            }), 400

        if structure is None:
            return jsonify({
                "success": False,
                "message": "structure parameter is required"
            }), 400

        if is_core is None:
            is_core = False
        if sub_type_name is None:
            sub_type_name = ''
        if gen_backend is None:
            gen_backend = True
        if gen_frontend is None:
            gen_frontend = True

        result = generate_scaffold(
            is_core=is_core,
            type_name=type_name,
            structure=structure,
            sub_type_name=sub_type_name,
            gen_backend=gen_backend,
            gen_frontend=gen_frontend
        )

        return jsonify(result), 200

    except ValueError as ve:
        return jsonify({
            "success": False,
            "message": str(ve)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Server error: {str(e)}"
        }), 500
