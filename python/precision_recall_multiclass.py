from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt 


def precision_recall_multiclass(y_pred,y_val,target_list):
    
    '''
    Args:   y_pred - raw output of model prediction (should be real proba values)
            y_val - validation set as used in cnn model (should be sparse dummy columns)
            target_list - list containing targets as strings
            
    retuns: Plots the individual precision-recall curves of every class.
            
    '''

    # set plot figure size
    fig, c_ax = plt.subplots(1,1, figsize = (12, 8))

    # calculate precsion and recall for every individual class
    # plotting every curve
    def multiclass_precision_recall(y_val, y_pred):
       
        for idx, c_label in enumerate(target_list):
            precision, recall, thresholds = precision_recall_curve(y_val[:,idx], y_pred[:,idx])
            c_ax.plot(precision, recall, label = c_label)
        

    # using the function
    multiclass_precision_recall(y_val, y_pred)
    

    # plot specifics
    c_ax.legend()
    c_ax.set_xlabel('Precision')
    c_ax.set_ylabel('Recall')
    plt.show()