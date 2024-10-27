# topic_modeling_raw.py
# Perform topic modeling on the manually labeled Reddit data for each category

import pandas as pd
import nltk
import re
import string
import gensim
from gensim import corpora
import pyLDAvis
import pyLDAvis.gensim_models
from nltk.corpus import stopwords

# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt_tab')

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

def topic_modeling():
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

    for level_name, level_column in levels.items():
        print(f"\nProcessing category: {level_name}")
        # Filter rows where the specific level column is 1
        df_level = df_labeled[df_labeled[level_column] == True].copy()

        # Preprocess the text data
        df_level['tokens'] = df_level['text'].apply(preprocess_text)

        # Remove empty tokens
        df_level = df_level[df_level['tokens'].map(lambda d: len(d)) > 0]

        # Create a dictionary and corpus
        dictionary = corpora.Dictionary(df_level['tokens'])
        corpus = [dictionary.doc2bow(text) for text in df_level['tokens']]

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
        print(f"Top {num_topics} topics for {level_name}:")
        topics = lda_model.print_topics(num_words=10)
        for topic in topics:
            print(topic)

        # Optional: Save the model and dictionary
        lda_model.save(f'/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/topic_modeling/models/{level_name.replace(" ", "_")}_lda_model.gensim')
        dictionary.save(f'/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/topic_modeling/models/{level_name.replace(" ", "_")}_dictionary.gensim')
        
        # Export to HTML using pyLDAvis
        vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
        
        # Save the visualization to an HTML file
        pyLDAvis.save_html(vis, f'/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/topic_modeling/plots/{level_name.replace(" ", "_")}_lda_vis.html')
if __name__ == '__main__':
    topic_modeling()
