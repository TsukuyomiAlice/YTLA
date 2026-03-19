import { getAllCardRegistries } from './cardRegistry.ts'

const loadedModules = new Set<string>()

export function loadCardRegistries(): void {
  console.groupCollapsed('[loadCardRegistries] Starting to load card registries')
  console.time('[loadCardRegistries] Total time')

  const moduleMap = import.meta.glob('@/features/**/cards/_type/registries/registries.ts', { eager: true })
  const totalModules = Object.keys(moduleMap).length

  console.debug(`[loadCardRegistries] Found ${totalModules} card registry files`)

  Object.keys(moduleMap).forEach((path, index) => {
    if (!loadedModules.has(path)) {
      loadedModules.add(path)
      console.debug(`[loadCardRegistries] [${index + 1}/${totalModules}] Card module loaded: ${path}`)
    } else {
      console.debug(`[loadCardRegistries] [${index + 1}/${totalModules}] Card module already loaded, skipping: ${path}`)
    }
  })

  console.timeEnd('[loadCardRegistries] Total time')

  const store = getAllCardRegistries()
  
  if (store.size > 0) {
    console.debug(`[loadCardRegistries] Successfully loaded ${store.size} card registries`)
    store.forEach((registry, namespace) => {
      console.debug(`[loadCardRegistries]  - ${namespace}: ${Object.keys(registry.components || {}).length} components`)
    })
  } else {
    console.warn('[loadCardRegistries] No card registries found, please check if registry files correctly call createCardRegistry')
  }

  console.groupEnd()
}

export function clearLoadedModules(): void {
  console.debug('[loadCardRegistries] Clearing loaded card module list')
  loadedModules.clear()
}
