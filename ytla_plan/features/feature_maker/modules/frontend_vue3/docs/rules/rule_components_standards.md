# 业务组件层规范文档 - 代码示例 (rule_components_standards.md)

## 概述

本文档专注于提供 `components` 目录下业务组件的编写规范和代码示例。

## 职责说明

`components` 目录负责：
- 实现业务功能的 UI 展示
- 处理用户交互
- 传递数据和事件

## 命名规范

### 组件命名
- **规则**：组件名称使用 PascalCase
- **示例**：`UserCard`, `ProductList`, `OrderForm`

### 文件命名
- **规则**：文件名使用 PascalCase
- **示例**：`UserCard.vue`, `ProductList.vue`

## 代码模板与示例

### 基础组件结构

```vue
<!-- components/UserCard.vue -->

<template>
  <div class="user-card">
    <img v-if="showAvatar" :src="user.avatar" :alt="user.name" />
    <div class="user-info">
      <h3>{{ user.name }}</h3>
      <p>{{ user.email }}</p>
    </div>
    <div class="actions">
      <button @click="handleEdit">Edit</button>
      <button @click="handleDelete">Delete</button>
    </div>
  </div>
</template>

<script setup lang="ts">
// 导入类型定义
import type { IUserCardProps, UserCardEmits } from '../definitions/user-card';

// 导入组合式函数
import { useUserActions } from '../composables/use-user-actions';

// 定义 Props
const props = withDefaults(defineProps<IUserCardProps>(), {
  showAvatar: true,
});

// 定义 Emits
const emit = defineEmits<UserCardEmits>();

// 使用组合式函数
const { handleEdit, handleDelete } = useUserActions(props, emit);
</script>

<style scoped lang="scss">
.user-card {
  padding: 16px;
  border: 1px solid #eee;
  border-radius: 8px;
}
</style>
```

### Props 和 Emits 类型定义

```typescript
// definitions/user-card.ts

import type { IUser } from './user';

export interface IUserCardProps {
  user: IUser;
  showAvatar?: boolean;
  size?: 'small' | 'medium' | 'large';
}

export type UserCardEmits = {
  (e: 'edit', userId: string): void;
  (e: 'delete', userId: string): void;
};
```

### 组合式函数实现

```typescript
// composables/use-user-actions.ts

import type { IUserCardProps, UserCardEmits } from '../definitions/user-card';

interface UseUserActionsOptions {
  emit: (e: keyof UserCardEmits, ...args: any[]) => void;
}

export function useUserActions(props: IUserCardProps, options: UseUserActionsOptions) {
  const { emit } = options;

  function handleEdit() {
    emit('edit', props.user.id);
  }

  function handleDelete() {
    emit('delete', props.user.id);
  }

  return {
    handleEdit,
    handleDelete,
  };
}
```

### 表单组件示例

```vue
<!-- components/LoginForm.vue -->

<template>
  <form @submit.prevent="handleSubmit" class="login-form">
    <div class="form-group">
      <label for="email">Email</label>
      <input
        id="email"
        type="email"
        :value="form.values.email"
        @input="form.setValue('email', ($event.target as HTMLInputElement).value)"
        :class="{ 'has-error': form.errors.email }"
      />
      <span v-if="form.errors.email" class="error">{{ form.errors.email }}</span>
    </div>
    
    <div class="form-group">
      <label for="password">Password</label>
      <input
        id="password"
        type="password"
        :value="form.values.password"
        @input="form.setValue('password', ($event.target as HTMLInputElement).value)"
        :class="{ 'has-error': form.errors.password }"
      />
      <span v-if="form.errors.password" class="error">{{ form.errors.password }}</span>
    </div>

    <button type="submit" :disabled="form.isSubmitting">
      {{ form.isSubmitting ? 'Logging in...' : 'Login' }}
    </button>
  </form>
</template>

<script setup lang="ts">
import type { LoginFormProps, LoginFormEmits } from '../definitions/login-form';
import { useLoginForm } from '../composables/use-login-form';

const props = defineProps<LoginFormProps>();
const emit = defineEmits<LoginFormEmits>();

const form = useLoginForm(props, { emit });
const handleSubmit = () => form.submit();
</script>

<style scoped lang="scss">
.login-form {
  max-width: 400px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 16px;
}

.error {
  color: red;
  font-size: 0.875rem;
}
</style>
```

## 依赖限制

### 允许的依赖
- ✅ `definitions` - 类型定义
- ✅ `composables` - 组合式函数
- ✅ `services` - 服务层
- ✅ UI 元件（ui 目录）

### 禁止的依赖
- ❌ `stores` - 状态管理（应通过 composables 访问）

## 设计原则

### 关注点分离
- Vue 文件仅负责视图
- 逻辑在 composables 中实现
- 样式在 SCSS 文件中

### Props/Emits 规范
- Props 定义在 definitions 中
- Emits 类型定义在 definitions 中
- 使用 withDefaults 提供默认值

### 可复用性
- 将通用逻辑提取到 composables
- 使用 slots 提供内容定制

### 可测试性
- 使用类型定义
- 提供清晰的接口

## 错误模式

### 反模式 1：组件直接访问 stores
```vue
<!-- ❌ 错误 -->
<script setup lang="ts">
import { useUserStore } from '../stores/user-store';
const store = useUserStore();
</script>

<!-- ✅ 正确 -->
<script setup lang="ts">
import { useUser } from '../composables/use-user';
const { user } = useUser();
</script>
```

### 反模式 2：内联逻辑
```vue
<!-- ❌ 错误 - 逻辑在组件中 -->
<script setup lang="ts">
const count = ref(0);
function increment() { count.value++; }
</script>

<!-- ✅ 正确 - 逻辑在 composables 中 -->
<script setup lang="ts">
import { useCounter } from '../composables/use-counter';
const { count, increment } = useCounter();
</script>
```

### 反模式 3：Props 内联定义
```vue
<!-- ❌ 错误 -->
<script setup lang="ts">
defineProps<{
  user: { id: string; name: string };
}>();
</script>

<!-- ✅ 正确 -->
<script setup lang="ts">
import type { IUserCardProps } from '../definitions/user-card';
defineProps<IUserCardProps>();
</script>
```

## 验证清单

- [ ] Props/Emits 类型定义在 definitions 中
- [ ] 使用 `<script setup>` 语法
- [ ] 逻辑在 composables 中实现
- [ ] 样式使用 `<style scoped>`
- [ ] 不直接访问 stores
- [ ] 使用 withDefaults 提供默认值
- [ ] 组件名称 PascalCase
- [ ] 导入顺序符合规范

---

**文档信息**
- 生成时间：2026年5月18日
- 适用场景：YTLA项目业务组件层规范
- 文件位置：rule_components_standards.md