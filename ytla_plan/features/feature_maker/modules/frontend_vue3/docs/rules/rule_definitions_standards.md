# 类型定义层规范文档 - 代码示例 (rule_definitions_standards.md)

## 概述

本文档专注于提供 `definitions` 目录下 TypeScript 类型定义的编写规范和代码示例。

## 职责说明

`definitions` 目录负责：
- 定义 TypeScript 类型和接口
- 定义数据结构的 Shape
- 定义函数参数和返回值类型
- 定义组件的 Props 和 Emits 类型

## 命名规范

### 接口命名
- **规则**：接口名称以 `I` 前缀开头，使用 PascalCase
- **示例**：`IUser`, `IUserCardProps`, `IButtonEmits`

### 类型命名
- **规则**：类型名称使用 PascalCase，不加前缀
- **示例**：`UserStatus`, `ButtonVariant`, `LoadingState`

### 文件命名
- **规则**：文件名使用 kebab-case
- **示例**：`user.ts`, `user-card.ts`, `button-props.ts`

## 代码模板与示例

### 基础接口定义

```typescript
// definitions/user.ts

// 接口定义示例
export interface IUser {
  id: string;
  name: string;
  email: string;
  createdAt: Date;
  status: UserStatus;
}

// 联合类型定义
export type UserStatus = 'active' | 'inactive' | 'pending';

// 类型别名
export type UserId = string;
export type Email = string;
```

### 组件 Props 类型定义

```typescript
// definitions/user-card.ts

// 导入基础类型
import type { IUser } from './user';

// Props 接口
export interface IUserCardProps {
  user: IUser;
  showAvatar?: boolean;
  size?: 'small' | 'medium' | 'large';
}

// Emits 类型
export type UserCardEmits = {
  (e: 'edit', userId: string): void;
  (e: 'delete', userId: string): void;
};
```

### 复杂类型定义

```typescript
// definitions/api.ts

// API 响应类型
export interface IApiResponse<T = unknown> {
  data: T;
  status: number;
  message?: string;
  timestamp: Date;
}

// 分页响应类型
export interface IPaginatedResponse<T = unknown> {
  data: T[];
  total: number;
  page: number;
  limit: number;
  hasNext: boolean;
  hasPrev: boolean;
}

// 错误响应类型
export interface IErrorResponse {
  error: string;
  code: number;
  details?: Record<string, string[]>;
}
```

### 状态管理类型定义

```typescript
// definitions/store.ts

// 异步状态三元组
export interface IAsyncState<T = unknown> {
  data: T | null;
  loading: boolean;
  error: string | null;
}

// Store 状态类型
export interface IUserStoreState {
  currentUser: IUser | null;
  users: IUser[];
  fetchStatus: IAsyncState<IUser[]>;
}
```

### 函数参数类型定义

```typescript
// definitions/functions.ts

// 分页查询参数
export interface IPaginationParams {
  page?: number;
  limit?: number;
  sortBy?: string;
  sortOrder?: 'asc' | 'desc';
}

// 查询过滤器
export interface IFilterOptions {
  search?: string;
  status?: string[];
  dateRange?: {
    start: Date;
    end: Date;
  };
}
```

## 类型导入规范

### 核心规则
1. **类型优先**：使用 `import type` 导入纯类型
2. **绝对导入**：跨模块使用 `@/` 前缀
3. **相对导入**：同模块使用同级目录 `./` 前缀
4. **路径限制**：相对路径不超过两层

### 导入顺序
```typescript
// definitions/user-card.ts

// 1. 第三方库类型（如有）
import type { Ref } from 'vue';

// 2. 绝对路径导入 - 跨模块类型
import type { IUser } from '@/definitions/user';

// 3. 相对路径导入 - 同模块类型
import type { IAsyncState } from './store';
```

## 设计原则

### 单一职责
- 每个文件只定义相关的类型
- 避免在一个文件中定义过多不相关的类型

### 可复用性
- 将通用类型提取到独立文件
- 使用泛型提高类型灵活性

### 可扩展性
- 使用接口而非类型别名定义复杂结构
- 预留扩展点使用可选属性

### 类型安全
- 避免使用 `any` 类型
- 使用严格的类型定义

## 错误模式

### 反模式 1：使用 any 类型
```typescript
// ❌ 错误
export interface IUser {
  data: any;
}

// ✅ 正确
export interface IUser {
  id: string;
  name: string;
}
```

### 反模式 2：内联类型定义
```typescript
// ❌ 错误 - 在组件中内联定义
<script setup lang="ts">
defineProps<{
  user: { id: string; name: string };
}>();
</script>

// ✅ 正确 - 提取到 definitions
import type { IUser } from '../definitions/user';
defineProps<{ user: IUser }>();
```

### 反模式 3：类型重复定义
```typescript
// ❌ 错误 - 重复定义相同类型
// file1.ts
interface IUser { id: string; }

// file2.ts  
interface IUser { id: string; name: string; }

// ✅ 正确 - 统一定义
// definitions/user.ts
export interface IUser { id: string; name: string; }
```

## 验证清单

- [ ] 接口名称以 `I` 前缀开头
- [ ] 文件命名使用 kebab-case
- [ ] 使用 `import type` 导入类型
- [ ] 避免使用 `any` 类型
- [ ] 复杂类型使用接口而非类型别名
- [ ] 泛型类型正确使用
- [ ] 导入顺序符合规范
- [ ] 没有重复的类型定义

---

**文档信息**
- 生成时间：2026年5月18日
- 适用场景：YTLA项目类型定义层规范
- 文件位置：rule_definitions_standards.md