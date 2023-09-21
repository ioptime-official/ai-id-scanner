# Extracting Text using PaddleOCR

## Installation

To install the required packages, you need to run the following command in your terminal:

```sh
python<=3.7
pip install -r requirements.txt
```
The models for inferenxing an be directly downloaded from PaddleOCR Github repo ![PaddleOCR]([https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_en/models_list_en.md])
## Inferencing

Use the command below on Terminal, change the Detection Model path, Recognition Model path and Classification Model path accordingly, after that provide the respective dictionary for the model used.

The card and passport images are in **doc/id/**

```sh
python3 tools/infer/predict_system.py --image_dir="./doc/id/passport.png" --det_model_dir="./en_PP-OCRv3_det_infer/" --cls_model_dir="./ch_ppocr_mobile_v2.0_cls_infer/" --rec_model_dir="./en_PP-OCRv3_rec_infer/" --use_angle_cls=true --rec_char_dict_path="ppocr/utils/en_dict.txt"
```

### South Africa ID Card

![sa_id_card2](https://github.com/ioptime-official/ai-id-scanner/assets/50315486/02d9e8f0-a1b8-4734-9a19-6d5e18cac4b7)

### Zimbabwe ID Card
![5](https://github.com/ioptime-official/ai-id-scanner/assets/50315486/c805fd5d-438e-485c-9842-e073455017b4)

### Passport
![south_africa_preview](https://github.com/ioptime-official/ai-id-scanner/assets/50315486/9ea69ed5-3d06-4eda-92a7-bff882f05b16)


## References

https://github.com/PaddlePaddle/PaddleOCR

