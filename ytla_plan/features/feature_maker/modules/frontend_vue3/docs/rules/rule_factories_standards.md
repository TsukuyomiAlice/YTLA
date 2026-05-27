# 工厂模式层规范文档 - 代码示例 (rule_factories_standards.md)

## 概述

本文档专注于提供 `factories` 目录下工厂模式的编写规范和代码示例。

## 职责说明

`factories` 目录负责：
- 实现工厂模式创建对象
- 封装对象创建逻辑
- 提供统一的创建接口
- 支持依赖注入

## 命名规范

### 文件命名
- **规则**：文件名使用 kebab-case，以 `-factory` 后缀结尾
- **示例**：`user-factory.ts`, `product-factory.ts`, `api-client-factory.ts`

### 类命名
- **规则**：使用 PascalCase，以 `Factory` 后缀结尾
- **示例**：`UserFactory`, `ProductFactory`, `ApiClientFactory`

### 方法命名
- **规则**：使用 camelCase，以 `create` 前缀开头
- **示例**：`create`, `createDefault`, `createFromData`

## 代码模板与示例

### 基础工厂类

```typescript
// factories/user-factory.ts

import type { IUser, UserStatus } from '../definitions';

export class UserFactory {
  static create(id: string, name: string, email: string): IUser {
    return {
      id,
      name,
      email,
      status: 'active' as UserStatus,
      createdAt: new Date(),
      updatedAt: new Date(),
    };
  }

  static createDefault(): IUser {
    return {
      id: '',
      name: '',
      email: '',
      status: 'active' as UserStatus,
      createdAt: new Date(),
      updatedAt: new Date(),
    };
  }

  static createFromData(data: Partial<IUser>): IUser {
    const now = new Date();
    return {
      id: data.id ?? '',
      name: data.name ?? '',
      email: data.email ?? '',
      status: data.status ?? ('active' as UserStatus),
      createdAt: data.createdAt ?? now,
      updatedAt: data.updatedAt ?? now,
    };
  }

  static createList(count: number): IUser[] {
    const users: IUser[] = [];
    for (let i = 0; i < count; i++) {
      users.push(this.create(
        `user-${i}`,
        `User ${i}`,
        `user${i}@example.com`
      ));
    }
    return users;
  }
}
```

### 带依赖的工厂类

```typescript
// factories/api-client-factory.ts

import type { AxiosInstance } from 'axios';
import axios from 'axios';

interface ApiClientConfig {
  baseURL: string;
  timeout?: number;
  headers?: Record<string, string>;
}

export class ApiClientFactory {
  private static instances = new Map<string, AxiosInstance>();

  static create(config: ApiClientConfig): AxiosInstance {
    const key = config.baseURL;
    
    if (this.instances.has(key)) {
      return this.instances.get(key)!;
    }

    const instance = axios.create({
      baseURL: config.baseURL,
      timeout: config.timeout ?? 10000,
      headers: {
        'Content-Type': 'application/json',
        ...config.headers,
      },
    });

    this.instances.set(key, instance);
    return instance;
  }

  static get(baseURL: string): AxiosInstance | undefined {
    return this.instances.get(baseURL);
  }

  static destroy(baseURL: string): void {
    this.instances.delete(baseURL);
  }
}
```

### 抽象工厂模式

```typescript
// factories/notification-factory.ts

import type { INotification, NotificationType } from '../definitions';

interface NotificationConfig {
  type: NotificationType;
  title: string;
  message: string;
  duration?: number;
}

export abstract class NotificationFactory {
  abstract create(config: NotificationConfig): INotification;

  static createByType(config: NotificationConfig): INotification {
    switch (config.type) {
      case 'success':
        return SuccessNotificationFactory.create(config);
      case 'error':
        return ErrorNotificationFactory.create(config);
      case 'warning':
        return WarningNotificationFactory.create(config);
      case 'info':
      default:
        return InfoNotificationFactory.create(config);
    }
  }
}

class SuccessNotificationFactory extends NotificationFactory {
  static create(config: NotificationConfig): INotification {
    return {
      id: `success-${Date.now()}`,
      type: 'success',
      title: config.title,
      message: config.message,
      duration: config.duration ?? 3000,
      icon: 'check-circle',
    };
  }
}

class ErrorNotificationFactory extends NotificationFactory {
  static create(config: NotificationConfig): INotification {
    return {
      id: `error-${Date.now()}`,
      type: 'error',
      title: config.title,
      message: config.message,
      duration: config.duration ?? 5000,
      icon: 'x-circle',
    };
  }
}

class WarningNotificationFactory extends NotificationFactory {
  static create(config: NotificationConfig): INotification {
    return {
      id: `warning-${Date.now()}`,
      type: 'warning',
      title: config.title,
      message: config.message,
      duration: config.duration ?? 4000,
      icon: 'alert-triangle',
    };
  }
}

class InfoNotificationFactory extends NotificationFactory {
  static create(config: NotificationConfig): INotification {
    return {
      id: `info-${Date.now()}`,
      type: 'info',
      title: config.title,
      message: config.message,
      duration: config.duration ?? 3000,
      icon: 'info-circle',
    };
  }
}
```

## 依赖限制

### 允许的依赖
- ✅ `definitions` - 类型定义
- ✅ `services` - 服务层（用于创建带依赖的对象）
- ✅ 其他 factory 文件

### 禁止的依赖
- ❌ `components` - 组件
- ❌ `stores` - 状态管理
- ❌ `composables` - 组合式函数

## 设计原则

### 封装创建逻辑
- 将对象创建逻辑封装在工厂类中
- 对外提供简单的创建接口

### 单一职责
- 每个工厂类只负责创建一种类型的对象
- 避免在一个工厂中创建多种不相关的对象

### 可扩展性
- 支持通过继承扩展工厂
- 支持配置化创建

### 缓存机制
- 对于昂贵的对象创建，提供缓存支持
- 避免重复创建相同配置的对象

## 错误模式

### 反模式 1：直接 new 对象
```typescript
// ❌ 错误
const user = { id: '1', name: 'John', email: 'john@example.com' };

// ✅ 正确
const user = UserFactory.create('1', 'John', 'john@example.com');
```

### 反模式 2：硬编码创建逻辑
```typescript
// ❌ 错误
function createUser(data: any) {
  return {
    id: data.id,
    name: data.name,
    status: 'active',
  };
}

// ✅ 正确
class UserFactory {
  static createFromData(data: Partial<IUser>): IUser {
    return {
      id: data.id ?? '',
      name: data.name ?? '',
      status: data.status ?? 'active',
    };
  }
}
```

### 反模式 3：不处理默认值
```typescript
// ❌ 错误
create(data: Partial<IUser>) {
  return { ...data }; // 缺少必需字段
}

// ✅ 正确
create(data: Partial<IUser>) {
  return {
    id: data.id ?? generateId(),
    name: data.name ?? '',
    createdAt: data.createdAt ?? new Date(),
    ...data,
  };
}
```

## 验证清单

- [ ] 使用类封装创建逻辑
- [ ] 文件命名使用 kebab-case，以 `-factory` 后缀结尾
- [ ] 提供 `create` 方法
- [ ] 处理默认值
- [ ] 使用类型定义
- [ ] 不依赖业务层组件
- [ ] 支持配置化创建
- [ ] 提供静态工厂方法

---

**文档信息**
- 生成时间：2026年5月18日
- 适用场景：YTLA项目工厂模式层规范
- 文件位置：rule_factories_standards.md