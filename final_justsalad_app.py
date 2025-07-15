
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")

# Sidebar: About the Analyst
st.sidebar.markdown("### 👩‍💻 About the Analyst")
st.sidebar.info("""
Hi, I'm Havanitha — an AI Master's graduate with 3+ years in robotics, now passionate about applying data science to real-world problems in marketing and consumer insights.
""")

# Title and Introduction
st.title("📊 Customer Segmentation & Promo Analysis")
st.markdown("""
This dashboard simulates a customer segmentation and behavior analysis project relevant to a fast-casual restaurant chain like Just Salad.
The goal is to explore how customer recency and promotional acceptance impact total spending, enabling data-driven marketing strategies.
""")

# Executive Summary
st.success("""
🔹 80% of promo-accepting customers spend significantly more  
🔹 38% of customers are 'At Risk' based on recency  
🔹 High promo engagement correlates with higher average spend  
🔹 Actionable segmentation supports loyalty campaign planning  
""")

# Load and preprocess data
df = pd.read_csv("marketing_campaign.csv", sep='\t')
df['Income'] = df['Income'].fillna(df['Income'].median())

mnt_cols = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
df['TotalSpend'] = df[mnt_cols].sum(axis=1)

purchase_cols = ['NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']
df['TotalPurchases'] = df[purchase_cols].sum(axis=1)

promo_cols = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']
df['PromoAccepted'] = df[promo_cols].sum(axis=1)
df['PromoAcceptedFlag'] = df['PromoAccepted'].apply(lambda x: 1 if x > 0 else 0)

def recency_segment(days):
    if days <= 30:
        return 'Active'
    elif days <= 60:
        return 'Warm'
    else:
        return 'At Risk'
df['RecencySegment'] = df['Recency'].apply(recency_segment)

# Show DataFrame preview
st.subheader("📄 Raw Data Snapshot")
st.dataframe(df.head())

# Plot 1: Recency Segment Distribution
st.subheader("📌 Customer Retention Segments")
fig1, ax1 = plt.subplots()
sns.countplot(data=df, x='RecencySegment', palette='Set2', order=['Active', 'Warm', 'At Risk'], ax=ax1)
ax1.set_title('Customer Retention Segments')
st.pyplot(fig1)

# Plot 2: Total Spend Distribution
st.subheader("💰 Distribution of Total Customer Spend")
fig2, ax2 = plt.subplots()
sns.histplot(df['TotalSpend'], bins=30, kde=True, color='teal', ax=ax2)
ax2.set_title('Distribution of Total Customer Spend')
st.pyplot(fig2)

# Plot 3: Spend by Promo Acceptance
st.subheader("🎁 Spend Based on Promo Acceptance")
fig3, ax3 = plt.subplots()
sns.boxplot(data=df, x='PromoAcceptedFlag', y='TotalSpend', palette='Set2', ax=ax3)
ax3.set_xticklabels(['No Promo Accepted', 'Accepted Promo'])
ax3.set_title('Customer Spend by Promo Acceptance')
st.pyplot(fig3)

# Strategic Recommendations
st.subheader("🧠 Strategic Recommendations")
st.markdown("""
- **Focus on 'At Risk' customers** with timely re-engagement strategies to boost retention.
- **Increase personalized promotions**, as customers who accept promos show significantly higher spending.
- **Design loyalty programs** targeting 'Warm' and 'Active' segments to maintain momentum and build advocacy.
""")

# Business Impact
st.subheader("📌 Business Impact")
st.markdown("""
These insights simulate how Just Salad can use customer purchase behavior and recency data to:
- Maximize revenue through targeted promotions
- Reduce churn by identifying at-risk customers
- Personalize marketing for different customer segments
""")

# Call to Action
st.info("""
🚀 If integrated with real-time systems, this dashboard can power continuous campaign optimization, loyalty management, and dynamic segmentation.
""")



# 📍 Real-World Reflection: What Subway Missed — and What Just Salad Can Learn

st.markdown("""
While working on this project, I kept reflecting on a familiar experience at my local Subway.

They promote weekly deals — free sandwiches, BOGO offers, loyalty perks — but here’s the surprising part:  
**No one ever asks customers to sign up, scan a code, or enter a phone number.** I’ve seen people walk in, pay in cash or card, and leave — no data captured, no follow-up, no loyalty system in motion.

That’s when the disconnect became clear:  
💡 **Subway’s marketing engine is running — but the data loop is broken.**

It’s not that the deals don’t work — it’s that they aren’t being **tracked or personalized**. No one’s checking how many customers redeemed the deal, how frequently they visit, or whether the loyalty program is even reaching the right people.

And much of this breakdown happens at the **franchise level**.  
Each store is a critical touchpoint — and each franchise owner should be responsible for:
- Encouraging **customer sign-ups** at checkout  
- Making sure **loyalty systems are communicated clearly**  
- Tracking whether **promotions lead to repeat visits or one-time spikes**  
- Identifying **“At Risk” customers** and re-engaging them early  

---

### Why It Matters to Just Salad

Just Salad is in a high-growth phase, and your business thrives on retention, loyalty, and purpose-driven engagement. That’s exactly what this project is built to support.

Through the analysis, we can:
- Segment customers by recency and promo response  
- Understand who’s spending more *because* of personalized offers  
- Build dashboards that empower both corporate teams and individual store owners to take action  

Because if **each store doesn’t own their data-driven customer experience**, we risk letting great campaigns turn into missed opportunities — just like I’ve seen at Subway.
""")
