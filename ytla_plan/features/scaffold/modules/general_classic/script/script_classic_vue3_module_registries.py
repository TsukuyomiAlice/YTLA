from pathlib import Path


def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s


def create_registries_file(base_path, module_type, module_sub_type):
    """
    生成 Module 具体功能实现目录的 registries 文件

    参数：
        base_path: str - 基础路径
        module_type: str - 模块类型
        module_sub_type: str - 模块子类型
    """
    module_sub_type_upper = first_letter_upper(module_sub_type)

    file_path = Path(base_path) / module_type / "modules" / module_sub_type / "registries" / f"{module_sub_type}ModuleConfig.ts"

    file_path.parent.mkdir(parents=True, exist_ok=True)

    content = f'''import {{ defineAsyncComponent }} from 'vue'
import type {{ ModuleRegistry }} from '@/core/classic/modules/registries/moduleRegistry.ts'
import {{ {module_sub_type}ModuleFlowManager }} from '@/features/{module_type}/flows/{module_sub_type}FlowManager'

export const {module_sub_type}ModuleConfig = <ModuleRegistry> {{
  moduleType: '{module_type}',
  moduleSubType: '{module_sub_type}',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/{module_type}/modules/{module_sub_type}/components/{module_sub_type_upper}Main.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/{module_type}/modules/{module_sub_type}/components/{module_sub_type_upper}Sub.vue')
  ),
  displayMode: 7,
  flowManager: {module_sub_type}ModuleFlowManager
}}
'''

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"已生成: {file_path}")



