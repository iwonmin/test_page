from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# 점수 저장 함수
def save_score(name, score):
    try:
        with open('/score.json', 'r') as f:
            scores = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        scores = []

    scores.append({'name': name, 'score': score})

    with open('/score.json', 'w') as f:
        json.dump(scores, f, indent=4)

# 점수 저장 API
@app.route('/save_score', methods=['POST'])
def save_score_api():
    data = request.json
    name = data.get('name')
    score = data.get('score')

    if name and isinstance(score, int):
        save_score(name, score)
        return jsonify({"message": "Score saved!"}), 200
    return jsonify({"error": "Invalid data"}), 400

# 점수 조회 API
@app.route('/get_scores', methods=['GET'])
def get_scores_api():
    try:
        with open('score.json', 'r') as f:
            scores = json.load(f)
            return jsonify(scores), 200
    except FileNotFoundError:
        return jsonify([]), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
