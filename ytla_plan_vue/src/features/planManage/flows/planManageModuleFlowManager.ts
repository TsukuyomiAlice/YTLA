import type { Component } from 'vue'
import { defineAsyncComponent, markRaw } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class PlanManageModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()

  initialStep: Component | null = null
  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }
  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const planManageModuleFlowManager = new PlanManageModuleFlowManager()

planManageModuleFlowManager.registerFlow('planManage-main-steps', [
  defineAsyncComponent(() => import('@/features/planManage/components/modules/planManager/PlanManagerMain_00.vue')),
])

planManageModuleFlowManager.registerFlow('planManage-sub-steps', [
  defineAsyncComponent(() => import('@/features/planManage/components/modules/planManager/PlanManagerSub_00.vue')),
])
