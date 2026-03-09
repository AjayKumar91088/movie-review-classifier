from flask import Flask, request, jsonify, render_template
import pickle
import string
import os

app = Flask(__name__)

# Stopwords (manual to avoid NLTK issues on Vercel)
stop_words = {
"a","about","above","after","again","against","all","am","an","and","any","are","as","at",
"be","because","been","before","being","below","between","both","but","by",
"could","did","do","does","doing","down","during",
"each","few","for","from","further",
"had","has","have","having","he","her","here","hers","herself","him","himself","his","how",
"i","if","in","into","is","it","its","itself",
"just","me","more","most","my","myself",
"no","nor","not","now",
"of","off","on","once","only","or","other","our","ours","ourselves","out","over","own",
"s","same","she","should","so","some","such",
"t","than","that","the","their","theirs","them","themselves","then","there","these","they","this","those","through","to","too",
"under","until","up",
"very",
"was","we","were","what","when","where","which","while","who","whom","why","will","with",
"you","your","yours","yourself","yourselves"
}

# Load model safely
BASE_DIR = os.path.dirname(__file__)

model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))


def clean_text(text):

    text = text.lower()

    # remove punctuation
    text = ''.join([c for c in text if c not in string.punctuation])

    words = text.split()

    # remove stopwords
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

    prob = model.predict_proba(vector).max()

    confidence = round(prob * 100, 2)

    result = "🎉 Blockbuster" if prediction == 1 else "💥 Flop"

    return jsonify({
        "prediction": result,
        "confidence": confidence
    })


if __name__ == "__main__":
    app.run()