import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class Create_moduleModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const create_moduleModuleFlowManager = new Create_moduleModuleFlowManager()

create_moduleModuleFlowManager.registerFlow('create_module-main-steps', [
  defineAsyncComponent(() => import('@/features/scaffold/modules/create_module/components/Create_moduleMain_00.vue')),
])

create_moduleModuleFlowManager.registerFlow('create_module-sub-steps', [
  defineAsyncComponent(() => import('@/features/scaffold/modules/create_module/components/Create_moduleSub_00.vue')),
])
