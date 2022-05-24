import os
import pandas as pd
import numpy as np
import shutil
import time
import random

# Define color for print
class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

# Define the directories for train and test using User input
path = input("Please enter the directory of 'Alzheimer_s Dataset': ")

# Check if the path is correct 
while os.path.isdir(path + "/Alzheimer_s Dataset") == False:
    path = input("Wrong directory, please enter the correct path: ")
while os.listdir(path + "/Alzheimer_s Dataset")[1] != "test":
    path = input("Wrong directory, please enter the correct path: ")

# Define validation split using User input 
validation_split = int(input("Please enter validation split: "))

# Define paths and image size
path = path + "/Alzheimer_s Dataset"
path_train = path + "/train/"
path_test = path + "/test/"
IMAGE_SIZE = [176, 208]

# Remove the test dataset
if os.path.isdir(path_test) == True:
    shutil.rmtree(path_test, ignore_errors=True)
    shutil.rmtree(path_test, ignore_errors=True)
    if os.path.isdir(path_test) == False:
        print("Successfully removed 'test' data")
        time.sleep(1)
else:
    print("No Test data directory found")
    time.sleep(1)

print("-" * 35)

# Define new and old folder names
old_folders = ["NonDemented", "VeryMildDemented", "MildDemented", "ModerateDemented"]
new_folders = ["1_not_demented", "2_very_mild_demented", "3_mild_demented", "4_moderate_demented"]

# Create directory for validation set
if os.path.isdir(path + "/validation") == False:
    os.mkdir(path + "/validation")
    print("Successfully created 'validation' folder")
    time.sleep(1)
else:
    print("'Validation' folder already exists")
    time.sleep(1)

# Create subfolders for validation set
for i in new_folders:
    if os.path.isdir(path + "/validation/" + i) == False:
        os.mkdir(path + "/validation/" + i)
        print(f"Successfully created '{i}' for 'validation' folder")
        time.sleep(1)
    else:
        print(f"'{i}' for 'validation' folder already exists")
        time.sleep(1) 

# renaming directories
for i in range(0, len(old_folders)):
    if os.path.isdir(path_train + old_folders[i]) == True:
        os.rename(path_train + old_folders[i], path_train + new_folders[i])
        print(f"'{old_folders[i]}' --> '{new_folders[i]}' \u2714")
        time.sleep(1) 
    else:
        print(f"'{old_folders[i]}' already renamed.")
        time.sleep(1) 
        continue

print("-" * 35)

# Moving percentage of validation split from train to validation folder
for classes in new_folders:
    if len(os.listdir(path + "/validation/" + classes)) > 0:
        print(f"Folder '{classes}' not empty. Please remove all files and try again")
        time.sleep(1) 
    else:
        image_list = os.listdir(path_train + classes)
        random.shuffle(image_list)
        for file in range (0, int((len(image_list) / 100) * validation_split) + 1):
            shutil.move(path_train + classes + "/" + image_list[file], path + "/validation/" + classes + "/" + image_list[file])
        print(f"Successfully moved {int((len(image_list) / 100) * validation_split)} images from 'train' to 'validation folder' for {classes}")
        time.sleep(1) 

# Print success message
print(f"{bcolors.OKGREEN}Successfully created correct folder structure. Use 'tf.keras.preprocessing.image_dataset_from_directory' to load the data properly{bcolors.ENDC}")
time.sleep(1) 
print("-" * 35)

# Show final folder structure
print("")
print("Folder structure")
print("")
print("-" * 35)
data = [[len(os.listdir(path + "/train/" + new_folders[0])), len(os.listdir(path + "/validation/" + new_folders[0]))],
        [len(os.listdir(path + "/train/" + new_folders[1])), len(os.listdir(path + "/validation/" + new_folders[1]))],
        [len(os.listdir(path + "/train/" + new_folders[2])), len(os.listdir(path + "/validation/" + new_folders[2]))],
        [len(os.listdir(path + "/train/" + new_folders[3])), len(os.listdir(path + "/validation/" + new_folders[3]))]]
headers=["    Train", "    Validation"]
rows=["Not demented", "Very mild demented", "Mild demented", "Moderate demented"]
print(pd.DataFrame(data, rows, headers))