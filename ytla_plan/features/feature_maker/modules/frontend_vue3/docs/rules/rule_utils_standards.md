# 工具函数层规范文档 - 代码示例 (rule_utils_standards.md)

## 概述

本文档专注于提供 `utils` 目录下工具函数的编写规范和代码示例。

## 职责说明

`utils` 目录负责：
- 提供通用工具函数
- 封装常用算法
- 处理数据转换和格式化
- 提供业务无关的辅助函数

## 命名规范

### 文件命名
- **规则**：文件名使用 kebab-case
- **示例**：`string-utils.ts`, `date-utils.ts`, `validation-utils.ts`

### 函数命名
- **规则**：函数名称使用 camelCase
- **示例**：`formatDate`, `validateEmail`, `debounce`

### 常量命名
- **规则**：常量名称使用 UPPER_CASE，单词间用下划线分隔
- **示例**：`MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT`

## 代码模板与示例

### 字符串工具函数

```typescript
// utils/string-utils.ts

/**
 * 格式化字符串，替换占位符
 * @param template - 包含占位符的模板字符串
 * @param data - 替换数据对象
 * @returns 格式化后的字符串
 */
export function formatString(template: string, data: Record<string, unknown>): string {
  return template.replace(/\{\{(\w+)\}\}/g, (_, key) => {
    return String(data[key] ?? '');
  });
}

/**
 * 生成随机字符串
 * @param length - 字符串长度
 * @returns 随机字符串
 */
export function generateRandomString(length: number): string {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let result = '';
  for (let i = 0; i < length; i++) {
    result += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return result;
}

/**
 * 截断字符串并添加省略号
 * @param str - 原始字符串
 * @param maxLength - 最大长度
 * @returns 截断后的字符串
 */
export function truncateString(str: string, maxLength: number): string {
  if (str.length <= maxLength) return str;
  return str.slice(0, maxLength) + '...';
}
```

### 日期工具函数

```typescript
// utils/date-utils.ts

/**
 * 格式化日期
 * @param date - 日期对象
 * @param format - 格式字符串
 * @returns 格式化后的日期字符串
 */
export function formatDate(date: Date, format: string = 'YYYY-MM-DD'): string {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');
  const seconds = String(date.getSeconds()).padStart(2, '0');

  return format
    .replace('YYYY', String(year))
    .replace('MM', month)
    .replace('DD', day)
    .replace('HH', hours)
    .replace('mm', minutes)
    .replace('ss', seconds);
}

/**
 * 计算两个日期之间的天数
 * @param date1 - 第一个日期
 * @param date2 - 第二个日期
 * @returns 天数差
 */
export function daysBetween(date1: Date, date2: Date): number {
  const diffTime = Math.abs(date2.getTime() - date1.getTime());
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  return diffDays;
}

/**
 * 判断是否是今天
 * @param date - 日期对象
 * @returns 是否是今天
 */
export function isToday(date: Date): boolean {
  const today = new Date();
  return (
    date.getDate() === today.getDate() &&
    date.getMonth() === today.getMonth() &&
    date.getFullYear() === today.getFullYear()
  );
}
```

### 验证工具函数

```typescript
// utils/validation-utils.ts

/**
 * 验证邮箱格式
 * @param email - 邮箱地址
 * @returns 是否有效
 */
export function validateEmail(email: string): boolean {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * 验证手机号码
 * @param phone - 手机号码
 * @returns 是否有效
 */
export function validatePhone(phone: string): boolean {
  const phoneRegex = /^1[3-9]\d{9}$/;
  return phoneRegex.test(phone);
}

/**
 * 验证密码强度
 * @param password - 密码
 * @returns 强度等级 (0-4)
 */
export function validatePasswordStrength(password: string): number {
  let score = 0;
  
  if (password.length >= 8) score++;
  if (password.length >= 12) score++;
  if (/[a-z]/.test(password)) score++;
  if (/[A-Z]/.test(password)) score++;
  if (/[0-9]/.test(password)) score++;
  if (/[^a-zA-Z0-9]/.test(password)) score++;
  
  return Math.min(score, 4);
}
```

### 防抖和节流工具函数

```typescript
// utils/debounce.ts

/**
 * 防抖函数
 * @param func - 要执行的函数
 * @param delay - 延迟时间（毫秒）
 * @returns 防抖后的函数
 */
export function debounce<T extends (...args: unknown[]) => void>(
  func: T,
  delay: number
): (...args: Parameters<T>) => void {
  let timeoutId: ReturnType<typeof setTimeout> | null = null;
  
  return (...args: Parameters<T>) => {
    if (timeoutId) {
      clearTimeout(timeoutId);
    }
    timeoutId = setTimeout(() => {
      func(...args);
    }, delay);
  };
}

/**
 * 节流函数
 * @param func - 要执行的函数
 * @param limit - 限制时间（毫秒）
 * @returns 节流后的函数
 */
export function throttle<T extends (...args: unknown[]) => void>(
  func: T,
  limit: number
): (...args: Parameters<T>) => void {
  let inThrottle = false;
  
  return (...args: Parameters<T>) => {
    if (!inThrottle) {
      func(...args);
      inThrottle = true;
      setTimeout(() => (inThrottle = false), limit);
    }
  };
}
```

## 依赖限制

### 允许的依赖
- ✅ TypeScript 标准库
- ✅ 第三方工具库（如 lodash）
- ✅ 其他 utils 文件

### 禁止的依赖
- ❌ `components` - 组件
- ❌ `stores` - 状态管理
- ❌ `services` - 服务层

## 设计原则

### 无副作用
- 工具函数不应产生副作用
- 输入相同，输出应相同

### 单一职责
- 每个函数只做一件事
- 函数长度不超过 50 行

### 可测试性
- 提供清晰的输入输出
- 避免依赖全局状态

### 可复用性
- 通用工具函数应与业务无关
- 使用泛型提高灵活性

## 错误模式

### 反模式 1：包含业务逻辑
```typescript
// ❌ 错误 - 包含业务逻辑
export function formatUserInfo(user: IUser): string {
  return `${user.name} (${user.role})`;
}

// ✅ 正确 - 通用格式化
export function formatNameAndRole(name: string, role: string): string {
  return `${name} (${role})`;
}
```

### 反模式 2：使用 any 类型
```typescript
// ❌ 错误
export function processData(data: any): any {
  // ...
}

// ✅ 正确
export function processData<T>(data: T): T {
  // ...
}
```

### 反模式 3：修改输入参数
```typescript
// ❌ 错误 - 修改输入参数
export function sortArray(arr: number[]): number[] {
  return arr.sort((a, b) => a - b); // 原地排序
}

// ✅ 正确 - 返回新数组
export function sortArray(arr: number[]): number[] {
  return [...arr].sort((a, b) => a - b); // 创建副本
}
```

## 验证清单

- [ ] 函数命名使用 camelCase
- [ ] 文件命名使用 kebab-case
- [ ] 无副作用
- [ ] 单一职责
- [ ] 使用类型定义
- [ ] 不依赖业务层
- [ ] 提供 JSDoc 注释
- [ ] 函数长度不超过 50 行

---

**文档信息**
- 生成时间：2026年5月18日
- 适用场景：YTLA项目工具函数层规范
- 文件位置：rule_utils_standards.md