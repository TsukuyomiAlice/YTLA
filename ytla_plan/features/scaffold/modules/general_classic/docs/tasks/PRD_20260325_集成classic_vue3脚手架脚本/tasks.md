本任务进度: 已完成

# 集成 Classic Vue3 脚手架脚本 - The Implementation Plan (Decomposed and Prioritized Task List)

## [x] Task 1: 修改所有已生成的脚本，去掉执行段
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 修改所有 22 个 script_classic_vue3_*.py 脚本
  - 删除 if __name__ == "__main__" 执行段
  - 只保留方法定义
- **Acceptance Criteria Addressed**: AC-1
- **Test Requirements**:
  - `programmatic` TR-1.1: 所有脚本文件中不包含 if __name__ == "__main__"
  - `human-judgement` TR-1.2: 抽查几个脚本，确认方法定义完整
- **Notes**: 逐个修改脚本文件

## [x] Task 2: 创建 constGenerators_vue3.py 配置文件
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 在 general_classic/const/ 目录创建 constGenerators_vue3.py
  - 定义 sidecard 类型的生成器列表（_type 和具体功能实现）
  - 定义 module 类型的生成器列表（_type 和具体功能实现）
  - 格式参考 frontend_vue3/const/constGenerators.py
- **Acceptance Criteria Addressed**: AC-2
- **Test Requirements**:
  - `programmatic` TR-2.1: constGenerators_vue3.py 文件存在
  - `programmatic` TR-2.2: 包含 sidecard 和 module 两个生成器列表
- **Notes**: 生成器映射到 script/ 目录下的对应脚本

## [x] Task 3: 创建 processGenerateFile_vue3.py
- **Priority**: P0
- **Depends On**: Task 1, Task 2
- **Description**: 
  - 在 general_classic/process/ 目录创建 processGenerateFile_vue3.py
  - 根据 structure 参数（cards/modules）判断是 sidecard 还是 module
  - 根据 sub_type_name 参数（_type 或具体名称）判断调用哪些生成器
  - 动态导入并调用相应的脚本方法
  - 参考 frontend_vue3/process/processGenerateStructure.py 的实现
- **Acceptance Criteria Addressed**: AC-3
- **Test Requirements**:
  - `programmatic` TR-3.1: processGenerateFile_vue3.py 文件存在
  - `programmatic` TR-3.2: 函数接受 is_core, structure, type_name, sub_type_name 参数
  - `human-judgement` TR-3.3: 代码逻辑清晰，与 frontend_vue3 架构一致
- **Notes**: 需要处理 _type 和具体功能实现的区分

## [x] Task 4: 修改 processGenerateStructure.py
- **Priority**: P0
- **Depends On**: Task 3
- **Description**: 
  - 修改 general_classic/process/processGenerateStructure.py
  - 当 gen_frontend 为 True 时，调用 processGenerateFile_vue3.py
  - 确认从 config.py 读取 CORE_VERSION、FRONTEND_VERSION
  - 保持与 backend_python_flask 和 frontend_vue3 的集成方式一致
- **Acceptance Criteria Addressed**: AC-4, AC-5
- **Test Requirements**:
  - `programmatic` TR-4.1: processGenerateStructure.py 已更新
  - `programmatic` TR-4.2: 导入了 config 模块
  - `programmatic` TR-4.3: gen_frontend 为 True 时调用新的 processGenerateFile_vue3
- **Notes**: 保持向后兼容性

## [x] Task 5: 添加测试用例
- **Priority**: P1
- **Depends On**: Task 4
- **Description**: 
  - 修改 features_test/scaffold/modules/general_classic/process/processGenerateStructureTest.py
  - 添加针对 classic_vue3 的测试用例
  - 测试 sidecard 类型（_type 和具体功能实现）
  - 测试 module 类型（_type 和具体功能实现）
- **Acceptance Criteria Addressed**: AC-6
- **Test Requirements**:
  - `programmatic` TR-5.1: processGenerateStructureTest.py 已更新
  - `programmatic` TR-5.2: 包含 sidecard 和 module 的测试用例
  - `human-judgement` TR-5.3: 测试用例能正确运行
- **Notes**: 参考现有的测试用例格式
