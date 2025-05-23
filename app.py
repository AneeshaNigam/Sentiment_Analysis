import streamlit as st
import joblib

model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title("🎬 IMDB Review Sentiment Analyzer")
review = st.text_area("Enter a movie review")

if st.button("Analyze"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        review_vector = vectorizer.transform([review])
        prediction = model.predict(review_vector)[0]
        probability = model.predict_proba(review_vector)[0].max()

        st.success(f"Sentiment: {prediction.capitalize()}")
        st.info(f"Confidence: {probability:.2f}")
