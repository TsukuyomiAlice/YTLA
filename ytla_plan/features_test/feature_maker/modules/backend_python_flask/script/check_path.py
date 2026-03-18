
import os

script_path = os.path.abspath(__file__)
print(f"当前脚本路径: {script_path}")

analyzer_path = os.path.join(
    os.path.dirname(__file__), 
    'features', 'feature_maker', 'modules', 'backend_python_flask', 
    'script', 'scriptImportAnalyzer.py'
)
print(f"分析器路径: {analyzer_path}")

# 从分析器路径计算根目录
root_from_analyzer = os.path.abspath(os.path.join(
    os.path.dirname(analyzer_path), '..', '..', '..', '..'
))
print(f"从分析器计算的根目录: {root_from_analyzer}")
