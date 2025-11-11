import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# Streamlit App
st.set_page_config(page_title="Sentiment Analysis App", layout="wide")
st.title("🧠 Sentiment Analysis of Tweets")

st.write("Enter a tweet or short text below to predict whether it's **Positive 😊** or **Negative 😞**")

user_input = st.text_area("Enter your text here:")

if st.button("Predict Sentiment"):
    if user_input.strip():
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]

        if prediction == 1:
            st.success("Predicted Sentiment: **Positive 😊**")
        else:
            st.error("Predicted Sentiment: **Negative 😞**")
    else:
        st.warning("Please enter some text before predicting.")

