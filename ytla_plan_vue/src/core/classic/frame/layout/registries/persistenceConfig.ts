import { createPersistenceNamespace } from '@/core/classic/frame/persistence/factories/persistenceRegistry.ts'

createPersistenceNamespace({
  namespace: 'layout',
  version: 1,
  defaultState: {
    swapped: false,
    sidebarVisible: false,
    layoutSwapped: false,
    userLanguage: 'en',
    hasPlan: false
  }
})
