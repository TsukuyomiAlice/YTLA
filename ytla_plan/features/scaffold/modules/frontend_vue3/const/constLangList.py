# encode = utf-8

def base_readme_lang_list(lan: str) -> str:
    return \
f"""<p>
 {lan}
 <a href="./docs/readme/zh-CN/readme.md"> 简体中文 </a>
 <a href="./docs/readme/en-US/readme.md"> English </a>
</p>
"""


def doc_readme_lang_list(lan: str) -> str:
    return \
f"""<p>
 {lan}
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="../en-US/readme.md"> English </a>
</p>
"""
