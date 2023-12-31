import io
import torch
from PIL import Image

# Model
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, force_reload=True)


# Read from bytes as we do in app
with open("popman.jpg", "rb") as file:
    img_bytes = file.read()
img = Image.open(io.BytesIO(img_bytes))

results = model(img, size=640) # includes NMS

print(results.pandas().xyxy[0])