import { loadCardRegistries } from '@/core/classic/cards/sideCard/factories/cardRegistryLoader'
import { loadCardEditorFlowRegistries } from '@/core/classic/cards/sideCardEditor/factories/cardEditorFlowRegistryLoader'
import { loadModuleRegistries } from '@/core/classic/modules/moduleCard/factories/moduleRegistryLoader'

console.groupCollapsed('[featuresRegistry] Starting to load feature domain registry files')
console.time('[featuresRegistry] Total time')

// Dynamically load all feature domain registry files
loadCardRegistries()
loadCardEditorFlowRegistries()
loadModuleRegistries()

console.timeEnd('[featuresRegistry] Total time')
console.groupEnd()