from ultralytics import YOLO
from PIL import Image
import torch
# Create a new YOLO model from scratch
model = YOLO('yolov8n.yaml')

# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8n.pt')

img='car.jpg'
# Train the model using the 'coco128.yaml' dataset for 3 epochs
results = model.predict(source=img, save= True, classes = [2], show = True)

image = Image.open(img)

for r in results:
    t=r.boxes.xyxy
    x=t[0][0].item()
    y=t[0][1].item()
    s=r.boxes.xywh
    w=s[0][2].item()
    h=s[0][3].item()
    print(x,y,w,h)
    cropped_image = image.crop((x, y, x + w, y + h))
    cropped_image.save('./runs/detect/cut/1.jpg')
    cropped_image.show()