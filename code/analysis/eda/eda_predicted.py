# eda_predicted.py
# Run an Exploratory Data Analysis on the Reddit data using predicted labels

import pandas as pd
import matplotlib.pyplot as plt
import re
from textblob import TextBlob
# import nltk
import os
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords

# Load the predicted data
df = pd.read_excel('/Users/joseph/GitHub/SFI_CGS_2024/data/predictions/unlabeled_data_with_predictions.xlsx')

# Only consider posts where 'C2 Worker RandomForest' == 1
df_predicted = df[df['C2 Worker RandomForest'] == 1].copy()

print(f"Number of posts predicted as 'C2 Worker': {len(df_predicted)}")

# Convert 'date' column to datetime
df_predicted['date'] = pd.to_datetime(df_predicted['date'])

# Set 'date' as index
df_predicted.set_index('date', inplace=True)

# Ensure the output directory exists
output_dir = '/Users/joseph/GitHub/SFI_CGS_2024/code/analysis/eda/plots/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 1) Create a line plot of the number of posts over time (per month)
plt.figure(figsize=(12, 6))
df_count = df_predicted.resample('M').size()

# Plot the data
df_count.plot()
plt.title('Number of Reddit posts predicted as C2 Worker per month')
plt.xlabel('Month')
plt.ylabel('Number of posts')

# Create a vertical line on November 30, 2022 (Release of ChatGPT)
plt.axvline(pd.to_datetime('2022-11-30'), color='r', linestyle='--')
plt.text(pd.to_datetime('2022-11-30'), df_count.max(), 'Release of ChatGPT', color='r', ha='right', va='center')

# Save the plot
plt.savefig(os.path.join(output_dir, 'C2_Worker_predicted_posts_per_month.png'), format='png')
plt.close()

# 2) Create a line plot of the average sentiment per month
df_predicted['sentiment'] = df_predicted['text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Resample to monthly mean sentiment
df_sentiment = df_predicted['sentiment'].resample('M').mean()

# Plot average sentiment over time
plt.figure(figsize=(12, 6))
df_sentiment.plot()
plt.title('Average sentiment of Reddit posts predicted as C2 Worker per month')
plt.xlabel('Month')
plt.ylabel('Average sentiment')

# Create a vertical line on November 30, 2022 (Release of ChatGPT)
plt.axvline(pd.to_datetime('2022-11-30'), color='r', linestyle='--')
plt.text(pd.to_datetime('2022-11-30'), df_sentiment.max(), 'Release of ChatGPT', color='r', ha='right', va='center')

# Save the plot
plt.savefig(os.path.join(output_dir, 'C2_Worker_predicted_sentiment_per_month.png'), format='png')
plt.close()

# 3) Word Frequency Analysis
# Remove stop words and tokenize
stop_words = set(stopwords.words('english'))
df_predicted['clean_text'] = df_predicted['text'].apply(lambda x: ' '.join([word.lower() for word in str(x).split() if word.lower() not in stop_words]))

# Get the top 6 most frequent words
all_words = df_predicted['clean_text'].str.split().explode()
top_words = all_words.value_counts().head(6).index.tolist()

print(f"Top 6 words in predicted 'C2 Worker' posts:\n{top_words}\n")

# Create subplots for frequency of top words over time
fig, axes = plt.subplots(3, 2, figsize=(20, 12))
axes = axes.flatten()

for i, word in enumerate(top_words):
    ax = axes[i]
    # Use word boundaries to match exact words
    word_count_over_time = df_predicted[df_predicted['clean_text'].str.contains(r'\b' + re.escape(word) + r'\b')].resample('M').size()
    word_count_over_time.plot(ax=ax, title=f'Frequency of "{word}" over time')
    ax.set_xlabel('Month')
    ax.set_ylabel('Count')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'C2_Worker_predicted_top_words_per_month.png'), format='png')
plt.close()
