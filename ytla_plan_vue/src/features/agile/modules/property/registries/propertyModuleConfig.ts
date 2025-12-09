import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'
import { propertyModuleFlowManager } from '@/features/agile/modules/property/flows/propertyFlowManager.ts'

export const propertyModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'property',
  moduleConcept: 'relation',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/property/components/PropertyMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/property/components/PropertySub.vue')
  ),
  displayMode: 7,
  flowManager: propertyModuleFlowManager
}
