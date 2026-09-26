import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------
# Step 1: Load the Final Data
# ---------------------------------------------------------
# Load the output from your Hugging Face script
df = pd.read_csv('final_analyzed_reviews.csv')

# Set a professional visual theme
sns.set_theme(style="whitegrid")

# Create a figure with two subplots side-by-side
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ---------------------------------------------------------
# Step 2: Chart 1 - Overall Sentiment Distribution
# ---------------------------------------------------------
# Count how many positive vs negative reviews we have
sentiment_counts = df['AI_Sentiment'].value_counts()

# Create a Pie Chart
axes[0].pie(
    sentiment_counts, 
    labels=sentiment_counts.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=['#4C72B0', '#C44E52'] # Blue for Positive, Red for Negative
)
axes[0].set_title('Overall Customer Sentiment', fontsize=14, fontweight='bold')

# ---------------------------------------------------------
# Step 3: Chart 2 - Sentiment Breakdown by Product
# ---------------------------------------------------------
# Create a bar chart showing positive/negative counts per product
sns.countplot(
    data=df, 
    x='Product', 
    hue='AI_Sentiment', 
    ax=axes[1],
    palette={'POSITIVE': '#4C72B0', 'NEGATIVE': "#C83E43"}
)
axes[1].set_title('Sentiment Breakdown by Product Category', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Product Category')
axes[1].set_ylabel('Number of Reviews')
axes[1].tick_params(axis='x', rotation=45) # Tilt the labels so they don't overlap

# --------------------------------------------------------------------
# Step 4: Display the Dashboard for graphical representation
# --------------------------------------------------------------------
plt.tight_layout()
plt.show()
