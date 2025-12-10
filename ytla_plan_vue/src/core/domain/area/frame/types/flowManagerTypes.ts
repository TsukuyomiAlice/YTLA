import type { Component } from 'vue'

export interface CardEditorFlowManager {
  initialStep: Component | null
  registerFlow(cardSubType: string, steps: Component[]): void
  getSteps(cardSubType: string): Component[]
}

export interface ModuleFlowManager {
  initialStep: Component | null
  registerFlow(flowName: string, steps: Component[]): void
  getSteps(flowName: string): Component[]
}
