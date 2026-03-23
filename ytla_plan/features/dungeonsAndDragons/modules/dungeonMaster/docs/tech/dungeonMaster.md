# dungeonMaster 模块技术文档

## 模块概述

### 模块定位
dungeonMaster 是 Dungeons &amp; Dragons 5e（龙与地下城第五版）的地下城主辅助模块，为游戏主持人和玩家提供规则查询、AI 辅助、骰子处理、内容嵌入等功能。

### 主要功能
- **规则数据集管理**：存储和管理 D&amp;D 5e 规则手册内容（玩家手册、城主指南、怪物图鉴等）
- **AI 提示词系统**：提供多种专门的 AI 提示词，用于规则查询、内容生成等场景
- **骰子模拟器**：经典骰子投掷功能
- **向量数据库集成**：支持将 D&amp;D 规则内容嵌入到 ChromaDB 中，实现智能检索
- **查询流程**：多阶段的规则查询流程，包括问题分析、关键词提取、内容检索和答案生成

### 设计目标
- 为 D&amp;D 游戏提供便捷的规则查询和辅助功能
- 利用 AI 技术简化游戏主持人的工作
- 提供可扩展的架构，便于后续功能扩展
- 遵循 YTLA 项目的整体架构规范

### 技术栈
- **后端语言**：Python
- **框架**：Flask
- **适用 YTLA core 版本**：classic
- **向量数据库**：ChromaDB

---

## 文件结构说明

### 整体目录结构
```
dungeonMaster/
├── __init__.py
├── ai_tools/              # AI 工具相关
├── api/                   # API 接口
├── caller/                # 调用器
├── const/                 # 常量定义
├── dao/                   # 数据访问对象
├── dataset/               # 数据集
├── docs/                  # 文档
│   ├── readme/           # 说明文档
│   ├── tech/             # 技术文档
│   └── tasks/            # 任务规划
├── func/                  # 功能函数
├── instance/              # 实例相关
├── process/               # 处理流程
├── prompts/               # AI 提示词
├── routes/                # 路由
├── schedule/              # 定时任务
├── script/                # 脚本工具
└── utils/                 # 工具函数
```

### 核心目录说明

#### 1. dataset/ - 数据集目录
存储 D&amp;D 5e 规则手册的数据集，包含 Python 源文件和转换后的 JSON 文件。

**关键文件**：
- `datasetJsonPicker.py`：JSON 数据集读取和提取工具
- `datasetPyToJson.py`：Python 源文件到 JSON 的转换工具
- `dnd_5e_*.py`：各规则手册的 Python 源文件
- `dnd_5e_*.json`：转换后的 JSON 数据文件

**数据集内容**：
- `dnd_5e_dmguide_*`：城主指南（Dungeon Master's Guide）
- `dnd_5e_monster_*`：怪物图鉴（Monster Manual）
- `dnd_5e_player_*`：玩家手册（Player's Handbook）

#### 2. process/ - 处理流程目录
包含核心业务处理逻辑的模块。

**关键文件**：
- `processAgentCore.py`：核心代理处理（当前为空）
- `processAgentDM.py`：地下城主代理处理
- `processAgentPL.py`：玩家代理处理（主要查询流程）
- `processClassicDice.py`：经典骰子处理

#### 3. prompts/ - 提示词目录
包含各种 AI 提示词，用于不同的查询和生成场景。

**关键文件**：
- `promptCore.py`：核心系统提示词
- `promptGuideAnswer.py`：答案生成提示词
- `promptGuideKeywordList.py`：关键词列表提示词
- `promptGuideKeywordPicker.py`：关键词选择提示词
- `promptGuideKeywordTopics.py`：关键词主题提示词
- `promptGuideMaskedKeywordTopics.py`：掩码关键词主题提示词
- `promptGuidePreAnswer.py`：预回答提示词

#### 4. script/ - 脚本目录
包含各种工具脚本，用于数据处理、嵌入等任务。

**关键文件**：
- `scriptDNDEmbedder.py`：D&amp;D 内容嵌入器（将 PDF 内容嵌入到 ChromaDB）
- `scriptDNDTextTransformer.py`：文本转换工具
- `scriptDNDtext.py`：原始文本存储
- `scriptDnDQuery.py`：D&amp;D 内容查询工具

---

## 核心组件说明

