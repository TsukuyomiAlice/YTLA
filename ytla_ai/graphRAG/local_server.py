from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# 加载本地 embedding 模型（首次运行会自动下载）
model = SentenceTransformer('BAAI/bge-small-zh-v1.5')  # 中文
model_name = 'BAAI/bge-small-zh-v1.5'

# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')  # 英文

@app.route('/v1/embeddings', methods=['POST'])
def embedding():
    data = request.json
    texts = data.get('input', [])
    if isinstance(texts, str):
        texts = [texts]

    # 生成向量
    embeddings = model.encode(texts)

    # 返回 OpenAI 兼容格式
    results = []
    for i, emb in enumerate(embeddings):
        results.append({
            "object": "embedding",
            "index": i,
            "embedding": emb.tolist()
        })

    return jsonify({
        "object": "list",
        "data": results,
        "model": model_name
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11434)