/**
 * 动态加载注册文件工具
 * 使用 Vite 的 import.meta.glob 实现按模式批量导入
 * 注意：由于 Vite 限制，import.meta.glob 的模式必须是字符串字面量
 * 因此我们预定义了一组支持的模式，通过模式键来引用
 */

// 缓存已加载的模块路径，避免重复加载
const loadedModules = new Set<string>()

interface LoadRegistriesOptions {
  /**
   * 是否立即导入模块（同步加载副作用）
   * @default false
   */
  eager?: boolean
}

// 预定义的 glob 模式映射
const PREDEFINED_PATTERNS = {
  // 功能域模块注册文件
  'features-modules': '@/features/**/modules/_type/registries/registries.ts',
  // 功能域卡片注册文件  
  'features-cards': '@/features/**/cards/_type/registries/registries.ts',
  // 核心注册文件
  'core': '@/core/classic/**/registries/*.ts',
  // planManage 模块注册文件
  'plan-manage': '@/features/planManage/modules/_type/registries/registries.ts',
} as const

type PatternKey = keyof typeof PREDEFINED_PATTERNS
type PatternValue = typeof PREDEFINED_PATTERNS[PatternKey]

/**
 * 根据预定义的模式键获取对应的 import.meta.glob 结果
 */
function getGlobMatches(patternKey: PatternKey, eager: boolean): Record<string, () => Promise<unknown>> {
  const pattern = PREDEFINED_PATTERNS[patternKey]
  return getGlobMatchesByLiteral(pattern, eager)
}

/**
 * 对字面量模式执行 import.meta.glob
 */
function getGlobMatchesByLiteral(pattern: PatternValue, eager: boolean): Record<string, () => Promise<unknown>> {
  // 使用 switch 确保 Vite 能静态分析所有可能的字面量
  switch (pattern) {
    case '@/features/**/modules/_type/registries/registries.ts':
      return import.meta.glob('@/features/**/modules/_type/registries/registries.ts', { eager })
    case '@/features/**/cards/_type/registries/registries.ts':
      return import.meta.glob('@/features/**/cards/_type/registries/registries.ts', { eager })
    case '@/core/classic/**/registries/*.ts':
      return import.meta.glob('@/core/classic/**/registries/*.ts', { eager })
    case '@/features/planManage/modules/_type/registries/registries.ts':
      return import.meta.glob('@/features/planManage/modules/_type/registries/registries.ts', { eager })
    default:
      // 类型安全：理论上不会到达这里
      const _exhaustiveCheck: never = pattern
      throw new Error(`Unsupported glob pattern: ${pattern}. Please add it to getGlobMatchesByLiteral switch statement.`)
  }
}

/**
 * 根据 glob 模式键动态加载注册文件
 * @param patternKeys - 预定义的模式键或键数组
 * @param options - 加载选项
 * @returns Promise<void>，当所有匹配文件加载完成后 resolve
 */
export async function loadRegistries(
  patternKeys: PatternKey | PatternKey[],
  options: LoadRegistriesOptions = {}
): Promise<void> {
  const { eager = false } = options
  const keyArray = Array.isArray(patternKeys) ? patternKeys : [patternKeys]
  
  // 收集所有匹配的模块
  const moduleMap: Record<string, () => Promise<unknown>> = {}
  
  for (const key of keyArray) {
    const matches = getGlobMatches(key, eager)
    Object.assign(moduleMap, matches)
  }
  
  // 如果 eager 为 true，模块已立即导入，副作用已执行
  if (eager) {
    Object.keys(moduleMap).forEach(path => {
      if (!loadedModules.has(path)) {
        loadedModules.add(path)
        console.debug(`[loadRegistries] 模块已同步加载: ${path}`)
      }
    })
    return
  }
  
  // 否则，异步加载每个模块
  const loadPromises = Object.entries(moduleMap).map(async ([path, importFn]) => {
    // 检查是否已加载
    if (loadedModules.has(path)) {
      console.debug(`[loadRegistries] 模块已加载，跳过: ${path}`)
      return
    }
    
    try {
      // 执行导入（触发模块副作用）
      await importFn()
      loadedModules.add(path)
      console.debug(`[loadRegistries] 模块加载成功: ${path}`)
    } catch (error) {
      console.error(`[loadRegistries] 模块加载失败: ${path}`, error)
      // 不抛出错误，允许其他模块继续加载
    }
  })
  
  // 等待所有导入完成，不因单个失败而中断
  await Promise.allSettled(loadPromises)
}

/**
 * 清空加载缓存（主要用于测试）
 */
export function clearLoadedModules(): void {
  loadedModules.clear()
}

// 导出类型，方便外部使用
export type { PatternKey }