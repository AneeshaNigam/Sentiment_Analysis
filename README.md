# 🎯 Sentiment Analysis App

A simple sentiment analysis web application built using a machine learning model trained on IMDB movie reviews. The app classifies input text as **positive** or **negative** sentiment.

🌐 **Live Demo:** [Try the App](https://sentimentanalysis-1.streamlit.app)

---

## 📦 Features

- ✅ Pretrained Logistic Regression model using TF-IDF vectorizer  
- 🎬 Trained on the IMDB Dataset of 50,000 reviews  
- ⚡ User-friendly frontend via Streamlit  
- 📦 Local execution without internet required  
- 🧼 Clean and modular code structure  

---

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/AneeshaNigam/Sentiment_Analysis.git
cd Sentiment_Analysis
```
**2. Create and activate a virtual environment**

```bash
python -m venv venv
# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

```
**3. Install dependencies**

```bash
pip install -r requirements.txt
```
**4. Run the app**

```bash
streamlit run app.py
```
📁 Project Structure
```bash
.
├── app.py                # Streamlit web app
├── model.py              # Model loading and preprocessing code
├── sentiment_model.pkl   # Trained ML model
├── vectorizer.pkl        # TF-IDF vectorizer
├── requirements.txt      # Dependencies
├── .gitignore
├── LICENSE
└── README.md
✅ Note: Dataset (IMDB Dataset.csv) and model training code are excluded from deployment for size and reproducibility reasons.
```

🧠 Model Training
Preprocessing: Lowercasing, removing HTML tags, punctuation, and stopwords

Vectorization: TF-IDF using sklearn

Model: Logistic Regression using scikit-learn

Training Environment: Google Colab

Exported Models: sentiment_model.pkl, vectorizer.pkl

📄 License
This project is licensed under the MIT License.

✨ Author
Aneesha Nigam
🎓 B.Tech CSE Student | 💡 Passionate about AI & Deployment
🔗 LinkedIn Profile: https://www.linkedin.com/in/aneesha-nigam/