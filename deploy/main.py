from fastapi import UploadFile, FastAPI
import uvicorn
import tensorflow as tf
from io import BytesIO
import numpy as np
from PIL import Image

app = FastAPI(title="Alzheimers - MRI Image Analysis")

@app.get('/')
async def Welcome():
    return "Welcome to the Brains Team. Here we are trying to support medical alzheimer's diagnostics. You can show us an MRI brain scan and we try our best to estimate if that image indicates early signs of alzheimer's disease"

#load model function
def load_model():
    model = tf.keras.models.load_model('./model_binary')
    return model


#check image shape to fit into model
def shape_image(image_array):
    
    if image_array.shape != (1, 208, 176, 3):
        image_array = image_array[np.newaxis,:,:,:]
    return image_array

#interpret prediction output
def interpret_pred(prediction):

    if prediction >= 0.5:
        return str("alzheimer :_(")
    else:
        return str("HEALTHY! YAAAYYY !! no shrinking :-D!")

#predict function
def predict(image_array,model):
        
    pred = model.predict(image_array)
    
    return pred

@app.post("/MRI_Image_Analysis/")
async def analyse_MRI_img(file: UploadFile):
    
    
    #load uploaded image
    image = await file.read()
    image = Image.open(BytesIO(image))
    image = image.convert("RGB")                    #to keep three channels

    #convert to array
    image = np.array(image)
        
    image = shape_image(image)

    model = load_model()
    pred = predict(image,model)
    diagnosis = interpret_pred(pred)
    return diagnosis
