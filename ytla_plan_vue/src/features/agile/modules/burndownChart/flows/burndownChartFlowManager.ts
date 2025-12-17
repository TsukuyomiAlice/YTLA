import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/types/flowManagerTypes.ts'

export class BurndownChartModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const burndownChartModuleFlowManager = new BurndownChartModuleFlowManager()

burndownChartModuleFlowManager.registerFlow('burndownChart-main-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/burndownChart/components/BurndownChartMain_00.vue')),
])

burndownChartModuleFlowManager.registerFlow('burndownChart-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/burndownChart/components/BurndownChartSub_00.vue')),
])

