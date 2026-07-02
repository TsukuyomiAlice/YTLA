# 验证清单

## Task 1: Service 层
- [ ] `data_minerService.ts` 存在且导出所有 5 个 API 方法
- [ ] `getSourceFiles(planId)` 调用 `/data_miner/source_files`
- [ ] `getProcessedFiles(planId)` 调用 `/data_miner/processed_files`
- [ ] `processFile(planId, sourceFilePath, moduleId)` 调用 `POST /data_miner/process`
- [ ] `viewProcessedFile(planId, filePath)` 调用 `GET /data_miner/view`
- [ ] `deleteProcessedFile(planId, filePath)` 调用 `DELETE /data_miner/delete`

## Task 2: Store 层
- [ ] `data_minerStore.ts` 存在且定义完整的 Pinia store
- [ ] Store 管理 `sourceFiles`、`processedFiles`、`currentViewFile`、`isSubActive` 状态
- [ ] Store 提供 action 方法来调用 Service 层 API

## Task 3: Main 区域组件
- [ ] Main 区域同时展示原始文件和已处理文件
- [ ] 表格包含列：文件名、模组ID、数据来源、大小、生成时间、操作
- [ ] 原始文件操作列显示"分析"按钮
- [ ] 已处理文件操作列显示"查看"和"删除"按钮
- [ ] 点击"分析"调用处理接口并刷新列表
- [ ] 点击"删除"调用删除接口并刷新列表
- [ ] 点击"查看"激活 sub 区域

## Task 4: Sub 区域组件
- [ ] Sub 区域展示被查看文件的详细内容
- [ ] Sub 区域顶部有 return to dashboard 按钮
- [ ] 点击 return 按钮关闭 sub 区域，返回 main 区域

## Task 5: FlowManager / Locales / Registries
- [ ] FlowManager 管理 main/sub 切换和当前文件状态
- [ ] locales/zh.json 包含所有中文显示文本
- [ ] locales/en.json 包含所有英文显示文本
- [ ] registries.ts 正确注册 Sub_00 组件

## Task 6: 后端新增接口
- [ ] `GET /data_miner/view` 接口存在且能返回文件内容
- [ ] `DELETE /data_miner/delete` 接口存在且能删除文件及元数据
- [ ] 删除操作正确移除文件目录和 .meta.json
- [ ] 查看操作对 .db 文件读取表数据，对 .json 文件读取 JSON 内容

## Task 7: 整体验证
- [ ] 页面加载后正确显示两种来源的文件
- [ ] 分析 → 生成 → 查看 → 删除 的完整流程可用
- [ ] 国际化切换（中/英）正常工作
