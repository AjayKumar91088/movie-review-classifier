from flask import Flask, request, jsonify, render_template
import pickle
import string
from nltk.corpus import stopwords

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

stop_words = stopwords.words("english")


def clean_text(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    words = text.split()
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

    # convert prediction to label
    result = "🎉 Blockbuster" if prediction == 1 else "💥 Flop"

    return jsonify({
        "prediction": result,
        "confidence": float(prob)
    })


if __name__ == "__main__":
    app.run(debug=True)