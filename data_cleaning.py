import pandas as pd
import numpy as np
import re

# ---------------------------------------------------------
# Step 1: Load the Dataset
# ---------------------------------------------------------
# Read the CSV file we just generated
df = pd.read_csv('mock_reviews.csv')

print("--- ORIGINAL DATASET (First 5 Rows) ---")
print(df.head())
print("\n")

# ---------------------------------------------------------
# Step 2: Handle Missing & Invalid Data (Cleaning)
# ---------------------------------------------------------
# Drop any rows where the actual review text is missing (NaN)
# A blank review is useless for Sentiment Analysis
df_cleaned = df.dropna(subset=['Raw_Review']).copy()

# Reset the index so our row numbers stay sequential after deleting rows
df_cleaned.reset_index(drop=True, inplace=True)

# ---------------------------------------------------------
# Step 3: Text Preprocessing Engine
# ---------------------------------------------------------
def clean_review_text(text):
    """
    Takes raw, messy review text and standardizes it for the AI model.
    """
    # Ensure the text is treated as a string and make it all lowercase
    text = str(text).lower()
    
    # Remove any stray HTML tags (like <br> or <html>)
    text = re.sub(r'<.*?>', '', text)
    
    # Remove punctuation and special characters (keep only letters and numbers)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    
    # Strip accidental extra spaces at the beginning or end of the sentence
    text = text.strip()
    
    return text

# ---------------------------------------------------------
# Step 4: Apply the Preprocessing
# ---------------------------------------------------------
# Run every single review through our cleaning function and save it to a new column
df_cleaned['Cleaned_Review'] = df_cleaned['Raw_Review'].apply(clean_review_text)

print("--- CLEANED & PREPROCESSED DATA (First 5 Rows) ---")
print(df_cleaned[['Review_ID', 'Raw_Review', 'Cleaned_Review']].head())

# Save this perfectly clean data to a new file for the NLP model to use
df_cleaned.to_csv('preprocessed_reviews.csv', index=False)
print("\nSuccess! Saved as 'preprocessed_reviews.csv'")