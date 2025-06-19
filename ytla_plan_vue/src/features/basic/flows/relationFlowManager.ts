import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class RelationModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const relationModuleFlowManager = new RelationModuleFlowManager()

relationModuleFlowManager.registerFlow('relation-main-steps', [
  defineAsyncComponent(() => import('@/features/basic/components/modules/relation/RelationMain_00.vue')),
])

relationModuleFlowManager.registerFlow('relation-sub-steps', [
  defineAsyncComponent(() => import('@/features/basic/components/modules/relation/RelationSub_00.vue')),
])

