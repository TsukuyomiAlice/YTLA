# Original Requirement - 原始需求

## 用户需求

为 data_power 特性下的 data_miner 模块实现前端页面，基于已实现的后端接口。

**目标模组**：`d:\YTLA\ytla_plan_vue\src\features\data_power\modules\data_miner`
**后端参考**：`d:\YTLA\ytla_plan\features\data_power\modules\data_miner`
**前端参考**：`d:\YTLA\ytla_plan_vue\src\features\data_power\modules\data_manager`、`d:\YTLA\ytla_plan_vue\src\features\investment`

### 页面设计

**main 区域**：类似于 data_manager 的 main 区域，在区域里列举以下内容：
1. 同一 plan 存储区域下所有其它 data_manager 模组下的原始数据文件
2. 由自身 plan_id / module_id 下存在的已生成的分析数据文件

**文件列举列**：文件名，模组ID，数据来源，大小，生成时间（注意：不是上传时间），操作

**操作区分**：
- 来源为（1）的原始文件：操作固定为"分析"，触发对应的分析功能
- 来源为（2）的分析数据：操作包括两种："查看"和"删除"

**sub 区域**：查看按钮点击后展示的内容出现在 sub 区域里。sub 区域的最上方包括一个 return to dashboard 按钮。

**后端联动**：需要根据前端页面上的显示内容，对应地改动后端的内容（新增 view/delete 接口等）。

## 分析

**Given**：
- 前端框架：Vue 3 + TypeScript
- 项目模式：组件（Main/Sub）+ Service + Store + Flows + Locales + Registries
- 后端已有接口：GET /data_miner/source_files, POST /data_miner/process, GET /data_miner/processed_files
- 参考模组 data_manager 已有完整的前端实现

**Target**：
- 实现 data_miner 前端页面，包含 main 区域的文件列表和 sub 区域的详情展示
- 新增/修改后端接口以支持前端操作

**Evidence**：
- data_manager 的 frontend 实现了 Main_00 表格列表 + Sub_00 详情展示 + Service/Store 的完整模式
- ReturnToPlanDashboardButton 组件存在于 investment/_type/ui 目录
- 后端 data_miner 的 processDataMiner.py 已有 source_files 和 processed_files 的接口逻辑
spec mode logging
