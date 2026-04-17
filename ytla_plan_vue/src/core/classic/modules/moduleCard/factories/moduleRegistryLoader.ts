import { getAllModuleRegistries } from './moduleRegistry.ts'

const loadedModules = new Set<string>()

export function loadModuleRegistries(): void {
  console.groupCollapsed('[loadModuleRegistries] Starting to load module registries')
  console.time('[loadModuleRegistries] Total time')

  const moduleMap = import.meta.glob('@/features/**/modules/**/registries/registries.ts', { eager: true })
  const totalModules = Object.keys(moduleMap).length

  console.debug(`[loadModuleRegistries] Found ${totalModules} module registry files`)

  Object.keys(moduleMap).forEach((path, index) => {
    if (!loadedModules.has(path)) {
      loadedModules.add(path)
      console.debug(`[loadModuleRegistries] [${index + 1}/${totalModules}] Module loaded: ${path}`)
    } else {
      console.debug(`[loadModuleRegistries] [${index + 1}/${totalModules}] Module already loaded, skipping: ${path}`)
    }
  })

  console.timeEnd('[loadModuleRegistries] Total time')

  const store = getAllModuleRegistries()

  if (store.size > 0) {
    console.debug(`[loadModuleRegistries] Successfully loaded ${store.size} module registries`)
    store.forEach((registry, moduleSubType) => {
      console.debug(`[loadModuleRegistries]  - ${moduleSubType} (${registry.moduleType}, ${registry.moduleConcept})`)
    })
  } else {
    console.warn('[loadModuleRegistries] No module registries found, please check if registry files correctly call createModuleRegistry')
  }

  console.groupEnd()
}

export function clearLoadedModules(): void {
  console.debug('[loadModuleRegistries] Clearing loaded module list')
  loadedModules.clear()
}
