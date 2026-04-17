# rule_harness_instructions_ver_direct.md 技术清单

## 一、概述

本文档罗列了使用 `rule_harness_instructions_ver_direct.md` 执行项目开发所需的外部工具，以及相应的实现脚本。

## 二、所需外部工具清单

### 2.1 文件操作工具

| 工具名称 | 用途 | 推荐实现 | 说明 |
|---------|------|---------|------|
| 文件读取器 | 读取文件内容 | Python 脚本、PowerShell 脚本 | 支持读取任意文本文件 |
| 文件写入器 | 写入文件内容 | Python 脚本、PowerShell 脚本 | 支持完整覆盖和追加模式 |
| 文件编辑器 | 修改文件内容 | Python 脚本、PowerShell 脚本 | 支持精确替换和搜索替换 |
| 目录列表器 | 列出目录结构 | Python 脚本、PowerShell 脚本 | 支持递归列出子目录 |
| 目录创建器 | 创建目录 | Python 脚本、PowerShell 脚本 | 支持递归创建多级目录 |
| 文件移动器 | 移动/重命名文件 | Python 脚本、PowerShell 脚本 | 支持跨目录移动 |
| 文件删除器 | 删除文件/目录 | Python 脚本、PowerShell 脚本 | 支持安全删除确认 |

### 2.2 代码搜索工具

| 工具名称 | 用途 | 推荐实现 | 说明 |
|---------|------|---------|------|
| 文件搜索器 | 按文件名搜索 | Python 脚本、PowerShell 脚本 | 支持通配符和正则表达式 |
| 内容搜索器 | 在文件中搜索内容 | Python 脚本、grep (Unix)、findstr (Windows) | 支持正则表达式 |

### 2.3 辅助工具

| 工具名称 | 用途 | 推荐实现 | 说明 |
|---------|------|---------|------|
| 文本比对器 | 比较文件差异 | Python difflib、git diff | 用于验证修改 |
| 格式化工具 | 格式化代码/文档 | 根据语言选择 | 保持代码风格一致 |

## 三、实现脚本

### 3.1 Python 实现（跨平台推荐）

#### 3.1.1 文件操作工具集

**文件**：`harness_tools.py`

