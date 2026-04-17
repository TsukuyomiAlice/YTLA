# graphRAG部署？指北？

## 0 一些参考的背景
用的是微软的graphRAG.  
官方文档: https://msdocs.cn/graphrag/  

### 0.1 开篇碎碎念
微软的这套东西实际上就是一个封装好了流程的知识图谱构筑过程.  
意图其实很好，非常傻瓜，一把梭，直达目标  
而且可以把重点关注放在提示词和模型配置这两块上  
但是...  
为什么要加载这么多有的没的的包？  
python用了pydantic，那还用python干嘛？

## 1 准备虚拟环境

### 1.1 创建环境
```
python -m venv graphrag-env  
```
这一步可以根据实际需要  
如果作为docker容器，那么这么做没问题  
如果是在集成项目里，那么可以选择单独创建环境，也可以集成到当前环境

### 1.2 激活  
这一步针对新建环境  

Linux:

```
source graphrag-env/bin/activate  
```

Windows:

```
graphrag-env\Scripts\activate  
```

## 2 安装
在该.venv所在的目录下执行  

```
pip install graphrag  
```

确认安装:

```
pip show graphrag  
```


到这一步，只要没有报错，那么graphRAG就已经成功安装到本地了  

接下来开始准备一个知识图谱的实例  

## 3 准备graphRAG目录

```
mkdir my-graphrag  
cd my-graphrag
```

## 4 初始化

执行:

```
python -m graphrag init  
```
以下输入仅作参考
```
Specify the default chat model to use [gpt-4.1]: gpt-4o-mini  
Specify the default embedding model to use [text-embedding-3-large]: text-embedding-3-small  
```
上述内容可以在生成的文件夹的settings.yaml中找到并进行更改.

打开settings.yaml和.env  
在.env中填入对应模型的api_key  
重要：.env绝对不能泄露.  

这是你打开之后会看到的:  

```yaml
### LLM settings ###

## There are a number of settings to tune the threading and token limits for LLM calls - check the docs.

completion_models:
default_completion_model:
  model_provider: openai
  model: gpt-4o-mini
  auth_method: api_key # or azure_managed_identity
  api_key: ${GRAPHRAG_API_KEY} # set this in the generated .env file, or remove if managed identity
  retry:
    type: exponential_backoff

embedding_models:
default_embedding_model:
  model_provider: openai
  model: text-embedding-3-small
  auth_method: api_key
  api_key: ${GRAPHRAG_EMBEDDING_API_KEY} # set this in the generated .env file, or remove if managed identity
  retry:
    type: exponential_backoff
```

准备一个智谱的账户，充一点点钱（不冲的免费版可能还跑不了，具体原因见后文）  
然后照着下面的改  
最终实际生效的配置如下:

```yaml
### LLM settings ###

## There are a number of settings to tune the threading and token limits for LLM calls - check the docs.

completion_models:
  default_completion_model:
    model_provider: openai
    model: glm-4-air
    auth_method: api_key
    api_key: ${GRAPHRAG_API_KEY}
    api_base: https://open.bigmodel.cn/api/paas/v4
    retry:
      type: exponential_backoff

embedding_models:
  default_embedding_model:
    model_provider: openai  
    model: bge-small-zh-v1.5   
    auth_method: api_key
    api_key: "dummy"  
    api_base: http://localhost:11434/v1  
    retry:
      type: exponential_backoff
```

## 4.1 准备模型

### Context LLM

还真的需要好好准备一下，很恶心  
正如下文的碎碎念，对于这个模型是有要求的  
而且很蠢.  
智谱的大模型支持json-schema的输出，所以用它就行了（估计免费的也行？）  

### embedding LLM

安装

```python
from sentence_transformers import SentenceTransformer
```
使用的嵌词模型在上面其实已经配好了  
之后，创建一个本地的embedding (flask) 服务，参考local_server.py的写法，一把过  
- 似乎会涉及到huggingface，这里暂时可以不用管


到这一步，本地的知识图谱实例就做完了，全新的.  

## 5 导入数据

将准备好的数据文件放入my-graphrag/input文件夹内

## 6 构建知识图 - 核心动作

在该目录执行:
```
python -m graphrag index  
```

