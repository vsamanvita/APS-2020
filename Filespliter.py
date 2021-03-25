# Code Snippet to break large files into smaller ones

"""
filetype supported: CSV
filepath: path of the input file(Format:path\\filename.csv)
Note: Use double back slash(\\) in the path so that it reads raw data
split_size: size which you what to break the fileinto(enter the value in bytes)
Replace {path to directory} with the path to the directory where you what the split files to be stored
(Format:path\\directoryname)
"""

import pandas as pd
import math
import os
import sys
filepath="C:\\Users\\VINAYA SAMANVITA\\Desktop\\REVIEW3\\input.csv"
df=pd.read_csv(filepath)
total_size=os.path.getsize(filepath)
split_size=20971520
no_of_files=total_size/split_size
no_of_rows=df.shape[0]//no_of_files
for i,chunk in enumerate(pd.read_csv(filepath, chunksize=no_of_rows)):
    chunk.to_csv('{path to directory}\\input_{}.csv'.format(i), index=False)
