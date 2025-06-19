import { type Component, defineAsyncComponent } from 'vue'

export interface ModuleRegistry<T extends string = string> {
  moduleType: string
  moduleSubType: string
  moduleConcept: 'system' | 'time' | 'space' | 'definition'  | 'relation' | 'interaction'
  mainComponent: Component
  subComponent?: Component
  displayMode: number
  flowManager?: any
}

const registryStore = new Map<string, ModuleRegistry>()

export const createModuleRegistry = <T extends string>(
  moduleSubType: T,
  config: ModuleRegistry<T>
): void => {
  registryStore.set(moduleSubType, config)
}

export const getModuleConfig = (moduleSubType: string): ModuleRegistry | undefined => {
  return registryStore.get(moduleSubType)
}


export function getRegisteredModules(): string[] {
  return Array.from(registryStore.keys());
}
