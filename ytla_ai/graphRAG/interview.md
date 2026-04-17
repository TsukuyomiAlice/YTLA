# GraphRAG 面试高频问题（精简版）

## 1. 什么是 GraphRAG？和普通 RAG 的区别？

答题要点：

GraphRAG = RAG + Knowledge Graph  
普通 RAG：  
基于向量相似度  
无法处理复杂关系、多跳推理  
GraphRAG：  
引入 entity / relation  
retrieval = vector + graph traversal  
优势：  
multi-hop reasoning  
更强一致性  
可解释性

加分点：

retrieval 引入结构化 inductive bias

## 2. 如何设计一个 GraphRAG pipeline？

答题结构：四层

数据处理  
chunking  
entity / relation 抽取  
triplet 构建  
存储  
vector DB  
graph DB（如 Neo4j）  
检索（核心）  
vector recall  
graph expansion  
rerank  
生成  
context 构造  
LLM 输出

关键点：

hybrid retrieval

## 3. GraphRAG 中 graph 如何提升 retrieval？

答题要点：

补充关系信息（A → B → C）  
支持 multi-hop  
扩展上下文  
降低 hallucination

加分点：

graph traversal = constrained search

## 4. 为什么不用 long context 替代 GraphRAG？

答题要点：

token 成本高  
attention 不可靠  
无结构信息

总结：

GraphRAG 是结构化检索，不是堆上下文

## 5. 如何评估 GraphRAG？

三类指标：

Retrieval  
recall@k

相关性  
Answer  
correctness  
hallucination

系统  
latency  
cost

加分点：

LLM-as-judge

## 6. 如何设计 Knowledge Graph？

答题要点：

定义 schema：  
entity types  
relation types  
数据来源：  
LLM / rule extraction  
存储：  
图数据库（如 Neo4j）

加分点：

flexibility vs consistency trade-off

## 7. 图数据库如何使用？（Cypher）

示例：

MATCH (a:Entity)-[:REL]->(b:Entity)  
RETURN a, b

答题重点：

能建模  
能查询  
支持多跳关系

## 8. 数据更新如何处理？

答题要点：

vector：  
增量 embedding  
graph：  
插入新节点/关系  
schema versioning（可选）

关键点：

vector 与 graph 一致性

## 9. 如何优化性能？

答题要点：

控制 graph traversal 深度  
top-k 限制  
caching（query / embedding）  
async / batch

## 10. GraphRAG 的缺点？

必须回答：

构建成本高  
schema 设计复杂  
latency 更高

总结：

用工程复杂度换推理能力

## 11. 为什么在你的项目中使用 GraphRAG？

推荐结构：

数据特点（强关系）  
普通 RAG 不足（关系断裂）  
GraphRAG 优势（连接、多跳）  