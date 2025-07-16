
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Customer Retention Dashboard", layout="wide")

# --- Intro ---
st.title("📊 Customer Retention Dashboard")
st.markdown("#### 👋 Hi, I'm Havanitha – a passionate data storyteller and recent AI graduate. After seeing a job posting from Just Salad, I was inspired to build this end-to-end project within a day to understand and solve real business problems around customer retention.")

# --- Problem Statement ---
st.header("🚀 Project Background & Use Case")
st.markdown("""
In a competitive food service market, retaining customers is just as important as acquiring new ones. This dashboard simulates a use case relevant to **Just Salad's** loyalty and marketing initiatives:
- How do promotions impact customer spending?
- Can we segment customers based on recency?
- How do spending patterns differ across these segments?
""")
st.markdown("Using a marketing dataset relevant to the domain, we performed cleaning, feature engineering, and drew visual insights to support strategic business decisions.")

# --- Load Data ---
df = pd.read_csv("marketing_campaign.csv", sep='\t')

# Fill missing values
df['Income'] = df['Income'].fillna(df['Income'].median())

# --- Feature Engineering ---
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

# --- Visual Insights ---
st.header("📌 Visual Insights")

st.subheader("📦 1. Recency-Based Segmentation")
fig1, ax1 = plt.subplots(figsize=(6, 4))
sns.countplot(data=df, x='RecencySegment', palette='Set2', order=['Active', 'Warm', 'At Risk'], ax=ax1)
ax1.set_title('Customer Recency Segments')
ax1.set_xlabel('Recency Category')
ax1.set_ylabel('Customer Count')
st.pyplot(fig1)
st.markdown("- A large portion of customers fall under the '**At Risk**' segment – they haven’t engaged in a while.")
st.markdown("- These are key targets for re-engagement strategies such as discounts or personalized promotions.")

st.subheader("💰 2. Distribution of Total Customer Spend")
fig2, ax2 = plt.subplots(figsize=(7, 4))
sns.histplot(df['TotalSpend'], bins=30, kde=True, color='teal', ax=ax2)
ax2.set_title('Distribution of Total Spend')
ax2.set_xlabel('Total Spend ($)')
ax2.set_ylabel('Customer Count')
st.pyplot(fig2)
st.markdown("- Majority of customers spend under $1,000.")
st.markdown("- A long tail of high spenders can be nurtured through exclusive offers or loyalty perks.")

st.subheader("🎯 3. Promo Response vs Spend")
fig3, ax3 = plt.subplots(figsize=(6, 4))
sns.boxplot(data=df, x='PromoAcceptedFlag', y='TotalSpend', palette='Set2', ax=ax3)
ax3.set_xticklabels(['No Promo Accepted', 'Accepted Promo'])
ax3.set_title('Spend by Promo Acceptance')
ax3.set_xlabel('Promo Status')
ax3.set_ylabel('Total Spend ($)')
st.pyplot(fig3)
st.markdown("- Customers who accepted **any** promotion clearly spent more.")
st.markdown("- This highlights the effectiveness of marketing campaigns in increasing revenue.")

# --- Strategic Takeaways ---
st.header("💡 Strategic Takeaways")

st.markdown("""
- 🔁 **Retention is a key challenge**: A majority of customers are inactive.
- 🎁 **Promos drive ROI**: Promo-accepting customers show a higher lifetime value.
- 📊 **Segmented campaigns**: Tailoring messages based on recency (Active, Warm, At Risk) can significantly improve engagement.
- 💳 **Encourage signups**: Customer data like phone/email is vital for delivering personalized value and tracking behavior.
""")

# --- Field Study ---
st.header("🔍 Field Observation: Subway Case Study")
st.markdown("""
While researching customer retention, I observed real-world breakdowns in loyalty strategy at a nearby **Subway** franchise:

- Despite ongoing weekly deals, customers were **not asked to submit emails or phone numbers** at checkout.
- Many customers, unaware of loyalty benefits, missed out on free meal opportunities.
- These missed interactions represent **lost engagement and data capture**.

**Takeaway**: Franchise-level operations must be held accountable for executing retention strategies. Monitoring, training, and periodic audits can ensure alignment with the brand's customer loyalty goals.
""")

# --- Final Note ---
st.markdown("---")
st.markdown(f"<p style='text-align:center'>Built with ❤️ by Havanitha | July 2025</p>", unsafe_allow_html=True)
