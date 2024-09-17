# Split the csv file into smaller files of 100_000 rows each
import os
import pandas as pd

INPUT_FILE_PATH = "/home/jmart130/GitHub/SFI_CGS_2024/data/all_reddit_csv/2022-07.csv"
OUTPUT_FOLDER = "/home/jmart130/GitHub/SFI_CGS_2024/data/all_reddit_csv/split"

def split_csv(input_file, output_folder, chunk_size=100_000):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process the CSV file in chunks
    chunk_iter = pd.read_csv(input_file, chunksize=chunk_size)
    for i, chunk in enumerate(chunk_iter, 1):
        if i % 100 == 0:
            print(f"Processing chunk {i} of {chunk_size}")
        output_file = os.path.join(output_folder, f"{os.path.basename(input_file).split('.')[0]}_{i}.csv")
        chunk.to_csv(output_file, index=False)

    print(f"CSV file split into chunks.")

if __name__ == "__main__":
    split_csv(INPUT_FILE_PATH, OUTPUT_FOLDER)