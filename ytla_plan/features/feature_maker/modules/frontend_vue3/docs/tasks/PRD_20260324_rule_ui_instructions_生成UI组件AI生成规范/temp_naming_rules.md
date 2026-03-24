# YTLA UI 组件命名规则规范

基于 sideCard 组件分析结果和现有 rule.md 规范，制定详细的 UI 组件命名规则。

## 1. 元件类型列表

基于 sideCard 组件分析，定义了以下 6 种元件类型：

| 元件类型 | 使用场景 | 示例组件 |
|---------|---------|---------|
| **Container**（容器） | 用于包裹和组织其他 UI 元素的布局容器，通常不直接包含业务逻辑 | ContainerSideCard、ContainerIcon、ContainerTags |
| **Bar**（条形/行） | 用于显示单行文本内容的水平区域，如标题栏、描述栏 | BarTitle、BarDescription |
| **Button**（按钮） | 用于用户交互的点击操作元素，执行特定动作 | ButtonPin、ButtonEdit、ButtonClose |
| **Panel**（面板） | 用于承载多个相关组件或功能的区域，通常具有特定的布局结构 | SideCardPanel |
| **Layer**（层/布局） | 用于整体页面布局的容器，通常包含多个 Panel 或 Container | SideCardLayer |
| **Card**（卡片） | 用于展示独立信息单元的自包含组件，通常包含完整的功能模块 | SideCard |

## 2. 复合组合词命名规则

### 2.1 命名结构
```
元件类型名 + 元件名 + 元件功能名
```

### 2.2 命名规范
1. **各部分首字母大写**（PascalCase）
2. **元件类型名**：从预定义列表中选择（Container、Bar、Button、Panel、Layer、Card）
3. **元件名**：描述组件所属的主要领域或功能模块（如 SideCard、Editor、Filter）
4. **元件功能名**：描述组件的具体功能（如 Pin、Edit、Title、Description）
5. **组合词应使用明确的业务术语**，避免通用名称
6. **确保名称清晰反映组件职责**，避免歧义

### 2.3 命名示例
- **Button + Pin** = `ButtonPin`（固定按钮）
- **Container + SideCard** = `ContainerSideCard`（卡片容器）
- **Bar + Title** = `BarTitle`（标题栏）
- **Panel + SideCard** = `SideCardPanel`（侧边栏卡片面板）
- **Layer + SideCard** = `SideCardLayer`（侧边栏卡片层）

## 3. 命名示例

### 3.1 正例（基于 sideCard 实际组件）

1. **ButtonPin** - 固定按钮
   - **文件位置**: `ui/ButtonPin.vue`
   - **元件类型**: Button（按钮）
   - **元件名**: Pin（固定功能）
   - **功能说明**: 用于固定/取消固定卡片的按钮组件

2. **ContainerSideCard** - 卡片容器
   - **文件位置**: `layouts/ContainerSideCard.vue`
   - **元件类型**: Container（容器）
   - **元件名**: SideCard（侧边栏卡片）
   - **功能说明**: 包裹整个卡片内容的布局容器

3. **SideCardPanel** - 侧边栏卡片面板
   - **文件位置**: `sideCardPanel/layouts/SideCardPanel.vue`
   - **元件类型**: Panel（面板）
   - **元件名**: SideCard（侧边栏卡片）
   - **功能说明**: 显示和管理所有卡片的布局面板

4. **SideCardLayer** - 侧边栏卡片层
   - **文件位置**: `sideCardLayer/layouts/SideCardLayer.vue`
   - **元件类型**: Layer（层/布局）
   - **元件名**: SideCard（侧边栏卡片）
   - **功能说明**: 整体侧边栏卡片区域的布局层

5. **BarTitle** - 标题栏
   - **文件位置**: `ui/BarTitle.vue`
   - **元件类型**: Bar（条形/行）
   - **元件名**: Title（标题）
   - **功能说明**: 显示卡片标题的文本行组件

### 3.2 反例（常见错误）

1. **错误示例**: `PinButton`
   - **问题**: 元件类型顺序错误，应为 ButtonPin
   - **影响**: 不符合命名约定，影响组件分类和查找

2. **错误示例**: `SideCardPinButton`
   - **问题**: 缺少元件类型前缀，应为 ButtonPin
   - **影响**: 无法快速识别组件类型，增加理解成本

