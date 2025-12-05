import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/_type/types/flowManagerTypes.ts'

export class DmdModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const dmdModuleFlowManager = new DmdModuleFlowManager()

dmdModuleFlowManager.registerFlow('dmd-main-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/dmd/components/DmdMain_00.vue')),
])

dmdModuleFlowManager.registerFlow('dmd-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/dmd/components/DmdSub_00.vue')),
])

