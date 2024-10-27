# eda.py
# Run an Exploratory Data Analysis on the Reddit data with 3 levels

import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
# import nltk
# nltk.download('stopwords') # Only download once
# nltk.download('punkt') # Only download once
from nltk.corpus import stopwords

# Load the labeled data
df = pd.read_excel('/Users/joseph/GitHub/SFI_CGS_2024/data/manually_labeled/llm_validated_reddits_with_false_negatives score 10 coded MPC.xlsx')

# Only consider rows where 'n' == 1 (those were labeled)
df_labeled = df[df['n'] == 1]

# Define the levels and their corresponding column names
levels = {
    'C1 Work': 'C1 Work',
    'C2 Worker': 'C2 Worker',
    'C3 Workforce': 'C3 Workforce'
}

stop_words = set(stopwords.words('english'))

# Iterate over each level to perform EDA
for level_name, level_column in levels.items():
    # Filter rows where the specific level column is True
    df_level = df_labeled[df_labeled[level_column]].copy()

    print(f"Number of posts in {level_name}: {len(df_level)}")

    # Convert 'date' column to datetime
    df_level['date'] = pd.to_datetime(df_level['date'])

    # Set 'date' as index
    df_level.set_index('date', inplace=True)

    # 1) Create a line plot of the number of posts over time (per month)
    plt.figure(figsize=(12, 6))
    df_count = df_level.resample('M').size()

    # Plot the data
    df_count.plot()
    plt.title(f'Number of Reddit posts in {level_name} per month')
    plt.xlabel('Month')
    plt.ylabel('Number of posts')

    # Create a vertical line on November 30, 2022 (Release of ChatGPT)
    plt.axvline(pd.to_datetime('2022-11-30'), color='r', linestyle='--')
    plt.text(pd.to_datetime('2022-11-30'), df_count.max(), 'Release of ChatGPT', color='r', ha='right', va='center')

    # Save the plot
    plt.savefig(f'/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/eda/plots/{level_name.replace(" ", "_")}_posts_per_month.png', format='png')
    plt.close()

    # 2) Create a line plot of the average sentiment per month
    df_level['sentiment'] = df_level['text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

    # Resample to monthly mean sentiment
    df_sentiment = df_level['sentiment'].resample('M').mean()

    # Plot average sentiment over time
    plt.figure(figsize=(12, 6))
    df_sentiment.plot()
    plt.title(f'Average sentiment of Reddit posts in {level_name} per month')
    plt.xlabel('Month')
    plt.ylabel('Average sentiment')

    # Create a vertical line on November 30, 2022 (Release of ChatGPT)
    plt.axvline(pd.to_datetime('2022-11-30'), color='r', linestyle='--')
    plt.text(pd.to_datetime('2022-11-30'), df_sentiment.max(), 'Release of ChatGPT', color='r', ha='right', va='center')

    # Save the plot
    plt.savefig(f'/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/eda/plots/{level_name.replace(" ", "_")}_sentiment_per_month.png', format='png')
    plt.close()

    # 3) Word Frequency Analysis
    # Remove stop words and tokenize
    df_level['clean_text'] = df_level['text'].apply(lambda x: ' '.join([word.lower() for word in str(x).split() if word.lower() not in stop_words]))

    # Get the top 6 most frequent words
    all_words = df_level['clean_text'].str.split().explode()
    top_words = all_words.value_counts().head(6).index.tolist()

    print(f"Top 6 words in {level_name}:\n{top_words}\n")

    # Create subplots for frequency of top words over time
    fig, axes = plt.subplots(3, 2, figsize=(20, 12))
    axes = axes.flatten()

    for i, word in enumerate(top_words):
        ax = axes[i]
        # Use word boundaries to match exact words
        word_count_over_time = df_level[df_level['clean_text'].str.contains(r'\b' + word + r'\b')].resample('M').size()
        word_count_over_time.plot(ax=ax, title=f'Frequency of "{word}" over time in {level_name}')
        ax.set_xlabel('Month')
        ax.set_ylabel('Count')

    plt.tight_layout()
    plt.savefig(f'/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/eda/plots/{level_name.replace(" ", "_")}_top_words_per_month.png', format='png')
    plt.close()
