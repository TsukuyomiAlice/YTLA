# Harness 模块 Readme 文档维护 - 产品需求文档

## Overview
本任务旨在维护 YTLA feature_maker harness 模块的 readme 文档，确保文档内容准确、完整，并符合 YTLA 项目规范。当前 harness 模块的 readme 文档存在占位符内容，作者名不一致，概念、目录结构和变更记录部分未填充。本任务将根据 `rule_harness_instructions.md` 和 `rule_readme.md` 规范，更新根目录 readme.md 及其多语言版本，提供清晰的概念描述、完整的文件结构列表和变更记录。

## Goals
1. 更新 harness 模块根目录 readme.md 文档，填充概念和特性包目录部分
2. 补充变更记录部分（如缺失则添加），记录本次文档更新内容
3. 同步更新 docs/readme/en-US/readme.md 和 docs/readme/zh-CN/readme.md 多语言版本
4. 统一所有 readme 文档的作者名为 "Official"（根据 readme 规范）
5. 确保所有 readme 文档符合标准模板和格式要求
6. 仅在内容实际变更时更新文件更新日期

## Non-Goals
1. 不修改 harness 模块的功能代码或配置文件
2. 不创建新的文档文件（仅维护现有的 readme.md 文件）
3. 不更改除 readme 文档外的其他文档（如 rules 目录下的规范文档）
4. 不调整目录结构或文件位置

## Background & Context
- harness 模块是 YTLA feature_maker 的一个子模块，用于提供 AI 代理进行软件工程的 harness 工程规范
- 当前 readme 文档使用脚手架自动生成，包含标准模板但占位符内容未填充
- 根据 `rule_readme.md` 规范，readme 文档应包含清晰的概念描述、准确的文件结构列表和变更记录
- 根据 `rule_harness_instructions.md` 规范，文档维护任务需要遵循规划先行、验证驱动的原则
- 根目录 readme.md 显示为中文版本，作者名为 "Official"，而多语言版本的作者名仍为占位符，需要统一
- 变更记录部分可能缺失或为空，需要根据 rule_readme.md 3.7 节的要求补齐

## Functional Requirements
### FR-1: 更新根目录 readme.md
- **FR-1.1**: 概念部分应提供简明描述，说明 harness 模块的用途和核心价值
- **FR-1.2**: 特性包目录部分应列出 harness 模块下的完整文件结构，反映当前实际状态
- **FR-1.3**: 变更记录部分：如缺失则添加，如已有则在最上方添加本次变更记录
- **FR-1.4**: 作者名应保持为 "Official"（已正确）
- **FR-1.5**: 文件更新日期应在内容实际变更时更新为当前日期（YYYY-MM-DD 格式）

### FR-2: 同步多语言版本
- **FR-2.1**: docs/readme/en-US/readme.md 应与根目录内容一致，但使用英文表述
- **FR-2.2**: docs/readme/zh-CN/readme.md 应与根目录内容一致，使用中文表述
- **FR-2.3**: 两个多语言版本的作者名应统一为 "Official"
- **FR-2.4**: 两个多语言版本的变更记录部分应与根目录一致（多语言翻译）
- **FR-2.5**: 文件更新日期应与根目录保持一致（如果根目录更新了日期）

### FR-3: 符合规范要求
- **FR-3.1**: 所有 readme 文档应符合 `rule_readme.md` 中定义的标准模板（包含变更记录部分）
- **FR-3.2**: 概念部分应简明扼要（1-3 句话）
- **FR-3.3**: 文件结构部分应使用缩进表示层级，按逻辑顺序排列
- **FR-3.4**: 变更记录部分格式应符合 rule_readme.md 3.7 节要求（标题格式、位置、内容描述）
- **FR-3.5**: 多语言版本应通过链接正确互连

## Non-Functional Requirements
### NFR-1: 准确性
- 文件结构列表必须准确反映当前 harness 模块的实际目录和文件
- 概念描述应基于 `rule_harness_instructions.md` 中的定义，准确反映模块用途
- 变更记录应准确描述本次文档更新的内容

