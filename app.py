import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from sklearn.linear_model import LinearRegression

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Amazon Recommendation System", layout="wide")

# ================= STYLE =================
st.markdown("""
<style>
h1, h2, h3 {
    color: #4CAF50;
}
</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown("""
# 🛍️ Amazon Product Recommendation Dashboard
### 📊 Insights • 🤖 AI Recommendations • 📈 Trends
""")

# ================= LOAD DATA =================
@st.cache_data
def load_data():
    return pd.read_csv("clean_amazon_data.csv")

df = load_data()

# ================= KPI =================
col1, col2, col3 = st.columns(3)

col1.metric("📦 Total Reviews", len(df))
col2.metric("⭐ Average Rating", round(df['rating'].mean(), 2))
col3.metric("✔ Verified (%)", round(df['verified_purchase'].mean()*100, 2))

# ================= SIDEBAR =================
st.sidebar.title("⚙️ Filters")

rating_range = st.sidebar.slider("Select Rating Range", 1, 5, (1,5))

filtered_df = df[(df['rating'] >= rating_range[0]) & 
                 (df['rating'] <= rating_range[1])]

# ================= PRODUCT VERDICT FUNCTION =================
def product_verdict(asin):
    product_data = df[df['asin'] == asin]
    
    avg_rating = product_data['rating'].mean()
    review_count = len(product_data)
    
    if avg_rating >= 4.2:
        return "✅ Recommended", avg_rating, review_count
    elif avg_rating >= 3:
        return "⚠️ Consider Carefully", avg_rating, review_count
    else:
        return "❌ Not Recommended", avg_rating, review_count

# ================= POPULAR RECOMMENDER =================
def get_popular_products(top_n=5):
    popular = df.groupby('asin').agg({
        'rating': 'mean',
        'asin': 'count'
    })
    popular.columns = ['avg_rating', 'review_count']
    popular['score'] = popular['avg_rating'] * popular['review_count']
    return popular.sort_values('score', ascending=False).head(top_n).index

# ================= TABS =================
tab1, tab2, tab3 = st.tabs(["📊 Overview", "🎯 Recommendations", "📈 Insights"])

# ================= TAB 1 =================
with tab1:
    st.subheader("📊 Rating Distribution")

    rating_counts = filtered_df['rating'].value_counts().sort_index()

    fig = px.bar(
        x=rating_counts.index,
        y=rating_counts.values,
        labels={'x': 'Rating', 'y': 'Count'},
        title="Rating Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📝 Sample Reviews")
    st.dataframe(filtered_df[['asin', 'rating', 'clean_review']].head(10))

# ================= TAB 2 =================
with tab2:
    st.subheader("🎯 Product Recommendations & Evaluation")

    product_list = df['asin'].unique()
    selected_product = st.selectbox("Select a Product", product_list)

    if selected_product:

        # ===== SELECTED PRODUCT =====
        st.subheader("🛒 Selected Product")

        selected_data = df[df['asin'] == selected_product].iloc[0]

        col1, col2 = st.columns([1,2])

        with col1:
            if pd.notnull(selected_data.get('image_url')):
                st.image(selected_data['image_url'], width=200)

        with col2:
            st.write(f"**ASIN:** {selected_product}")
            st.write(f"⭐ Rating: {selected_data['rating']}")
            st.write(f"📝 Review: {selected_data['clean_review'][:150]}...")

        # ===== PRODUCT VERDICT =====
        verdict, avg_rating, review_count = product_verdict(selected_product)

        st.subheader("📌 Should You Buy This Product?")

        col1, col2 = st.columns(2)
        col1.metric("⭐ Average Rating", round(avg_rating, 2))
        col2.metric("📝 Total Reviews", review_count)

        if "Recommended" in verdict:
            st.success(verdict)
        elif "Consider" in verdict:
            st.warning(verdict)
        else:
            st.error(verdict)

        st.divider()

        # ===== RECOMMENDATIONS =====
        st.subheader("🔥 Similar / Popular Products")

        recommendations = get_popular_products()

        cols = st.columns(5)

        for i, asin in enumerate(recommendations):
            product_data = df[df['asin'] == asin].iloc[0]

            with cols[i]:
                if pd.notnull(product_data.get('image_url')):
                    st.image(product_data['image_url'], width=150)

                st.caption(f"ASIN: {asin}")
                st.write(f"⭐ {product_data['rating']}")
# ================= TAB 3 =================
with tab3:
    st.subheader("📈 Monthly Review Trend")

    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df['month'] = df['timestamp'].dt.month

    monthly = df.groupby('month').size()

    fig2 = px.line(
        x=monthly.index,
        y=monthly.values,
        labels={'x': 'Month', 'y': 'Reviews'},
        title="Monthly Review Trend"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # ===== PREDICTION =====
    st.subheader("🤖 Future Trend Prediction")

    last_values = monthly.tail(3)
    prediction = int(last_values.mean())

    st.metric("📊 Estimated Next Month Reviews", prediction)

    # ===== INSIGHTS =====
    st.subheader("📌 Key Insights")

    st.markdown("""
- ⭐ Most users give high ratings → strong satisfaction  
- 📈 Monthly trends show variation in engagement  
- 🖼️ Image-based reviews improve trust  
- 🤖 Recommendation system enhances product discovery  
""")

# ===== FOOTER =====
st.markdown("---")

st.markdown("""
<div style='text-align: center; font-size: 14px; color: white;'>
© 2026 Aby Sebastian <br>
Capstone Project – Amazon Recommendation System <br>
</div>
""", unsafe_allow_html=True)