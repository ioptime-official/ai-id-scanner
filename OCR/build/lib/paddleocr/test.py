import os
import paddleocr

def main():
    # Image path
    image_path = "./doc/id/9.jpg"

    # Load OCR toolkit
    ocr = paddleocr.OCR(lang='en',
                        det_model_dir="./en_PP-OCRv3_det_infer/",
                        cls_model_dir="./ch_ppocr_mobile_v2.0_cls_infer/",
                        rec_model_dir="./en_PP-OCRv3_rec_infer/",
                        char_dict_path="./ppocr/utils/en_dict.txt")

    # Perform OCR
    text = ocr.ocr(image_path)

    # Save recognized text to a file
    with open("output.txt", "w") as f:
        f.write(text)

if __name__ == '__main__':
    main()
