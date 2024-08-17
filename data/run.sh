#!/bin/bash
#SBATCH -p gpu
#SBATCH --gres gpu:1
#SBATCH -c 8

module load container_env python3/2023.2-py310

cd /home/jmart130/GitHub/SFI_CGS_2024/data

rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2022-07 --file_filter "^RS_2022-07"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2022-08 --file_filter "^RS_2022-08"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2022-09 --file_filter "^RS_2022-09"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2022-10 --file_filter "^RS_2022-10"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2022-11 --file_filter "^RS_2022-11"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2022-12 --file_filter "^RS_2022-12"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2023-01 --file_filter "^RS_2023-01"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2023-02 --file_filter "^RS_2023-02"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2023-03 --file_filter "^RS_2023-03"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2023-04 --file_filter "^RS_2023-04"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2023-05 --file_filter "^RS_2023-05"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2023-06 --file_filter "^RS_2023-06"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2023-07 --file_filter "^RS_2023-07"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2023-08 --file_filter "^RS_2023-08"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2023-09 --file_filter "^RS_2023-09"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2023-10 --file_filter "^RS_2023-10"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2023-11 --file_filter "^RS_2023-11"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2023-12 --file_filter "^RS_2023-12"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2024-01 --file_filter "^RS_2024-01"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2024-02 --file_filter "^RS_2024-02"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2024-03 --file_filter "^RS_2024-03"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2024-04 --file_filter "^RS_2024-04"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2024-05 --file_filter "^RS_2024-05"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2024-07 --file_filter "^RS_2024-07"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working