from pathlib import Path

def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s

def create_stores_file(base_path, module_type, module_sub_type):
    """
    生成 SideCard 具体功能实现目录的 stores 文件（可选）

    参数：
        base_path: str - 基础路径
        module_type: str - 模块类型
        module_sub_type: str - 模块子类型
    """
    module_sub_type_upper = first_letter_upper(module_sub_type)

    file_path = Path(base_path) / module_type / "cards" / module_sub_type / "stores" / f"{module_sub_type_upper}Store.ts"

    file_path.parent.mkdir(parents=True, exist_ok=True)

    content = f'''export const {module_sub_type}Store = {{

}}
'''

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"已生成: {file_path}")



