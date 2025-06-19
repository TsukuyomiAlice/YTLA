import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class BibleModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const bibleModuleFlowManager = new BibleModuleFlowManager()

bibleModuleFlowManager.registerFlow('bible-main-steps', [
  defineAsyncComponent(() => import('@/features/agile/components/modules/bible/BibleMain_00.vue')),
])

bibleModuleFlowManager.registerFlow('bible-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/components/modules/bible/BibleSub_00.vue')),
])

