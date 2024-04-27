from fastapi import FastAPI, HTTPException, status
from fastapi.responses import StreamingResponse
import io
from db.data import data

sins_data = {
    "apple": "سیب",
    "sumac":"سماق",
    "oleaster":"سنجد",
    "greenery":"سبزه",
    "samanoo":"سمنو",
    "coin":"سکه",
    "hyacinth":"سنبل"
}

def get_key_by_value(value):
    for key, val in sins_data.items():
        if val == value:
            return key
    return None

app = FastAPI()

@app.get("/")
def read_root():
    return data['description']


@app.get("/sins")
def read_sins():
    return data['list']


@app.get("/sins/{sin_name}")
def read_sin(sin_name: str):
    index = get_key_by_value(sin_name)
    if index != None:
        return data['info'][index]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sins Not Found')
    
@app.get("/sins/{sin_name}/image")
def read_image(sin_name: str):
    index = get_key_by_value(sin_name)
    if index != None:
        image_path = data['images'][index]
        with open(image_path, "rb") as file:
            return StreamingResponse(io.BytesIO(file.read()), media_type='image/png')

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sins Not Found')