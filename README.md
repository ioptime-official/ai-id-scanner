# Extracting Text from IDs and Passports using PaddleOCR

![Card Extraction Workflow](https://github.com/ioptime-official/ai-id-scanner/assets/50315486/d922ba71-ede9-4a42-83e2-ae63ec70b110)


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

## NER and Text Classification for ID Card Analysis

This repository contains two key components Other than OCR: Named Entity Recognition (NER) and Text Classification. 

- **NER Subrepository**: The [NER](https://github.com/ioptime-official/ai-id-scanner/tree/main/NER) focuses on extracting valuable information from OCR (Optical Character Recognition) results obtained using PaddleOCR on various ID cards. NER enables the identification and categorization of entities such as names, dates, addresses, and more from the OCR text.

- **Text Classification Subrepository**: The [Text Classification](https://github.com/ioptime-official/ai-id-scanner/tree/main/text_classification) is responsible for classifying the pre-processed OCR text into specific ID card categories. This classification step helps determine which type of ID card the extracted information belongs to, providing valuable insights for further analysis and processing.

Feel free to explore, contribute, and utilize the functionalities for more detailed the sub repositories from the links above

## References

https://github.com/PaddlePaddle/PaddleOCR

