# Policies 代码规范

## 1 依赖限制表

| 功能域类型 | policies可依赖此功能域 | policies可被此功能域依赖 |
| :--- | :--- | :--- |
| definitions | ✓ |  |
| styles |  |  |
| utils |  |  |
| locales |  |  |
| avatar |  |  |
| factories |  |  |
| flows |  |  |
| registries |  |  |
| services |  |  |
| policies | ✓(非自身) |  |
| stores |  |  |
| composables |  |  |
| uis |  |  |
| components |  |  |
| layouts |  |  |

## 2 标准代码格式

以下内容仅供参考，不作为实际项目代码使用.  

### 2.1 策略接口定义

```typescript
// policies/[策略名]Policy.ts

export interface [策略名]Policy<T, R> {
  execute(context: T): R
  validate(context: T): boolean
}

export abstract class BasePolicy<T, R> implements [策略名]Policy<T, R> {
  abstract execute(context: T): R

  validate(context: T): boolean {
    return true
  }
}
```

### 2.2 具体策略实现

```typescript
// policies/validationPolicy.ts

import type { ValidationContext, ValidationResult } from '../definitions'
import { BasePolicy } from './basePolicy'

export class RequiredValidationPolicy extends BasePolicy<ValidationContext, ValidationResult> {
  constructor(private field: string, private message: string = '此字段为必填项') {
    super()
  }

  validate(context: ValidationContext): boolean {
    return context.data[this.field] !== undefined && context.data[this.field] !== null
  }

  execute(context: ValidationContext): ValidationResult {
    const isValid = this.validate(context)
    return {
      field: this.field,
      valid: isValid,
      message: isValid ? '' : this.message
    }
  }
}

export class LengthValidationPolicy extends BasePolicy<ValidationContext, ValidationResult> {
  constructor(
    private field: string,
    private min: number = 0,
    private max: number = Infinity,
    private message: string = '长度不符合要求'
  ) {
    super()
  }

  validate(context: ValidationContext): boolean {
    const value = String(context.data[this.field] || '')
    return value.length >= this.min && value.length <= this.max
  }

  execute(context: ValidationContext): ValidationResult {
    const isValid = this.validate(context)
    return {
      field: this.field,
      valid: isValid,
      message: isValid ? '' : this.message
    }
  }
}

export class EmailValidationPolicy extends BasePolicy<ValidationContext, ValidationResult> {
  constructor(private field: string, private message: string = '邮箱格式不正确') {
    super()
  }

  validate(context: ValidationContext): boolean {
    const value = String(context.data[this.field] || '')
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return emailRegex.test(value)
  }

  execute(context: ValidationContext): ValidationResult {
    const isValid = this.validate(context)
    return {
      field: this.field,
      valid: isValid,
      message: isValid ? '' : this.message
    }
  }
}
```

### 2.3 策略上下文和执行器

```typescript
// policies/policyExecutor.ts

import type { Policy } from './basePolicy'

export class PolicyExecutor<T, R> {
  private policies: Policy<T, R>[] = []

  addPolicy(policy: Policy<T, R>): this {
    this.policies.push(policy)
    return this
  }

  executeAll(context: T): R[] {
    return this.policies.map(policy => policy.execute(context))
  }

  executeUntilFailure(context: T): R | null {
    for (const policy of this.policies) {
      const result = policy.execute(context)
      if (!policy.validate(context)) {
        return result
      }
    }
    return null
  }

  validateAll(context: T): boolean {
    return this.policies.every(policy => policy.validate(context))
  }

  clear(): void {
    this.policies = []
  }
}
```

### 2.4 策略工厂

```typescript
// policies/policyFactory.ts

import type { ValidationPolicyType, ValidationContext, ValidationResult } from '../definitions'
import { RequiredValidationPolicy, LengthValidationPolicy, EmailValidationPolicy } from './validationPolicy'
import { BasePolicy } from './basePolicy'

export class ValidationPolicyFactory {
  static create(
    type: ValidationPolicyType,
    config: Record<string, unknown>
  ): BasePolicy<ValidationContext, ValidationResult> {
    switch (type) {
      case 'required':
        return new RequiredValidationPolicy(
          config.field as string,
          config.message as string
        )
      case 'length':
        return new LengthValidationPolicy(
          config.field as string,
          config.min as number,
          config.max as number,
          config.message as string
        )
      case 'email':
        return new EmailValidationPolicy(
          config.field as string,
          config.message as string
        )
      default:
        throw new Error(`Unknown validation policy type: ${type}`)
    }
  }

  static createMany(
    policies: Array<{ type: ValidationPolicyType; config: Record<string, unknown> }>
  ): BasePolicy<ValidationContext, ValidationResult>[] {
    return policies.map(({ type, config }) => this.create(type, config))
  }
}
```