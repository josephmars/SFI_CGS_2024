# preprocessing.py
# Handles data preprocessing for the Reddit dataset

import pandas as pd
import numpy as np
import re
# import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# nltk.download('stopwords') # Only download once
# nltk.download('punkt') # Only download once
# nltk.download('wordnet') # Only download once

def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Remove extra whitespace
    text = text.strip()
    return text

def preprocess_data():
    # Load the labeled data
    df = pd.read_excel('/Users/joseph/GitHub/SFI_CGS_2024/data/manually_labeled/llm_validated_reddits_with_false_negatives score 10 coded MPC.xlsx')

    # Only consider rows where 'n' == 1 (those were labeled)
    df_labeled = df[df['n'] == 1].copy()

    # Define the levels and their corresponding column names
    levels = {
        'C1 Work': 'C1 Work',
        'C2 Worker': 'C2 Worker',
        'C3 Workforce': 'C3 Workforce'
    }

    # Keep only necessary columns
    df_labeled = df_labeled[['text', 'date'] + list(levels.values())]

    # Fill NaN values in label columns with 0
    df_labeled[list(levels.values())] = df_labeled[list(levels.values())].fillna(0)

    # Convert label columns to integers (if they aren't already)
    df_labeled[list(levels.values())] = df_labeled[list(levels.values())].astype(int)

    # Clean the text data
    df_labeled['clean_text'] = df_labeled['text'].apply(clean_text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    df_labeled['clean_text'] = df_labeled['clean_text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

    # Handle multilabels
    df_labeled['labels'] = df_labeled[list(levels.values())].values.tolist()

    # Create a binary matrix for labels
    df_labeled['labels'] = df_labeled['labels'].apply(lambda x: [int(i) for i in x])

    # Prepare the TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer(max_features=5000)

    # Fit and transform the clean_text
    X = tfidf_vectorizer.fit_transform(df_labeled['clean_text'])

    # Convert labels to a NumPy array
    y = np.array(df_labeled['labels'].tolist())

    # Save the preprocessed data and vectorizer
    with open('/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/models/preprocessed_data.pkl', 'wb') as f:
        pickle.dump((X, y), f)

    with open('/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/models/tfidf_vectorizer.pkl', 'wb') as f:
        pickle.dump(tfidf_vectorizer, f)

    print("Preprocessing complete. Data and vectorizer saved.")

if __name__ == '__main__':
    preprocess_data()
