import type { Component } from 'vue'
import ModuleCard from '@/features/planManage/components/card/ModuleCard.vue'

export interface ModuleCardRegistry {
  components: { default: Component }
  getModuleProps: (module: any) => Record<string, any>
}

const registryStore = new Map<string, ModuleCardRegistry>()

export const createModuleCardRegistry = (): void => {
  registryStore.set('module', {
    components: { default: ModuleCard },
    getModuleProps: (module) => ({
      moduleId: module.module_id,
      name: module.name,
      tags: module.tags,
      description: module.description,
      message: module.message,
      icon: module.icon_path,
      background: module.background_path
    })
  })
}

export const getModuleCardRegistry = () => {
  return registryStore.get('module')
}

