import { createPersistenceNamespace } from '@/core/classic/busline/persistence/factories/persistenceRegistry.ts'
import type { PersistenceNamespace } from '@/core/classic/busline/persistence/definitions/persistenceTypes.ts'

createPersistenceNamespace({
  namespace: 'plans',
  version: 1,
  defaultState: {
    plan_manage: {
      currentModule: 'planManage',
      modules: {}
    }
  },
  /**
   * 特殊逻辑：当传入的 key 值为 undefined 时，删除该 key
   * 用于清理已删除 plan 的持久化数据
   */
  onBeforeSet: (updates: Record<string, any>, current: Record<string, any>) => {
    for (const key in updates) {
      if (updates[key] === undefined) {
        delete current[key]
        delete updates[key]
      }
    }
    return updates
  }
})
