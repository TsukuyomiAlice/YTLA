import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/domain/area/frame/types/flowManagerTypes.ts'

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
  defineAsyncComponent(() => import('@/features/basic/modules/relation/components/RelationMain_00.vue')),
])

relationModuleFlowManager.registerFlow('relation-sub-steps', [
  defineAsyncComponent(() => import('@/features/basic/modules/relation/components/RelationSub_00.vue')),
])

