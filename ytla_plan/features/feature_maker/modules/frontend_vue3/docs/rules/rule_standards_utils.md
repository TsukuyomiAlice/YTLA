# Utils 代码规范

## 1 依赖限制表

| 功能域类型 | utils可依赖此功能域 | utils可被此功能域依赖 |
| :--- | :--- | :--- |
| definitions |  |  |
| styles |  |  |
| utils |  |  |
| locales |  |  |
| avatar |  |  |
| factories |  |  |
| flows |  |  |
| registries |  |  |
| services |  | ✓ |
| policies |  |  |
| stores |  |  |
| composables |  |  |
| uis |  |  |
| components |  |  |
| layouts |  |  |

## 2 标准代码格式

---  

以下内容仅供参考，不作为实际项目代码使用.  

---  

### 2.1 配置常量文件

```typescript
// utils/config.ts

/**
 * 模块配置常量
 * 用于存储模块相关的配置参数和常量值
 */

// 模块基础配置
export const MODULE_CONFIG = {
  // 模块名称
  moduleName: 'default',
  
  // 模块描述
  moduleDescription: '',
  
  // 是否启用
  enabled: true,
  
  // 优先级
  priority: 100,
};

// API 配置
export const API_CONFIG = {
  // 基础 URL
  baseUrl: '/api',
  
  // 请求超时时间（毫秒）
  timeout: 30000,
  
  // 最大重试次数
  maxRetries: 3,
  
  // 请求间隔（毫秒）
  retryDelay: 1000,
};

// 缓存配置
export const CACHE_CONFIG = {
  // 缓存过期时间（秒）
  expiresIn: 3600,
  
  // 是否启用缓存
  enabled: true,
  
  // 缓存键前缀
  keyPrefix: 'app_',
};

// 日志配置
export const LOG_CONFIG = {
  // 是否启用日志
  enabled: true,
  
  // 日志级别: debug, info, warn, error
  level: 'info',
  
  // 是否输出到控制台
  consoleEnabled: true,
};

// 路由配置
export const ROUTE_CONFIG = {
  // 默认路由
  defaultRoute: '/',
  
  // 登录路由
  loginRoute: '/login',
  
  // 404路由
  notFoundRoute: '/404',
};

// 分页配置
export const PAGINATION_CONFIG = {
  // 默认每页条数
  defaultPageSize: 20,
  
  // 可选每页条数
  pageSizes: [10, 20, 50, 100],
  
  // 最大每页条数
  maxPageSize: 100,
};

// 日期格式配置
export const DATE_FORMAT_CONFIG = {
  // 日期格式
  date: 'YYYY-MM-DD',
  
  // 日期时间格式
  datetime: 'YYYY-MM-DD HH:mm:ss',
  
  // 时间格式
  time: 'HH:mm:ss',
};
```

### 2.2 枚举常量文件

```typescript
// utils/enums.ts

/**
 * 枚举常量定义
 * 用于定义项目中使用的枚举类型
 */

// 用户状态枚举
export enum UserStatus {
  ACTIVE = 'active',
  INACTIVE = 'inactive',
  PENDING = 'pending',
  DELETED = 'deleted',
}

// 角色枚举
export enum Role {
  ADMIN = 'admin',
  USER = 'user',
  GUEST = 'guest',
}

// 操作类型枚举
export enum ActionType {
  CREATE = 'create',
  READ = 'read',
  UPDATE = 'update',
  DELETE = 'delete',
}

// 消息类型枚举
export enum MessageType {
  SUCCESS = 'success',
  ERROR = 'error',
  WARNING = 'warning',
  INFO = 'info',
}

// 组件尺寸枚举
export enum Size {
  SMALL = 'small',
  MEDIUM = 'medium',
  LARGE = 'large',
}

// 按钮类型枚举
export enum ButtonType {
  PRIMARY = 'primary',
  SECONDARY = 'secondary',
  DANGER = 'danger',
  LINK = 'link',
}
```