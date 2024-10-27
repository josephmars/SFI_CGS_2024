# topic_modeling_predicted.py
# Perform topic modeling on the predicted C2 Worker category in the predicted data

import pandas as pd
import nltk
import re
import string
import gensim
from gensim import corpora
from nltk.corpus import stopwords
import pyLDAvis
import pyLDAvis.gensim_models

# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt')

def preprocess_text(text):
    # Lowercase
    text = text.lower()
    # Remove URLs and HTML tags
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    # Remove punctuation and numbers
    text = text.translate(str.maketrans('', '', string.punctuation + string.digits))
    # Tokenize
    tokens = nltk.word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Lemmatization
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

def topic_modeling_predicted():
    # Load the predicted data
    df = pd.read_excel('/Users/joseph/GitHub/SFI_CGS_2024/data/predictions/unlabeled_data_with_predictions.xlsx')

    # Only consider posts where 'C2 Worker RandomForest' == 1
    df_predicted = df[df['C2 Worker RandomForest'] == 1].copy()

    print(f"Number of posts predicted as 'C2 Worker': {len(df_predicted)}")

    # Preprocess the text data
    df_predicted['tokens'] = df_predicted['text'].apply(preprocess_text)

    # Remove empty tokens
    df_predicted = df_predicted[df_predicted['tokens'].map(lambda d: len(d)) > 0]

    # Create a dictionary and corpus
    dictionary = corpora.Dictionary(df_predicted['tokens'])
    corpus = [dictionary.doc2bow(text) for text in df_predicted['tokens']]

    # Build the LDA model
    num_topics = 5  # You can adjust the number of topics
    lda_model = gensim.models.LdaModel(corpus=corpus,
                                       id2word=dictionary,
                                       num_topics=num_topics,
                                       random_state=42,
                                       update_every=1,
                                       chunksize=100,
                                       passes=10,
                                       alpha='auto',
                                       per_word_topics=True)

    # Print the topics
    print(f"Top {num_topics} topics for predicted C2 Worker:")
    topics = lda_model.print_topics(num_words=10)
    for topic in topics:
        print(topic)

    # Optional: Save the model and dictionary
    lda_model.save('/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/topic_modeling/models/C2_Worker_predicted_lda_model.gensim')
    dictionary.save('/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/topic_modeling/models/C2_Worker_predicted_dictionary.gensim')
    
    # Export to HTML using pyLDAvis
    vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
    
    # Save the visualization to an HTML file
    pyLDAvis.save_html(vis, '/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/topic_modeling/plots/C2_Worker_predicted_lda_vis.html')

if __name__ == '__main__':
    topic_modeling_predicted()
