Harness Instructions file version: rule_harness_instructions_ver_ide.md  
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement: 
/spec `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions_ver_ide.md` 
 我检查了 `d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule_ui_instructions.md` 发现了问题 
 在'代码模板与示例'章节里，.vue组件模板的ts与scss部分存在以下问题 
 对于vue文件，应该只负责导入ts和scss，而不应再在vue文件内存在相关的ts与css代码 
 你应该理解为： 
 .vue文件——专用于html template 
 .ts文件——专用于组合式函数 
 .scss文件——专用于组件式样 
 所以.vue文件里的scope和style部分只应该负责导入，所有的具体逻辑应该写在对应的ts和scss文档内

## Analyze：
**Given**： 
- 输入的harness规则文件：`d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions_ver_ide.md`
- 目标UI组件规则文件：`d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule_ui_instructions.md`
- 用户指出了文档中的问题：.vue 组件模板中包含了具体的 TypeScript 和 SCSS 代码，而不应该只负责导入

**Target**： 
- 修改 rule_ui_instructions.md 文档中的代码模板与示例章节
- 确保 .vue 文件只负责 HTML 模板和导入
- 确保具体的 TypeScript 逻辑在 .ts 文件中
- 确保具体的 SCSS 样式在 .scss 文件中
- 提供清晰的分离关注点示例

**Evidence**： 
- 用户明确指出了问题所在的章节："代码模板与示例"
- 用户说明了正确的职责分离：.vue专用于template，.ts专用于组合式函数，.scss专用于组件样式
- 需要修改文档中的模板和示例部分

## Evaluation Result：
### 产物1：更新后的 rule_ui_instructions.md 文档
- 形式：Markdown 文档
- 内容：修改代码模板与示例章节，实现关注点分离

### 产物2：规划文档（PRD）
- 形式：origin.md、spec.md、tasks.md、checklist.md、actions.md
- 位置：目标模组 docs/tasks/PRD_20260407_rule_ui_instructions_重构Vue组件模板分离关注点/ 目录下

spec mode logging
