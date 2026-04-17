from pathlib import Path

def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s

def create_styles_file(base_path, module_type, module_sub_type):
    """
    生成 SideCard 具体功能实现目录的 styles 文件（可选）

    参数：
        base_path: str - 基础路径
        module_type: str - 模块类型
        module_sub_type: str - 模块子类型
    """
    file_path = Path(base_path) / module_type / "cards" / module_sub_type / "styles" / f"{module_sub_type}.scss"

    file_path.parent.mkdir(parents=True, exist_ok=True)

    content = '''// 样式文件

'''

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"已生成: {file_path}")



