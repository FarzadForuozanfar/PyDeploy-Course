from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import easyocr
import numpy as np
import cv2

app = FastAPI()
reader = easyocr.Reader(['ch_sim', 'en'])

@app.post("/pic2word")
async def pic2word(input_file: UploadFile = File(...)):
    if not input_file.content_type.startswith("image/"):
        raise HTTPException(status_code=415, detail="Unsupported file type")

    contents = await input_file.read()
    np_array = np.frombuffer(contents, np.uint8)
    image_rgb = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    results = reader.readtext(image_rgb)
    response = []
    
    for text in results:
        response.append(text[1])

    return {"text": response}