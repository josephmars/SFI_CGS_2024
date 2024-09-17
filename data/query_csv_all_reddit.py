"""Script to query the csv files from Reddit data for all reddit
"""
import os
import pandas as pd
import time
# Path to the folder containing the csv files
PATH = "/home/jmart130/GitHub/SFI_CGS_2024/data/all_reddit_csv/"

# Path to the folder where the filtered csv files will be saved
OUTPUT_PATH = "/home/jmart130/GitHub/SFI_CGS_2024/data/all_reddit_csv/filtered_all_reddit.csv"

# Query to filter the text
# query = '(ai OR "artificial intelligence" OR chatgpt) AND (job OR jobs OR work OR career OR employment OR profession) AND (replace OR replaced OR replaces OR replacement OR affected OR affect OR affecting OR disappear OR disappearing OR disappeared OR fired OR hiring OR hire OR lose OR lost OR losing OR eliminate OR eliminates OR eliminating OR redundant OR safe OR obsolete OR threaten)'
query = '("ai " OR " ai" OR "artificial intelligence" OR chatgpt) AND (job OR jobs OR work OR career OR employment OR profession OR worker OR workers OR employee OR replace OR replaced OR replaces OR replacement OR affected OR affect OR affecting OR disappear OR disappearing OR disappeared OR fired OR hiring OR hire OR lose OR lost OR losing OR eliminate OR eliminates OR eliminating OR redundant OR safe OR obsolete)'

# Get csv files in a folder
def get_files():
    # return [f for f in os.listdir(PATH) if f.endswith(".csv")]
    return ['2024-01.csv', '2024-02.csv', '2024-03.csv', '2024-04.csv', '2024-05.csv', '2024-06.csv', '2024-07.csv']

# Check if a text matches a query
def match_query(query, text, exact_match=False):
    ands = [x.replace('(', '').replace(')', '').replace('"', '') for x in query.split(' AND ')]
    for and_terms in ands:
        ors = and_terms.split(' OR ')
        for or_term in ors:
            if exact_match:
                if or_term in text:
                    break
            else:
                if or_term.lower() in text.lower():
                    break
        else:
            return False
    return True

# Save the concatenated dataframe to a csv file
def save_df(df, output_path):
    print(f"Saving filtered data to {output_path} ...")
    df.to_csv(output_path, index=False)


# Filter all files and save them in individual files
def filter_files():
    start_time = time.time()
    files = get_files()
    print(f"Number of files received to filter: {len(files)}")
    print(f"Filtering files {files} ...")
    
    chunk_size = 100_000  # Adjust this value based on your system's memory capacity
    
    for file in files:
        print(f"Filtering file {file} ...")
        file_start_time = time.time()
        output_file = os.path.join(PATH, f"filtered_{file}")
        
        # Use chunks to read and process the CSV file
        chunks = pd.read_csv(os.path.join(PATH, file), chunksize=chunk_size)
        
        for i, chunk in enumerate(chunks):
            chunk['match'] = chunk['text'].apply(lambda x: match_query(query, str(x)))
            filtered_chunk = chunk[chunk['match'] == True]
            
            # Save the filtered chunk, appending if not the first chunk
            mode = 'w' if i == 0 else 'a'
            header = i == 0
            filtered_chunk.to_csv(output_file, mode=mode, header=header, index=False)
        
        print(f"Filtered file {file} in {(time.time() - file_start_time)/60:.2f} minutes")
    
    end_time = time.time()
    print(f"Time taken to filter {len(files)} files: {(end_time - start_time)/60:.2f} minutes")

# Concatenate all csv files in a folder while filtering by query (removing unmatching rows)
# def concat_files():
#     files = get_files()
#     dfs = [pd.read_csv(os.path.join(PATH, f)) for f in files]
#     print(f"Number of files received to concatenate and query: {len(dfs)}")
#     filtered_dfs = []
#     for df in dfs:
#         print(f"Processing and querying file {df} ...")
#         df['match'] = df['text'].apply(lambda x: match_query(query, str(x)))
#         filtered_df = df[df['match'] == True]
#         filtered_dfs.append(filtered_df)
#     # Concatenate all filtered DataFrames into one
#     result_df = pd.concat(filtered_dfs, ignore_index=True)

#     return result_df
  

if __name__ == "__main__":    
    filter_files()
    print("Done!")

