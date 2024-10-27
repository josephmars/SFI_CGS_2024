# Project
## Get data form Reddit API
https://www.jcchouinard.com/reddit-api/
Since the API limits in the number of posts and comments we can get, we decided to use the Archive of Reddit. We need to use Torrent to download the data (predicted to be ~2TB).
To extract the data from Reddit using _academictorrents_ in the Wahab cluster: https://academictorrents.com/docs/downloading.html. Use the command `at-get 9c263fc85366c1ef8f5bb9da0203f4c8c8db75f4`.
- [2005-2023](https://academictorrents.com/details/9c263fc85366c1ef8f5bb9da0203f4c8c8db75f4)
- [All (until 2024-07)](https://github.com/ArthurHeitmann/arctic_shift/blob/master/download_links.md)


### Download data and upload to HPC 
  1. Command used to split files in Windows: https://github.com/anseki/split-win/tree/master. Download the .cmd and .ps1 files to System32/. 
  2. Use the command `split D:\REDDIT_DATA\reddit\submissions\RS_2023-12.zst -size 1gb` to split the files. HPC's limit is 10GB, uploading 1GB parts works the best.
  3. In the HPC Create a folder with the name of the file and upload all the parts there. For instance `RS_2023-12/`
  4. Use the command `cat /home/jmart130/GitHub/SFI_CGS_2024/data/reddit/submissions/RS_2023-12/* > /home/jmart130/GitHub/SFI_CGS_2024/data/reddit/submissions/RS_2023-12.zst` to join the files in the HPC files.

### Data preprocessing
Use the files from this [repository](https://github.com/Watchful1/PushshiftDumps) to preprocess the data.
     1. `single_file.py` decompresses and iterates over a single zst compressed file.
     2. `iterate_folder.py` does the same, but for all files in a folder.
     3. Queries:
      - Getting 1 subreddit: `python combine_folder_multiprocess.py reddit/submissions --field subreddit --value careerguidance --output pushshift2 --processes 20 --file_filter "^RS_2024-07"`
      - Getting all subreddits: `python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2024-04 --file_filter "^RS_2024-04"`
      4. Use `filter_file.py` to convert the compressed .zst files into csv.
      5. Use `query_csv.py` to query the csv files for each month and subreddit into only one.
      6. Use `get_sample.py` to get a sample of the data either by month or by subreddit (proportionally).

## Results
  1. Number of reddits that matches the query on the 10 subreddits from 2022-07 to 2024-07: `7,616,585`
  2. Number of reddits that matches the query on the 1o subreddits and was labeled by Llama 3.1 7B: `18,159`.
  3. We manually labeled 555 with multilabel classification for 3 categories or levels below. From the labeling, we identified that 67 are in level C1, 192 in level C2, and 80 in level C3.
     1. The post talks about task-oriented thoughts, like a new summarization model.
     2. Worker-oriented, meaning how a worker might have been impacted in its work environment.
     3. Workforce, meaning that it affects a huge amount of workers in a specific sector or in general.

## Models training
We trained the models SVM and Random Forest. The models and results are in the `code/analysis/models/` folder. Training results (also in the `analysis.docx` file):
| Random Forest | Precision | Recall | F1-Score | Support |
| C1 Work | 1.00 | 0.10 | 0.18 | 10 |
| C2 Worker | 0.61 | 0.33 | 0.43 | 33 |
| C3 Workforce | 0.00 | 0.00 | 0.00 | 16 |

| SVM | Precision | Recall | F1-Score | Support |
| C1 Work | 0.00 | 0.00 | 0.00 | 10 |
| C2 Worker | 0.69 | 0.27 | 0.39 | 33 |
| C3 Workforce | 0.50 | 0.12 | 0.20 | 16 |

Number of posts predicted per category and model:
| Category | Random Forest | SVM |
| C1 Work | 0 | 10 |
| C2 Worker | 920 | 942 |
| C3 Workforce | 7 | 61 |

Considering that for both models the number of posts predicted for C1 and C3 are very low, we decided to use only C2 for the next steps. This is also reflected in the table of performances where Random Forest struggles with C1 and C3, and SVM with C2. Since the F-1 score for the C2 is higher for Random Forest, we decided to use that model for the analysis.

Topic modeling was done using LDA for 4 datasets:
- Raw data
- Predicted data
- Raw data with C2 Worker
- Predicted data with C2 Worker
The results of the topic modeling are in the `code/analysis/topic_modeling/` folder. The visualizations are in the `plots/` folder. The equations of the topics are in the `equations.txt` file. And the interpretations of the topics are in the analysis file `code/analysis/analysis.docx`.





## Meetings
### Alejandro
1. Do a sentiment analysis to check the change in emotion/fear on the workers
2. Jobs with risk could be a boundary to the perception. Validation OR pushback OR alternative. Is this related to the risk of automation? Variables:
  1.  Profession
  2.  Strategy
  3.  Response (validation/pushback)
3. Word embeddigs if LLMs for labeling does not work. 

## Day 4 - Thu
Scaling theory is a new field (~10 years), and right now it accounts for a lot of noise, but it is evolving on how to flatten up the curves.
Doing interdisciplinary research is difficult, because the researchers want to do different things and somethimes methods are really diverse. So not anything "calls you". Is there danger in there or is it just a defense mechanism?

### Ask me Everything session 10:20
Andrew: You need to really care about the other discipline, otherwise you won't be motivated.
Emma: How do you "fix" or improve a group that is already doing interdisciplinary research but is not that good?
Probably just patience is the best option, and time helps in "smooth things up". 
Rajiv: 


# CGS in Uniandes (in person)

## Day 3 - Wed
15 minutes talk about the project

The power of side projects, some of those turn into bigger ones, so do not underestimate them.

What about the cases when you have discussions with radically different people? 
- It is more difficult, but it can be worth it. Because the "common language" is more difficult to get to.
- They need, however, to be open to discussions, and not them telling you what they think and that they would not change.
- Sometimes the science of others have better solutions than yours, and it is worth talking to them and knowing about it.

https://kumu.io/


### Chris Kempes session 3:45
One can use a principle of scale in Biology and apply it into companies, countries, etc. We need to define the variables like mass.
In the case of a company:
log(assets) would be the x; and log(liability), revenue, would be the y variable.

