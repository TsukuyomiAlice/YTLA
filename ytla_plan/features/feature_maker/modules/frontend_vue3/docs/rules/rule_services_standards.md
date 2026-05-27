# 服务层规范文档 - 代码示例 (rule_services_standards.md)

## 概述

本文档专注于提供 `services` 目录下后端服务调用的编写规范和代码示例。

## 职责说明

`services` 目录负责：
- 封装后端 API 调用
- 处理 HTTP 请求/响应
- 统一错误处理
- 数据格式转换

## 命名规范

### 类命名
- **规则**：类名称使用 PascalCase，以 `Service` 后缀结尾
- **示例**：`UserService`, `ProductService`, `AuthService`

### 文件命名
- **规则**：文件名使用 kebab-case，以 `-service` 后缀结尾
- **示例**：`user-service.ts`, `product-service.ts`

### 方法命名
- **规则**：方法名称使用 camelCase
- **示例**：`getUserById`, `createProduct`, `updateUser`

## 代码模板与示例

### 基础服务类

```typescript
// services/user-service.ts

// 导入类型定义
import type { IUser, IApiResponse, IErrorResponse } from '../definitions';

// 服务类
export class UserService {
  private baseUrl = '/api/users';

  // 获取用户列表
  async getUsers(): Promise<IApiResponse<IUser[]>> {
    const response = await fetch(this.baseUrl);
    return response.json();
  }

  // 根据ID获取用户
  async getUserById(id: string): Promise<IApiResponse<IUser>> {
    const response = await fetch(`${this.baseUrl}/${id}`);
    return response.json();
  }

  // 创建用户
  async createUser(user: Omit<IUser, 'id'>): Promise<IApiResponse<IUser>> {
    const response = await fetch(this.baseUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(user),
    });
    return response.json();
  }

  // 更新用户
  async updateUser(id: string, user: Partial<IUser>): Promise<IApiResponse<IUser>> {
    const response = await fetch(`${this.baseUrl}/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(user),
    });
    return response.json();
  }

  // 删除用户
  async deleteUser(id: string): Promise<IApiResponse<void>> {
    const response = await fetch(`${this.baseUrl}/${id}`, {
      method: 'DELETE',
    });
    return response.json();
  }
}

// 导出单例实例
export const userService = new UserService();
```

### 统一错误处理

```typescript
// services/base-service.ts

import type { IErrorResponse } from '../definitions';

export abstract class BaseService {
  protected baseUrl = '/api';

  protected async handleResponse<T>(response: Response): Promise<T> {
    const data = await response.json();

    if (!response.ok) {
      const error = data as IErrorResponse;
      throw new Error(error.message || `Request failed with status ${response.status}`);
    }

    return data;
  }

  protected getHeaders(): Headers {
    const headers = new Headers({
      'Content-Type': 'application/json',
    });

    const token = localStorage.getItem('token');
    if (token) {
      headers.set('Authorization', `Bearer ${token}`);
    }

    return headers;
  }
}
```

### 使用 BaseService 的服务类

```typescript
// services/product-service.ts

import type { IProduct } from '../definitions';
import { BaseService } from './base-service';

export class ProductService extends BaseService {
  private endpoint = '/products';

  async getProducts(): Promise<IProduct[]> {
    const response = await fetch(`${this.baseUrl}${this.endpoint}`, {
      headers: this.getHeaders(),
    });
    return this.handleResponse<IProduct[]>(response);
  }

  async getProductById(id: string): Promise<IProduct> {
    const response = await fetch(`${this.baseUrl}${this.endpoint}/${id}`, {
      headers: this.getHeaders(),
    });
    return this.handleResponse<IProduct>(response);
  }
}

export const productService = new ProductService();
```

### 分页查询服务

```typescript
// services/order-service.ts

import type { IOrder, IPaginatedResponse, IPaginationParams } from '../definitions';
import { BaseService } from './base-service';

export class OrderService extends BaseService {
  private endpoint = '/orders';

  async getOrders(params?: IPaginationParams): Promise<IPaginatedResponse<IOrder>> {
    const url = new URL(`${this.baseUrl}${this.endpoint}`);
    
    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined) {
          url.searchParams.set(key, String(value));
        }
      });
    }

    const response = await fetch(url.toString(), {
      headers: this.getHeaders(),
    });
    return this.handleResponse<IPaginatedResponse<IOrder>>(response);
  }
}

export const orderService = new OrderService();
```

## 依赖限制

### 允许的依赖
- ✅ `definitions` - 类型定义
- ✅ 第三方 HTTP 库（如 axios）
- ✅ 工具函数

### 禁止的依赖
- ❌ `stores` - 状态管理
- ❌ `components` - 组件
- ❌ `composables` - 组合式函数

## 设计原则

### 单一职责
- 每个服务类只负责一个资源
- 避免在服务中处理业务逻辑

### 可测试性
- 使用依赖注入
- 提供 mock 接口

### 错误处理
- 统一错误格式
- 提供错误日志

### 可配置性
- 使用环境变量配置
- 支持多种环境

## 错误模式

### 反模式 1：服务层访问 stores
```typescript
// ❌ 错误
import { useUserStore } from '../stores/user-store';

export async function fetchUser() {
  const store = useUserStore();
  const data = await api.get('/user');
  store.setUser(data);
}

// ✅ 正确
export async function fetchUser(): Promise<IUser> {
  const response = await api.get('/user');
  return response.data;
}
```

### 反模式 2：内联 API 调用
```typescript
// ❌ 错误 - 在组件中直接调用
<script setup lang="ts">
const fetchUser = async () => {
  const res = await fetch('/api/users');
  return res.json();
};
</script>

// ✅ 正确 - 提取到服务层
import { userService } from '../services/user-service';
const users = await userService.getUsers();
```

### 反模式 3：重复的错误处理
```typescript
// ❌ 错误 - 每个方法重复错误处理
async getUser() {
  try {
    const res = await fetch('/api/users');
    if (!res.ok) throw new Error('Failed');
    return res.json();
  } catch (e) {
    console.error(e);
    throw e;
  }
}

// ✅ 正确 - 使用 BaseService 统一处理
async getUser() {
  const response = await fetch('/api/users');
  return this.handleResponse(response);
}
```

## 验证清单

- [ ] 服务类以 `Service` 后缀结尾
- [ ] 文件以 `-service` 后缀结尾
- [ ] 方法返回 Promise
- [ ] 统一错误处理
- [ ] 不依赖 stores 或 components
- [ ] 使用类型定义
- [ ] 导出单例实例
- [ ] 使用 BaseService 基类

---

**文档信息**
- 生成时间：2026年5月18日
- 适用场景：YTLA项目服务层规范
- 文件位置：rule_services_standards