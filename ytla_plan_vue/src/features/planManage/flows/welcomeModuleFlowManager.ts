import type { Component } from 'vue'
import { defineAsyncComponent, markRaw } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/_type/types/flowManagerTypes.ts'

export class WelcomeModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null
  registerFlow(flowName: string, steps: Component[]) {
    this.flows.set(flowName, steps)
  }
  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const welcomeModuleFlowManager = new WelcomeModuleFlowManager()

welcomeModuleFlowManager.registerFlow('welcome-main-steps', [
  markRaw(defineAsyncComponent(() => import('@/features/planManage/components/modules/welcome/WelcomePageMain_00.vue'))),
  markRaw(defineAsyncComponent(() => import('@/features/planManage/components/modules/welcome/WelcomePageMain_01.vue'))),
  markRaw(defineAsyncComponent(() => import('@/features/planManage/components/modules/welcome/WelcomePageMain_02.vue'))),
])

welcomeModuleFlowManager.registerFlow('welcome-sub-steps', [
  markRaw(defineAsyncComponent(() => import('@/features/planManage/components/modules/welcome/WelcomePageSub_00.vue'))),
  markRaw(defineAsyncComponent(() => import('@/features/planManage/components/modules/welcome/WelcomePageSub_01.vue'))),
])
