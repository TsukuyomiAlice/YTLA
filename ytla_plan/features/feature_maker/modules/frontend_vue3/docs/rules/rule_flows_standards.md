# 流程管理层规范文档 - 代码示例 (rule_flows_standards.md)

## 概述

本文档专注于提供 `flows` 目录下流程管理的编写规范和代码示例。

## 职责说明

`flows` 目录负责：
- 管理页面流程和状态转换
- 实现向导式表单流程
- 处理多步骤操作流程
- 提供流程状态管理

## 命名规范

### 文件命名
- **规则**：文件名使用 kebab-case，以 `-flow` 后缀结尾
- **示例**：`setup-flow.ts`, `checkout-flow.ts`, `wizard-flow.ts`

### 类命名
- **规则**：使用 PascalCase，以 `Flow` 后缀结尾
- **示例**：`SetupFlow`, `CheckoutFlow`, `WizardFlow`

### 步骤命名
- **规则**：使用 camelCase，以 `step` 前缀开头
- **示例**：`step1`, `step2`, `stepPersonalInfo`

## 代码模板与示例

### 基础流程类

```typescript
// flows/wizard-flow.ts

import { ref, computed } from 'vue';

export interface StepConfig {
  id: string;
  name: string;
  component: string;
  validate?: () => boolean;
}

export class WizardFlow {
  private steps: StepConfig[] = [];
  private currentIndex = ref(0);
  private completedSteps = new Set<string>();

  constructor(steps: StepConfig[]) {
    this.steps = steps;
  }

  currentStep = computed(() => this.steps[this.currentIndex.value]);
  isFirstStep = computed(() => this.currentIndex.value === 0);
  isLastStep = computed(() => this.currentIndex.value === this.steps.length - 1);
  progress = computed(() => ((this.currentIndex.value + 1) / this.steps.length) * 100);

  next(): boolean {
    if (this.isLastStep.value) return false;
    
    const currentStep = this.currentStep.value;
    if (currentStep.validate && !currentStep.validate()) {
      return false;
    }

    this.completedSteps.add(currentStep.id);
    this.currentIndex.value++;
    return true;
  }

  previous(): boolean {
    if (this.isFirstStep.value) return false;
    this.currentIndex.value--;
    return true;
  }

  goTo(stepId: string): boolean {
    const index = this.steps.findIndex(step => step.id === stepId);
    if (index === -1) return false;
    
    for (let i = 0; i < index; i++) {
      if (!this.completedSteps.has(this.steps[i].id)) {
        return false;
      }
    }
    
    this.currentIndex.value = index;
    return true;
  }

  reset(): void {
    this.currentIndex.value = 0;
    this.completedSteps.clear();
  }

  getCompletedSteps(): string[] {
    return Array.from(this.completedSteps);
  }

  getAllSteps(): StepConfig[] {
    return [...this.steps];
  }
}
```

### 状态机流程

```typescript
// flows/checkout-flow.ts

type CheckoutState = 'cart' | 'shipping' | 'payment' | 'review' | 'complete';

type CheckoutAction = 
  | { type: 'GO_TO_SHIPPING' }
  | { type: 'GO_TO_PAYMENT' }
  | { type: 'GO_TO_REVIEW' }
  | { type: 'GO_TO_COMPLETE' }
  | { type: 'GO_BACK' }
  | { type: 'RESET' };

interface CheckoutContext {
  cartItems: unknown[];
  shippingInfo: unknown;
  paymentInfo: unknown;
}

export class CheckoutFlow {
  private state: CheckoutState = 'cart';
  private context: CheckoutContext = {
    cartItems: [],
    shippingInfo: null,
    paymentInfo: null,
  };

  private transitions: Record<CheckoutState, Record<string, CheckoutState>> = {
    cart: { GO_TO_SHIPPING: 'shipping' },
    shipping: { GO_TO_PAYMENT: 'payment', GO_BACK: 'cart' },
    payment: { GO_TO_REVIEW: 'review', GO_BACK: 'shipping' },
    review: { GO_TO_COMPLETE: 'complete', GO_BACK: 'payment' },
    complete: { RESET: 'cart' },
  };

  getState(): CheckoutState {
    return this.state;
  }

  getContext(): CheckoutContext {
    return { ...this.context };
  }

  dispatch(action: CheckoutAction): CheckoutState {
    const currentTransitions = this.transitions[this.state];
    const nextState = currentTransitions[action.type];

    if (!nextState) {
      console.warn(`Invalid action "${action.type}" for state "${this.state}"`);
      return this.state;
    }

    switch (action.type) {
      case 'GO_TO_SHIPPING':
        if (this.context.cartItems.length === 0) {
          console.warn('Cart is empty');
          return this.state;
        }
        break;
      case 'GO_TO_PAYMENT':
        if (!this.context.shippingInfo) {
          console.warn('Shipping info is required');
          return this.state;
        }
        break;
      case 'GO_TO_REVIEW':
        if (!this.context.paymentInfo) {
          console.warn('Payment info is required');
          return this.state;
        }
        break;
      case 'RESET':
        this.context = {
          cartItems: [],
          shippingInfo: null,
          paymentInfo: null,
        };
        break;
    }

    this.state = nextState;
    return this.state;
  }

  updateContext(updates: Partial<CheckoutContext>): void {
    this.context = { ...this.context, ...updates };
  }
}
```

