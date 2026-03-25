from pathlib import Path

def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s

def create_composables_file(base_path, module_type, module_sub_type):
    """
    生成 SideCard 具体功能实现目录的 composables 文件

    参数：
        base_path: str - 基础路径
        module_type: str - 模块类型
        module_sub_type: str - 模块子类型
    """
    module_sub_type_upper = first_letter_upper(module_sub_type)

    file_path = Path(base_path) / module_type / "cards" / module_sub_type / "composables" / f"use{module_sub_type_upper}.ts"

    file_path.parent.mkdir(parents=True, exist_ok=True)

    content = f'''import {{ useSideCardEditor }} from '@/core/classic/cards/sideCardEditor/composables/useSideCardEditor.ts'
import type {{ {module_sub_type_upper}CardData }} from '../definitions/cardDataType.ts'

export const use{module_sub_type_upper} = (props, emit) => {{
  const handleEdit = () => {{
    const {{ showEdit }} = useSideCardEditor()
    showEdit({{
      card_id: props.cardId,
      name: props.name,
      tags: props.tags,
      description: props.description,
      card_sub_type: '{module_sub_type}',
    }} as {module_sub_type_upper}CardData)
  }}

  return {{
    handleEdit
  }}
}}
'''

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"已生成: {file_path}")



