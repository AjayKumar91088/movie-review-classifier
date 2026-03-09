cat << 'EOF' > README.md
# 🎬 Movie Review Sentiment Classifier

A Machine Learning web application that predicts whether a movie review is **Positive 😊** or **Negative 😞** and displays the **confidence percentage**.

---

## 🚀 Live Demo
https://movie-review-classifier.vercel.app/

---

## 📌 Features

- Predicts movie review sentiment
- Shows confidence percentage
- Interactive UI with progress bar
- Fast predictions using trained ML model
- Deployed as a web application

---

## 🧠 Machine Learning Model

The model uses Natural Language Processing (NLP):

1. Text preprocessing
2. TF-IDF Vectorization
3. Sentiment classification
4. Confidence score using predict_proba()

---

## 🛠 Tech Stack

- Python
- Flask
- Scikit-learn
- HTML
- CSS
- JavaScript
- Vercel (Deployment)

---

## 📂 Project Structure

movie-review-classifier

├── app.py  
├── model.pkl  
├── vectorizer.pkl  
├── requirements.txt  
├── vercel.json  

├── static  
│   ├── script.js  
│   └── styles.css  

└── templates  
    └── index.html  

---

## ⚙️ Run Locally

Clone repository:

git clone https://github.com/AjayKumar91088/movie-review-classifier.git

Go to project folder:

cd movie-review-classifier

Install dependencies:

pip install -r requirements.txt

Run application:

python app.py

Open browser:

http://127.0.0.1:5000

---

## 📊 Example

Input:
This movie was amazing and the acting was fantastic!

Output:
Prediction: Positive  
Confidence: 92

---

## 🌍 Deployment

The project is deployed using Vercel.

Steps:
1. Push code to GitHub
2. Import repository in Vercel
3. Deploy automatically

---

## 👨‍💻 Author

Ajay  
Machine Learning Enthusiast

---

⭐ If you like this project, give it a star!
EOF