### 1. 数据集管理组件

#### datasetJsonPicker.py
提供从 JSON 数据集中提取内容的功能。

**主要函数**：
- `get_data_file_list()`：获取所有 JSON 数据文件列表
- `extract_file_index(json_filename)`：从 JSON 文件中提取主题索引
- `generate_topic_key_list()`：生成所有主题键列表
- `generate_topic_file_list()`：生成主题到文件的映射
- `generate_topic_keyword_list(topic_list)`：生成主题关键词列表
- `generate_article_part(keyword_list)`：根据关键词生成文章片段
- `generate_article_part_by_whole_search(keyword, article)`：通过全文搜索生成文章片段

#### datasetPyToJson.py
将 Python 源文件中的字符串常量转换为 JSON 格式。

**主要函数**：
- `get_data_file_list()`：获取所有 Python 数据文件列表
- `extract_topics_and_articles(py_file_path)`：从 Python 文件中提取主题和文章
- `convert_to_json(py_file_path)`：将 Python 文件转换为 JSON 文件

### 2. 处理流程组件

#### processAgentPL.py - 玩家代理处理
实现主要的规则查询流程。

**主要函数**：
- `topic_word_list()`：获取主题词列表
- `create_keyword_list(topic_list)`：创建关键词列表
- `grab_article(keyword_list)`：获取文章片段
- `grab_article_by_keyword(keyword_list, article)`：通过关键词获取文章
- `question_keyword_picker(request_prompt, temperature)`：问题关键词选择器
- `question_pre_answer(request_prompt, temperature)`：预回答生成
- `masked_keyword_topics(request_prompt, temperature)`：掩码关键词主题分析
- `select_keyword_topics(request_prompt, temperature)`：选择关键词主题
- `select_keyword_list(topic_chat, request_prompt, temperature)`：选择关键词列表
- `guide_answer(keyword_chat, question_keywords, request_prompt, temperature)`：引导生成最终答案
- `query(chat)`：完整的查询流程入口

**查询流程**：
1. 问题关键词提取（question_keyword_picker）
2. 预回答生成（question_pre_answer）
3. 问题大类分析（masked_keyword_topics）
4. 问题大类筛选（select_keyword_topics）
5. 问题子类筛选（select_keyword_list）
6. 最终答案生成（guide_answer）

#### processAgentDM.py - 地下城主代理处理
提供地下城主相关的辅助功能。

**主要函数**：
- `process_agent_dm_dungeon_maker(demand, temperature)`：随机地下城生成器
- `process_agent_dm_story_teller(story_teller, temperature)`：故事讲述者（待实现）

#### processClassicDice.py - 骰子处理
提供经典骰子投掷功能。

**主要函数**：
- `roll_dice(dice)`：模拟骰子投掷
  - 参数：骰子表达式，如 "2d6" 表示投掷 2 个 6 面骰
  - 返回：包含总点数和单个骰子结果的元组

### 3. 提示词组件

各个提示词文件定义了不同场景下的 AI 系统提示词：

- **promptCore.py**：核心系统提示词，定义游戏辅助系统管理员的角色
- **promptGuideAnswer.py**：答案生成提示词，包含前后两部分
- **promptGuideKeywordTopics.py**：关键词主题选择提示词，用于确定问题所属的章节
- **promptGuideMaskedKeywordTopics.py**：掩码关键词主题提示词
- **promptGuideKeywordPicker.py**：关键词选择提示词
- **promptGuideKeywordList.py**：关键词列表提示词
- **promptGuidePreAnswer.py**：预回答提示词

### 4. 脚本组件

#### scriptDNDEmbedder.py - D&amp;D 内容嵌入器
将 D&amp;D PDF 规则手册内容嵌入到 ChromaDB 向量数据库中。

**主要类**：
- `DNDEmbedder`：D&amp;D 内容嵌入器类

**主要方法**：
- `__init__(pdf_paths)`：初始化嵌入器，指定 PDF 文件路径
- `generate_id(content, page_num, source_file)`：生成内容唯一 ID
- `chunk_text(text, chunk_size, overlap, preserve_sentences)`：将文本分割成块
- `_chunk_by_sentences(text, chunk_size, overlap)`：基于句子边界分割文本
- `extract_content_from_pdf()`：从 PDF 中提取内容
- `prepare_embedding_data(content_dict, chunk_size, overlap, preserve_sentences)`：准备嵌入数据
- `embed_into_chroma(documents, metadatas, ids)`：将数据嵌入到 ChromaDB
- `create_index_if_not_exists()`：创建索引（如果不存在）
- `clear_collection()`：清空集合内容
- `run_full_embedding_process(clear_existing, chunk_size, overlap, preserve_sentences)`：运行完整的嵌入流程

