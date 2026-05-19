# Definitions 代码规范

## 1 依赖限制表

| 功能域类型 | definitions可依赖此功能域 | definitions可被此功能域依赖 |
| :--- | :--- | :--- |
| definitions | ✓(非自身) |  |
| styles |  |  |
| utils |  |  |
| locales |  |  |
| avatar |  |  |
| factories |  | ✓ |
| flows |  |  |
| registries |  | ✓ |
| services |  | ✓ |
| policies |  | ✓ |
| stores |  | ✓ |
| composables |  | ✓ |
| uis |  | ✓ |
| components |  | ✓ |
| layouts |  | ✓ |

## 2 标准代码格式

---  

以下内容仅供参考，不作为实际项目代码使用.  

---  

### 2.1 Props 类型定义

```typescript
// definitions/[组件名].ts

// 导入其他类型定义（如需要）
import type { IUser } from './user';

// Props 接口定义
// 命名规则：I[组件名]Props，使用 PascalCase，以 I 前缀开头
export interface IComponentProps {
  // 必填属性 - 无默认值
  requiredProp: string;
  
  // 可选属性 - 带默认值
  optionalProp?: boolean;
  
  // 联合类型属性
  variant?: 'primary' | 'secondary' | 'tertiary';
  
  // 数字类型属性
  count?: number;
  
  // 对象类型属性
  data?: IUser;
  
  // 数组类型属性
  items?: string[];
  
  // 函数类型属性（回调函数）
  onCustomEvent?: (value: string) => void;
}
```

### 2.2 Emits 类型定义

```typescript
// definitions/[组件名].ts

// Emits 类型定义
// 命名规则：[组件名]Emits，使用 PascalCase，无 I 前缀
export type ComponentEmits = {
  // 事件名称使用 kebab-case
  (e: 'click', event: MouseEvent): void;
  
  // 带参数的事件
  (e: 'update:model-value', value: string): void;
  
  // 自定义事件
  (e: 'custom-event', payload: { id: string; data: unknown }): void;
  
  // 无参数事件
  (e: 'submit'): void;
};
```

### 2.3 Props 与 Emits 组合定义

```typescript
// definitions/[组件名].ts

// 组合式导出 Props 和 Emits
export interface IButtonProps {
  // 按钮文本
  text: string;
  
  // 按钮尺寸
  size?: 'small' | 'medium' | 'large';
  
  // 是否禁用
  disabled?: boolean;
  
  // 按钮类型
  type?: 'button' | 'submit' | 'reset';
}

export type ButtonEmits = {
  // 点击事件
  (e: 'click', event: MouseEvent): void;
  
  // 鼠标进入事件
  (e: 'mouseenter', event: MouseEvent): void;
  
  // 鼠标离开事件
  (e: 'mouseleave', event: MouseEvent): void;
};

// 统一导出
export type { IButtonProps, ButtonEmits };
```

