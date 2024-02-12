#%%
from ultralytics import YOLO
import time 
import torch
import cv2
import os
import shutil

# %%
# draw bus boxes to output_path
def draw_boxes(image_path, boxes, cls, output_path):
    # Read the image
    image = cv2.imread(image_path)
    # Convert tensor to NumPy array
    boxes_np = boxes.cpu().numpy() if isinstance(boxes, torch.Tensor) else boxes
    
    # Draw bounding boxes
    for cls, box in zip(cls, boxes_np):
        if cls != 5:
            continue
        x, y, x2, y2 = box
        x, y, x2, y2 = int(x), int(y), int(x2), int(y2)
        cv2.rectangle(image, (x, y), (x2, y2), (0, 255, 0), 2)  # Green rectangle with thickness 2
    cv2.imwrite(output_path, image)



def bus_crop_and_save(image_path, boxes, boxes_cls, output_dir):
    # Read the image
    image = cv2.imread(image_path)
    

    # 해당 경로에 디렉토리 또는 파일이 존재하는지 확인
    if os.path.exists(output_dir):
        # 디렉토리인 경우 내부 파일/디렉토리까지 모두 삭제
        if os.path.isdir(output_dir):
            shutil.rmtree(output_dir)

    # 새 디렉토리 생성
    os.mkdir(output_dir)
    
    # Convert tensor to NumPy array
    # boxes_np = boxes.cpu().numpy() if isinstance(boxes, torch.Tensor) else boxes
    idx = 0
    # Draw bounding boxes
    for xyxy, cls in zip(boxes, boxes_cls):
        if cls == 5:
            # import pdb;pdb.set_trace()
            x, y, x2, y2 = xyxy
            x, y, x2, y2 = int(x), int(y), int(x2), int(y2)
            output_path = os.path.join(output_dir,f'{idx}.jpg')
            cv2.imwrite(output_path,image[y:y2,x:x2,:])
            idx+=1



if __name__ == "__main__":
    
    image_path = "/home/cvlab09/projects/joungbin/iSEE-AI/test8.jpg"
    output_path = 'output_image.jpg'
    output_dir = './cropped_bus' # 바꾸지말기
    if torch.cuda.is_available():
        torch.cuda.set_device(0)

    # model = YOLO("yolov8m.pt")
    model = YOLO("./yolo_onnx/yolov8n.onnx")
    # model = YOLO("./yolo_onnx/yolov8m.onnx")
    # model = YOLO("./yolo_onnx/yolov8s.onnx")
    input_image = cv2.imread(image_path)

    start_time = time.time()
    results = model(input_image)
    end_time = time.time()
    print("Model inference time: ", end_time - start_time)

    print("Found", results[0].boxes.cls.tolist().count(5), "buses")
    for xyxy, cls in zip(results[0].boxes.xyxy.tolist(), results[0].boxes.cls.tolist()):
        if cls == 5:
            print("Bus at", xyxy)
            
    # import pdb;pdb.set_trace()
    draw_boxes(image_path, results[0].boxes.xyxy.tolist(), results[0].boxes.cls.tolist(), output_path)
    bus_crop_and_save(image_path, results[0].boxes.xyxy.tolist(), results[0].boxes.cls.tolist(), output_dir)
# %%
