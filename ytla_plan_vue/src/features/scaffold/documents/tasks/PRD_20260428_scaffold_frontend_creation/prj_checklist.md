# Scaffold Frontend Creation - Project Design Document

## 项目概述
本文档详细记录前端需要创建/完善的所有文件及其详细信息。包含create_card和create_module两个子模块。

---

## 第一部分：create_card模块文件列表

### 1. components/Create_cardMain_00.vue
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card\components\Create_cardMain_00.vue
- **用途**: create_card模块的主界面组件，包含表单输入和提交功能
- **包含的内容**:
  - Template部分：
    - 表单容器
    - Core/Feature单选框组
    - 版本选择下拉框（默认classic）
    - Type Name文本输入框
    - Sub Type Name文本输入框
    - 生成后端复选框
    - 生成前端复选框
    - 提交按钮
    - Loading状态指示器
    - 成功/错误消息显示
  - Script部分：
    - 使用&lt;script setup lang="ts"&gt;
    - 导入useScaffoldCardStore
    - 响应式表单数据绑定
    - 表单验证逻辑
    - 提交处理函数handleSubmit
    - 重置处理函数handleReset
  - Style部分：
    - 使用&lt;style scoped lang="scss"&gt;
    - 表单样式
    - 按钮样式
    - 消息样式
- **用途说明**: 提供用户输入脚手架参数的主界面

---

### 2. components/Create_cardSub_00.vue
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card\components\Create_cardSub_00.vue
- **用途**: create_card模块的子界面组件，显示说明信息和生成结果
- **包含的内容**:
  - Template部分：
    - 模块说明文本
    - 使用说明
    - 成功时显示生成结果信息
    - 显示backend_path和frontend_path
  - Script部分：
    - 使用&lt;script setup lang="ts"&gt;
    - 导入useScaffoldCardStore
    - 获取store中的result状态
  - Style部分：
    - 使用&lt;style scoped lang="scss"&gt;
- **用途说明**: 提供模块说明和结果展示

---

### 3. services/scaffoldCardService.ts
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card\services\scaffoldCardService.ts
- **用途**: 封装与后端API的通信
- **包含的内容**:
  - TypeScript类型定义：
    - ScaffoldCardRequest接口：isCore, typeName, structure, subTypeName, genBackend, genFrontend
    - ScaffoldCardResponse接口：success, message, backendPath, frontendPath
  - ScaffoldCardService类：
    - 构造函数：接受API_BASE参数
    - generateScaffold方法：
      - 参数：request: ScaffoldCardRequest
      - 返回：Promise&lt;{ success: boolean; data: ScaffoldCardResponse }&gt;
      - 功能：发送POST请求到 /scaffold/generate
- **用途说明**: 提供类型安全的API调用服务

---

### 4. stores/scaffoldCardStore.ts
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card\stores\scaffoldCardStore.ts
- **用途**: 使用Pinia管理create_card模块的状态
- **包含的内容**:
  - 导入defineStore from 'pinia'
  - 导入ScaffoldCardService
  - 从环境变量获取API_BASE
  - 定义useScaffoldCardStore：
    - State:
      - isCore: boolean (默认false)
      - typeName: string (默认'')
      - subTypeName: string (默认'')
      - version: string (默认'classic')
      - genBackend: boolean (默认false)
      - genFrontend: boolean (默认false)
      - isLoading: boolean (默认false)
      - error: string | null (默认null)
      - result: ScaffoldCardResponse | null (默认null)
    - Actions:
      - updateForm(field: string, value: any): 更新表单字段
      - async submitForm(): 提交表单，调用API
      - resetForm(): 重置表单到初始状态
      - private _handleError(error: any, defaultMsg: string): 处理错误
- **用途说明**: 集中管理表单状态和业务逻辑

---

### 5. flows/create_cardFlowManager.ts
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card\flows\create_cardFlowManager.ts
- **用途**: 管理create_card模块的流程
- **包含的内容**:
  - 导入defineAsyncComponent from 'vue'
  - 导入ModuleFlowManager类型
  - 定义Create_cardFlowManager类，实现ModuleFlowManager
    - flows: Map&lt;string, Component[]&gt;
    - initialStep: Component | null
    - registerFlow(flowName: string, steps: Component[]): void
    - getSteps(flowName: string): Component[]
  - 创建create_cardFlowManager实例
  - 注册流程：
    - 'create_card-main-steps': [Create_cardMain_00]
    - 'create_card-sub-steps': [Create_cardSub_00]
- **用途说明**: 管理模块的多步骤流程

---

