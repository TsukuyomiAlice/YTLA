const loadedModules = new Set<string>()

export function loadCardRegistries(): void {
  const moduleMap = import.meta.glob('@/features/**/cards/_type/registries/registries.ts', { eager: true })

  Object.keys(moduleMap).forEach(path => {
    if (!loadedModules.has(path)) {
      loadedModules.add(path)
      console.debug(`[loadCardRegistries] 卡片模块已同步加载: ${path}`)
    }
  })
}

export function clearLoadedModules(): void {
  loadedModules.clear()
}
