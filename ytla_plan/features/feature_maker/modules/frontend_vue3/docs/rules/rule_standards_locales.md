# Locales 代码规范

## 1 依赖限制表

| 功能域类型 | locales可依赖此功能域 | locales可被此功能域依赖 |
| :--- | :--- | :--- |
| definitions |  |  |
| styles |  |  |
| utils |  |  |
| locales |  |  |
| avatar |  |  |
| factories |  |  |
| flows |  |  |
| registries |  |  |
| services |  |  |
| policies |  |  |
| stores |  |  |
| composables |  |  |
| uis |  |  |
| components |  |  |
| layouts |  |  |

## 2 标准代码格式

---
以下为预生成内容.  
预生成内容包含基础的 `type_name` 和 `type_description` 字段，用于模块的基本标识.
---

### 2.1 _type 目录中文语言文件

```json
{
  "type_name": "模块类型名称(按语种填写)",
  "type_description": "(这里填入你的定义)"
}
```

### 2.2 _type 目录英文语言文件

```json
{
  "type_name": "Module Type Name(according to the language)",
  "type_description": "(add your definition)"
}
```

### 2.3 sub_type 目录中文语言文件

```json
{
  "subtype_name": "子类型名称(按语种填写)",
  "subtype_description": "(这里填入你的定义)"
}
```

### 2.4 sub_type 目录英文语言文件

```json
{
  "subtype_name": "Subtype Name(according to the language)",
  "subtype_description": "(add your definition)"
}
```

---

以下为自定义内容区域，可根据业务需求按需添加额外字段.

---

### 2.5 直接添加内容

```json
{
  "type_name": "模块类型名称(按语种填写)",
  "type_description": "(这里填入你的定义)",
  "custom_field": "自定义字段内容",
  "custom_action": "自定义操作"
}
```

### 2.6 详细示例

```json
{
  "type_name": "用户管理",
  "type_description": "用户管理模块，包含用户列表、用户详情、用户编辑等功能",
  "pages": {
    "list": "用户列表",
    "detail": "用户详情",
    "create": "创建用户",
    "edit": "编辑用户"
  },
  "actions": {
    "view": "查看",
    "edit": "编辑",
    "delete": "删除",
    "create": "创建",
    "search": "搜索",
    "export": "导出",
    "import": "导入"
  },
  "labels": {
    "name": "姓名",
    "email": "邮箱",
    "phone": "电话",
    "role": "角色",
    "status": "状态",
    "createdAt": "创建时间",
    "updatedAt": "更新时间"
  },
  "status": {
    "active": "活跃",
    "inactive": "不活跃",
    "pending": "待审核",
    "disabled": "已禁用"
  },
  "messages": {
    "success": {
      "create": "用户创建成功",
      "update": "用户更新成功",
      "delete": "用户删除成功"
    },
    "error": {
      "create": "用户创建失败",
      "update": "用户更新失败",
      "delete": "用户删除失败"
    },
    "confirm": {
      "delete": "确定要删除该用户吗？"
    }
  }
}
```