# Scaffold Backend Integration - Project Design Document

## 项目概述
本文档详细记录后端集成需要创建的所有文件及其详细信息。按照用户要求，只需要两个文件。

---

## 文件列表

### 1. process/processGenerateScaffold.py
- **生成位置**: d:\YTLA\ytla_plan\features\scaffold\modules\general_classic\process\processGenerateScaffold.py
- **用途**: 所有业务处理全部在此实现，负责调用processGenerateStructure
- **包含的函数**:
  - `generate_scaffold(is_core: bool, type_name: str, structure: str, sub_type_name: str, gen_backend: bool, gen_frontend: bool)`
    - **参数**: 
      - is_core: 是否是core模块
      - type_name: 类型名称
      - structure: 结构类型（cards/modules）
      - sub_type_name: 子类型名称
      - gen_backend: 是否生成后端
      - gen_frontend: 是否生成前端
    - **返回**: 生成结果字典
    - **功能**: 
      - 参数验证
      - 调用processGenerateStructure.process_generate_structure
      - 处理返回结果
      - 错误处理
- **用途说明**: 所有业务处理在此文件内实现

---

### 2. routes/routeScaffold.py
- **生成位置**: d:\YTLA\ytla_plan\features\scaffold\modules\general_classic\routes\routeScaffold.py
- **用途**: Flask Blueprint实现，只用来负责调用processGenerateScaffold
- **包含的函数/对象**:
  - `scaffold_bp = Blueprint('scaffold', __name__)` - Blueprint对象
  - `/health` GET端点 - 健康检查
    - 函数: `health_check()`
    - 返回: JSON {"status": "ok"}, 200
  - `/generate` POST端点 - 脚手架生成
    - 函数: `generate_scaffold_endpoint()`
    - 功能: 
      - 获取请求JSON数据
      - 提取参数
      - 调用processGenerateScaffold.generate_scaffold
      - 返回JSON响应
    - 错误处理: 400（参数错误）, 500（服务器错误）
- **用途说明**: 只负责调用processGenerateScaffold，不包含业务逻辑

---

### 3. routes/__init__.py（更新）
- **生成位置**: d:\YTLA\ytla_plan\features\scaffold\modules\general_classic\routes\__init__.py
- **用途**: 导出scaffold_bp
- **包含的内容**:
  - 从routeScaffold导入scaffold_bp
  - __all__列表
- **用途说明**: 确保Blueprint可以被正确导入

---

## 目录结构示意

```
d:\YTLA\ytla_plan\features\scaffold\modules\general_classic\
├── process\
│   ├── __init__.py
│   ├── processGenerateFile_vue3.py
│   ├── processGenerateStructure.py
│   └── processGenerateScaffold.py (新增)
└── routes\
    ├── __init__.py (更新)
    └── routeScaffold.py (新增)
```

---

## API接口说明

### POST /scaffold/generate
生成项目脚手架

**请求体**:
```json
{
  "is_core": false,
  "type_name": "my_feature",
  "structure": "cards",
  "sub_type_name": "my_card",
  "gen_backend": true,
  "gen_frontend": true
}
```

**成功响应 (200)**:
```json
{
  "success": true,
  "message": "Structure generated successfully",
  "data": {
    "results": {
      "backend": "...",
      "frontend": "..."
    }
  }
}
```

**错误响应 (400)**:
```json
{
  "success": false,
  "message": "type parameter cannot be empty"
}
```

### GET /scaffold/health
健康检查

**响应 (200)**:
```json
{
  "status": "ok"
}
```

---

## 参考实现

- 主要参考: d:\YTLA\ytla_plan\features\llm_caller\modules\deepseek\routes\routesDeepseekChat.py
- 遵循相同的Flask Blueprint模式
