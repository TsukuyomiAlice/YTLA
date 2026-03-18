
import os

# 模拟分析器中的代码
script_path = r'/features/feature_maker/modules/backend_python_flask/script/scriptImportAnalyzer.py'
script_dir = os.path.dirname(os.path.abspath(script_path))
print(f"script_dir: {script_dir}")

# 测试不同的层级
for i in range(1, 6):
    parts = ['..'] * i
    root_test = os.path.abspath(os.path.join(script_dir, *parts))
    print(f"Test {i} levels up: {root_test}")
