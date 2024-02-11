#%%
from ultralytics import YOLO
import time 
import torch
import cv2

image_path = "bus.jpg"
output_path = 'output_image.jpg'

if torch.cuda.is_available():
    torch.cuda.set_device(0)

model = YOLO("yolov8m.pt")
input_image = cv2.imread(image_path)

start_time = time.time()
results = model(input_image)
end_time = time.time()
print("Model inference time: ", end_time - start_time)

print("Found", results[0].boxes.cls.tolist().count(5), "buses")
for xyxy, cls in zip(results[0].boxes.xyxy.tolist(), results[0].boxes.cls.tolist()):
    if cls == 5:
        print("Bus at", xyxy)

# %%
# draw bus boxes to output_path
def draw_boxes(image_path, boxes, output_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert tensor to NumPy array
    boxes_np = boxes.cpu().numpy() if isinstance(boxes, torch.Tensor) else boxes
    
    # Draw bounding boxes
    for box in boxes_np:
        x, y, x2, y2 = box
        x, y, x2, y2 = int(x), int(y), int(x2), int(y2)
        cv2.rectangle(image, (x, y), (x2, y2), (0, 255, 0), 2)  # Green rectangle with thickness 2
    cv2.imwrite(output_path, image)

draw_boxes(image_path, results[0].boxes.xyxy.tolist(), output_path)
