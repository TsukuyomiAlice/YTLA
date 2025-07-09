import type { Component } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export interface ModuleRegistry<T extends string = string> {
  moduleType: string
  moduleSubType: string
  moduleConcept: 'system' | 'time' | 'space' | 'definition'  | 'relation' | 'interaction'
  mainComponent: Component
  subComponent?: Component
  displayMode: number
  flowManager?: ModuleFlowManager
}

const moduleRegistryStore = new Map<string, ModuleRegistry>()

export const createModuleRegistry = <T extends string>(
  moduleSubType: string,
  config: ModuleRegistry<T>
): ModuleRegistry<T> => {
  moduleRegistryStore.set(moduleSubType, config)
  return config
}

export const getModuleConfig = (moduleSubType: string): ModuleRegistry | undefined => {
  return moduleRegistryStore.get(moduleSubType)
}


export function getRegisteredModules(): string[] {
  return Array.from(moduleRegistryStore.keys());
}
