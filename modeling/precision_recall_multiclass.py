from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt 
from sklearn.metrics import recall_score, precision_score
import numpy as np

def precision_recall_multiclass(y_pred,y_val,target_list):
    
    '''
    Args:   y_pred - raw output of model prediction (should be real proba values)
            y_val - validation set as used in cnn model (should be sparse dummy columns)
            target_list - list containing targets as strings
            
    retuns: Plots the individual precision-recall curves of every class.
            
    '''
    #collect recalls and precisions
    recalls = []
    precisions = []
    accuracies = []

    #convert prediction probas to absolute values (0,1)
    y_pred_absolutes = []
    for row in y_pred:
        if np.argmax(row) == 0:
            y_pred_absolutes.append([1,0,0])
        if np.argmax(row) == 1:
            y_pred_absolutes.append([0,1,0])
        if np.argmax(row) == 2:
            y_pred_absolutes.append([0,0,1])
    y_pred_absolutes = np.array(y_pred_absolutes)
    
    # set plot figure size
    fig, c_ax = plt.subplots(1,1, figsize = (12, 8))

    # calculate precsion and recall for every individual class
    # plotting every curve
    def multiclass_precision_recall(y_val, y_pred):
       
        for idx, c_label in enumerate(target_list):
            precision, recall, thresholds = precision_recall_curve(y_val[:,idx], y_pred[:,idx])
            c_ax.plot(precision, recall, label = c_label)

            # collect scores
            recalls.append(recall_score(y_val[:,idx], y_pred_absolutes[:,idx]))
            precisions.append(precision_score(y_val[:,idx], y_pred_absolutes[:,idx]))
            accuracies.append(precision_score(y_val[:,idx], y_pred_absolutes[:,idx]))
        

    # using the function
    multiclass_precision_recall(y_val, y_pred)
    
    # plot specifics
    c_ax.legend()
    c_ax.set_xlabel('Precision')
    c_ax.set_ylabel('Recall')
    plt.show()

    # print individual scores
    print("-----Recalls-----")
    for idx, c_label in enumerate(target_list):
        print(c_label, "Recall:", recalls[idx])
    print("-------#####-------")
    print("\n")
    print("-----Precisions-----")
    for idx, c_label in enumerate(target_list):
        print(c_label, "Precision:", precisions[idx])
    print("-------#####-------")
    print("\n")
    print("-----Accuracy-----")
    for idx, c_label in enumerate(target_list):
        print(c_label, "Accuracy:", accuracies[idx])
    print("-------#####-------")
    print("\n")
    print("-----Macro Recall and Precisions-----")
    print("Macro recall:",recall_score(y_val,y_pred_absolutes, average="macro"))
    print("Macro recall:",precision_score(y_val,y_pred_absolutes, average="macro"))
    print("------------#####------------")