### 6. registries/create_cardModuleConfig.ts
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card\registries\create_cardModuleConfig.ts
- **用途**: 定义create_card模块的配置
- **包含的内容**:
  - 导入defineAsyncComponent from 'vue'
  - 导入ModuleRegistry类型
  - 导入create_cardFlowManager
  - 定义create_cardModuleConfig: ModuleRegistry
    - moduleType: 'scaffold'
    - moduleSubType: 'create_card'
    - moduleConcept: 'create_card'
    - mainComponent: defineAsyncComponent(() =&gt; import('../components/Create_cardMain.vue'))
    - subComponent: defineAsyncComponent(() =&gt; import('../components/Create_cardSub.vue'))
    - displayMode: 7
    - flowManager: create_cardFlowManager
- **用途说明**: 配置模块的基本信息和组件映射

---

### 7. registries/registries.ts
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card\registries\registries.ts
- **用途**: 模块注册文件
- **包含的内容**:
  - 导入create_cardModuleConfig
  - 导出create_cardModuleConfig
- **用途说明**: 方便其他模块导入和使用

---

### 8. locales/zh.json
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card\locales\zh.json
- **用途**: 中文语言包
- **包含的内容**:
  - "subtype_name": "创建卡片"
  - "subtype_description": "生成新的卡片模块"
  - "title": "创建卡片脚手架"
  - "label_is_core": "Core模块"
  - "label_is_feature": "Feature模块"
  - "label_version": "版本"
  - "label_type_name": "类型名称"
  - "label_sub_type_name": "子类型名称"
  - "label_gen_backend": "生成后端"
  - "label_gen_frontend": "生成前端"
  - "button_submit": "生成"
  - "button_reset": "重置"
  - "msg_loading": "正在生成..."
  - "msg_success": "生成成功！"
  - "msg_error": "生成失败：{error}"
  - "validation_type_name_required": "请输入类型名称"
  - "sub_00_000": "关于卡片创建"
  - "sub_00_001": "使用此工具快速创建新的卡片模块"
  - "sub_00_002": "生成的后端路径：{path}"
  - "sub_00_003": "生成的前端路径：{path}"
- **用途说明**: 提供中文界面文本

---

### 9. locales/en.json
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card\locales\en.json
- **用途**: 英文语言包
- **包含的内容**:
  - "subtype_name": "Create Card"
  - "subtype_description": "Generate new card module"
  - "title": "Create Card Scaffold"
  - "label_is_core": "Core Module"
  - "label_is_feature": "Feature Module"
  - "label_version": "Version"
  - "label_type_name": "Type Name"
  - "label_sub_type_name": "Sub Type Name"
  - "label_gen_backend": "Generate Backend"
  - "label_gen_frontend": "Generate Frontend"
  - "button_submit": "Generate"
  - "button_reset": "Reset"
  - "msg_loading": "Generating..."
  - "msg_success": "Generation successful!"
  - "msg_error": "Generation failed: {error}"
  - "validation_type_name_required": "Please enter type name"
  - "sub_00_000": "About Card Creation"
  - "sub_00_001": "Use this tool to quickly create new card modules"
  - "sub_00_002": "Generated backend path: {path}"
  - "sub_00_003": "Generated frontend path: {path}"
- **用途说明**: 提供英文界面文本

---

### 10. avatar/Avatar.vue
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card\avatar\Avatar.vue
- **用途**: create_card模块的头像组件
- **包含的内容**:
  - Template部分：
    - SVG图标或img标签显示卡片相关图标
  - Script部分：
    - 使用&lt;script setup lang="ts"&gt;
  - Style部分：
    - 使用&lt;style scoped lang="scss"&gt;
- **用途说明**: 显示模块的图标/头像

---

## 第二部分：create_module模块文件列表

### 11. components/Create_moduleMain_00.vue
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module\components\Create_moduleMain_00.vue
- **用途**: create_module模块的主界面组件，包含表单输入和提交功能
- **包含的内容**:
  - 与Create_cardMain_00.vue基本相同
  - 主要区别：
    - structure参数固定为'modules'
    - 文本提示使用module相关的语言
  - Template部分：
    - 表单容器
    - Core/Feature单选框组
    - 版本选择下拉框（默认classic）
    - Type Name文本输入框
    - Sub Type Name文本输入框
    - 生成后端复选框
    - 生成前端复选框
    - 提交按钮
    - Loading状态指示器
    - 成功/错误消息显示
  - Script部分：
    - 使用&lt;script setup lang="ts"&gt;
    - 导入useScaffoldModuleStore
    - 响应式表单数据绑定
    - 表单验证逻辑
    - 提交处理函数handleSubmit
    - 重置处理函数handleReset
  - Style部分：
    - 使用&lt;style scoped lang="scss"&gt;
