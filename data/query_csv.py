"""Script to query the csv files from Reddit data
"""
import os
import csv
from collections import defaultdict

# Path to the folder containing the csv files under a folder for each month
PATH = "/home/jmart130/GitHub/SFI_CGS_2024/data/all_reddit_csv/"

# Path to the folder where the filtered csv files will be saved
OUTPUT_PATH = "/home/jmart130/GitHub/SFI_CGS_2024/data/all_reddit_csv/filtered.csv"

# Query to filter the text
# query = '(ai OR "artificial intelligence" OR chatgpt) AND (job OR jobs OR work OR career OR employment OR profession) AND (replace OR replaced OR replaces OR replacement OR affected OR affect OR affecting OR disappear OR disappearing OR disappeared OR fired OR hiring OR hire OR lose OR lost OR losing OR eliminate OR eliminates OR eliminating OR redundant OR safe OR obsolete OR threaten)'
query = '("ai " OR " ai" OR "artificial intelligence" OR chatgpt) AND (job OR jobs OR work OR career OR employment OR profession OR worker OR workers OR employee OR replace OR replaced OR replaces OR replacement OR affected OR affect OR affecting OR disappear OR disappearing OR disappeared OR fired OR hiring OR hire OR lose OR lost OR losing OR eliminate OR eliminates OR eliminating OR redundant OR safe OR obsolete)'

# Get folder names in PATH
def get_folders():
    print(f"Getting folders in {PATH} ...")
    folder_list = sorted([f for f in os.listdir(PATH) if os.path.isdir(os.path.join(PATH, f))])
    print("Folders found: ", folder_list)
    return folder_list

# Get csv files in a folder
def get_files(folder):
    return [f for f in os.listdir(os.path.join(PATH, folder)) if f.endswith(".csv")]

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

# Concatenate all csv files in a folder while filtering by query (removing unmatching rows)
def concat_files(folder):
    print(f"Processing folder {folder} ...")
    files = get_files(folder)
    result = []
    for file in files:
        with open(os.path.join(PATH, folder, file), 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if match_query(query, str(row.get('text', ''))):
                    result.append(row)
    return result

# Concatenate all csv files in all folders while filtering by query (removing unmatching rows)
def concat_all_files():
    folders = get_folders()
    all_results = []
    for folder in folders:
        all_results.extend(concat_files(folder))
    return all_results

# Save the concatenated data to a csv file
def save_data(data, output_path):
    print(f"Saving filtered data to {output_path} ...")
    if not data:
        print("No data to save.")
        return
    fieldnames = data[0].keys()
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main():
    data = concat_all_files()
    save_data(data, OUTPUT_PATH)

if __name__ == "__main__":    
    main()
    print("Done!")