```python
#!/usr/bin/env python3
"""
Harness 工程规范 - 文件操作工具集
用于 rule_harness_instructions_ver_direct.md 的配套工具
"""

import os
import shutil
import re
from pathlib import Path
from typing import List, Optional


class HarnessFileTools:
    """Harness 文件操作工具类"""

    @staticmethod
    def read_file(file_path: str) -> str:
        """读取文件内容"""
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def write_file(file_path: str, content: str, mode: str = 'w') -> None:
        """写入文件内容
        
        Args:
            mode: 'w' = 覆盖, 'a' = 追加
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, mode, encoding='utf-8') as f:
            f.write(content)

    @staticmethod
    def replace_in_file(file_path: str, old_str: str, new_str: str) -> None:
        """精确替换文件内容"""
        content = HarnessFileTools.read_file(file_path)
        content = content.replace(old_str, new_str)
        HarnessFileTools.write_file(file_path, content)

    @staticmethod
    def search_replace_in_file(file_path: str, pattern: str, replacement: str) -> None:
        """使用正则表达式搜索替换"""
        content = HarnessFileTools.read_file(file_path)
        content = re.sub(pattern, replacement, content)
        HarnessFileTools.write_file(file_path, content)

    @staticmethod
    def list_directory(dir_path: str, recursive: bool = True) -> List[str]:
        """列出目录内容"""
        result = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                full_path = os.path.join(root, file)
                result.append(full_path)
            if not recursive:
                break
        return result

    @staticmethod
    def create_directory(dir_path: str) -> None:
        """创建目录（支持多级）"""
        os.makedirs(dir_path, exist_ok=True)

    @staticmethod
    def move_file(src_path: str, dst_path: str) -> None:
        """移动/重命名文件"""
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        shutil.move(src_path, dst_path)

    @staticmethod
    def delete_file(file_path: str, confirm: bool = True) -> None:
        """删除文件"""
        if confirm:
            response = input(f"确认删除文件 {file_path}? (y/N): ")
            if response.lower() != 'y':
                print("已取消删除")
                return
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

    @staticmethod
    def search_files(dir_path: str, pattern: str) -> List[str]:
        """按文件名搜索"""
        result = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if re.search(pattern, file):
                    result.append(os.path.join(root, file))
        return result

    @staticmethod
    def search_in_files(dir_path: str, pattern: str, file_pattern: str = "*") -> List[str]:
        """在文件内容中搜索"""
        result = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if not re.search(file_pattern, file):
                    continue
                file_path = os.path.join(root, file)
                try:
                    content = HarnessFileTools.read_file(file_path)
                    if re.search(pattern, content):
                        result.append(file_path)
                except:
                    pass
        return result


def main():
    """命令行接口"""
    import argparse

    parser = argparse.ArgumentParser(description="Harness 文件操作工具")
    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    # 读取文件
    read_parser = subparsers.add_parser("read", help="读取文件")
    read_parser.add_argument("file", help="文件路径")

    # 写入文件
    write_parser = subparsers.add_parser("write", help="写入文件")
    write_parser.add_argument("file", help="文件路径")
    write_parser.add_argument("content", help="文件内容")
    write_parser.add_argument("--append", "-a", action="store_true", help="追加模式")

    # 列出目录
    list_parser = subparsers.add_parser("list", help="列出目录")
    list_parser.add_argument("dir", help="目录路径")
    list_parser.add_argument("--no-recursive", action="store_true", help="不递归")

    # 创建目录
    mkdir_parser = subparsers.add_parser("mkdir", help="创建目录")
    mkdir_parser.add_argument("dir", help="目录路径")

    args = parser.parse_args()

    tools = HarnessFileTools()

    if args.command == "read":
        print(tools.read_file(args.file))
    elif args.command == "write":
        mode = 'a' if args.append else 'w'
        tools.write_file(args.file, args.content, mode)
        print(f"已写入文件: {args.file}")
    elif args.command == "list":
        recursive = not args.no_recursive
        files = tools.list_directory(args.dir, recursive)
        for f in files:
            print(f)
    elif args.command == "mkdir":
        tools.create_directory(args.dir)
        print(f"已创建目录: {args.dir}")


if __name__ == "__main__":
    main()
```

#### 3.1.2 使用示例

```bash
# 读取文件
python harness_tools.py read path/to/file.md

# 写入文件
python harness_tools.py write path/to/file.md "文件内容"

# 追加内容
python harness_tools.py write --append path/to/file.md "追加内容"

# 列出目录
python harness_tools.py list path/to/dir

# 创建目录
python harness_tools.py mkdir path/to/new/dir
```

### 3.2 PowerShell 实现（Windows 推荐）

#### 3.2.1 文件操作工具脚本

**文件**：`harness_tools.ps1`

