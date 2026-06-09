import { createPersistenceNamespace } from '@/core/classic/frame/persistence/factories/persistenceRegistry.ts'

createPersistenceNamespace({
  namespace: 'planCards',
  version: 1,
  defaultState: {
    pinned: {},
    order: []
  }
})
