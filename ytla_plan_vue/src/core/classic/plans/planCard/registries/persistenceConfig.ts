import { createPersistenceNamespace } from '@/core/classic/busline/persistence/factories/persistenceRegistry.ts'

createPersistenceNamespace({
  namespace: 'planCards',
  version: 1,
  defaultState: {
    pinned: {},
    order: []
  }
})
