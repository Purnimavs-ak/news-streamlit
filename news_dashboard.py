import streamlit as st
import pandas as pd
import pickle
from datetime import datetime

# =============================
# 1️⃣ Page Setup
# =============================
st.set_page_config(page_title="News Analytics Sentiment Dashboard", layout="wide")
st.title("📰 News Analytics Sentiment Score Dashboard")

st.sidebar.header("About This Dashboard")
st.sidebar.write("""
This dashboard analyzes the sentiment of news headlines or descriptions using your trained model.
Positive sentiment → optimistic or favorable tone.  
Negative sentiment → pessimistic or unfavorable tone.
""")

# =============================
# 2️⃣ Load Model & Vectorizer
# =============================
try:
    model = pickle.load(open("sentiment_model.pkl", "rb"))
    vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))
    st.sidebar.success("✅ Model & Vectorizer loaded successfully.")
except Exception as e:
    st.sidebar.error(f"❌ Error loading model/vectorizer: {e}")
    st.stop()

# =============================
# 3️⃣ Load Data
# =============================
data_path = "data/sample_news.csv"

try:
    df = pd.read_csv(data_path)
    st.sidebar.success("✅ News dataset loaded successfully.")
except Exception as e:
    st.sidebar.error(f"❌ Could not load dataset from {data_path}. Error: {e}")
    st.stop()

# Check required columns
required_columns = ["timestamp", "author", "description"]
if not all(col in df.columns for col in required_columns):
    st.error(f"❌ CSV must contain these columns: {required_columns}")
    st.stop()

# =============================
# 4️⃣ Predict Sentiments
# =============================
with st.spinner("Analyzing sentiment..."):
    df["clean_text"] = df["description"].astype(str)
    X_vec = vectorizer.transform(df["clean_text"])
    df["sentiment_pred"] = model.predict(X_vec)
    df["sentiment_label"] = df["sentiment_pred"].apply(lambda x: "Positive 😀" if x == 1 else "Negative 😞")

# =============================
# 5️⃣ Display Results
# =============================
st.subheader("🧾 Latest News and Sentiment Results")

# Apply color formatting
def color_sentiment(val):
    color = 'green' if 'Positive' in val else 'red'
    return f'color: {color}; font-weight: bold;'

# Display table with style
st.dataframe(
    df[["timestamp", "author", "description", "sentiment_label"]]
      .style.applymap(color_sentiment, subset=["sentiment_label"]),
    use_container_width=True
)

# =============================
# 6️⃣ Sentiment Summary
# =============================
st.subheader("📈 Sentiment Summary")

total_news = len(df)
positive = len(df[df["sentiment_label"].str.contains("Positive")])
negative = len(df[df["sentiment_label"].str.contains("Negative")])

col1, col2, col3 = st.columns(3)
col1.metric("Total News Articles", total_news)
col2.metric("Positive News 😀", positive)
col3.metric("Negative News 😞", negative)

# =============================
# 7️⃣ Sentiment Distribution Chart
# =============================
st.subheader("📊 Sentiment Distribution")
sentiment_counts = df["sentiment_label"].value_counts()
st.bar_chart(sentiment_counts)


# =============================
# 6️⃣ Sentiment Distribution Chart
# =============================
st.subheader("📊 Sentiment Distribution")
sentiment_counts = df["sentiment_label"].value_counts()
st.bar_chart(sentiment_counts)

# =============================
# 7️⃣ Optional: Download Results
# =============================
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    "📥 Download Analyzed Data as CSV",
    csv,
    "news_sentiment_results.csv",
    "text/csv",
    key='download-csv'
)
