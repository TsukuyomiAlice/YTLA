from pathlib import Path

def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s

def create_registries_file(base_path, module_type):
    """
    生成 Module _type 目录的 registries 文件

    参数：
        base_path: str - 基础路径
        module_type: str - 模块类型
    """
    file_path = Path(base_path) / module_type / "modules" / "_type" / "registries" / "registries.ts"

    file_path.parent.mkdir(parents=True, exist_ok=True)

    content = '''// 注册表汇总文件
// 用于导入和导出所有注册表
'''

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"已生成: {file_path}")