```powershell
<#
.SYNOPSIS
Harness 工程规范 - PowerShell 文件操作工具集
用于 rule_harness_instructions_ver_direct.md 的配套工具
#>

function Read-HarnessFile {
    <#
    .SYNOPSIS
    读取文件内容
    #>
    param(
        [Parameter(Mandatory=$true)]
        [string]$FilePath
    )
    Get-Content -Path $FilePath -Raw -Encoding UTF8
}

function Write-HarnessFile {
    <#
    .SYNOPSIS
    写入文件内容
    #>
    param(
        [Parameter(Mandatory=$true)]
        [string]$FilePath,
        [Parameter(Mandatory=$true)]
        [string]$Content,
        [switch]$Append
    )
    
    $dir = Split-Path -Path $FilePath -Parent
    if (-not (Test-Path -Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
    
    if ($Append) {
        Add-Content -Path $FilePath -Value $Content -Encoding UTF8
    } else {
        Set-Content -Path $FilePath -Value $Content -Encoding UTF8 -NoNewline
    }
    
    Write-Host "已写入文件: $FilePath"
}

function Replace-HarnessInFile {
    <#
    .SYNOPSIS
    精确替换文件内容
    #>
    param(
        [Parameter(Mandatory=$true)]
        [string]$FilePath,
        [Parameter(Mandatory=$true)]
        [string]$OldString,
        [Parameter(Mandatory=$true)]
        [string]$NewString
    )
    
    $content = Read-HarnessFile -FilePath $FilePath
    $content = $content.Replace($OldString, $NewString)
    Write-HarnessFile -FilePath $FilePath -Content $content
}

function SearchReplace-HarnessInFile {
    <#
    .SYNOPSIS
    使用正则表达式搜索替换
    #>
    param(
        [Parameter(Mandatory=$true)]
        [string]$FilePath,
        [Parameter(Mandatory=$true)]
        [string]$Pattern,
        [Parameter(Mandatory=$true)]
        [string]$Replacement
    )
    
    $content = Read-HarnessFile -FilePath $FilePath
    $content = $content -replace $Pattern, $Replacement
    Write-HarnessFile -FilePath $FilePath -Content $content
}

function List-HarnessDirectory {
    <#
    .SYNOPSIS
    列出目录内容
    #>
    param(
        [Parameter(Mandatory=$true)]
        [string]$DirectoryPath,
        [switch]$NoRecursive
    )
    
    $recurse = -not $NoRecursive
    Get-ChildItem -Path $DirectoryPath -Recurse:$recurse -File | Select-Object -ExpandProperty FullName
}

function New-HarnessDirectory {
    <#
    .SYNOPSIS
    创建目录
    #>
    param(
        [Parameter(Mandatory=$true)]
        [string]$DirectoryPath
    )
    
    New-Item -ItemType Directory -Path $DirectoryPath -Force | Out-Null
    Write-Host "已创建目录: $DirectoryPath"
}

function Move-HarnessFile {
    <#
    .SYNOPSIS
    移动/重命名文件
    #>
    param(
        [Parameter(Mandatory=$true)]
        [string]$SourcePath,
        [Parameter(Mandatory=$true)]
        [string]$DestinationPath
    )
    
    $dir = Split-Path -Path $DestinationPath -Parent
    if (-not (Test-Path -Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
    
    Move-Item -Path $SourcePath -Destination $DestinationPath -Force
    Write-Host "已移动文件: $SourcePath -> $DestinationPath"
}

function Remove-HarnessFile {
    <#
    .SYNOPSIS
    删除文件/目录
    #>
    param(
        [Parameter(Mandatory=$true)]
        [string]$Path,
        [switch]$Force
    )
    
    if (-not $Force) {
        $confirm = Read-Host "确认删除 $Path ? (y/N)"
        if ($confirm -ne 'y') {
            Write-Host "已取消删除"
            return
        }
    }
    
    Remove-Item -Path $Path -Recurse -Force
    Write-Host "已删除: $Path"
}

function Search-HarnessFiles {
    <#
    .SYNOPSIS
    按文件名搜索
    #>
    param(
        [Parameter(Mandatory=$true)]
        [string]$DirectoryPath,
        [Parameter(Mandatory=$true)]
        [string]$Pattern
    )
    
    Get-ChildItem -Path $DirectoryPath -Recurse -File | Where-Object { $_.Name -match $Pattern } | Select-Object -ExpandProperty FullName
}

function Search-HarnessInFiles {
    <#
    .SYNOPSIS
    在文件内容中搜索
    #>
    param(
        [Parameter(Mandatory=$true)]
        [string]$DirectoryPath,
        [Parameter(Mandatory=$true)]
        [string]$Pattern,
        [string]$FilePattern = "*"
    )
    
    Get-ChildItem -Path $DirectoryPath -Recurse -File -Filter $FilePattern | ForEach-Object {
        try {
            $content = Get-Content -Path $_.FullName -Raw -Encoding UTF8
            if ($content -match $Pattern) {
                $_.FullName
            }
        } catch {
            # 跳过无法读取的文件
        }
    }
}

# 导出函数
Export-ModuleMember -Function *-Harness*
```

#### 3.2.2 使用示例

```powershell
# 导入模块
Import-Module .\harness_tools.ps1

# 读取文件
Read-HarnessFile -FilePath "path\to\file.md"

# 写入文件
Write-HarnessFile -FilePath "path\to\file.md" -Content "文件内容"

# 追加内容
Write-HarnessFile -FilePath "path\to\file.md" -Content "追加内容" -Append

# 列出目录
List-HarnessDirectory -DirectoryPath "path\to\dir"

# 创建目录
New-HarnessDirectory -DirectoryPath "path\to\new\dir"
```

