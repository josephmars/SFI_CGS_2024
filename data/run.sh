#!/bin/bash
#SBATCH -p gpu
#SBATCH --gres gpu:1
#SBATCH -c 8

module load container_env python3/2023.2-py310

cd /home/jmart130/GitHub/SFI_CGS_2024/data

rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working

crun.python3 -p ~/envs/default-python3-2023.2-py310 python combine_folder_multiprocess.py reddit/submissions --output all_reddit_csv/2022-07 --file_filter "^RS_2022-07"
rm -rf /home/jmart130/GitHub/SFI_CGS_2024/data/pushshift_working
