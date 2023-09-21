import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', 'signature-fp16.tflite')
# Images
img = 'test5.jpeg'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
