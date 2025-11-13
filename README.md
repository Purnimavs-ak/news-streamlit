# 📰 News Sentiment Analysis Dashboard using Streamlit & AWS

An interactive **Sentiment Analysis Dashboard** that classifies news articles and headlines into positive, negative, or neutral sentiment.  
Built using **Streamlit** for visualization and **AWS SageMaker + EC2** for end-to-end machine learning model deployment.

---

## 🚀 Project Overview

This dashboard helps analyze real-world news data to understand overall public or media sentiment.  
The model was trained and deployed on **AWS SageMaker**, invoked using **Lambda**, exposed via **API Gateway**, and finally hosted persistently on an **EC2 instance** using `tmux` and `crontab`.

✅ Key Features:
- Real-time sentiment prediction from news text  
- Interactive Streamlit web dashboard  
- Deployed on AWS EC2 and runs even after reboot  
- Model trained using TF-IDF Vectorizer + Logistic Regression  
- Fully integrated AWS workflow (S3, SageMaker, Lambda, API Gateway, EC2)

---

## ☁️ AWS Architecture Overview

**Components Used:**
- **Amazon S3** – Data and model storage  
- **Amazon SageMaker** – Model training and hosting  
- **AWS Lambda** – Invokes the model for prediction  
- **Amazon SNS** – For alert notifications  
- **Amazon API Gateway** – Public API endpoint  
- **AWS EC2** – Hosting Streamlit frontend permanently  

📊 **Workflow:**
1. Data uploaded to S3  
2. Model trained and deployed using SageMaker endpoint  
3. Lambda function invokes the endpoint for real-time predictions  
4. Streamlit dashboard (hosted on EC2) displays predictions live  

---

## 🧠 Machine Learning Model Details

- **Model Type:** Logistic Regression  
- **Text Processing:** TF-IDF Vectorizer  
- **Training Framework:** scikit-learn  
- **Dataset:** Preprocessed news articles with sentiment labels  
- **Accuracy:** ~85% on test data  

Files used:
- `sentiment_model.pkl` – Trained model  
- `tfidf_vectorizer.pkl` – Saved text vectorizer  

---

## 💻 Live Demo

🌐 **Live Dashboard:**  
> http://98.90.196.238:8501  

⚠️ *Note:* The instance must be running on AWS EC2 for the link to work.

---

## 🧩 Folder Structure


---

### ✅ Next Steps
Once you’ve pasted that in VS Code:
1. Save it.  
2. Then run these commands in PowerShell (inside the same folder):

```bash
git add README.md
git commit -m "Added professional README with AWS deployment details"
git push