如果成功运行，会出现以下内容:
```
python -m graphrag index
Starting pipeline with workflows: load_input_documents, create_base_text_units, create_final_documents, extract_graph, finalize_graph, extract_covariates, create_communities, create_final_text_units, create_community_reports, generate_text_embeddings
Starting workflow: load_input_documents

Workflow complete: load_input_documents
Starting workflow: create_base_text_units
  1 / 1 ............................................................................................
Workflow complete: create_base_text_units
Starting workflow: create_final_documents

Workflow complete: create_final_documents
Starting workflow: extract_graph
  138 / 138 ........................................................................................
Workflow complete: extract_graph
Starting workflow: finalize_graph

Workflow complete: finalize_graph
Starting workflow: extract_covariates

Workflow complete: extract_covariates
Starting workflow: create_communities

Workflow complete: create_communities
Starting workflow: create_final_text_units

Workflow complete: create_final_text_units
Starting workflow: create_community_reports
  7 / 7 ............................................................................................
Workflow complete: create_community_reports
Starting workflow: generate_text_embeddings
  1 / 1 ............................................................................................
Workflow complete: generate_text_embeddings
Pipeline complete

```

### 6.1 错误提示
最容易遇到的错误  
Pipeline error: community  
https://github.com/microsoft/graphrag/issues/2200  
这个问题是由于graphrag要求json-schema的返回，而对于很多大模型并不支持这个要求导致的  
实际上是，一些模型就根本不支持指定json格式的返回  
画蛇添足的类型check，大模型之间的商战就是这么简单朴实还无聊.  

另一个蠢到让人无语的错误  
你会看到json.loads()出错  
去看一下提示词，community_report_graph.txt和community_report_text.txt  
找到输出的提示内容，把原本的英语内容改成类似于下面这种Trump式发言：  
```text
Return output as a well-formed python Dict, strictly follow the following format, especially the quote and comma usage, AND WITHOUT ANY LANGUAGE HINT QUOTES!:
```
这坑我以前踩过，再次看到照样踩，但是很好改——可你想不到居然是这样改. Made.

## 7 查询

```
python -m graphrag query [OPTIONS] QUERY 
```

例如:

```
python -m graphrag query "城主指南是什么？"
```

返回如下: 
```
# 城主指南概述

城主指南（Dungeon Master's Guide）是龙与地下城（D&D）游戏系统的核心规则书之一，与玩家手册和怪物手册共同构成游戏的基础规则体系 [Data: Reports (0, 2, 5, 6)]。作为D&D游戏系统的核心组件，它专门为游戏主持人提供详细的规则说明和指导是构建和管理复杂游戏叙事的权威参考资源 [Data: Reports (0, 1, 2, 5)]。

## 主要功能和内容

城主指南包含游戏主持人的角色定义和职责，涵盖以下关键方面：

- **游戏世界创建**：指导主持人如何构建丰富、连贯的虚构世界
- **冒险设计**：提供设计引人入胜冒险情节的框架和方法
- **非玩家角色管理**：阐述如何创建和控制NPC以推动故事发展
- **游戏平衡性**：确保游戏体验的公平性和趣味性 [Data: Reports (0, 1)]

特别值得注意的是，城主指南包含专门的"规则大师"（Master of Rules）部分，详细阐述游戏规则和主持人的裁判职能，为复杂情况下的决策提供权威指导 [Data: Reports (0)]。

## 在D&D生态系统中的地位

城主指南在D&D社区中占据核心地位，与游戏的其他关键组件紧密相连。它被视为游戏主持人的必备参考工具，用于处理游戏过程中可能出现的各种规则和叙事挑战 [Data: Reports (0, 1, 2, 5)]。作为三本核心规则书之一，它与玩家手册（针对玩家角色 ）和怪物手册（针对游戏中的生物）共同构成了完整的D&D游戏规则体系，确保了游戏体验的一致性和深度 [Data: Reports (2, 5)]。

城主指南的重要性不仅体现在其作为规则书的职能上，更体现在它如何帮助主持人创造沉浸式的游戏体验，引导玩家探索虚构世界的奥秘。它既是规则的技术参考，也是叙事创作的灵感来源，体现了D&D作为角色扮演游戏的精髓 [Data: Reports (0, 1, 2, 5, 6)]。

```

调优？不存在的，不调。  

到这一步做完，其实知识图谱就已经搭完了.  

之后分三个部分进行:  

- **API化** 将知识图谱封装成应用
- **安装可视化工具** 直观地了解数据被做成了什么样
- **使用特定的graphDB** 进行特定查询

## 8 可视化
这个简单，先贴链接:  
https://msdocs.cn/graphrag/visualization_guide/#4-install-the-leiden-algorithm-plugin  
顺着做就完事儿了  

## 9 LanceDB: 向量数据库
在微软的graphRAG里使用的是lanceDB.  
怎么还要用到docker的，什么坏习惯.  