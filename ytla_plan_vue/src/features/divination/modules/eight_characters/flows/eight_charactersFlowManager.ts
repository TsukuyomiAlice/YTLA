import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class Eight_charactersModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const eight_charactersModuleFlowManager = new Eight_charactersModuleFlowManager()

eight_charactersModuleFlowManager.registerFlow('eight_characters-main-steps', [
  defineAsyncComponent(() => import('@/features/divination/modules/eight_characters/components/Eight_charactersMain_00.vue')),
])

eight_charactersModuleFlowManager.registerFlow('eight_characters-sub-steps', [
  defineAsyncComponent(() => import('@/features/divination/modules/eight_characters/components/Eight_charactersSub_00.vue')),
])
