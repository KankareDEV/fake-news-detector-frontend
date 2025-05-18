from flask import Flask, request, jsonify
import pickle
import traceback

app = Flask(__name__)

# Load model and vectorizer
with open("news_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

@app.route("/ping", methods=["GET"])
def ping():
    return "Pong", 200

@app.route("/invocations", methods=["POST"])
def predict():
    try:
        input_data = request.get_json()
        texts = input_data["texts"]
        vectors = vectorizer.transform(texts)
        preds = model.predict(vectors)
        return jsonify({"predictions": preds.tolist()})
    except Exception as e:
        return jsonify({"error": str(e), "trace": traceback.format_exc()}), 500
