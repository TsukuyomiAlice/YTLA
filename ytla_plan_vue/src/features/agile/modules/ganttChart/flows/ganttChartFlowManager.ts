import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class GanttChartModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const ganttChartModuleFlowManager = new GanttChartModuleFlowManager()

ganttChartModuleFlowManager.registerFlow('ganttChart-main-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/ganttChart/components/GanttChartMain_00.vue')),
])

ganttChartModuleFlowManager.registerFlow('ganttChart-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/ganttChart/components/GanttChartSub_00.vue')),
])

