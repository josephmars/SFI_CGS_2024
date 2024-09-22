# Run a Exploratory Data Analysis on the Reddit data

import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import numpy as np
import nltk
nltk.download('stopwords')

# Load the data
df = pd.read_excel('/Users/joseph/GitHub/SFI_CGS_2024/data/all_reddits/llm_validated_reddits_fewshot.xlsx')

df_valid = df[df['valid'] == True]

print("Number of valid reddits: ", len(df_valid))

# 1) Create a line plot of the number of valid reddits over time (per month)
plt.figure(figsize=(12, 6))  # Create a new figure with specified size
df_valid_count = df_valid.copy()
df_valid_count['date'] = pd.to_datetime(df_valid_count['date'])
df_valid_count.set_index('date', inplace=True)
df_valid_count['count'] = 1
df_valid_count = df_valid_count.resample('M').sum()

# Plot the data
df_valid_count['count'].plot()
plt.title('Number of Reddit posts about AI taking over jobs per month')
plt.xlabel('Month')
plt.ylabel('Number of posts')

# Create an vertical line on November 30 2022 (Release of ChatGPT)
plt.axvline(x='2022-11-30', color='r', linestyle='--')
plt.text('2022-11-30', df_valid_count['count'].loc['2022-11-30'], 'Release of ChatGPT', color='r', ha='right', va='center')

# Save to png   
plt.savefig('/Users/joseph/GitHub/SFI_CGS_2024/code/eda/reddit_posts_per_month.png', format='png')
plt.close()  # Close the current figure



# 2) Create a line plot of the average sentiment per month (using TextBlob's sentiment analyzer)

df_valid_sentiment = df_valid.copy()
df_valid_sentiment['date'] = pd.to_datetime(df_valid_sentiment['date'])
df_valid_sentiment.set_index('date', inplace=True)

df_valid_sentiment['sentiment'] = df_valid_sentiment['text'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Filter for only numeric columns before resampling and calculating mean
numeric_columns = df_valid_sentiment.select_dtypes(include=[np.number]).columns
df_valid_sentiment = df_valid_sentiment[numeric_columns].resample('ME').mean()

# No need for rolling mean if we're already calculating monthly average
plt.figure(figsize=(12, 6))
df_valid_sentiment['sentiment'].plot(kind='line')
plt.title('Average sentiment of Reddit posts about AI taking over jobs per month')
plt.xlabel('Month')
plt.ylabel('Average sentiment')

# Create a vertical line on November 30 2022 (Release of ChatGPT)
plt.axvline(x='2022-11-30', color='r', linestyle='--')
plt.text('2022-11-30', df_valid_sentiment['sentiment'].loc['2022-11-30'], 'Release of ChatGPT', color='r', ha='right', va='center')

plt.savefig('/Users/joseph/GitHub/SFI_CGS_2024/code/eda/reddit_posts_sentiment_per_month.png', format='png')
plt.close()  # Close the second figure


# 3) Create 6 subplots of the frequency of the top 6 most frequent words over time (per month)
# Each subplot will show the frequency of a different word over time

# Tokenize the text data
df_valid_words = df_valid.copy()
df_valid_words['date'] = pd.to_datetime(df_valid_words['date'])
df_valid_words.set_index('date', inplace=True)

# Remove stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
df_valid_words['text'] = df_valid_words['text'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in stop_words]))

# Get the top 6 most frequent words
top_words = df_valid_words['text'].str.split().explode().value_counts().head(6).index

# Create subplots
fig, axes = plt.subplots(3, 2, figsize=(20, 12))

for i, word in enumerate(top_words):
    ax = axes[i // 2, i % 2]
    df_valid_words[df_valid_words['text'].str.contains(word)]['text'].resample('M').count().plot(ax=ax, title=f'Frequency of "{word}" over time')

plt.savefig('/Users/joseph/GitHub/SFI_CGS_2024/code/eda/top_6_frequent_words_per_month.png', format='png')
plt.close()  # Close the fourth figure


