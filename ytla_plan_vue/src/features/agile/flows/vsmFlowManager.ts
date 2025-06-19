import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class VsmModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const vsmModuleFlowManager = new VsmModuleFlowManager()

vsmModuleFlowManager.registerFlow('vsm-main-steps', [
  defineAsyncComponent(() => import('@/features/agile/components/modules/vsm/VsmMain_00.vue')),
])

vsmModuleFlowManager.registerFlow('vsm-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/components/modules/vsm/VsmSub_00.vue')),
])

