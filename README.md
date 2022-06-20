# Stop Shrinking: Early Detection of Alzheimer’s Disease 

## Introduction 
_____
Alzheimer's Disease is a common neurodegenerative disease affecting about 8% of the elderly population. The decay of memory and cognitive functions with the course of the disease poses a challenge for the quality of life. With medication, a healthy lifestyle and nourishing social contacts, the progress of the disease can be slowed down when it is detected early on. **This project is therefore aimed to develop an Artificial Intelligence algorithm to enable early detection of AD.** 

<br>

## Approach
----
Our solution uses a Deep Convolutional-Neuronal-Network (CNN) algorithm to classify different AD stages. CNN models have been widely used to identify brain diseases based on images by using so-called Convolutional technique to extract high representations of the input images, thus differentiate one stage from the other. Another big advantage of CNN is the reduction of the computational needs required for imaging processing.

<br>

## Data Set
-----
For this project, we used a Data Set provided by [Kaggle](https://www.kaggle.com/datasets/tourist55/alzheimers-dataset-4-class-of-images?datasetId=457093&searchQuery=data+set) containing over 5000 cross-sectional preprocessed Magnetic Resonance Imaging (MRI) brain images. In order to download the data set locally, both training and test set, the .py file has been included in the main notebook.

<br>

## Repository Structure
____
Following information is intended to explain the different folders of this repository, set as follows: 

* EDA Folder:
    It includes the Exploratory Data Analysis (EDA) applied on our initial Baseline model, based on only tabular psychological testing information (no images)

* Modelling Folder:
    It contains all .py scripts needed for metrics evaluation, loading the data set, CNN visualization and building the CNN model. All these functions are then called in the main notebook. 

* Deploy Folder:
     It contains all related files to a small application developed for classifying AD

<br>

## Final CNN Model Architecture
_____

A CCN Model has been built using the pre-trained VGG16 model as a backbone for the convolutional and pooling layers, here the weights from ImageNet were used for the neurons initialization and set as trainable, so they could re-learn from the MRI images during the training process. On top fully connected dense layers were added as classification layers. <br>

The main notebook contains the final implementation of our selected model architecture.

<br>

## Setup
_____

Use the requirements file in this repository to create a new environment. The `requirements` file contains all libraries needed for deployment and ensures compatibility of used API. Following command lines are used to set an virtual environment and install needed libraries within it: 

```
pyenv local 3.9.8
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

**Then if running on Windows machine,**

```
pip install -r requirements.txt
```

**Or if running on macOS machine,**

```
pip install -r requirements_2.txt
```

<br>

## Issues with our code
____

Feel free to add any issue regarding the notebook or code to this github repository. <br>

Happy Coding! :)
