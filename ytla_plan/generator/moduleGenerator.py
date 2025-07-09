from pathlib import Path

"""
做成目标
moduleGenerator(本文档)
前端框架
后端框架
注册函数
注册基础参数

dataGenerator
Dao层面控制
Process层控制

apiGenerator
route层面和service层面联动

"""

base_path = Path(__file__).parent.parent.parent / "ytla_plan_vue" / "src" / "features"


def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s

def create_module_files(module_type, module_sub_type):
    """
    自动生成Vue模块化开发所需的完整目录结构和基础代码文件

    参数：
        module_type: str - 模块大类（如sample）
        module_sub_type: str - 模块子类型（如sample）

    生成内容：
        1. 标准化的目录结构
        2. 基础组件模板文件
        3. 模块流程管理器（Flow Manager）
        4. 模块注册表（Module Registry）

    副作用：
        - 在文件系统中创建目录和文件
        - 输出需要在main.ts和locale中手动添加的代码提示
    """
    module_path = base_path / module_type

    # 1. 创建基础目录结构（符合Vue模块化开发规范）
    # 包含组件、组合式API、流程管理等多层目录
    dirs_to_create = [
        module_path,
        module_path / "components",  # 通用组件目录
        module_path / "components/modules",  # 模组目录
        module_path / "components/modules" / module_sub_type,  # 子模块专属目录
        module_path / "composables", # 组合式API逻辑
        module_path / "flows",       # 流程管理器
        module_path / "layouts",     # 画面区域布置
        module_path / "locales",     # 国际化配置
        module_path / "registries",  # 模块注册配置
        module_path / "services",        # 服务定义
        module_path / "stores",        # 存储定义
        module_path / "styles",        # 式样定义
        module_path / "types",       # TS类型定义
        module_path / "utils"        # 配置定义
    ]

    # 递归创建所有缺失目录（已存在目录自动跳过）
    for d in dirs_to_create:
        d.mkdir(parents=True, exist_ok=True)

    # 2. 创建模块组件文件（Main/Sub 组件对模式）
    # 支持主流程和子流程的组件分离设计
    module_files = [
        (f"{first_letter_upper(module_sub_type)}Main.vue", "MainComponent"),     # 主组件入口
        (f"{first_letter_upper(module_sub_type)}Main_00.vue", "Main00Component"),# 主流程步骤组件
        (f"{first_letter_upper(module_sub_type)}Sub.vue", "SubComponent"),       # 子组件入口
        (f"{first_letter_upper(module_sub_type)}Sub_00.vue", "Sub00Component")    # 子流程步骤组件
    ]

    # 生成组件模板文件（SFC单文件组件结构）
    for file, component_type in module_files:
        with open(module_path / "components/modules" / module_sub_type / file, "w", encoding="utf-8") as f:
            f.write(
f'''<template>
                
</template>

<script setup lang="ts">

</script>
<style scoped lang="scss">

</style>
''')

    # 3. 创建Flow Manager（流程管理器）
    # 实现模块流程的注册和管理功能
    flow_manager_content = \
f'''import type {{ Component }} from 'vue'
import {{ defineAsyncComponent }} from 'vue'
import type {{ ModuleFlowManager }} from '@/core/frame/types/flowManagerTypes.ts'

export class {first_letter_upper(module_sub_type)}ModuleFlowManager implements ModuleFlowManager {{
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {{
    this.flows.set(flowName, steps)
  }}

  getSteps(flowName: string): Component[] {{
    return this.flows.get(flowName) || []
  }}
}}

export const {module_sub_type}ModuleFlowManager = new {first_letter_upper(module_sub_type)}ModuleFlowManager()

{module_sub_type}ModuleFlowManager.registerFlow('{module_sub_type}-main-steps', [
  defineAsyncComponent(() => import('@/features/{module_type}/components/modules/{module_sub_type}/{first_letter_upper(module_sub_type)}Main_00.vue')),
])

{module_sub_type}ModuleFlowManager.registerFlow('{module_sub_type}-sub-steps', [
  defineAsyncComponent(() => import('@/features/{module_type}/components/modules/{module_sub_type}/{first_letter_upper(module_sub_type)}Sub_00.vue')),
])

'''
    with open(module_path / "flows" / f"{module_sub_type}FlowManager.ts", "w", encoding="utf-8") as f:
        f.write(flow_manager_content)

    # 4. 创建Module Config（模块注册表）
    # 实现模块的全局注册和配置管理
    registry_content = \
f'''import {{ defineAsyncComponent }} from 'vue'
import type {{ ModuleRegistry }} from '@/core/modules/registries/moduleRegistry.ts'
import {{ {module_sub_type}ModuleFlowManager }} from '@/features/{module_type}/flows/{module_sub_type}FlowManager'

export const {module_sub_type}ModuleConfig = <ModuleRegistry> {{
  moduleType: '{module_type}',
  moduleSubType: '{module_sub_type}',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/{module_type}/components/modules/{module_sub_type}/{first_letter_upper(module_sub_type)}Main.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/{module_type}/components/modules/{module_sub_type}/{first_letter_upper(module_sub_type)}Sub.vue')
  ),
  displayMode: 7,
  flowManager: {module_sub_type}ModuleFlowManager
}}
'''
    with open(module_path / "registries" / f"{module_sub_type}ModuleConfig.ts", "w", encoding="utf-8") as f:
        f.write(registry_content)


    # 输出需要在main.ts添加的代码
    print("\n// 在 @/features/{module_type}/registries/registries.ts 中添加以下代码：")
    print(f"import {{ {module_sub_type}ModuleFlowManager }} from '@/features/{module_type}/flows/{module_sub_type}FlowManager'")
    print(f"createModuleFlowRegistry('{module_sub_type}', {module_sub_type}ModuleFlowManager)")
    print(f"import {{ {module_sub_type}ModuleConfig }} from '@/features/{module_type}/registries/{module_sub_type}ModuleConfig'")
    print(f"createModuleRegistry('{module_sub_type}', {module_sub_type}ModuleConfig)")
    print("\n// 在 locale 中添加以下代码：")
    print(f'"{ module_sub_type}_subtype_name": "{ module_sub_type}(按语种填写)",')
    print(f'"{ module_sub_type}_subtype_description": "(这里填入你的定义)",')
    print("不要忘记在后台生成对应相关的类型数据！！！")


if __name__ == "__main__":
    a = input("请输入moduleType（例如 sample）: ").strip()
    b = input("请输入moduleSubType（例如 sample）: ").strip()
    create_module_files(a, b)
