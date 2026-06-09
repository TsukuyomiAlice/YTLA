import { getAllNamespaces } from '../factories/persistenceRegistry.ts'

const PERSISTENCE_KEY = 'ytla_persistence'

class PersistenceStore {
  private data: Record<string, any> | null = null

  private ensureLoaded() {
    if (this.data !== null) return

    const raw = localStorage.getItem(PERSISTENCE_KEY)
    const parsed: Record<string, any> = raw ? JSON.parse(raw) : {}

    this.data = {}

    // 以 registry 中的 defaultState 为基底，用已存储的值覆盖
    for (const [ns, config] of getAllNamespaces()) {
      this.data[ns] = { ...config.defaultState, ...parsed[ns] }
    }

    this.save()
  }

  private save() {
    if (this.data === null) return
    localStorage.setItem(PERSISTENCE_KEY, JSON.stringify(this.data))
  }

  get(namespace: string, key?: string) {
    this.ensureLoaded()
    if (!key) return this.data![namespace]
    return this.data![namespace]?.[key]
  }

  set(namespace: string, updates: Record<string, any>) {
    this.ensureLoaded()
    const config = getAllNamespaces().get(namespace)
    const current = this.data![namespace] || {}

    // 调用 namespace 自定义逻辑（如 plans 的 key 删除）
    this.data![namespace] = config?.onBeforeSet
      ? { ...current, ...config.onBeforeSet(updates, current) }
      : { ...current, ...updates }

    this.save()
  }
}

export const persistenceStore = new PersistenceStore()
