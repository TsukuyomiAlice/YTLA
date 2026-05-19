# Services 代码规范

## 1 依赖限制表

| 功能域类型 | services可依赖此功能域 | services可被此功能域依赖 |
| :--- | :--- | :--- |
| definitions | ✓ |  |
| styles |  |  |
| utils |  |  |
| locales |  |  |
| avatar |  |  |
| factories |  |  |
| flows |  |  |
| registries |  |  |
| services | ✓(非自身) |  |
| policies |  |  |
| stores |  | ✓ |
| composables |  |  |
| uis |  |  |
| components |  |  |
| layouts |  |  |

## 2 标准代码格式

以下内容仅供参考，不作为实际项目代码使用.  

### 2.1 基础 API 服务

```typescript
// services/[模块名]Service.ts

import type { [模块名]Data, Create[模块名]Data, Update[模块名]Data } from '../definitions'
import { apiClient } from './apiClient'

export const [模块名]Service = {
  async getList(params?: Record<string, unknown>): Promise<[模块名]Data[]> {
    const response = await apiClient.get('/[模块名]s', { params })
    return response.data
  },

  async getById(id: string): Promise<[模块名]Data> {
    const response = await apiClient.get(`/[模块名]s/${id}`)
    return response.data
  },

  async create(data: Create[模块名]Data): Promise<[模块名]Data> {
    const response = await apiClient.post('/[模块名]s', data)
    return response.data
  },

  async update(id: string, data: Update[模块名]Data): Promise<[模块名]Data> {
    const response = await apiClient.put(`/[模块名]s/${id}`, data)
    return response.data
  },

  async remove(id: string): Promise<void> {
    await apiClient.delete(`/[模块名]s/${id}`)
  }
}
```

### 2.2 带请求配置的 API 服务

```typescript
// services/[模块名]Service.ts

import type { AxiosResponse, AxiosRequestConfig } from 'axios'
import type { [模块名]Data } from '../definitions'
import { apiClient } from './apiClient'

interface [模块名]QueryParams {
  page?: number
  pageSize?: number
  keyword?: string
  sortBy?: string
  sortOrder?: 'asc' | 'desc'
}

interface [模块名]Response<T = [模块名]Data> {
  data: T
  message: string
  success: boolean
}

interface [模块名]ListResponse<T = [模块名]Data> {
  data: T[]
  total: number
  page: number
  pageSize: number
}

export const [模块名]Service = {
  async getList(
    params?: [模块名]QueryParams,
    config?: AxiosRequestConfig
  ): Promise<[模块名]ListResponse> {
    const response: AxiosResponse<[模块名]ListResponse> = await apiClient.get(
      '/[模块名]s',
      { params, ...config }
    )
    return response.data
  },

  async getById(id: string, config?: AxiosRequestConfig): Promise<[模块名]Response> {
    const response: AxiosResponse<[模块名]Response> = await apiClient.get(
      `/[模块名]s/${id}`,
      config
    )
    return response.data
  },

  async create(
    data: Partial<[模块名]Data>,
    config?: AxiosRequestConfig
  ): Promise<[模块名]Response> {
    const response: AxiosResponse<[模块名]Response> = await apiClient.post(
      '/[模块名]s',
      data,
      config
    )
    return response.data
  },

  async update(
    id: string,
    data: Partial<[模块名]Data>,
    config?: AxiosRequestConfig
  ): Promise<[模块名]Response> {
    const response: AxiosResponse<[模块名]Response> = await apiClient.put(
      `/[模块名]s/${id}`,
      data,
      config
    )
    return response.data
  },

  async remove(id: string, config?: AxiosRequestConfig): Promise<void> {
    await apiClient.delete(`/[模块名]s/${id}`, config)
  },

  async batchRemove(ids: string[], config?: AxiosRequestConfig): Promise<void> {
    await apiClient.delete('/[模块名]s/batch', {
      data: { ids },
      ...config
    })
  }
}
```

### 2.3 API 客户端配置

```typescript
// services/apiClient.ts

import axios, { type AxiosInstance, type AxiosRequestConfig } from 'axios'

const baseURL = import.meta.env.VITE_API_BASE_URL || '/api'

const apiClient: AxiosInstance = axios.create({
  baseURL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json'
  }
})

apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

apiClient.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

export { apiClient }
```