import type { PersistenceNamespace } from '../definitions/persistenceTypes.ts'

const registry = new Map<string, PersistenceNamespace>()

export function createPersistenceNamespace<T>(config: PersistenceNamespace<T>) {
  if (registry.has(config.namespace)) return
  registry.set(config.namespace, config)
}

export function getNamespace(namespace: string) {
  return registry.get(namespace)
}

export function getAllNamespaces() {
  return registry
}
