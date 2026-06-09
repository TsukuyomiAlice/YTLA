import { persistenceStore } from '../services/persistenceStore.ts'

export function usePersistence() {
  return {
    getPersistence: persistenceStore.get.bind(persistenceStore),
    setPersistence: persistenceStore.set.bind(persistenceStore),
  }
}

export type { PanelContentState } from '../definitions/persistenceTypes.ts'
