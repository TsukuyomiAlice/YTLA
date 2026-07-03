import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class Xiao_liu_renModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const xiao_liu_renModuleFlowManager = new Xiao_liu_renModuleFlowManager()

xiao_liu_renModuleFlowManager.registerFlow('xiao_liu_ren-main-steps', [
  defineAsyncComponent(() => import('@/features/divination/modules/xiao_liu_ren/components/Xiao_liu_renMain_00.vue')),
])

xiao_liu_renModuleFlowManager.registerFlow('xiao_liu_ren-sub-steps', [
  defineAsyncComponent(() => import('@/features/divination/modules/xiao_liu_ren/components/Xiao_liu_renSub_00.vue')),
])
