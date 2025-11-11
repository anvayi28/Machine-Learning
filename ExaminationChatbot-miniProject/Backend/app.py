from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util
import torch
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend access

# Load model and data
model = SentenceTransformer('all-MiniLM-L6-v2')
with open('../data/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

questions = [d['question'] for d in data]
answers = [d['answer'] for d in data]
embeddings = model.encode(questions, convert_to_tensor=True)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input.strip():
        return jsonify({"response": "Please type a question."})
    
    query_emb = model.encode(user_input, convert_to_tensor=True)
    scores = util.cos_sim(query_emb, embeddings)
    best_idx = torch.argmax(scores).item()
    return jsonify({"response": answers[best_idx]})

if __name__ == "__main__":
    app.run(debug=True)
