import pandas as pd
import numpy as np
import os
import random

products = ['Smartphone', 'Laptop', 'Wireless Mouse', 'Headphones', 'Mechanical Keyboard']
good_reviews = ["Absolutely LOVE this!", "Great battery life.", "Super fast and reliable.", "Highly recommend it.", "Best purchase ever!!"]
bad_reviews = ["Terrible... broke in two days.", "Worst customer service. <br>", "Too loud and clunky.", "DO NOT BUY THIS.", "overpriced garbage."]
neutral = ["It's okay, does the job.", "3/5 stars. Not bad.", "Average product."]

data = []
for i in range(1, 51):
    prod = random.choice(products)
    sentiment_choice = random.choice(['good', 'bad', 'neutral', 'messy'])
    
    if sentiment_choice == 'good':
        review = random.choice(good_reviews)
        rating = random.randint(4, 5)
    elif sentiment_choice == 'bad':
        review = random.choice(bad_reviews)
        rating = random.randint(1, 2)
    elif sentiment_choice == 'neutral':
        review = random.choice(neutral)
        rating = 3
    else: # Injecting messy data for your cleaning script to catch
        review = np.nan if random.random() > 0.5 else "   messy formatting!!! <html tag>   "
        rating = np.nan

    data.append({'Review_ID': i, 'Product': prod, 'Raw_Review': review, 'User_Rating': rating})

df_sample = pd.DataFrame(data)
df_sample.to_csv('mock_reviews.csv', index=False)
print("mock_reviews.csv with 50 rows has been generated!")
print("the file is saved here:", os.path.abspath('mock_reviews.csv'))