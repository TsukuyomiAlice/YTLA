import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/domain/area/frame/types/flowManagerTypes.ts'

export class KanbanModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()

  initialStep: Component | null = null
  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }
  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const kanbanModuleFlowManager = new KanbanModuleFlowManager()

kanbanModuleFlowManager.registerFlow('kanban-main-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/kanban/components/KanbanMain_00.vue')),
])

kanbanModuleFlowManager.registerFlow('kanban-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/kanban/components/KanbanSub_00.vue')),
])

