# encode = utf-8

from flask import Flask, jsonify
from flask_cors import CORS
from core.classic.frame.dao import daoInitiator
from core.classic.frame.router.process.processRouter import register_dynamic_blueprints

app = Flask(__name__)
app.config.from_object('ytla_plan.config')
CORS(app, resources={r"/*": {"origins": "*"}})

register_dynamic_blueprints(app)


@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'error': '资源未找到'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'success': False, 'error': '服务器内部错误'}), 500


if __name__ == '__main__':
    daoInitiator.initiate()

    app.run(host="0.0.0.0", port=5000, debug=True)
