@echo off

:: Set the environment
setlocal

:: Change to the appropriate directory
cd /d C:\Users\joseph\OneDrive - Old Dominion University\GitHub\SFI_CGS_2024

:: Load Python environment
call activate .venv

:: Change to the appropriate directory
cd /d data

rmdir /s /q pushshift_working

:: Run the Python scripts
python combine_folder_multiprocess.py reddit\submissions --field subreddit --value anti-work,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2024-07 --file_filter "^RS_2024-07"
rmdir /s /q pushshift_working

python combine_folder_multiprocess.py reddit\submissions --field subreddit --value antiwork,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2024-05 --file_filter "^RS_2024-05"
rmdir /s /q pushshift_working

python combine_folder_multiprocess.py reddit\submissions --field subreddit --value antiwork,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2024-04 --file_filter "^RS_2024-04"
rmdir /s /q pushshift_working

python combine_folder_multiprocess.py reddit\submissions --field subreddit --value antiwork,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2024-03 --file_filter "^RS_2024-03"
rmdir /s /q pushshift_working

python combine_folder_multiprocess.py reddit\submissions --field subreddit --value antiwork,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2024-02 --file_filter "^RS_2024-02"
rmdir /s /q pushshift_working

python combine_folder_multiprocess.py reddit\submissions --field subreddit --value antiwork,AskReddit,careerguidance,changemyview,Economics,Futurology,jobs,NoStupidQuestions,Showerthoughts,technology --output all_subreddits_2024-01 --file_filter "^RS_2024-01"
rmdir /s /q pushshift_working

:: End
endlocal