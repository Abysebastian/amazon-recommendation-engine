# 🛍️ Amazon Product Recommendation System

## 📌 Overview
This project builds an intelligent product recommendation system using real-world review data. It analyzes user behavior, product ratings, and textual reviews to suggest relevant products and assist decision-making.

---

## 🎯 Objectives
- Build a recommendation engine using ML techniques
- Analyze user reviews using NLP
- Provide insights through interactive dashboard
- Evaluate recommendation quality using relevant metrics

---

## 📂 Dataset
The dataset contains:
- Rating
- Review text
- Product ID (ASIN)
- User ID
- Timestamp
- Helpful votes
- Verified purchase

---

## 🧹 Data Preprocessing
- Handled missing values and duplicates
- Cleaned text data (lowercasing, removing special characters)
- Feature engineering (review length, sentiment, date features)

---

## 🧠 NLP Techniques
- Text cleaning and normalization
- Sentiment analysis
- Feature extraction for content-based filtering

---

## 🤖 Machine Learning Models
- Collaborative Filtering
- Content-Based Filtering (TF-IDF)
- Hybrid Recommendation System
- Popularity-based fallback (for sparse data)

---

## 📊 Evaluation Metrics
- Precision
- Recall
- F1 Score

Verified purchase was used as a proxy for relevance.

---

## 📈 Dashboard Features
- KPI metrics (ratings, reviews)
- Product recommendation system
- Product evaluation (Recommended / Consider / Not Recommended)
- Rating distribution charts
- Monthly trend analysis
- Future prediction (moving average)
- Product images for better understanding

---

## 🚀 Deployment
The dashboard is deployed using Streamlit Cloud.

👉 Live App: [Add your link here]

---

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- NLP (Text processing)
- Streamlit
- Plotly

- 
---

## 🧾 Conclusion
This project demonstrates a complete data science pipeline from data collection to deployment. The hybrid recommendation system effectively handles real-world challenges like sparse data and provides meaningful product suggestions.

---

## 👤 Author
Aby Sebastian  
Capstone Project – 2026

---
## 📁 Project Structure

├── app.py                      # Streamlit dashboard  
├── scraper.py                 # Web scraping script  
├── clean_amazon_data.csv      # Cleaned dataset  
├── requirements.txt           # Dependencies  
├── README.md                  # Project documentation  