- **用途说明**: 提供用户输入脚手架参数的主界面

---

### 12. components/Create_moduleSub_00.vue
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module\components\Create_moduleSub_00.vue
- **用途**: create_module模块的子界面组件，显示说明信息和生成结果
- **包含的内容**:
  - 与Create_cardSub_00.vue基本相同
  - Template部分：
    - 模块说明文本
    - 使用说明
    - 成功时显示生成结果信息
    - 显示backend_path和frontend_path
  - Script部分：
    - 使用&lt;script setup lang="ts"&gt;
    - 导入useScaffoldModuleStore
    - 获取store中的result状态
  - Style部分：
    - 使用&lt;style scoped lang="scss"&gt;
- **用途说明**: 提供模块说明和结果展示

---

### 13. services/scaffoldModuleService.ts
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module\services\scaffoldModuleService.ts
- **用途**: 封装与后端API的通信
- **包含的内容**:
  - 与scaffoldCardService.ts基本相同
  - TypeScript类型定义：
    - ScaffoldModuleRequest接口：isCore, typeName, structure, subTypeName, genBackend, genFrontend
    - ScaffoldModuleResponse接口：success, message, backendPath, frontendPath
  - ScaffoldModuleService类：
    - 构造函数：接受API_BASE参数
    - generateScaffold方法：
      - 参数：request: ScaffoldModuleRequest
      - 返回：Promise&lt;{ success: boolean; data: ScaffoldModuleResponse }&gt;
      - 功能：发送POST请求到 /scaffold/generate，structure固定为'modules'
- **用途说明**: 提供类型安全的API调用服务

---

### 14. stores/scaffoldModuleStore.ts
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module\stores\scaffoldModuleStore.ts
- **用途**: 使用Pinia管理create_module模块的状态
- **包含的内容**:
  - 与scaffoldCardStore.ts基本相同
  - 导入defineStore from 'pinia'
  - 导入ScaffoldModuleService
  - 从环境变量获取API_BASE
  - 定义useScaffoldModuleStore：
    - State:
      - isCore: boolean (默认false)
      - typeName: string (默认'')
      - subTypeName: string (默认'')
      - version: string (默认'classic')
      - genBackend: boolean (默认false)
      - genFrontend: boolean (默认false)
      - isLoading: boolean (默认false)
      - error: string | null (默认null)
      - result: ScaffoldModuleResponse | null (默认null)
    - Actions:
      - updateForm(field: string, value: any): 更新表单字段
      - async submitForm(): 提交表单，调用API，structure固定为'modules'
      - resetForm(): 重置表单到初始状态
      - private _handleError(error: any, defaultMsg: string): 处理错误
- **用途说明**: 集中管理表单状态和业务逻辑

---

### 15. flows/create_moduleFlowManager.ts
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module\flows\create_moduleFlowManager.ts
- **用途**: 管理create_module模块的流程
- **包含的内容**:
  - 与create_cardFlowManager.ts基本相同
  - 导入defineAsyncComponent from 'vue'
  - 导入ModuleFlowManager类型
  - 定义Create_moduleFlowManager类，实现ModuleFlowManager
    - flows: Map&lt;string, Component[]&gt;
    - initialStep: Component | null
    - registerFlow(flowName: string, steps: Component[]): void
    - getSteps(flowName: string): Component[]
  - 创建create_moduleFlowManager实例
  - 注册流程：
    - 'create_module-main-steps': [Create_moduleMain_00]
    - 'create_module-sub-steps': [Create_moduleSub_00]
- **用途说明**: 管理模块的多步骤流程

---

### 16. registries/create_moduleModuleConfig.ts
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module\registries\create_moduleModuleConfig.ts
- **用途**: 定义create_module模块的配置
- **包含的内容**:
  - 与create_cardModuleConfig.ts基本相同
  - 导入defineAsyncComponent from 'vue'
  - 导入ModuleRegistry类型
  - 导入create_moduleFlowManager
  - 定义create_moduleModuleConfig: ModuleRegistry
    - moduleType: 'scaffold'
    - moduleSubType: 'create_module'
    - moduleConcept: 'create_module'
    - mainComponent: defineAsyncComponent(() =&gt; import('../components/Create_moduleMain.vue'))
    - subComponent: defineAsyncComponent(() =&gt; import('../components/Create_moduleSub.vue'))
    - displayMode: 7
    - flowManager: create_moduleFlowManager
- **用途说明**: 配置模块的基本信息和组件映射

---

### 17. registries/registries.ts
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module\registries\registries.ts
- **用途**: 模块注册文件
- **包含的内容**:
  - 导入create_moduleModuleConfig
  - 导出create_moduleModuleConfig
