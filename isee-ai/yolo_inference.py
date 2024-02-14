# %%
from typing import List
from ultralytics import YOLO
from PIL import Image

YOLO_ONNX_PATH = "./yolo_onnx/yolov8n.onnx"

def bus_crop(input_image: Image.Image, boxes, boxes_cls):
    result = []
    for xyxy, cls in zip(boxes, boxes_cls):
        if cls == 5:
            x, y, x2, y2 = map(int, xyxy)
            cropped_image = input_image.crop((x, y, x2, y2))
            result.append(cropped_image)
    return result


def yolo_inference(input_image: Image.Image)-> List[Image.Image]:
    model = YOLO(YOLO_ONNX_PATH)
    model_results = model(input_image)
    results = bus_crop(input_image, model_results[0].boxes.xyxy.tolist(), model_results[0].boxes.cls.tolist())
    
    return results
