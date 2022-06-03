from fastapi import UploadFile, FastAPI
import uvicorn


app = FastAPI(title="Alzheimers - MRI Image Analysis")

@app.get('/')
async def Welcome():
    return "Welcome to the Brains Team. Here we are trying to support medical alzheimer's diagnostics. You can show us an MRI brain scan and we try our best to estimate if that image indicates early signs of alzheimer's disease"