### NFR-2: 一致性
- 所有三个 readme 文档的内容应保持一致，仅语言不同
- 作者名、版本号、核心版本等元数据应完全一致
- 变更记录在各语言版本中应准确翻译，内容一致

### NFR-3: 可维护性
- 文档应易于后续维护，结构清晰，内容完整
- 占位符内容应被实际内容替换，避免未来混淆
- 变更记录格式规范，便于未来添加新的变更记录

## Constraints
1. 必须遵循 `rule_harness_instructions.md` 中关于 PRD 目录位置的规定（在目标模组的 docs/design 下）
2. 必须遵循 `rule_readme.md` 中关于 readme 文档内容和格式的规定，特别是变更记录部分的格式（3.7节）
3. 不得修改现有文件结构，仅更新文件内容
4. 日期格式必须为 YYYY-MM-DD

## Assumptions
1. harness 模块的功能和用途如 `rule_harness_instructions.md` 所述
2. 当前文件结构（通过 LS 获取）是准确且最新的
3. 根目录 readme.md 的语言是中文，因此作为主语言版本
4. 用户期望使用中文编写本次规划文档（根据用户输入语言）
5. 如果变更记录部分缺失，我们只需要添加本次变更记录，不需要追溯历史变更

## Acceptance Criteria
### AC-1: 根目录 readme.md 内容完整准确
- **Given**: 当前根目录 readme.md 包含占位符内容，变更记录部分可能缺失
- **When**: 完成文档维护任务后
- **Then**: 根目录 readme.md 的概念部分包含对 harness 模块用途的简明描述
- **Then**: 特性包目录部分列出 harness 模块的完整文件结构，使用缩进表示层级
- **Then**: 变更记录部分存在，且在最上方有本次变更记录（格式符合 rule_readme.md 3.7节）
- **Then**: 作者名保持为 "Official"
- **Then**: 文件更新日期在内容变更时更新为当前日期
- **Verification**: `programmatic`（通过文件内容检查）
- **Notes**: 概念描述应基于 harness 规范，文件结构应准确反映实际目录，变更记录应在最上方

### AC-2: 多语言版本与根目录内容一致
- **Given**: 当前多语言版本作者名为占位符，内容未同步，变更记录可能缺失
- **When**: 完成文档维护任务后
- **Then**: docs/readme/en-US/readme.md 的概念、目录和变更记录部分为英文翻译，与根目录内容一致
- **Then**: docs/readme/zh-CN/readme.md 的概念、目录和变更记录部分为中文，与根目录内容一致
- **Then**: 两个多语言版本的作者名均为 "Official"
- **Then**: 文件更新日期与根目录保持一致
- **Verification**: `programmatic`（通过文件内容比对）
- **Notes**: 多语言版本应通过链接正确互连，变更记录准确翻译

### AC-3: 符合 readme 规范标准模板
- **Given**: 当前 readme 文档使用标准模板但占位符未填充，变更记录可能缺失
- **When**: 完成文档维护任务后
- **Then**: 所有三个 readme 文档均包含标准模板的所有部分（语言链接、标题、作者、版本、概念、目录、变更记录等）
- **Then**: 各部分格式符合 `rule_readme.md` 中的要求，特别是变更记录部分的格式（3.7节）
- **Then**: 概念部分简明扼要（1-3 句话）
- **Then**: 变更记录部分使用规范格式：### YYYY-MM-DD 作为标题，变更内容简明描述
- **Verification**: `human-judgment`（人工审查格式和完整性）
- **Notes**: 确保没有遗漏任何必填部分，特别是变更记录部分

### AC-4: 仅在实际变更时更新日期
- **Given**: 当前文件更新日期为 2026-03-20
- **When**: 完成文档维护任务后
- **Then**: 如果内容实际发生变更，文件更新日期更新为变更当天日期
- **Then**: 如果内容未变更，文件更新日期保持不变
- **Verification**: `programmatic`（检查日期是否与变更匹配）
- **Notes**: 根据 readme 规范，只有实际更新内容时才更新日期

## Open Questions
1. 无 - 所有要求均基于现有规范文档，清晰明确