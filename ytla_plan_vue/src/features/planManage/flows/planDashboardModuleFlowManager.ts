import type { Component } from 'vue'
import { defineAsyncComponent, markRaw } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class PlanDashboardModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()

  initialStep: Component | null = null
  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }
  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const planDashboardModuleFlowManager = new PlanDashboardModuleFlowManager()

planDashboardModuleFlowManager.registerFlow('planDashboard-main-steps', [
  defineAsyncComponent(() => import('@/features/planManage/components/modules/planDashboard/PlanDashboardMain_00.vue')),
])

planDashboardModuleFlowManager.registerFlow('planDashboard-sub-steps', [
  defineAsyncComponent(() => import('@/features/planManage/components/modules/planDashboard/PlanDashboardSub_00.vue')),
])
