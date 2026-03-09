from flask import Flask, request, jsonify, render_template
import pickle
import string
from nltk.corpus import stopwords

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

stop_words = stopwords.words('english')

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

    review = request.json["review"]

    cleaned = clean_text(review)
    vector = vectorizer.transform([cleaned])

    pred = model.predict(vector)[0]
    prob = model.predict_proba(vector)[0]

    confidence = round(max(prob)*100,2)

    if pred == 1:
        result = "🎉 Blockbuster"
    else:
        result = "💥 Flop"

    return jsonify({
        "prediction": result,
        "confidence": confidence
    })

if __name__ == "__main__":
    app.run(debug=True)