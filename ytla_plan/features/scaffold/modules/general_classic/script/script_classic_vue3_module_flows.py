from pathlib import Path


def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s


def create_flows_file(base_path, module_type, module_sub_type):
    """
    生成 Module 具体功能实现目录的 flows 文件

    参数：
        base_path: str - 基础路径
        module_type: str - 模块类型
        module_sub_type: str - 模块子类型
    """
    module_sub_type_upper = first_letter_upper(module_sub_type)

    file_path = Path(base_path) / module_type / "modules" / module_sub_type / "flows" / f"{module_sub_type}FlowManager.ts"

    file_path.parent.mkdir(parents=True, exist_ok=True)

    content = f'''import type {{ Component }} from 'vue'
import {{ defineAsyncComponent }} from 'vue'
import type {{ ModuleFlowManager }} from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class {module_sub_type_upper}ModuleFlowManager implements ModuleFlowManager {{
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {{
    this.flows.set(flowName, steps)
  }}

  getSteps(flowName: string): Component[] {{
    return this.flows.get(flowName) || []
  }}
}}

export const {module_sub_type}ModuleFlowManager = new {module_sub_type_upper}ModuleFlowManager()

{module_sub_type}ModuleFlowManager.registerFlow('{module_sub_type}-main-steps', [
  defineAsyncComponent(() => import('@/features/{module_type}/modules/{module_sub_type}/components/{module_sub_type_upper}Main_00.vue')),
])

{module_sub_type}ModuleFlowManager.registerFlow('{module_sub_type}-sub-steps', [
  defineAsyncComponent(() => import('@/features/{module_type}/modules/{module_sub_type}/components/{module_sub_type_upper}Sub_00.vue')),
])
'''

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"已生成: {file_path}")