## 4. 文件命名约定

### 4.1 Vue 组件文件
- **命名规则**: PascalCase
- **示例**: 
  - `SideCard.vue` (主组件)
  - `ButtonPin.vue` (UI 组件)
  - `ContainerSideCard.vue` (布局组件)

### 4.2 TypeScript 组合式函数文件
- **命名规则**: camelCase，前缀为 `use`
- **示例**: 
  - `useSideCard.ts` (主组合式函数)
  - `useButtonPin.ts` (按钮交互逻辑)
  - `useBarTitle.ts` (标题栏逻辑)

### 4.3 SCSS 样式文件
- **命名规则**: kebab-case
- **示例**: 
  - `side-card.scss` (主样式)
  - `button-pin.scss` (按钮样式)
  - `container-side-card.scss` (容器样式)

### 4.4 TypeScript 类型定义文件
- **命名规则**: camelCase，后缀为 `Type`
- **示例**: 
  - `sideCardType.ts` (卡片类型定义)
  - `cardDataType.ts` (卡片数据类型定义)

### 4.5 工厂文件
- **命名规则**: camelCase，后缀为 `Registry` 或 `Helper`
- **示例**: 
  - `cardRegistry.ts` (卡片注册表)
  - `cardRegistryHelper.ts` (注册表辅助函数)

### 4.6 服务文件
- **命名规则**: PascalCase，后缀为 `Service`
- **示例**: `cardService.ts` (卡片服务)

### 4.7 布局组件
- **命名规则**: PascalCase，后缀为布局类型
- **示例**: `SideCardPanel.vue`、`SideCardLayer.vue`

## 5. 目录结构示例

```
sideCard/
├── components/          # 主组件目录
│   └── SideCard.vue     # 主组件
├── composables/         # 组合式函数目录
│   ├── useSideCard.ts   # 主组合式函数
│   ├── useButtonPin.ts  # 按钮交互逻辑
│   └── useBarTitle.ts   # 标题栏逻辑
├── definitions/         # 类型定义目录
│   ├── sideCardType.ts  # 卡片类型定义
│   └── cardDataType.ts  # 卡片数据类型定义
├── layouts/             # 布局组件目录
│   └── ContainerSideCard.vue  # 卡片容器布局
├── ui/                  # UI 组件目录
│   ├── ButtonPin.vue    # 固定按钮
│   ├── BarTitle.vue     # 标题栏
│   └── ContainerIcon.vue # 图标容器
├── styles/              # 样式文件目录
│   ├── side-card.scss   # 主样式
│   ├── button-pin.scss  # 按钮样式
│   └── container-side-card.scss  # 容器样式
└── factories/           # 工厂文件目录
    └── cardRegistry.ts  # 卡片注册表
```

## 6. 应用实践指南

### 6.1 新组件命名步骤
1. **确定元件类型**：从预定义类型列表中选择最合适的类型
2. **识别元件名**：确定组件所属的功能模块或领域
3. **定义功能名**：描述组件的具体功能
4. **组合命名**：按照"类型+名称+功能"顺序组合
5. **验证命名**：检查是否符合约定，避免歧义

### 6.2 命名检查清单
- [ ] 是否使用 PascalCase 格式？
- [ ] 元件类型是否正确（Container、Bar、Button 等）？
- [ ] 元件名是否清晰反映所属模块？
- [ ] 功能名是否准确描述组件用途？
- [ ] 整体名称是否简洁且无歧义？

### 6.3 扩展建议
1. **保持一致性**：相同功能的组件使用相同命名模式
2. **遵循现有模式**：参考 sideCard 组件的命名实践
3. **文档化命名**：在组件文档中说明命名依据
4. **定期审查**：定期检查命名规范执行情况

## 7. 总结

本命名规则基于 YTLA 项目的实际需求制定，旨在：
1. 提供清晰的组件分类和识别标准
2. 确保代码的一致性和可维护性
3. 降低新开发者的学习成本
4. 支持项目的可扩展性和团队协作

通过遵循这些命名规则，可以确保 YTLA 项目的 UI 组件命名系统化、规范化，便于团队协作和项目维护。

---
*文档生成日期: 2026-03-24*
*基于 sideCard 组件分析版本: 20260323*