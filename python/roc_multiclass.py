# imports
import matplotlib.pyplot as plt 
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import roc_curve, auc, roc_auc_score
import numpy as np

def roc_multiclass(y_pred,y_val,target_list,variant):
    
    '''
    Args:   y_pred - raw output of model prediction (should be real proba values)
            y_val - validation set as used in cnn model (should be sparse dummy columns)
            target_list - list containing targets as strings
            variant - "macro" or "micro": sets the averaging method 
    retuns: Plots the individual Roc-auc curves of every class.
            Also prints the "macro" or "micro" average Roc-auc-score
    '''


    # flatten CNN output in such way that we change the sparse columns (each only containing 0 and 1)
    # to one column labeling classes as continues numbers. e.g. 1,2,3,4 (etc)
    y_pred = np.argmax(y_pred,axis=-1)
    y_val = np.argmax(y_val, axis=-1)

    # set plot figure size
    fig, c_ax = plt.subplots(1,1, figsize = (12, 8))

    # core function: here the roc score is calculated. The estimator results are calculated for all
    # thresholds. Macro sets the evaluation to "one vs all".
    # Multiclass_roc_auc_score is acutually the roc_auc_score function of sklearn
    # within this Multiclass_roc_auc_score function the roc_curve of each individual class is calculated
    # and plotted (see loop)
    def multiclass_roc_auc_score(y_val, y_pred, average=variant):
        # creates dummy columns so we have one for each class (with 0s and 1s)
        lb = LabelBinarizer()   
        lb.fit(y_val)
        y_val = lb.transform(y_val)
        y_pred = lb.transform(y_pred)

        # calculate the roc score for each class individually to all thresholds the sample set provides
        # first the false and true positive rates are calculated (fpr, tpr) then the score is
        # calculated in the return (both uses sklearn)
        # roc_auc_score which is returned gives the roc score as "one vs all" average
        for (idx, c_label) in enumerate(target_list):
            fpr, tpr, thresholds = roc_curve(y_val[:,idx].astype(int), y_pred[:,idx])
            c_ax.plot(fpr, tpr, label = '%s (AUC:%0.2f)'  % (c_label, auc(fpr, tpr)))
        c_ax.plot(fpr, fpr, 'b',linestyle='dashed', label = 'Random Guessing')
        return roc_auc_score(y_val, y_pred, average=average)

    # using the function
    macro_roc_auc_score = multiclass_roc_auc_score(y_val, y_pred)
    print(str.upper(variant),'ROC AUC SCORE:', macro_roc_auc_score)

    # plot specifics
    c_ax.legend()
    c_ax.set_xlabel('False Positive Rate')
    c_ax.set_ylabel('True Positive Rate')
    plt.show()

    