# 组合式函数层规范文档 - 代码示例 (rule_composables_standards.md)

## 概述

本文档专注于提供 `composables` 目录下组合式函数的编写规范和代码示例。

## 职责说明

`composables` 目录负责：
- 封装可复用的组件逻辑
- 处理组件间共享的业务逻辑
- 提供响应式状态和方法

## 命名规范

### 函数命名
- **规则**：函数名称使用 camelCase，以 `use` 前缀开头
- **示例**：`useUser`, `useForm`, `usePagination`

### 文件命名
- **规则**：文件名使用 kebab-case，以 `use-` 前缀开头
- **示例**：`use-user.ts`, `use-form.ts`

## 代码模板与示例

### 基础组合式函数

```typescript
// composables/use-user.ts

import { ref, computed } from 'vue';
import type { IUser } from '../definitions';
import { userService } from '../services/user-service';

export function useUser() {
  // 响应式状态
  const user = ref<IUser | null>(null);
  const loading = ref(false);
  const error = ref<string | null>(null);

  // 计算属性
  const isLoggedIn = computed(() => !!user.value);

  // 操作方法
  async function fetchUser(userId: string) {
    loading.value = true;
    error.value = null;
    try {
      const response = await userService.getUserById(userId);
      user.value = response.data;
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to fetch user';
    } finally {
      loading.value = false;
    }
  }

  function clearUser() {
    user.value = null;
  }

  // 返回响应式对象
  return {
    // 状态
    user,
    loading,
    error,
    // 计算属性
    isLoggedIn,
    // 方法
    fetchUser,
    clearUser,
  };
}
```

### 带参数的组合式函数

```typescript
// composables/use-form.ts

import { ref, computed, watch } from 'vue';
import type { FormErrors } from '../definitions';

interface UseFormOptions<T> {
  initialValues: T;
  validate?: (values: T) => FormErrors<T>;
}

export function useForm<T extends Record<string, unknown>>({
  initialValues,
  validate,
}: UseFormOptions<T>) {
  // 表单值
  const values = ref<T>({ ...initialValues });
  
  // 表单错误
  const errors = ref<FormErrors<T>>({} as FormErrors<T>);
  
  // 表单状态
  const isSubmitting = ref(false);
  const isDirty = ref(false);

  // 表单是否有效
  const isValid = computed(() => {
    if (validate) {
      const validationErrors = validate(values.value);
      errors.value = validationErrors;
      return Object.keys(validationErrors).length === 0;
    }
    return true;
  });

  // 更新表单值
  function setValue<K extends keyof T>(key: K, value: T[K]) {
    values.value[key] = value;
    isDirty.value = true;
  }

  // 重置表单
  function reset() {
    values.value = { ...initialValues };
    errors.value = {} as FormErrors<T>;
    isDirty.value = false;
  }

  // 提交表单
  async function submit(callback: (values: T) => Promise<void>) {
    isSubmitting.value = true;
    try {
      if (!isValid.value) return;
      await callback(values.value);
      reset();
    } finally {
      isSubmitting.value = false;
    }
  }

  // 监听值变化
  watch(values, () => {
    if (validate) {
      errors.value = validate(values.value);
    }
  }, { deep: true });

  return {
    values,
    errors,
    isSubmitting,
    isDirty,
    isValid,
    setValue,
    reset,
    submit,
  };
}
```

### 状态管理组合式函数

```typescript
// composables/use-cart.ts

import { computed } from 'vue';
import { useCartStore } from '../stores/cart-store';

export function useCart() {
  // 获取 store
  const store = useCartStore();

  // 暴露状态
  const items = computed(() => store.items);
  const totalItems = computed(() => store.totalItems);
  const totalPrice = computed(() => store.totalPrice);

  // 暴露方法
  function addItem(item: { id: string; name: string; price: number; quantity: number }) {
    store.addItem(item);
  }

  function removeItem(itemId: string) {
    store.removeItem(itemId);
  }

  function updateQuantity(itemId: string, quantity: number) {
    store.updateQuantity(itemId, quantity);
  }

  function clearCart() {
    store.clearCart();
  }

  return {
    items,
    totalItems,
    totalPrice,
    addItem,
    removeItem,
    updateQuantity,
    clearCart,
  };
}
```

### 生命周期组合式函数

```typescript
// composables/use-mounted.ts

import { onMounted, onUnmounted } from 'vue';

export function useMounted(callback: () => void) {
  onMounted(callback);
}

export function useUnmounted(callback: () => void) {
  onUnmounted(callback);
}

export function useMountedAsync(callback: () => Promise<void>) {
  onMounted(async () => {
    await callback();
  });
}
```

## 依赖限制

### 允许的依赖
- ✅ `definitions` - 类型定义
- ✅ `services` - 服务层
- ✅ `stores` - 状态管理
- ✅ Vue Composition API

### 禁止的依赖
- ❌ `components` - 组件

## 设计原则

### 单一职责
- 每个组合式函数只做一件事
- 避免在一个函数中处理多个不相关的逻辑

### 可复用性
- 将通用逻辑提取到独立的 composables
- 使用泛型提高灵活性

### 响应式
- 返回响应式状态（ref/computed）
- 保持状态的响应式更新

### 可测试性
- 提供清晰的输入输出
- 使用依赖注入

## 错误模式

### 反模式 1：函数过长
```typescript
// ❌ 错误 - 一个函数处理太多逻辑
export function useEverything() {
  // 用户逻辑...
  // 表单逻辑...
  // 状态逻辑...
}

// ✅ 正确 - 拆分多个小函数
export function useUser() { /* 用户逻辑 */ }
export function useForm() { /* 表单逻辑 */ }
export function useCart() { /* 状态逻辑 */ }
```

### 反模式 2：直接修改状态
```typescript
// ❌ 错误 - 返回 ref 让外部直接修改
export function useCounter() {
  const count = ref(0);
  return { count }; // 外部可以直接 count.value++
}

// ✅ 正确 - 提供修改方法
export function useCounter() {
  const count = ref(0);
  function increment() { count.value++; }
  function decrement() { count.value--; }
  return { count, increment, decrement };
}
```

### 反模式 3：未清理副作用
```typescript
// ❌ 错误 - 没有清理定时器
export function useTimer() {
  const count = ref(0);
  setInterval(() => { count.value++; }, 1000);
  return { count };
}

// ✅ 正确 - 使用 onUnmounted 清理
export function useTimer() {
  const count = ref(0);
  const timer = setInterval(() => { count.value++; }, 1000);
  onUnmounted(() => clearInterval(timer));
  return { count };
}
```

## 验证清单

- [ ] 函数名称以 `use` 前缀开头
- [ ] 文件以 `use-` 前缀开头
- [ ] 返回响应式对象
- [ ] 单一职责
- [ ] 没有循环依赖
- [ ] 清理副作用
- [ ] 使用类型定义
- [ ] 不依赖 components

---

**文档信息**
- 生成时间：2026年5月18日
- 适用场景：YTLA项目组合式函数层规范
- 文件位置：rule_composables_standards.md