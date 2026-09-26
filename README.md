# 📊 AI Customer Review Sentiment Analysis

A Python-based **NLP Sentiment Analysis project** that analyzes customer reviews and classifies them as **Positive** or **Negative** using a pre-trained **DistilBERT** model from Hugging Face.

The project demonstrates a complete NLP pipeline:

**Data Generation → Data Cleaning → Text Preprocessing → AI Sentiment Analysis → Visualization**

---

## 🚀 Features

- Generate a sample dataset containing customer reviews
- Handle missing and invalid data
- Clean and preprocess review text
- Remove HTML tags and special characters
- Convert text to lowercase
- Perform sentiment analysis using **DistilBERT**
- Generate AI confidence scores
- Save processed results to CSV files
- Visualize overall sentiment distribution
- Compare sentiment across different products

---

## 🧠 Technologies Used

- **Python**
- **Pandas** – Data processing
- **NumPy** – Numerical operations
- **Regular Expressions (re)** – Text cleaning
- **Hugging Face Transformers** – NLP model
- **DistilBERT** – Sentiment analysis
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization

---

## 📁 Project Structure

```text
AI-Sentiment-Analysis/
│
├── mock_data.py
├── data_cleaning.py
├── NLP_script.py
├── visualize.py
│
├── mock_reviews.csv
├── preprocessed_reviews.csv
├── final_analyzed_reviews.csv
│
└── README.md
```

---

## 🔄 Project Workflow

### 1. Generate Mock Data

`mock_data.py` creates a dataset containing **50 customer reviews** for products such as:

- Smartphone
- Laptop
- Wireless Mouse
- Headphones
- Mechanical Keyboard

It also intentionally adds missing and messy data for testing the cleaning process.

Run:

```bash
python mock_data.py
```

This generates:

```text
mock_reviews.csv
```

---

### 2. Clean and Preprocess Data

`data_cleaning.py` removes missing reviews and cleans the text.

The preprocessing includes:

- Removing missing reviews
- Converting text to lowercase
- Removing HTML tags
- Removing punctuation and special characters
- Removing unnecessary spaces

The cleaned data is saved as:

```text
preprocessed_reviews.csv
```



Run:

```bash
python data_cleaning.py
```

---

### 3. AI Sentiment Analysis

`NLP_script.py` uses the Hugging Face model:

```text
distilbert-base-uncased-finetuned-sst-2-english
```

The model analyzes each review and produces:

- Sentiment label
- AI confidence score



Example:

```text
Review: Great battery life.
Sentiment: POSITIVE
Confidence: 0.9987
```

Run:

```bash
python NLP_script.py
```

The final results are saved as:

```text
final_analyzed_reviews.csv
```

---

## 📈 Data Visualization

`visualize.py` creates visual representations of the sentiment results.

It includes:

### Overall Sentiment Distribution

Shows the proportion of positive and negative reviews.

### Product-wise Sentiment

Shows the sentiment breakdown for each product category.

The script uses **Matplotlib** and **Seaborn** for visualization.

Run:

```bash
python visualize.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn transformers torch
```

---

## ▶️ Run the Complete Project

Run the scripts in this order:

```bash
python mock_data.py
python data_cleaning.py
python NLP_script.py
python visualize.py
```

The pipeline will generate the required CSV files automatically.

---

## 📂 Generated Files

| File | Purpose |
|---|---|
| `mock_reviews.csv` | Original generated review dataset |
| `preprocessed_reviews.csv` | Cleaned review data |
| `final_analyzed_reviews.csv` | Reviews with AI sentiment and confidence scores |

---

## 🎯 Learning Objectives

This project demonstrates practical implementation of:

- Natural Language Processing
- Text preprocessing
- Sentiment classification
- Transformer-based AI models
- Data cleaning
- Data analysis with Pandas
- Data visualization
- Machine learning workflow

---

## 🔮 Future Improvements

- Add a web interface using Flask or Streamlit
- Allow users to upload their own CSV files
- Add more sentiment categories such as **Neutral**
- Analyze larger real-world datasets
- Add sentiment trends over time
- Create an interactive analytics dashboard
- Compare multiple NLP models

---

## 👨‍💻 Author

**Akshat Gupta**

Computer Science Engineering Student

---

## ⭐ If You Like This Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
