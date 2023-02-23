import onnxruntime
import numpy as np
import streamlit as st
from PIL import Image

# Load ONNX models
session_det = onnxruntime.InferenceSession("./inference/det_onnx/model.onnx")
session_rec = onnxruntime.InferenceSession("./inference/rec_onnx/model.onnx")
session_cls = onnxruntime.InferenceSession("./inference/cls_onnx/model.onnx")

# Read character dictionary
with open("./home/ioptime/workfolder/PaddleOCR/PaddleOCR/ppocr/utils/dict/en_dict.txt", "r") as f:
    char_dict = f.read().split("\n")

def predict(image_path):
    # Load image and preprocess
    image = Image.open(image_path).convert("RGB")
    image = np.array(image).astype("float32") / 255.0
    image = np.transpose(image, (2, 0, 1))[np.newaxis, :, :, :]

    # Run detection
    input_name = session_det.get_inputs()[0].name
    output_name = session_det.get_outputs()[0].name
    boxes, scores = session_det.run(output_name, {input_name: image})

    # Run recognition
    input_name = session_rec.get_inputs()[0].name
    output_name = session_rec.get_outputs()[0].name
    rec_out = session_rec.run(output_name, {input_name: image})

    # Run classification
    input_name = session_cls.get_inputs()[0].name
    output_name = session_cls.get_outputs()[0].name
    cls_out = session_cls.run(output_name, {input_name: image})

    # Decode the results
    boxes = boxes[0][scores[0] > 0.5]
    rec_out = np.argmax(rec_out, axis=-1)
    cls_out = np.argmax(cls_out, axis=-1)

    results = []
    for box, rec, cls in zip(boxes, rec_out[0], cls_out[0]):
        rec = [char_dict[i] for i in rec if i != 0]
        results.append("".join(rec))

    return results

st.set_page_config(page_title="OCR Prediction", page_icon=":telescope:", layout="wide")

# Display header
st.header("Optical Character Recognition (OCR)")

# Get image file from user
image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if image_file:
    results = predict(image_file)
    st.image(image_file, width=300)
    st.write("Prediction Results:")
    for result in results:
        st.write("- {}".format(result))
        st.write(result)
else:
    st.write("Please upload an image for OCR prediction.")