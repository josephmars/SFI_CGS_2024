# eda_combined.py
# Run an Exploratory Data Analysis combining the 3 levels into unified plots

import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import nltk
nltk.download('stopwords')

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

# Initialize DataFrames to collect counts and sentiments per level
counts_df = pd.DataFrame()
sentiment_df = pd.DataFrame()

for level_name, level_column in levels.items():
    # Filter rows where the specific level column is True
    df_level = df_labeled[df_labeled[level_column]].copy()
    
    # Convert 'date' to datetime and set as index
    df_level['date'] = pd.to_datetime(df_level['date'])
    df_level.set_index('date', inplace=True)
    
    # Resample to monthly counts
    df_count = df_level.resample('M').size()
    counts_df[level_name] = df_count
    
    # Calculate sentiment
    df_level['sentiment'] = df_level['text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    # Resample to monthly average sentiment
    df_sentiment = df_level['sentiment'].resample('M').mean()
    sentiment_df[level_name] = df_sentiment

# Plotting the number of posts over time for all categories
plt.figure(figsize=(12, 6))
counts_df.plot()
plt.title('Number of Reddit posts per month by Category')
plt.xlabel('Month')
plt.ylabel('Number of posts')
# Vertical line for ChatGPT release
plt.axvline(pd.to_datetime('2022-11-30'), color='r', linestyle='--')
plt.text(pd.to_datetime('2022-11-30'), counts_df.max().max(), 'Release of ChatGPT', color='r', ha='right', va='center')
plt.legend()
plt.savefig('/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/eda/plots/posts_per_month_combined.png', format='png')
plt.close()

# Plotting the average sentiment over time for all categories
plt.figure(figsize=(12, 6))
sentiment_df.plot()
plt.title('Average Sentiment per month by Category')
plt.xlabel('Month')
plt.ylabel('Average Sentiment')
plt.legend()
plt.savefig('/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/eda/plots/sentiment_per_month_combined.png', format='png')
plt.close()
