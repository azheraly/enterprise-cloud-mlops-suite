from flask import Flask, request, jsonify
from model.intent_model import IntentModel

app = Flask(__name__)

# Load the model once when the worker starts
model = IntentModel()


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}

    text = data.get("text")

    if not text:
        return jsonify({
            "error": "text is required"
        }), 400

    try:
        result = model.predict(text)
        return jsonify(result), 200

    except Exception as e:
        app.logger.exception("Prediction failed")
        return jsonify({
            "error": "prediction failed"
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)