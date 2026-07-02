# encode = utf-8

import json as json_lib
import os
import sqlite3

import pandas as pd


def read_xlsx(file_path):
    """
    读取 xlsx/xls 文件，遍历所有 sheet。
    返回统一结构：
        {"success": bool, "data": {...}, "format_type": "relational", "metadata": {...}}
    """
    try:
        xls = pd.ExcelFile(file_path, engine='openpyxl')
        sheet_names = xls.sheet_names
        data = {}
        metadata = {
            'sheet_names': sheet_names,
            'sheet_info': {}
        }

        for sheet in sheet_names:
            df = xls.parse(sheet)
            data[sheet] = df
            metadata['sheet_info'][sheet] = {
                'rows': len(df),
                'columns': len(df.columns)
            }

        return {
            'success': True,
            'data': data,
            'format_type': 'relational',
            'metadata': metadata
        }
    except Exception as e:
        return {
            'success': False,
            'data': {},
            'format_type': 'relational',
            'metadata': {'error': str(e)}
        }


def read_csv(file_path):
    """
    读取 csv 文件，自动检测分隔符。
    返回统一结构：
        {"success": bool, "data": {...}, "format_type": "relational", "metadata": {...}}
    """
    try:
        # 自动检测分隔符
        delimiters = [',', '\t', ';', '|', ':']
        detected_delimiter = None

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            first_line = f.readline()
            for delim in delimiters:
                if delim in first_line:
                    detected_delimiter = delim
                    break
            if detected_delimiter is None:
                detected_delimiter = ','

        df = pd.read_csv(file_path, delimiter=detected_delimiter, encoding='utf-8', engine='python')

        return {
            'success': True,
            'data': {'data': df},
            'format_type': 'relational',
            'metadata': {
                'row_count': len(df),
                'column_count': len(df.columns),
                'column_names': list(df.columns),
                'detected_delimiter': detected_delimiter
            }
        }
    except Exception as e:
        return {
            'success': False,
            'data': {},
            'format_type': 'relational',
            'metadata': {'error': str(e)}
        }


def read_json(file_path):
    """
    读取 json 文件，判断数据结构类型。
    返回统一结构：
        {"success": bool, "data": {...}, "format_type": "relational" | "non_relational", "metadata": {...}}
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_data = json_lib.load(f)

        # 判断是否为数组对象（列表 of dicts）→ 可展平为表格
        if isinstance(raw_data, list) and len(raw_data) > 0 and isinstance(raw_data[0], dict):
            df = pd.DataFrame(raw_data)
            return {
                'success': True,
                'data': {'data': df},
                'format_type': 'relational',
                'metadata': {
                    'record_count': len(raw_data),
                    'top_level_keys': list(raw_data[0].keys()) if raw_data else []
                }
            }
        elif isinstance(raw_data, dict):
            # 嵌套 dict → 非关系型
            return {
                'success': True,
                'data': raw_data,
                'format_type': 'non_relational',
                'metadata': {
                    'top_level_keys': list(raw_data.keys()),
                    'record_count': 1
                }
            }
        else:
            # 其他情况（简单列表等）→ 非关系型
            return {
                'success': True,
                'data': raw_data,
                'format_type': 'non_relational',
                'metadata': {
                    'record_count': len(raw_data) if isinstance(raw_data, list) else 1
                }
            }
    except Exception as e:
        return {
            'success': False,
            'data': {},
            'format_type': 'non_relational',
            'metadata': {'error': str(e)}
        }


def read_db(file_path):
    """
    读取 db/sqlite/sqlite3 文件，提取所有表数据。
    返回统一结构：
        {"success": bool, "data": {...}, "format_type": "relational", "metadata": {...}}
    """
    try:
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()

        # 获取所有表名
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_names = [row[0] for row in cursor.fetchall()]

        data = {}
        metadata = {
            'table_names': table_names,
            'table_info': {}
        }

        for table in table_names:
            df = pd.read_sql_query(f"SELECT * FROM [{table}]", conn)
            data[table] = df
            metadata['table_info'][table] = {
                'record_count': len(df),
                'column_count': len(df.columns)
            }

        conn.close()

        return {
            'success': True,
            'data': data,
            'format_type': 'relational',
            'metadata': metadata
        }
    except Exception as e:
        return {
            'success': False,
            'data': {},
            'format_type': 'relational',
            'metadata': {'error': str(e)}
        }


def get_reader_for_file(file_path):
    """
    根据文件扩展名返回对应的读取方法名。
    支持的扩展名：xlsx, xls, csv, json, db, sqlite, sqlite3
    不支持的扩展名返回 None。
    """
    ext = os.path.splitext(file_path)[1].lower().lstrip('.')

    reader_map = {
        'xlsx': 'read_xlsx',
        'xls': 'read_xlsx',
        'csv': 'read_csv',
        'json': 'read_json',
        'db': 'read_db',
        'sqlite': 'read_db',
        'sqlite3': 'read_db',
    }

    return reader_map.get(ext, None)
