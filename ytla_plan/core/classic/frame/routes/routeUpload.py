import os
import datetime

from flask import Blueprint, jsonify, request, send_from_directory, current_app
from werkzeug.utils import secure_filename
from core.classic.frame.func.loggerConfig import router_log

upload_bp = Blueprint('upload', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@upload_bp.route('/upload/<file_type>', methods=['POST'])
@router_log
def upload_file(file_type):
    # 添加文件类型白名单
    valid_types = ['icon', 'background']
    if file_type not in valid_types:
        return jsonify({'success': False, 'error': '无效文件类型'}), 400
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No selected file'})
    if file and allowed_file(file.filename):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{file_type}_{timestamp}_{secure_filename(file.filename)}"
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'success': True, 'filename': filename})
    return jsonify({'success': False, 'error': 'Invalid file type'})

@upload_bp.route('/uploads/<filename>')
@router_log
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)


@upload_bp.route('/static/<path:filename>')
@router_log
def static_files(filename):
    return send_from_directory(os.path.join(current_app.root_path, 'static'), filename)
