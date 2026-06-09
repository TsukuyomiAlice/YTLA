export function loadPersistenceRegistries(): void {
  // 扫描 core 下的 persistenceConfig.ts
  import.meta.glob('@/core/classic/**/registries/persistenceConfig.ts', { eager: true })
  // 扫描 features 下的 persistenceConfig.ts（方便未来扩展）
  import.meta.glob('@/features/**/registries/persistenceConfig.ts', { eager: true })
}
