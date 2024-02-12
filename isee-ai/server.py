import sys

from pydantic import BaseModel
sys.path.append('./')
import base64
import time
from typing import List
import cv2
from fastapi import FastAPI, Response
import numpy as np
import yolo_inference
from PIL import Image
import io
from PIL import Image
import paddle_ocr_inference

app = FastAPI()
text_sys = paddle_ocr_inference.ocr_load()

class ImagePayload(BaseModel):
    bus_image: str

def decode_base64_image(image_string):
        if image_string.startswith("data:image"):
            image_string = image_string.split(",")[1]
        image_bytes = base64.b64decode(image_string)
        image_np_array = np.frombuffer(image_bytes, dtype=np.uint8)
        image_cv = cv2.imdecode(image_np_array, cv2.IMREAD_COLOR)
        return image_cv

def pil_to_cv2(pil_images: List[Image.Image]):
        result =[]
        for pil_image in pil_images:
            np_array = np.array(pil_image)
            opencv_image = cv2.cvtColor(np_array, cv2.COLOR_RGB2BGR)
            result.append(opencv_image)
        return result

@app.get("/")
async def read_root():
    return f"Hello {tmp}"

@app.get("/ocr")
async def read_root(json_body: dict):
    base64_string = json_body["bus_image"]
    cv2_image = [decode_base64_image(base64_string)]
    paddle_ocr_inference.inference(cv2_image)
    return "Hello World"

@app.post("/yolo")
async def detect_bus(json_body: dict):
    image_bytes = base64.b64decode(json_body["bus_image"])
    pil_image = Image.open(io.BytesIO(image_bytes))
    cropped_images = yolo_inference.yolo_inference(pil_image)
    image_bytes = io.BytesIO()
    if len(cropped_images) == 0:
        return {}
    cropped_images[0].save(image_bytes, format='PNG')
    return Response(content=image_bytes.getvalue(), media_type='image/png')

@app.post("/inference")
async def inference_pipeline(json_body: dict):
    start_time = time.time()
    image_bytes = base64.b64decode(json_body["bus_image"])
    pil_image = Image.open(io.BytesIO(image_bytes))
    cropped_images = yolo_inference.yolo_inference(pil_image)
    med_time = time.time()
    bus_images = pil_to_cv2(cropped_images)
    result = paddle_ocr_inference.ocr_inference(text_sys, bus_images)
    end_time = time.time()

    print(f"Total time: {end_time - start_time:.3f}", f"\n\tYOLO: {med_time - start_time:.3f}", f"\n\tOCR: {end_time - med_time:.3f}")
    return {"result": result}


def run():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    run()