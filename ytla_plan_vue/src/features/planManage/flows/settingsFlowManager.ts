import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class SettingsModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const settingsModuleFlowManager = new SettingsModuleFlowManager()

settingsModuleFlowManager.registerFlow('settings-main-steps', [
  defineAsyncComponent(() => import('@/features/planManage/components/modules/settings/SettingsMain_00.vue')),
])

settingsModuleFlowManager.registerFlow('settings-sub-steps', [
  defineAsyncComponent(() => import('@/features/planManage/components/modules/settings/SettingsSub_00.vue')),
])

