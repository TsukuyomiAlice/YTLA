import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/domain/area/frame/types/flowManagerTypes.ts'

export class BacklogModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const backlogModuleFlowManager = new BacklogModuleFlowManager()

backlogModuleFlowManager.registerFlow('backlog-main-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/backlog/components/BacklogMain_00.vue')),
])

backlogModuleFlowManager.registerFlow('backlog-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/backlog/components/BacklogSub_00.vue')),
])

