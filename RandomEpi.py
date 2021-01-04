#Author - Raghav Agrawal
#Task - Plays a random file from your pc

import os
import random

pth = r"path to folder" # path of the folder which contains the file to be played

os.chdir(pth) ## changing the current directory to the folder which contains the playable file

folder_name = random.choice(os.listdir())  ## selecting a random folder for a season 
 
folder_path = str(os.path.realpath(folder_name)) ## obtaining the path of the file to be played

os.chdir(folder_path) ## making the current directory to playable media directory 

file_name = random.choice(os.listdir()) ## selecting a random file from a sequence

print("Any Random file will start playing")

os.system("start " + file_name) ## command to play the media ## for windows
#  os.system("open " + file_name) ## command to play the media ## for Mac



