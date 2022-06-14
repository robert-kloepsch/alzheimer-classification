# Import dependencies
from tensorflow.keras.applications import ResNet50, VGG16, DenseNet201, InceptionV3
import tensorflow as tf

INPUT_SHAPE = (208, 176, 3)

# Function definition
def base_model(MODEL, input_shape=INPUT_SHAPE, classes=3, freeze_layers=True):
    '''
    Creates base model from keras applications pre-trained architectures. Model includes weights from ImageNet data set
    
    Function parameters: 
    MODEL: pre-trained keras model tp be set (VGG16, ResNet50, inceptionV3, Densenet201])
    input_shape: image size as it is after loading data sets, 3 channels are needed <- TBD, maybe it should be related to a global variable
    classes: end classes number, default value set to 4
    freeze_layers: it defines whether the layers from pre-trained model are trainable, set not to train only the classification (dense) layers
    
    Keras application parameters:
    # include_top: set to False, since I'm going to use my input and output dimensions
    # weights: taking the weight of pre-trained model, otherwise will be initialized randomly
    # input_shape: to set only if include_top = False
    # classes: otherwise 1000 classes coming from ImageNet Dataset
    
    '''
    # Defining instances of each model
    if MODEL== 'VGG16':
        model = tf.keras.applications.VGG16(include_top=False, weights="imagenet", input_shape=INPUT_SHAPE, classes=3, classifier_activation="softmax")
    elif MODEL== 'ResNet50':
        model = tf.keras.applications.ResNet50(include_top=False, weights="imagenet", input_shape=INPUT_SHAPE, classes=3, classifier_activation="softmax")
    elif MODEL=='InceptionV3':
        model = tf.keras.applications.InceptionV3(include_top=False, weights="imagenet", input_shape=INPUT_SHAPE, classes=3, classifier_activation="softmax")
    elif MODEL=='DenseNet201':
        model = tf.keras.applications.DenseNet201(include_top=False, weights="imagenet", input_shape=INPUT_SHAPE, classes=3, classifier_activation='softmax')
    elif MODEL=='DenseNet169':
        model = tf.keras.applications.DenseNet169(include_top=False, weights="imagenet", input_shape=INPUT_SHAPE, classes=3, classifier_activation='softmax')
    elif MODEL=='DenseNet121':
        model = tf.keras.applications.DenseNet121(include_top=False, weights="imagenet", input_shape=INPUT_SHAPE, classes=3, classifier_activation='softmax')

    # Print only Conv and Pooling layer from model architecture
    #print('PRE-TRAINED MODEL ARCHITECTURE')
    #base_model.summary()
    
    # Freezing the weights of pre-trained layers for making not trainable
    if freeze_layers is True:
        #model.layers.trainable = False
        for layer in model.layers:
            layer.trainable = False
    else:
        pass

    return model