import pandas as pd
import subprocess
import time 
from numpy import nan


reddits_path = '/Users/joseph/GitHub/SFI_CGS_2024/data/all_subreddits/filtered.csv' # Will be ignored if checkpoint is True
filtered_path = '/Users/joseph/GitHub/SFI_CGS_2024/data/all_reddits/llm_validated_reddits_with_false_negatives.xlsx' # Will be used as input if checkpoint is True
examples_path = '/Users/joseph/GitHub/SFI_CGS_2024/code/labeling/examples.txt'
checkpoint = True

def run_llama(prompt):
    """
    Runs the LLaMA model using Ollama with the given prompt.

    Args:
        prompt (str): The input prompt for the model.

    Returns:
        str: The output from the model or error message if any.
    """
    try:
        # Running the Ollama command and capturing the output
        result = subprocess.run(
            ["ollama", "run", "llama3.1", prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Check if the command was successful
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error: {result.stderr}"

    except Exception as e:
        return f"Exception occurred: {str(e)}"

def import_data(path):
    if path.endswith('.csv'):
        return pd.read_csv(path)
    elif path.endswith('.xlsx'):
        return pd.read_excel(path)
    else:
        raise ValueError("Unsupported file format. Please use either CSV or Excel files.")

def export(df, path):
    if path.endswith('.csv'):
        df.to_csv(path, index=False)
    elif path.endswith('.xlsx'):
        df.to_excel(path, index=False)


# # Identify whether each individual reddit it talking about AI taking over jobs using ollama (llama 3.1 7b)
def llm_labeling_validation(reddit, max_retries=1):
    with open(examples_path, 'r') as file:
        examples = file.readlines()
    examples_str = "\n".join([example.strip() for example in examples])
    prompt = f"Is the following reddit about AI taking over jobs? (TRUE or FALSE). Do not include any other information in your response, limit your response to just TRUE or FALSE. These are few examples of reddit posts that are and are not about AI taking over jobs. Use them to help you label the data.\n---------\nExamples:\n{examples_str}\n\n---------\nReddit:\n{reddit}"
    output = run_llama(prompt)
    n_retries = 0
    while output.strip().upper().replace(".", "") not in ["TRUE", "FALSE"] and n_retries < max_retries:
        print(f"Invalid response, retrying ({n_retries+1}/{max_retries})...")
        prompt = run_llama(f"Modify this prompt to make it more clear. I need an answer of TRUE or FALSE but I am getting some other response.\nPrompt:\n{prompt}. \nThis is the output I am getting: {output}")
        output = run_llama(prompt)
        n_retries += 1
        
    if output.strip().upper().replace(".", "") not in ["TRUE", "FALSE"]:
        print(f"Failed to get a valid response after {n_retries} retries. set to FALSE.")
        return "FALSE"
    else:
        return output.strip().upper().replace(".", "")

def run_llm_validation(logging=100, exporting=300, resting=300, rest_time=60):
    try:
        if checkpoint:
            reddits = import_data(filtered_path)
        else:
            reddits = import_data(reddits_path)
            reddits['valid'] = "NaN"
            
        start_time = time.time()
        n_labeled = 0
        for index, row in reddits.iterrows():
            reddit_text = str(row['text'])
            empty = True
            if str(row['valid']).strip().upper() not in ["TRUE", "FALSE"]:
                # print(f"Processing row {index}...")
                empty = False
                output = llm_labeling_validation(reddit_text, max_retries=0)
                reddits.at[index, 'valid'] = output
                n_labeled += 1
            
            if index % logging == 0 and not empty: # Log the progress
                elapsed_time = time.time() - start_time
                expected_time = (elapsed_time/(n_labeled)) * (len(reddits)-index)
                print(f"Processed {index}/{len(reddits)} rows in {elapsed_time/60:.2f} minutes, expected {expected_time/60:.2f} minutes remaining.")
            if index % exporting == 0 and index != 0 and not empty: # Export the data checkpoint 
                export(reddits, filtered_path)
                print(f"Exported {index} rows to {filtered_path}")
            if index % resting == 0 and index != 0 and not empty: # Rest the GPU/CPU to avoid overloading
                print(f"Resting for {rest_time} seconds...")
                time.sleep(rest_time)
        print("Done!")
        
        export(reddits, filtered_path)
    except KeyboardInterrupt:
        print("\nProcess interrupted! Saving progress...")
        export(reddits, filtered_path)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

        
# Example usage
if __name__ == "__main__":
    run_llm_validation(logging=25, exporting=100, resting=200, rest_time=20)