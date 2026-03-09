from flask import Flask, request, jsonify, render_template
import pickle
import string
import os

app = Flask(__name__)

# Simple stopwords list
stop_words = {
"a","an","the","is","are","was","were","in","on","at","for","to","of","and","or","but","if","with","as","by","about","from"
}

BASE_DIR = os.path.dirname(__file__)

model = pickle.load(open(os.path.join(BASE_DIR,"model.pkl"),"rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR,"vectorizer.pkl"),"rb"))

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

    data = request.get_json()

    review = data["text"]

    cleaned = clean_text(review)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)[0]

    result = "Blockbuster" if prediction == 1 else "Flop"

    return jsonify({
        "prediction": result
    })


if __name__ == "__main__":
    app.run()