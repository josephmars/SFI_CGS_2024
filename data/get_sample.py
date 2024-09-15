"""Get a sample of the data in a csv file per subreddit and per month
"""
import pandas as pd
#-----------------
# INPUTS
#-----------------
# Path to the single csv file containing all the data
PATH = "/home/jmart130/GitHub/SFI_CGS_2024/data/all_reddit_csv/filtered_2024-07.csv"
# PATH = "/home/jmart130/GitHub/SFI_CGS_2024/data/10subreddits_csv/2022-07/careerguidance_submissions.csv"
# Path to the folder where the sample csv file will be saved
OUTPUT_PATH = "/home/jmart130/GitHub/SFI_CGS_2024/data/all_reddit_csv/sample_2000_monthly.xlsx"
# Number of rows to get
n = 2000
# Stratify the sample by subreddit or by month, use None to not stratify
stratification_column = 'month'
# If true, the sample will have the same proportion of each subreddit or month as the original data, otherwise the sample will have the same number of rows for each subreddit or month
proportional = True

#---------------

def get_month(x):
    if '-' in x:
        return x.split('-')[0] + '-' + x.split('-')[1]
    else:
        return None
    
def add_month_to_df(df):
    df['month'] = df['created'].astype(str).apply(get_month)
    return df

def get_sample(df, n=1000, stratification_column = 'month'):
    print(f"Getting sample of {n} rows on the column {stratification_column} ...")
    sample = []
    if stratification_column is None:
        for level in df[stratification_column].unique():
            if proportional:
                proportion = int(n * len(df[df[stratification_column] == level]) / len(df))
            else:
                proportion = n // len(df[stratification_column].unique())
            sample.append(df[df[stratification_column] == level].sample(n=proportion))
    else:
        sample.append(df.sample(n))
    return pd.concat(sample, ignore_index=True)

# Save the sample to a csv file
def save_sample(sample, output_path):
    print(f"Saving sample to {output_path} ...")
    sample.to_excel(output_path, index=False)
    
if __name__ == "__main__":
    print(f"Getting sample from {PATH} ...")
    df = pd.read_csv(PATH)
    print("Original data size: ", len(df))
    df = add_month_to_df(df)
    sample = get_sample(df, n, stratification_column)
    save_sample(sample, OUTPUT_PATH)
    print("Done!")