### 3.3 简易包装脚本

#### 3.3.1 一键创建 PRD 目录脚本

**文件**：`create_prd_dir.bat` (Windows) / `create_prd_dir.sh` (Linux/Mac)

```batch
@echo off
REM 创建 PRD 目录脚本 - Windows 版本
REM 用法: create_prd_dir.bat [模组路径] [日期] [任务描述]

set MODULE_PATH=%~1
set DATE=%~2
set TASK_DESC=%~3

if "%MODULE_PATH%"=="" (
    echo 用法: create_prd_dir.bat [模组路径] [日期] [任务描述]
    echo 示例: create_prd_dir.bat d:\YTLA\ytla_plan\features\feature_maker\modules\harness 20260325 "创建非IDE依赖版本"
    exit /b 1
)

if "%DATE%"=="" set DATE=%date:~0,4%%date:~5,2%%date:~8,2%
if "%TASK_DESC%"=="" set TASK_DESC=未命名任务

set PRD_DIR=%MODULE_PATH%\docs\tasks\PRD_%DATE%_%TASK_DESC%

echo 正在创建 PRD 目录: %PRD_DIR%
mkdir "%PRD_DIR%" 2>nul

echo PRD 目录创建完成: %PRD_DIR%
```

```bash
#!/bin/bash
# 创建 PRD 目录脚本 - Linux/Mac 版本
# 用法: ./create_prd_dir.sh [模组路径] [日期] [任务描述]

MODULE_PATH="$1"
DATE="$2"
TASK_DESC="$3"

if [ -z "$MODULE_PATH" ]; then
    echo "用法: ./create_prd_dir.sh [模组路径] [日期] [任务描述]"
    echo "示例: ./create_prd_dir.sh /path/to/module 20260325 \"创建非IDE依赖版本\""
    exit 1
fi

if [ -z "$DATE" ]; then
    DATE=$(date +%Y%m%d)
fi

if [ -z "$TASK_DESC" ]; then
    TASK_DESC="未命名任务"
fi

PRD_DIR="${MODULE_PATH}/docs/tasks/PRD_${DATE}_${TASK_DESC}"

echo "正在创建 PRD 目录: ${PRD_DIR}"
mkdir -p "${PRD_DIR}"

echo "PRD 目录创建完成: ${PRD_DIR}"
```

## 四、推荐工作流程

### 4.1 使用 Python 工具的工作流程

1. **准备环境**：
   ```bash
   # 确保已安装 Python 3
   python --version
   ```

2. **保存脚本**：
   - 将 `harness_tools.py` 保存到项目根目录或 PATH 路径中

3. **执行项目开发**：
   - 将 `rule_harness_instructions_ver_direct.md` 作为系统提示词发送给大模型
   - 大模型会告知需要执行的文件操作
   - 使用 `harness_tools.py` 执行相应的文件操作

### 4.2 使用 PowerShell 工具的工作流程

1. **准备环境**：
   ```powershell
   # 确保 PowerShell 版本 >= 5.1
   $PSVersionTable.PSVersion
   ```

2. **保存脚本**：
   - 将 `harness_tools.ps1` 保存到项目目录

3. **执行项目开发**：
   - 将 `rule_harness_instructions_ver_direct.md` 作为系统提示词发送给大模型
   - 大模型会告知需要执行的文件操作
   - 导入并使用 `harness_tools.ps1` 中的函数执行文件操作

## 五、工具安装建议

### 5.1 最小配置（推荐）

- **Python 3.7+**（跨平台）
- 或 **PowerShell 5.1+**（Windows）

### 5.2 增强配置

- **Git** - 用于版本控制和文件比较
- **VS Code** 或其他文本编辑器 - 用于手动编辑文件
- **grep** / **ripgrep** - 用于快速代码搜索（可选）

## 六、注意事项

1. **备份重要文件**：在执行大规模文件操作前，建议先备份
2. **版本控制**：建议使用 Git 等版本控制系统
3. **权限管理**：确保脚本有足够的文件读写权限
4. **路径处理**：注意 Windows 和 Linux/Mac 路径分隔符的差异