- **用途说明**: 方便其他模块导入和使用

---

### 18. locales/zh.json
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module\locales\zh.json
- **用途**: 中文语言包
- **包含的内容**:
  - "subtype_name": "创建模块"
  - "subtype_description": "生成新的功能模块"
  - "title": "创建模块脚手架"
  - "label_is_core": "Core模块"
  - "label_is_feature": "Feature模块"
  - "label_version": "版本"
  - "label_type_name": "类型名称"
  - "label_sub_type_name": "子类型名称"
  - "label_gen_backend": "生成后端"
  - "label_gen_frontend": "生成前端"
  - "button_submit": "生成"
  - "button_reset": "重置"
  - "msg_loading": "正在生成..."
  - "msg_success": "生成成功！"
  - "msg_error": "生成失败：{error}"
  - "validation_type_name_required": "请输入类型名称"
  - "sub_00_000": "关于模块创建"
  - "sub_00_001": "使用此工具快速创建新的功能模块"
  - "sub_00_002": "生成的后端路径：{path}"
  - "sub_00_003": "生成的前端路径：{path}"
- **用途说明**: 提供中文界面文本

---

### 19. locales/en.json
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module\locales\en.json
- **用途**: 英文语言包
- **包含的内容**:
  - "subtype_name": "Create Module"
  - "subtype_description": "Generate new feature module"
  - "title": "Create Module Scaffold"
  - "label_is_core": "Core Module"
  - "label_is_feature": "Feature Module"
  - "label_version": "Version"
  - "label_type_name": "Type Name"
  - "label_sub_type_name": "Sub Type Name"
  - "label_gen_backend": "Generate Backend"
  - "label_gen_frontend": "Generate Frontend"
  - "button_submit": "Generate"
  - "button_reset": "Reset"
  - "msg_loading": "Generating..."
  - "msg_success": "Generation successful!"
  - "msg_error": "Generation failed: {error}"
  - "validation_type_name_required": "Please enter type name"
  - "sub_00_000": "About Module Creation"
  - "sub_00_001": "Use this tool to quickly create new feature modules"
  - "sub_00_002": "Generated backend path: {path}"
  - "sub_00_003": "Generated frontend path: {path}"
- **用途说明**: 提供英文界面文本

---

### 20. avatar/Avatar.vue
- **生成位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module\avatar\Avatar.vue
- **用途**: create_module模块的头像组件
- **包含的内容**:
  - 与create_card的Avatar.vue基本相同
  - Template部分：
    - SVG图标或img标签显示模块相关图标
  - Script部分：
    - 使用&lt;script setup lang="ts"&gt;
  - Style部分：
    - 使用&lt;style scoped lang="scss"&gt;
- **用途说明**: 显示模块的图标/头像

---

## 目录结构示意

```
d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\
├── create_card\
│   ├── avatar\
│   │   └── Avatar.vue
│   ├── components\
│   │   ├── Create_cardMain.vue
│   │   ├── Create_cardMain_00.vue
│   │   ├── Create_cardSub.vue
│   │   └── Create_cardSub_00.vue
│   ├── docs\readme\
│   │   ├── en-US\readme.md
│   │   └── zh-CN\readme.md
│   ├── flows\
│   │   └── create_cardFlowManager.ts
│   ├── locales\
│   │   ├── en.json
│   │   └── zh.json
│   ├── registries\
│   │   ├── create_cardModuleConfig.ts
│   │   └── registries.ts
│   ├── services\
│   │   └── scaffoldCardService.ts
│   ├── stores\
│   │   └── scaffoldCardStore.ts
│   └── readme.md
└── create_module\
    ├── avatar\
    │   └── Avatar.vue
    ├── components\
    │   ├── Create_moduleMain.vue
    │   ├── Create_moduleMain_00.vue
    │   ├── Create_moduleSub.vue
    │   └── Create_moduleSub_00.vue
    ├── docs\readme\
    │   ├── en-US\readme.md
    │   └── zh-CN\readme.md
    ├── flows\
    │   └── create_moduleFlowManager.ts
    ├── locales\
    │   ├── en.json
    │   └── zh.json
    ├── registries\
    │   ├── create_moduleModuleConfig.ts
    │   └── registries.ts
    ├── services\
    │   └── scaffoldModuleService.ts
    ├── stores\
    │   └── scaffoldModuleStore.ts
    └── readme.md
```

---

## 参考实现

- 主要参考：d:\YTLA\ytla_plan_vue\src\features\language\modules\dictionary\
- 次要参考：d:\YTLA\ytla_plan_vue\src\features\mathematics\modules\sphere\
- 注意create_card和create_module两个模块的代码非常相似，主要区别是structure参数和语言包文本
