import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/types/flowManagerTypes.ts'

export class WhiteboardModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const whiteboardModuleFlowManager = new WhiteboardModuleFlowManager()

whiteboardModuleFlowManager.registerFlow('whiteboard-main-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/whiteboard/components/WhiteboardMain_00.vue')),
])

whiteboardModuleFlowManager.registerFlow('whiteboard-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/whiteboard/components/WhiteboardSub_00.vue')),
])

