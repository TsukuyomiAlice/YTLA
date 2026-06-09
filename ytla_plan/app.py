# encode = utf-8

from flask import Flask, jsonify
from flask_cors import CORS
from core.classic.frame.initiate.dao import daoInitiator
from core.classic.frame.router.process.processRouter import register_dynamic_blueprints
from core.classic.cards.sideCard.process.processCardHandlerFactory import CardHandlerFactory
from core.classic.frame.database.process.processDatabaseSqlite import initialize as initialize_db_config

app = Flask(__name__)
app.config.from_object('ytla_plan.config')
CORS(app, resources={r"/*": {"origins": "*"}})

# 初始化数据库配置加载器
initialize_db_config()
register_dynamic_blueprints(app)
CardHandlerFactory.load_and_register_handlers()


@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'error': '资源未找到'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'success': False, 'error': '服务器内部错误'}), 500


if __name__ == '__main__':
    daoInitiator.initiate()

    app.run(host="127.0.0.1", port=5000, debug=False)