#### scriptDnDQuery.py - D&amp;D 内容查询工具
提供查询已嵌入到 ChromaDB 中的 D&amp;D 内容的功能。

**主要类**：
- `DnDQueryTool`：D&amp;D 内容查询工具类

**主要方法**：
- `__init__()`：初始化查询工具
- `similarity_search(query_text, n_results, distance_threshold)`：基于相似度搜索
- `search_with_content_filter(query_text, content_keywords, n_results)`：结合相似度搜索和内容关键词过滤
- `hybrid_search(query_text, metadata_filter, content_keywords, n_results, distance_threshold)`：混合搜索方法
- `search_by_metadata(metadata_filter, n_results)`：基于元数据筛选搜索
- `get_by_ids(ids)`：根据 ID 获取特定记录
- `get_collection_stats()`：获取集合统计信息
- `pretty_print_results(results, query_text, sort_by, deduplicate)`：美观打印搜索结果
- `search_by_page_range(min_page, max_page, n_results)`：通过页码范围搜索内容

---

## 数据处理流程

### 1. 数据集转换流程
Python 源文件 → JSON 数据文件

1. `datasetPyToJson.py` 读取 Python 源文件
2. 提取字符串常量中的主题（以 `# ` 开头的行）
3. 生成 `topics` 和 `articles` 字典
4. 保存为 JSON 文件

### 2. 规则查询流程
用户问题 → 多阶段处理 → 最终答案

1. **问题分析阶段**：
   - 提取问题中的 D&amp;D 术语关键词
   - 生成预回答
   - 分析问题所属大类

2. **内容检索阶段**：
   - 选择相关的主题章节
   - 选择具体的关键词
   - 从数据集中提取相关文章片段

3. **答案生成阶段**：
   - 将检索到的文章片段提供给 AI
   - 基于原文内容生成完整、准确的回答
   - 附上原文段落和解释说明

### 3. 内容嵌入流程
PDF 文件 → ChromaDB 向量数据库

1. **PDF 内容提取**：
   - 打开 PDF 文档
   - 提取所有页面的文本
   - 关闭文档

2. **文本分块**：
   - 将页面文本分割成适当大小的块
   - 支持句子级别的分割
   - 支持块之间的重叠

3. **数据准备**：
   - 生成唯一 ID
   - 准备元数据（页码、来源、位置等）
   - 构建文档列表、元数据列表、ID 列表

4. **数据库嵌入**：
   - 创建或获取集合
   - 清空现有内容（可选）
   - 将数据插入到 ChromaDB
   - 验证嵌入结果

---

## 配置和部署

### 环境要求
- Python 3.x
- Flask 框架
- ChromaDB 向量数据库
- YTLA core classic 版本

### 依赖项
- `ytla_ai.client.contentHandler`：AI 内容处理客户端
- `core.classic.frame.chromaDBConnector`：ChromaDB 连接器
- `core.classic.frame.pdfProcessor`：PDF 处理器
- `core.classic.frame.loggerConfig`：日志配置

### 关键配置
- **数据库名称**：`dnd_5e_db`
- **集合名称**：`phb_content`
- **默认 PDF 路径**：指向 D&amp;D 5e 玩家手册 PDF 文件

---

## 扩展开发指南

### 添加新的规则数据集
1. 在 `dataset/` 目录下创建新的 Python 文件
2. 使用字符串常量存储规则内容，主题行以 `# ` 开头
3. 运行 `datasetPyToJson.py` 转换为 JSON 格式

### 添加新的查询提示词
1. 在 `prompts/` 目录下创建新的提示词文件
2. 定义提示词字符串变量
3. 在 `processAgentPL.py` 中导入并使用

### 添加新的处理流程
1. 在 `process/` 目录下创建新的处理模块
2. 实现相关的处理函数
3. 在适当的位置集成到现有流程中

---

## 作者
Official

## 文件更新日期
2026-03-23
