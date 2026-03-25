from pathlib import Path

def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s

def create_definitions_files(base_path, module_type):
    """
    生成 SideCard _type 目录的 definitions 文件

    参数：
        base_path: str - 基础路径
        module_type: str - 模块类型
    """
    dir_path = Path(base_path) / module_type / "cards" / "_type" / "definitions"
    dir_path.mkdir(parents=True, exist_ok=True)

    module_type_upper = first_letter_upper(module_type)

    card_type_content = f'''export type {module_type_upper}CardType = '{module_type}';

export type {module_type_upper}CardSubType = '[sub_type1]' | '[sub_type2]';
'''

    card_data_type_content = f'''import type {{ CardData }} from '@/core/classic/cards/sideCard/definitions/cardDataType.ts'
import type {{ {module_type_upper}CardType, {module_type_upper}CardSubType }} from './cardType.ts'

export interface {module_type_upper}CardData extends CardData {{
  card_id: number;
  name: string;
  tags: string;
  description: string;
  card_type: {module_type_upper}CardType;
  card_sub_type: {module_type_upper}CardSubType;
  icon_path?: string;
  background_path?: string;
  delete_flag: string;
  active_flag: string;
}}
'''

    with open(dir_path / "cardType.ts", "w", encoding="utf-8") as f:
        f.write(card_type_content)
    print(f"已生成: {dir_path / 'cardType.ts'}")

    with open(dir_path / "cardDataType.ts", "w", encoding="utf-8") as f:
        f.write(card_data_type_content)
    print(f"已生成: {dir_path / 'cardDataType.ts'}")



