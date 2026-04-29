import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class Create_cardModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const create_cardModuleFlowManager = new Create_cardModuleFlowManager()

create_cardModuleFlowManager.registerFlow('create_card-main-steps', [
  defineAsyncComponent(() => import('@/features/scaffold/modules/create_card/components/Create_cardMain_00.vue')),
])

create_cardModuleFlowManager.registerFlow('create_card-sub-steps', [
  defineAsyncComponent(() => import('@/features/scaffold/modules/create_card/components/Create_cardSub_00.vue')),
])
