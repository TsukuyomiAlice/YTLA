from pathlib import Path

def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s

def create_definitions_files(base_path, module_type, module_sub_type):
    """
    生成 SideCard 具体功能实现目录的 definitions 文件

    参数：
        base_path: str - 基础路径
        module_type: str - 模块类型
        module_sub_type: str - 模块子类型
    """
    dir_path = Path(base_path) / module_type / "cards" / module_sub_type / "definitions"
    dir_path.mkdir(parents=True, exist_ok=True)

    module_sub_type_upper = first_letter_upper(module_sub_type)

    type_content = f'''export interface {module_sub_type_upper}Type {{

}}
'''

    data_type_content = f'''export interface {module_sub_type_upper}CardData {{
  card_id: number
  name: string
  tags: string
  description: string
  card_sub_type: string
}}
'''

    with open(dir_path / f"{module_sub_type_upper}Type.ts", "w", encoding="utf-8") as f:
        f.write(type_content)
    print(f"已生成: {dir_path / f'{module_sub_type_upper}Type.ts'}")

    with open(dir_path / "cardDataType.ts", "w", encoding="utf-8") as f:
        f.write(data_type_content)
    print(f"已生成: {dir_path / 'cardDataType.ts'}")



