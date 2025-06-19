# encode = utf-8

from flask import Flask, jsonify
from flask_cors import CORS
from core.frame.dao import daoInitiator
from core.frame.routes.registration import register_all_blueprints

app = Flask(__name__)
app.config.from_object('ytla_plan.config')
CORS(app, resources={r"/*": {"origins": "*"}})  # 允许所有域名跨域访问

register_all_blueprints(app)


@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'error': '资源未找到'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'success': False, 'error': '服务器内部错误'}), 500

if __name__ == '__main__':
    daoInitiator.initiate()
    app.run(debug=True)
