import pandas as pd

reddits_path = '/home/jmart130/GitHub/SFI_CGS_2024/data/10subreddits_csv/filtered.csv'

reddits = pd.read_csv(reddits_path)

# Identify whether each individual reddit it talking about AI taking over jobs using ollama (llama 3.1 7b)
def llm_labeling(text):
    
