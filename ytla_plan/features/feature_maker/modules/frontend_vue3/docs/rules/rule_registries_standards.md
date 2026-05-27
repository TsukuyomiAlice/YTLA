# 注册机制层规范文档 - 代码示例 (rule_registries_standards.md)

## 概述

本文档专注于提供 `registries` 目录下注册式加载机制的编写规范和代码示例。

## 职责说明

`registries` 目录负责：
- 提供模块、组件的注册和加载机制
- 实现插件化架构
- 管理动态模块的生命周期
- 提供统一的注册接口

## 命名规范

### 文件命名
- **规则**：文件名使用 kebab-case
- **示例**：`component-registry.ts`, `plugin-registry.ts`, `module-registry.ts`

### 类命名
- **规则**：使用 PascalCase，以 `Registry` 后缀结尾
- **示例**：`ComponentRegistry`, `PluginRegistry`, `ModuleRegistry`

### 方法命名
- **规则**：使用 camelCase
- **示例**：`register`, `unregister`, `get`, `has`, `list`

## 代码模板与示例

### 基础注册类

```typescript
// registries/component-registry.ts

import type { Component } from 'vue';

interface ComponentEntry {
  name: string;
  component: Component;
  options?: Record<string, unknown>;
}

export class ComponentRegistry {
  private components = new Map<string, ComponentEntry>();

  register(name: string, component: Component, options?: Record<string, unknown>): void {
    if (this.components.has(name)) {
      console.warn(`Component "${name}" is already registered`);
      return;
    }
    this.components.set(name, { name, component, options });
  }

  unregister(name: string): void {
    this.components.delete(name);
  }

  get(name: string): Component | undefined {
    const entry = this.components.get(name);
    return entry?.component;
  }

  has(name: string): boolean {
    return this.components.has(name);
  }

  list(): string[] {
    return Array.from(this.components.keys());
  }

  getAll(): ComponentEntry[] {
    return Array.from(this.components.values());
  }
}

export const componentRegistry = new ComponentRegistry();
```

### 插件注册机制

```typescript
// registries/plugin-registry.ts

import type { Plugin } from 'vue';

interface PluginEntry {
  name: string;
  plugin: Plugin;
  priority: number;
  enabled: boolean;
}

export class PluginRegistry {
  private plugins = new Map<string, PluginEntry>();

  register(name: string, plugin: Plugin, priority: number = 0): void {
    if (this.plugins.has(name)) {
      console.warn(`Plugin "${name}" is already registered`);
      return;
    }
    this.plugins.set(name, { name, plugin, priority, enabled: true });
  }

  unregister(name: string): void {
    this.plugins.delete(name);
  }

  enable(name: string): void {
    const entry = this.plugins.get(name);
    if (entry) {
      entry.enabled = true;
    }
  }

  disable(name: string): void {
    const entry = this.plugins.get(name);
    if (entry) {
      entry.enabled = false;
    }
  }

  getEnabledPlugins(): Plugin[] {
    return Array.from(this.plugins.values())
      .filter(entry => entry.enabled)
      .sort((a, b) => a.priority - b.priority)
      .map(entry => entry.plugin);
  }

  list(): string[] {
    return Array.from(this.plugins.keys());
  }
}

export const pluginRegistry = new PluginRegistry();
```

### 模块注册机制

```typescript
// registries/module-registry.ts

interface ModuleConfig {
  name: string;
  routes?: unknown[];
  stores?: string[];
  components?: string[];
  composables?: string[];
}

interface ModuleEntry extends ModuleConfig {
  loaded: boolean;
  dependencies?: string[];
}

export class ModuleRegistry {
  private modules = new Map<string, ModuleEntry>();

  register(config: ModuleConfig, dependencies?: string[]): void {
    if (this.modules.has(config.name)) {
      console.warn(`Module "${config.name}" is already registered`);
      return;
    }
    this.modules.set(config.name, {
      ...config,
      loaded: false,
      dependencies,
    });
  }

  async load(name: string): Promise<void> {
    const module = this.modules.get(name);
    if (!module) {
      throw new Error(`Module "${name}" not found`);
    }

    if (module.loaded) {
      return;
    }

    if (module.dependencies) {
      for (const dep of module.dependencies) {
        await this.load(dep);
      }
    }

    module.loaded = true;
    console.log(`Module "${name}" loaded successfully`);
  }

  isLoaded(name: string): boolean {
    return this.modules.get(name)?.loaded ?? false;
  }

  list(): string[] {
    return Array.from(this.modules.keys());
  }

  getConfig(name: string): ModuleConfig | undefined {
    const module = this.modules.get(name);
    if (!module) return undefined;
    const { loaded, dependencies, ...config } = module;
    return config;
  }
}

export const moduleRegistry = new ModuleRegistry();
```

## 依赖限制

### 允许的依赖
- ✅ `definitions` - 类型定义
- ✅ Vue 核心库
- ✅ 其他 registry 文件

### 禁止的依赖
- ❌ `components` - 组件
- ❌ `stores` - 状态管理（除非通过注册机制加载）
- ❌ `services` - 服务层

## 设计原则

### 单一职责
- 每个注册类只负责一种类型的注册管理
- 避免在一个注册类中管理多种类型

### 插件化
- 支持动态注册和卸载
- 支持启用/禁用状态

### 可扩展性
- 提供统一的注册接口
- 支持优先级排序

### 生命周期管理
- 跟踪模块加载状态
- 处理依赖关系

## 错误模式

### 反模式 1：硬编码依赖
```typescript
// ❌ 错误
import { UserModule } from '../modules/user';

// ✅ 正确
moduleRegistry.register({ name: 'user' });
await moduleRegistry.load('user');
```

### 反模式 2：全局变量管理
```typescript
// ❌ 错误
export const components: Record<string, Component> = {};

// ✅ 正确
export class ComponentRegistry {
  private components = new Map<string, Component>();
}
```

### 反模式 3：不处理重复注册
```typescript
// ❌ 错误
register(name: string, component: Component) {
  this.components[name] = component;
}

// ✅ 正确
register(name: string, component: Component) {
  if (this.components.has(name)) {
    console.warn(`Component "${name}" is already registered`);
    return;
  }
  this.components.set(name, component);
}
```

## 验证清单

- [ ] 使用类封装注册逻辑
- [ ] 文件命名使用 kebab-case
- [ ] 提供 register/unregister 方法
- [ ] 处理重复注册
- [ ] 不依赖业务层
- [ ] 支持动态加载
- [ ] 处理依赖关系
- [ ] 使用类型定义

---

**文档信息**
- 生成时间：2026年5月18日
- 适用场景：YTLA项目注册机制层规范
- 文件位置：rule_registries_standards.md