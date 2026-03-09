from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()
    text = data["text"]

    vec = vectorizer.transform([text])

    prediction = model.predict(vec)[0]
    proba = model.predict_proba(vec).max()

    if prediction == 1:
        result = "Positive"
    else:
        result = "Negative"

    return jsonify({
        "prediction": result,
        "confidence": float(proba)
    })

if __name__ == "__main__":
    app.run(debug=True)