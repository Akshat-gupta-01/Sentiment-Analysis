import pandas as pd
from transformers import pipeline

# ---------------------------------------------------------
# Step 1: Load the Preprocessed Data
# ---------------------------------------------------------
# Loading the clean data we generated in the previous script
df = pd.read_csv('preprocessed_reviews.csv')

# ---------------------------------------------------------
# Step 2: Initialize the AI Model Pipeline
# ---------------------------------------------------------
print("Loading Hugging Face NLP model... (This may take a moment)")

# We specifically define the model. 
# DistilBERT is chosen because it is faster and lighter than full BERT, 
# while retaining over 95% of its language understanding capabilities.
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    truncation=True, # Critical: Truncates reviews that are too long for the AI to read
    max_length=512
)

# ---------------------------------------------------------
# Step 3: Define the Processing Function
# ---------------------------------------------------------
def analyze_sentiment(text):
    """
    Passes the cleaned text into the Hugging Face model and extracts 
    both the sentiment label and the AI's confidence score.
    """
    try:
        # The pipeline returns a list with a dictionary: [{'label': 'POSITIVE', 'score': 0.99}]
        result = sentiment_analyzer(str(text))[0]
        
        # We return it as a Pandas Series so it easily splits into two new dataframe columns
        return pd.Series([result['label'], round(result['score'], 4)])
    except Exception as e:
        # Failsafe in case a weird string breaks the model
        return pd.Series(["ERROR", 0.0])

# ---------------------------------------------------------
# Step 4: Run the Inference
# ---------------------------------------------------------
print("Analyzing sentiment for all reviews...")

# Apply the function to the 'Cleaned_Review' column and create two new columns for the results
df[['AI_Sentiment', 'AI_Confidence_Score']] = df['Cleaned_Review'].apply(analyze_sentiment)

print("\n--- FINAL NLP SENTIMENT RESULTS (First 10 Rows) ---")
# Showing the raw text next to the AI's prediction so you can verify accuracy
print(df[['Raw_Review', 'AI_Sentiment', 'AI_Confidence_Score']].head(10))

# ---------------------------------------------------------
# Step 5: Export for Visualization
# ---------------------------------------------------------
df.to_csv('final_analyzed_reviews.csv', index=False)
print("\nSuccess! Pipeline complete. Data saved as 'final_analyzed_reviews.csv'")