import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class DashboardModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const dashboardModuleFlowManager = new DashboardModuleFlowManager()

dashboardModuleFlowManager.registerFlow('dashboard-main-steps', [
  defineAsyncComponent(() => import('@/features/agile/components/modules/dashboard/DashboardMain_00.vue')),
])

dashboardModuleFlowManager.registerFlow('dashboard-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/components/modules/dashboard/DashboardSub_00.vue')),
])

