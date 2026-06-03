import { createPersistenceNamespace } from '@/core/classic/busline/persistence/factories/persistenceRegistry.ts'

createPersistenceNamespace({
  namespace: 'cards',
  version: 1,
  defaultState: {
    pinned: {},
    expanded: {},
    order: []
  }
})
