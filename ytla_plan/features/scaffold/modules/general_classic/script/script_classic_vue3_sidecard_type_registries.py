from pathlib import Path

def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s

def create_registries_files(base_path, module_type):
    """
    生成 SideCard _type 目录的 registries 文件

    参数：
        base_path: str - 基础路径
        module_type: str - 模块类型
    """
    dir_path = Path(base_path) / module_type / "cards" / "_type" / "registries"
    dir_path.mkdir(parents=True, exist_ok=True)

    module_type_upper = first_letter_upper(module_type)

    card_registry_content = f'''import type {{ sideCardRegistry }} from '@/core/classic/cards/sideCard/factories/cardRegistry.ts'
import {{ buildCardRegistry }} from '@/core/classic/cards/sideCard/factories/cardRegistryHelper.ts'
import SideCard from '@/core/classic/cards/sideCard/components/SideCard.vue'

const registryModules = import.meta.glob('@/features/{module_type}/cards/**/registries/registry.ts', {{ eager: true }})

export const {module_type}CardConfig = buildCardRegistry(SideCard, registryModules) as sideCardRegistry
'''

    registries_content = '''// 注册表汇总文件
// 用于导入和导出所有注册表
'''

    with open(dir_path / "cardRegistry.ts", "w", encoding="utf-8") as f:
        f.write(card_registry_content)
    print(f"已生成: {dir_path / 'cardRegistry.ts'}")

    with open(dir_path / "registries.ts", "w", encoding="utf-8") as f:
        f.write(registries_content)
    print(f"已生成: {dir_path / 'registries.ts'}")



