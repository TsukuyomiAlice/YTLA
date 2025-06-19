import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { propertyModuleFlowManager } from '@/features/agile/flows/propertyFlowManager'

createModuleRegistry('property', {
  moduleType: 'agile',
  moduleSubType: 'property',
  moduleConcept: 'relation',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/property/PropertyMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/property/PropertySub.vue')
  ),
  displayMode: 7,
  flowManager: propertyModuleFlowManager
})
