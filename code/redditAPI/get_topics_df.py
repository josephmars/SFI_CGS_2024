import pandas as pd
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer

# Example loading from a CSV file
df = pd.read_excel("../data/1000_per_subreddit/long_query subreddit_Economics sort_new t_all n_24.xlsx")

texts = df['Body'].astype(str).tolist()
# Initialize BERTopic model
topic_model = BERTopic(calculate_probabilities=True)

# Fit the model to your texts
print("Training model...")
topics, probs = topic_model.fit_transform(texts)

# Get the topics with their respective words
topics_overview = topic_model.get_topic_info()

# Print topics overview
print(topics_overview)

# Access words of a specific topic (e.g., topic 0)
print(topic_model.get_topic(0))

# Plot topics
# topic_model.visualize_topics()

# Plot topic probability distribution
# topic_model.visualize_distribution(probs[0])

# Save the model
topic_model.save("bertopic_model")

# Load the model
loaded_model = BERTopic.load("bertopic_model")
topic_names = {}
for i in range(len(topics_overview)):
    topic_names[topics_overview['Topic'][i]] = topics_overview['Name'][i]

df['Topic'] = topics
df['Topic_name'] = df['Topic'].map(topic_names)

df.to_excel("../data/1000_per_subreddit/Economics_topics.xlsx", index=False)