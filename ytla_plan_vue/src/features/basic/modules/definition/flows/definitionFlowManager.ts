import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class DefinitionModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const definitionModuleFlowManager = new DefinitionModuleFlowManager()

definitionModuleFlowManager.registerFlow('definition-main-steps', [
  defineAsyncComponent(() => import('@/features/basic/modules/definition/components/DefinitionMain_00.vue')),
])

definitionModuleFlowManager.registerFlow('definition-sub-steps', [
  defineAsyncComponent(() => import('@/features/basic/modules/definition/components/DefinitionSub_00.vue')),
])

