const loadedModules = new Set<string>()

export function loadModuleRegistries(): void {
  const moduleMap = import.meta.glob('@/features/**/modules/_type/registries/registries.ts', { eager: true })
  
  Object.keys(moduleMap).forEach(path => {
    if (!loadedModules.has(path)) {
      loadedModules.add(path)
      console.debug(`[loadModuleRegistries] 模块注册文件已同步加载: ${path}`)
    }
  })
}

export function clearLoadedModules(): void {
  loadedModules.clear()
}
