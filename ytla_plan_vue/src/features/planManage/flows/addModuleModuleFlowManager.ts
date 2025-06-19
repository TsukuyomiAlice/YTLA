import type { Component } from 'vue'
import { defineAsyncComponent, markRaw } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class AddModuleModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()

  initialStep: Component | null = null
  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }
  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const addModuleModuleFlowManager = new AddModuleModuleFlowManager()

addModuleModuleFlowManager.registerFlow('addModule-main-steps', [
  defineAsyncComponent(() => import('@/features/planManage/components/modules/addModule/AddModuleMain_00.vue')),
])

addModuleModuleFlowManager.registerFlow('addModule-sub-steps', [
  defineAsyncComponent(() => import('@/features/planManage/components/modules/addModule/AddModuleSub_00.vue')),
])
