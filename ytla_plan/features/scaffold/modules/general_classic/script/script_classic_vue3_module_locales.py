from pathlib import Path


def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s


def create_locales_files(base_path, module_type, module_sub_type):
    """
    生成 Module 具体功能实现目录的 locales 文件

    参数：
        base_path: str - 基础路径
        module_type: str - 模块类型
        module_sub_type: str - 模块子类型
    """
    dir_path = Path(base_path) / module_type / "modules" / module_sub_type / "locales"
    dir_path.mkdir(parents=True, exist_ok=True)

    en_content = f'''{{
  "{module_sub_type}_subtype_name": "{module_sub_type}(按语种填写)",
  "{module_sub_type}_subtype_description": "(这里填入你的定义)"
}}
'''

    zh_content = f'''{{
  "{module_sub_type}_subtype_name": "{module_sub_type}(按语种填写)",
  "{module_sub_type}_subtype_description": "(这里填入你的定义)"
}}
'''

    with open(dir_path / "en.json", "w", encoding="utf-8") as f:
        f.write(en_content)
    print(f"已生成: {dir_path / 'en.json'}")

    with open(dir_path / "zh.json", "w", encoding="utf-8") as f:
        f.write(zh_content)
    print(f"已生成: {dir_path / 'zh.json'}")



