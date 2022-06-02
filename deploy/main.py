from fastapi import File, UploadFile, FastAPI
import uvicorn
import tensorflow as tf
import cv2
import numpy as np
from io import BytesIO
from PIL import Image

app = FastAPI(title='Hello world')

@app.get('/index')
def hello_world():
    return "hello world"

#load model function
def load_model():
    model = tf.keras.models.load_model('/Users/stephanbremser/neuefische/alzheimer-classification/deploy/model_binary')
    return model
model = load_model()

#load image
def read_imagefile():
    image = cv2.imread(file)
    if image.shape != (1, 208, 176, 3):
        image = image[np.newaxis,:,:,:]
    return image

#predict function
@app.post("/predict/image")
def predict(image):
    image = read_imagefile(image)
    
    pred = model.predict(image)
    
    return pred

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    image = await file.read()
    nparr = np.fromstring(image, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    x = img.shape
    
   # t = x.tolist()
    
    #x = np.array(Image.open(BytesIO(image)))
    #x = x.shape
    #t = x.tolist()
    #image = read_imagefile(image)
    #prediction = predict(image)
    #print(prediction)
    return x

    

uvicorn.run(app, debug=True)