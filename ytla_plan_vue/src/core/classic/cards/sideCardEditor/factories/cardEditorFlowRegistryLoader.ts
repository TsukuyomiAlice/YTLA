import { getAllCardEditorFlowManagers } from './cardEditorFlowRegistry.ts'

const loadedModules = new Set<string>()

export function loadCardEditorFlowRegistries(): void {
  console.groupCollapsed('[loadCardEditorFlowRegistries] Starting to load card editor flow registries')
  console.time('[loadCardEditorFlowRegistries] Total time')

  const moduleMap = import.meta.glob('@/features/**/cards/_type/registries/registries.ts', { eager: true })
  const totalModules = Object.keys(moduleMap).length

  console.debug(`[loadCardEditorFlowRegistries] Found ${totalModules} card editor flow registry files`)

  Object.keys(moduleMap).forEach((path, index) => {
    if (!loadedModules.has(path)) {
      loadedModules.add(path)
      console.debug(`[loadCardEditorFlowRegistries] [${index + 1}/${totalModules}] Card editor flow module loaded: ${path}`)
    } else {
      console.debug(`[loadCardEditorFlowRegistries] [${index + 1}/${totalModules}] Card editor flow module already loaded, skipping: ${path}`)
    }
  })

  console.timeEnd('[loadCardEditorFlowRegistries] Total time')

  const store = getAllCardEditorFlowManagers()
  
  if (store.size > 0) {
    console.debug(`[loadCardEditorFlowRegistries] Successfully loaded ${store.size} card editor flow managers`)
    store.forEach((manager, cardType) => {
      console.debug(`[loadCardEditorFlowRegistries]  - ${cardType}`)
    })
  } else {
    console.warn('[loadCardEditorFlowRegistries] No card editor flow managers found, please check if registry files correctly call createCardEditorFlowRegistry')
  }

  console.groupEnd()
}

export function clearLoadedModules(): void {
  console.debug('[loadCardEditorFlowRegistries] Clearing loaded card editor flow module list')
  loadedModules.clear()
}
