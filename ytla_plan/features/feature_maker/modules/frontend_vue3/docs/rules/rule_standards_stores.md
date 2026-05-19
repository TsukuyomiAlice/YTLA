# Stores 代码规范

## 1 依赖限制表

| 功能域类型 | stores可依赖此功能域 | stores可被此功能域依赖 |
| :--- | :--- | :--- |
| definitions | ✓ |  |
| styles |  |  |
| utils |  |  |
| locales |  |  |
| avatar |  |  |
| factories |  |  |
| flows |  |  |
| registries |  |  |
| services | ✓ |  |
| policies |  |  |
| stores |  |  |
| composables |  | ✓ |
| uis |  |  |
| components |  |  |
| layouts |  |  |

## 2 标准代码格式

以下内容仅供参考，不作为实际项目代码使用.  

### 2.1 基础状态管理

```typescript
// stores/[模块名].ts

import { reactive, readonly, computed } from 'vue'

interface [模块名]State {
  items: [数据类型][]
  loading: boolean
  error: string | null
  currentId: string | null
}

const state = reactive<[模块名]State>({
  items: [],
  loading: false,
  error: null,
  currentId: null
})

export function use[模块名]Store() {
  const items = computed(() => readonly(state.items))
  const loading = computed(() => state.loading)
  const error = computed(() => state.error)
  const currentItem = computed(() => 
    state.items.find(item => item.id === state.currentId) ?? null
  )

  function setItems(items: [数据类型][]): void {
    state.items = items
  }

  function addItem(item: [数据类型]): void {
    state.items.push(item)
  }

  function updateItem(id: string, updates: Partial<[数据类型]>): void {
    const index = state.items.findIndex(item => item.id === id)
    if (index !== -1) {
      state.items[index] = { ...state.items[index], ...updates }
    }
  }

  function removeItem(id: string): void {
    const index = state.items.findIndex(item => item.id === id)
    if (index !== -1) {
      state.items.splice(index, 1)
    }
  }

  function setLoading(loading: boolean): void {
    state.loading = loading
  }

  function setError(error: string | null): void {
    state.error = error
  }

  function setCurrentId(id: string | null): void {
    state.currentId = id
  }

  function clear(): void {
    state.items = []
    state.loading = false
    state.error = null
    state.currentId = null
  }

  return {
    items,
    loading,
    error,
    currentItem,
    setItems,
    addItem,
    updateItem,
    removeItem,
    setLoading,
    setError,
    setCurrentId,
    clear
  }
}
```

### 2.2 带 API 集成的状态管理

```typescript
// stores/[模块名]Store.ts

import { reactive, readonly, computed } from 'vue'
import type { [模块名]Data } from '../definitions'
import { [模块名]Service } from '../services'

interface [模块名]State {
  data: [模块名]Data | null
  list: [模块名]Data[]
  loading: boolean
  error: string | null
}

const state = reactive<[模块名]State>({
  data: null,
  list: [],
  loading: false,
  error: null
})

export function use[模块名]Store() {
  const data = computed(() => readonly(state.data))
  const list = computed(() => readonly(state.list))
  const loading = computed(() => state.loading)
  const error = computed(() => state.error)

  async function fetchList(): Promise<void> {
    state.loading = true
    state.error = null
    try {
      const result = await [模块名]Service.getList()
      state.list = result.data
    } catch (err) {
      state.error = err instanceof Error ? err.message : 'Failed to fetch list'
    } finally {
      state.loading = false
    }
  }

  async function fetchById(id: string): Promise<void> {
    state.loading = true
    state.error = null
    try {
      const result = await [模块名]Service.getById(id)
      state.data = result.data
    } catch (err) {
      state.error = err instanceof Error ? err.message : 'Failed to fetch data'
    } finally {
      state.loading = false
    }
  }

  async function create(data: Omit<[模块名]Data, 'id'>): Promise<void> {
    state.loading = true
    state.error = null
    try {
      const result = await [模块名]Service.create(data)
      state.list.unshift(result.data)
    } catch (err) {
      state.error = err instanceof Error ? err.message : 'Failed to create'
    } finally {
      state.loading = false
    }
  }

  async function update(id: string, data: Partial<[模块名]Data>): Promise<void> {
    state.loading = true
    state.error = null
    try {
      const result = await [模块名]Service.update(id, data)
      const index = state.list.findIndex(item => item.id === id)
      if (index !== -1) {
        state.list[index] = result.data
      }
      if (state.data?.id === id) {
        state.data = result.data
      }
    } catch (err) {
      state.error = err instanceof Error ? err.message : 'Failed to update'
    } finally {
      state.loading = false
    }
  }

  async function remove(id: string): Promise<void> {
    state.loading = true
    state.error = null
    try {
      await [模块名]Service.remove(id)
      const index = state.list.findIndex(item => item.id === id)
      if (index !== -1) {
        state.list.splice(index, 1)
      }
      if (state.data?.id === id) {
        state.data = null
      }
    } catch (err) {
      state.error = err instanceof Error ? err.message : 'Failed to remove'
    } finally {
      state.loading = false
    }
  }

  function clear(): void {
    state.data = null
    state.list = []
    state.loading = false
    state.error = null
  }

  return {
    data,
    list,
    loading,
    error,
    fetchList,
    fetchById,
    create,
    update,
    remove,
    clear
  }
}
```

### 2.3 多状态管理组合

```typescript
// stores/combinedStore.ts

import { reactive, readonly, computed } from 'vue'

interface FilterState {
  keyword: string
  page: number
  pageSize: number
  sortBy: string
  sortOrder: 'asc' | 'desc'
}

interface PaginationState {
  total: number
  currentPage: number
  pageSize: number
}

interface CombinedState {
  filter: FilterState
  pagination: PaginationState
}

const state = reactive<CombinedState>({
  filter: {
    keyword: '',
    page: 1,
    pageSize: 20,
    sortBy: 'createdAt',
    sortOrder: 'desc'
  },
  pagination: {
    total: 0,
    currentPage: 1,
    pageSize: 20
  }
})

export function useCombinedStore() {
  const filter = computed(() => readonly(state.filter))
  const pagination = computed(() => readonly(state.pagination))

  function setFilter(key: keyof FilterState, value: FilterState[keyof FilterState]): void {
    (state.filter[key] as any) = value
    if (key !== 'page') {
      state.filter.page = 1
    }
  }

  function resetFilter(): void {
    state.filter = {
      keyword: '',
      page: 1,
      pageSize: 20,
      sortBy: 'createdAt',
      sortOrder: 'desc'
    }
  }

  function setPagination(pagination: Partial<PaginationState>): void {
    Object.assign(state.pagination, pagination)
  }

  return {
    filter,
    pagination,
    setFilter,
    resetFilter,
    setPagination
  }
}
```