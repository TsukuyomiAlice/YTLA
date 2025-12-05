import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/_type/types/flowManagerTypes.ts'

export class SpaceModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const spaceModuleFlowManager = new SpaceModuleFlowManager()

spaceModuleFlowManager.registerFlow('space-main-steps', [
  defineAsyncComponent(() => import('@/features/basic/modules/space/components/SpaceMain_00.vue')),
])

spaceModuleFlowManager.registerFlow('space-sub-steps', [
  defineAsyncComponent(() => import('@/features/basic/modules/space/components/SpaceSub_00.vue')),
])

