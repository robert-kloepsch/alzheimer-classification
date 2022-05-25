import pandas as pd
import os
import glob
from sklearn.model_selection import train_test_split

#load csv data to get the ID and class/target
# !!!win and mac pathing is different (you have to add YOUR correct path)!!!
#this is for windows
metaData = pd.read_csv("../data/OASIS/oasis_cross-sectional.csv")
# MR2-->MR1 in oasis_cross-sectional.csv
# #this is for mac
metaData = metaData[["ID","CDR"]]

# # imputing missing 0
metaData.CDR[metaData.CDR.isna() == True] = 0

#get file names
path = "../data/OASIS/3D/"
path_list = glob.glob(path + '*.img')
#create file list matching the path_list
t = pd.DataFrame(path_list)
#merge metadata dataframe with file list on ID
f = lambda x: x[-13:-4] + '_MR1' #merge on first 13 letters (eg "OAS1_0001_MR1")
t["ID"]=t[0].apply(f)

metaData = pd.merge(metaData, t,on="ID", how="left")
metaData = metaData.rename(columns={0:"file"}).reset_index()
metaData = metaData.dropna()

X = metaData["file"]
y = metaData["CDR"]
X_train, X_test, y_train, y_test = train_test_split(X,y, stratify=y, random_state=10)
meta_train = pd.DataFrame(index=range(len(X_train)))
meta_test = pd.DataFrame(index=range(len(X_test)))
meta_train['CDR'] = y_train
meta_train['file'] = X_train
meta_train = meta_train.dropna()

meta_test['CDR'] = y_test
meta_test['file'] = X_test
meta_test = meta_test.dropna()
meta_test.to_csv('../data/OASIS/meta_test.csv')
meta_train.to_csv('../data/OASIS/meta_train.csv')