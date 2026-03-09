from flask import Flask, request, jsonify, render_template
import pickle
import string
import os
import nltk
from nltk.corpus import stopwords

app = Flask(__name__)

# Ensure stopwords are available
try:
    stop_words = stopwords.words("english")
except LookupError:
    nltk.download("stopwords")
    stop_words = stopwords.words("english")

# Get current directory
BASE_DIR = os.path.dirname(__file__)

# Load model and vectorizer safely
model_path = os.path.join(BASE_DIR, "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))


def clean_text(text):
    text = text.lower()

    # remove punctuation
    text = ''.join([c for c in text if c not in string.punctuation])

    # tokenize
    words = text.split()

    # remove stopwords
    words = [w for w in words if w not in stop_words]

    return " ".join(words)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # get text from frontend
    data = request.get_json()
    review = data["text"]

    # clean text
    cleaned = clean_text(review)

    # vectorize
    vector = vectorizer.transform([cleaned])

    # prediction
    prediction = model.predict(vector)[0]

    # probability
    prob = model.predict_proba(vector).max()

    # label
    result = "🎉 Blockbuster" if prediction == 1 else "💥 Flop"

    return jsonify({
        "prediction": result,
        "confidence": float(prob)
    })


if __name__ == "__main__":
    app.run()