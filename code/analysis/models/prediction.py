
# prediction.py
# Uses trained models to predict labels on the unlabeled dataset

import pandas as pd
import pickle
import re
# import nltk
import string

# nltk.download('stopwords') # Only download once
# nltk.download('punkt') # Only download once
# nltk.download('wordnet') # Only download once

def clean_text(text):
    # Same cleaning function used during preprocessing
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    text = text.strip()
    return text

def predict_unlabeled_data():
    # Load the original data
    df = pd.read_excel('/Users/joseph/GitHub/SFI_CGS_2024/data/manually_labeled/llm_validated_reddits_with_false_negatives score 10 coded MPC.xlsx')

    # Only consider rows where 'n' != 1 (those were not labeled)
    df_unlabeled = df[df['n'] != 1].copy()

    # Clean the text data
    df_unlabeled['clean_text'] = df_unlabeled['text'].apply(clean_text)

    # Remove stopwords
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    df_unlabeled['clean_text'] = df_unlabeled['clean_text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

    # Load the saved TF-IDF vectorizer
    with open('/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/models/tfidf_vectorizer.pkl', 'rb') as f:
        tfidf_vectorizer = pickle.load(f)

    # Transform the clean_text using the loaded vectorizer
    X_unlabeled = tfidf_vectorizer.transform(df_unlabeled['clean_text'])

    # Load the trained models
    with open('/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/models/random_forest_model.pkl', 'rb') as f:
        rf_classifier = pickle.load(f)

    with open('/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/models/svm_model.pkl', 'rb') as f:
        svm_classifier = pickle.load(f)

    # Predict using Random Forest
    y_pred_rf = rf_classifier.predict(X_unlabeled)

    # Predict using SVM
    y_pred_svm = svm_classifier.predict(X_unlabeled)
    # Define category names
    category_names = ['C1 Work', 'C2 Worker', 'C3 Workforce']

    # Add predictions to the DataFrame
    for i, category in enumerate(category_names):
        # Random Forest predictions
        df_unlabeled[f'{category} RandomForest'] = y_pred_rf[:, i]
        # SVM predictions
        df_unlabeled[f'{category} SVM'] = y_pred_svm[:, i]

    # Save the DataFrame with predictions
    df_unlabeled.to_excel('/Users/joseph/GitHub/SFI_CGS_2024/data/predictions/unlabeled_data_with_predictions.xlsx', index=False)

    print("Predictions added to the DataFrame and saved.")

if __name__ == '__main__':
    predict_unlabeled_data()