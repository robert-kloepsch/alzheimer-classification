import pandas as pd
import os
import numpy as np
from sklearn.utils import shuffle
import tensorflow as tf

def load_oasis_set():
    path1 = "F:\\MRI_class\\data"
    path2 = path1+"\\horizontal_masked"

    #load csv

    metaData = pd.read_csv(path1+"\\oasis_cross_sectional.csv")

    #only consider persons 50+ years of age
    metaData = metaData[metaData.Age >= 50]
    metaData = metaData[["ID","CDR"]]

    # imputing missing 0
    metaData.CDR[metaData.CDR.isna() == True] = 0
    #metaData = metaData.drop(metaData.CDR[metaData.CDR > 1].index)

    #load file names


    path_list = os.listdir(path2)

    #create file list matching the path_list
    fileList = pd.DataFrame(path_list)

    #merge metadata dataframe with file list on ID
    f = lambda x: x[0:13]                               #merge on first 13 letters (eg "OAS1_0001_MR1"). This is the ID of each image
    fileList["ID"]=fileList[0].apply(f)

    metaData = pd.merge(metaData, fileList,on="ID", how="left")
    metaData = metaData.rename(columns={0:"file"})

    #relable since class 0.5 can not be evaluated and must be 1 (~very mild)
    metaData.loc[:,"CDR"] = metaData.loc[:,"CDR"].apply(lambda x: 3 if x==2 else x)
    metaData.loc[:,"CDR"] = metaData.loc[:,"CDR"].apply(lambda x: 2 if x==1 else x)
    metaData.loc[:,"CDR"] = metaData.loc[:,"CDR"].apply(lambda x: 1 if x==0.5 else x)


    images_class0 = []
    images_class1 = []
    images_class2 = []
    images_class3 = []

    label_class0 = []
    label_class1 = []
    label_class2 = []
    label_class3 = []


    #iterate through list and load each image from disk to numpy array. Using keras method as it is very fast
    for t, i in enumerate(metaData.file):
        
        temp_path = path2+"/"+i
        if metaData.CDR[t] == 0:
            
            image1 = tf.keras.preprocessing.image.load_img(temp_path)
            image1 = tf.keras.preprocessing.image.img_to_array(image1)
            images_class0.append(image1)
            label_class0.append(metaData.CDR[t])
            
        if metaData.CDR[t] == 1:
                    
            image1 = tf.keras.preprocessing.image.load_img(temp_path)
            image1 = tf.keras.preprocessing.image.img_to_array(image1)
            images_class1.append(image1)
            label_class1.append(metaData.CDR[t])

        if metaData.CDR[t] == 2:
                    
            image1 = tf.keras.preprocessing.image.load_img(temp_path)
            image1 = tf.keras.preprocessing.image.img_to_array(image1)
            images_class2.append(image1)
            label_class2.append(metaData.CDR[t])

        if metaData.CDR[t] == 3:
                    
            image1 = tf.keras.preprocessing.image.load_img(temp_path)
            image1 = tf.keras.preprocessing.image.img_to_array(image1)
            images_class3.append(image1)
            label_class3.append(metaData.CDR[t])

    #convert to lists to array
    images_class0 = np.array(images_class0)    
    images_class1 = np.array(images_class1)
    images_class2 = np.array(images_class2)
    images_class3 = np.array(images_class3)

    label_class0 = np.array(label_class0)
    label_class1 = np.array(label_class1)
    label_class2 = np.array(label_class2)
    label_class3 = np.array(label_class3)


    oasis_test_images = np.concatenate((images_class0,images_class1,images_class2,images_class3))
    oasis_test_labels = np.concatenate((label_class0,label_class1,label_class2,label_class3))
    X_test_oasis, y_test_oasis = shuffle(oasis_test_images, oasis_test_labels, random_state=10)         #<--- change random seed if you like

    print("\n")
    print("Image Array Shape:", oasis_test_images.shape,"\n")
    print("Image Count:",oasis_test_images.shape[0],"\n")
    print("labels:",np.unique(oasis_test_labels),"\n")
    print("Class Counts:")
    print(metaData[["ID","CDR"]].groupby("CDR").count())

    return X_test_oasis, y_test_oasis