### 异步流程管理

```typescript
// flows/setup-flow.ts

import { ref } from 'vue';

export interface SetupStep {
  id: string;
  title: string;
  description: string;
  action: () => Promise<void>;
  skip?: () => boolean;
}

export interface SetupState {
  currentStep: number;
  steps: SetupStep[];
  completed: string[];
  errors: Record<string, string>;
  isRunning: boolean;
}

export class SetupFlow {
  private state = ref<SetupState>({
    currentStep: 0,
    steps: [],
    completed: [],
    errors: {},
    isRunning: false,
  });

  constructor(steps: SetupStep[]) {
    this.state.value.steps = steps;
  }

  getState() {
    return this.state.value;
  }

  async run(): Promise<void> {
    this.state.value.isRunning = true;
    this.state.value.errors = {};

    for (let i = 0; i < this.state.value.steps.length; i++) {
      const step = this.state.value.steps[i];
      this.state.value.currentStep = i;

      if (step.skip && step.skip()) {
        this.state.value.completed.push(step.id);
        continue;
      }

      try {
        await step.action();
        this.state.value.completed.push(step.id);
      } catch (error) {
        this.state.value.errors[step.id] = error instanceof Error ? error.message : 'Unknown error';
        this.state.value.isRunning = false;
        throw error;
      }
    }

    this.state.value.isRunning = false;
  }

  async runStep(stepId: string): Promise<void> {
    const step = this.state.value.steps.find(s => s.id === stepId);
    if (!step) {
      throw new Error(`Step "${stepId}" not found`);
    }

    try {
      await step.action();
      if (!this.state.value.completed.includes(stepId)) {
        this.state.value.completed.push(stepId);
      }
    } catch (error) {
      this.state.value.errors[stepId] = error instanceof Error ? error.message : 'Unknown error';
      throw error;
    }
  }

  reset(): void {
    this.state.value = {
      currentStep: 0,
      steps: this.state.value.steps,
      completed: [],
      errors: {},
      isRunning: false,
    };
  }
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

### 状态管理
- 使用状态机管理流程状态
- 定义清晰的状态转换规则

### 可验证性
- 每个步骤可以有验证逻辑
- 提供错误处理机制

### 可扩展性
- 支持动态添加步骤
- 支持跳过某些步骤

### 异步支持
- 支持异步操作
- 提供加载状态

## 错误模式

### 反模式 1：硬编码步骤顺序
```typescript
// ❌ 错误
if (currentStep === 1) {
  goToStep(2);
}

// ✅ 正确
class WizardFlow {
  private steps: StepConfig[] = [];
  next() {
    if (this.currentIndex < this.steps.length - 1) {
      this.currentIndex++;
    }
  }
}
```

### 反模式 2：不处理错误
```typescript
// ❌ 错误
async runStep() {
  await someAsyncOperation();
}

// ✅ 正确
async runStep() {
  try {
    await someAsyncOperation();
  } catch (error) {
    this.errors[stepId] = error.message;
    throw error;
  }
}
```

### 反模式 3：共享可变状态
```typescript
// ❌ 错误
let currentStep = 0;

// ✅ 正确
class Flow {
  private currentStep = ref(0);
}
```

## 验证清单

- [ ] 使用类封装流程逻辑
- [ ] 文件命名使用 kebab-case，以 `-flow` 后缀结尾
- [ ] 定义清晰的状态转换规则
- [ ] 提供前进/后退方法
- [ ] 支持步骤验证
- [ ] 处理错误和异常
- [ ] 使用类型定义
- [ ] 不依赖组件

---

**文档信息**
- 生成时间：2026年5月18日
- 适用场景：YTLA项目流程管理层规范
- 文件位置：rule_flows_standards.md