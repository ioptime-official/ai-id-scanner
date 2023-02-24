# Extracting Text from IDs and Passports using PaddleOCR

## Scope
This repository includes files and instructions on how to use PaddleOCR to extract text from images of South African/Zimbabwe IDs and passports. 

## Installation

To install the required packages, you need to run the following command in your terminal:

```sh
python<=3.7
pip install -r requirements.txt
```
## Inferencing

Use the command below on Terminal, change the Detection Model path, Recognition Model path and Classification Model path accordingly, after that provide the respective dictionary for the model used.

The card and passport images are in **doc/id/**

```sh
python3 tools/infer/predict_system.py --image_dir="./doc/id/passport.png" --det_model_dir="./en_PP-OCRv3_det_infer/" --cls_model_dir="./ch_ppocr_mobile_v2.0_cls_infer/" --rec_model_dir="./en_PP-OCRv3_rec_infer/" --use_angle_cls=true --rec_char_dict_path="ppocr/utils/en_dict.txt"
```
## OCR Results on ID Cards

The inferencing results on Id cards and passports are as follows:

### South Africa ID Card
![Card Image 1](https://github.com/ioptime-official/ai-id-scanner/blob/main/inference_results/1.jpg)

### Zimbabwe ID Card
![Card Image 2](https://github.com/ioptime-official/ai-id-scanner/blob/main/inference_results/15.png)

### Passport
![Passport Image 1](https://github.com/ioptime-official/ai-id-scanner/blob/main/inference_results/5.jpg)

## References

https://github.com/PaddlePaddle/PaddleOCR

