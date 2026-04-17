# SideCardFilter UI组件分析报告（修正版）

## 目录结构检查

当前目录结构（仅关注规范范围内）：
```
sideCardFilter/
├── composables/
│   └── useSideCardFilter.ts（注：这是主组件的composable，超出UI组件规范范围）
├── definitions/
│   └── sideCardFilterType.ts（注：超出UI组件规范范围，除非UI组件需要）
├── layouts/
│   └── SideCardFilter.vue（注：超出UI组件规范范围）
├── styles/
│   └── side-card-filter.scss
└── ui/
    ├── ButtonClear.vue
    └── FilterInput.vue
```

## 规范范围说明

根据 rule_ui_instructions.md 第 129-147 页：

**本规范仅限于以下范围**：
1. **UI组件文件**：`ui`目录下的Vue文件（`.vue`）
2. **组合式函数文件**：与这些UI组件相关的`composables`目录下的文件（`.ts`）
3. **样式文件**：与这些UI组件相关的`styles`目录下的文件（`.scss`）

**明确排除以下内容**：
- 图标文件 (avatar)
- 主组件文件（components）
- 布局文件（layouts）
- 语言文件（locales）
- 服务文件（services）
- 存储文件（stores）
- 工厂文件（factories）
- 流程文件（flows）
- 注册表文件（registries）

## 发现的问题（仅规范范围内）

### 1. 组件命名不符合规范

根据 rule_ui_instructions.md 第 161-171 页的元件类型列表，UI组件的命名应该遵循 `元件类型 + 元件名 + 元件功能名` 的规则。

**问题文件：**
- `ui/ButtonClear.vue` → 应改为 `ui/ButtonFilterClear.vue`
- `ui/FilterInput.vue` → 应改为 `ui/BarFilterInput.vue`（Input不是预定义的元件类型，应该使用Bar）

### 2. UI组件使用i18n（关注点分离问题）

根据规范，UI组件不应该处理i18n。

**问题文件：**
- `ui/ButtonClear.vue` 中使用了 `{{ $t('classic.cards.sideCardFilter.clear') }}`
- `ui/FilterInput.vue` 中使用了 `:placeholder="$t('classic.cards.sideCardFilter.hint')"`

### 3. 缺少相应的composables文件

UI组件 ButtonClear 和 FilterInput 缺少自己的 composables 文件。

### 4. 样式文件不完整

`styles/side-card-filter.scss` 缺少 FilterInput 的样式定义。

## 总结（仅规范范围内）

需要重构的内容：
1. 重命名UI组件以符合命名规范
2. 移除UI组件中的i18n使用，通过props接收文本
3. 为UI组件添加composables文件
4. 完善样式文件
