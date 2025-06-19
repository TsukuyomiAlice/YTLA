import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class DictionaryModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const dictionaryModuleFlowManager = new DictionaryModuleFlowManager()

dictionaryModuleFlowManager.registerFlow('dictionary-main-steps', [
  defineAsyncComponent(() => import('@/features/language/components/modules/dictionary/DictionaryMain_00.vue')),
])

dictionaryModuleFlowManager.registerFlow('dictionary-sub-steps', [
  defineAsyncComponent(() => import('@/features/language/components/modules/dictionary/DictionarySub_00.vue')),
])

