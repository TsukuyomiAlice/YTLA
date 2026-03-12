const loadedModules = new Set<string>()

function loadSystemRegistries(): void {
  const coreModules = import.meta.glob('@/core/classic/**/registries/*.ts', { eager: true })
  const planManageModules = import.meta.glob('@/features/planManage/modules/_type/registries/registries.ts', { eager: true })

  const moduleMap = { ...coreModules, ...planManageModules }

  Object.keys(moduleMap).forEach(path => {
    if (!loadedModules.has(path)) {
      loadedModules.add(path)
      console.debug(`[loadSystemRegistries] 系统模块已同步加载: ${path}`)
    }
  })
}

// 动态加载核心注册文件
loadSystemRegistries()
