import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/domain/area/frame/types/flowManagerTypes.ts'

export class PlumYiModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const plumYiModuleFlowManager = new PlumYiModuleFlowManager()

plumYiModuleFlowManager.registerFlow('plumYi-main-steps', [
  defineAsyncComponent(() => import('@/features/divination/modules/plumYi/components/PlumYiMain_00.vue')),
])

plumYiModuleFlowManager.registerFlow('plumYi-sub-steps', [
  defineAsyncComponent(() => import('@/features/divination/modules/plumYi/components/PlumYiSub_00.vue')),
])

