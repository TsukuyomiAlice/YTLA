from pathlib import Path

def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s

def create_locales_files(base_path, module_type):
    """
    生成 SideCard _type 目录的 locales 文件

    参数：
        base_path: str - 基础路径
        module_type: str - 模块类型
    """
    dir_path = Path(base_path) / module_type / "cards" / "_type" / "locales"
    dir_path.mkdir(parents=True, exist_ok=True)

    en_content = '''{
  
}
'''

    zh_content = '''{
  
}
'''

    with open(dir_path / "en.json", "w", encoding="utf-8") as f:
        f.write(en_content)
    print(f"已生成: {dir_path / 'en.json'}")

    with open(dir_path / "zh.json", "w", encoding="utf-8") as f:
        f.write(zh_content)
    print(f"已生成: {dir_path / 'zh.json'}")



