from fastapi import UploadFile, FastAPI
import uvicorn
import tensorflow as tf
import cv2
import numpy as np

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
    # convert to numpy array
    image = np.asarray(bytearray(image))
    # decode byte-array to usable ndarray
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    img = shape_image(img)

    model = load_model()
    pred = predict(img,model)
    diagnosis = interpret_pred(pred)
    return diagnosis

    

#uvicorn.run(app, debug=True)