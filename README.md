# Extracting Text from IDs and Passports using PaddleOCR

![Card Extraction Workflow](https://github.com/ioptime-official/ai-id-scanner/assets/50315486/d922ba71-ede9-4a42-83e2-ae63ec70b110)


## Scope
This repository includes files and instructions on how to use PaddleOCR to extract text from images of South African/Zimbabwe IDs and passports. 

## ID Card Analysis

This repository contains differentt key components, which are as follows:

- **OCR Subrepository**: The [OCR Subrepository](https://github.com/ioptime-official/ai-id-scanner/tree/main/OCR) is dedicated to extracting text content from a variety of ID cards through optical character recognition (OCR). This pivotal process involves converting OCR data into readable text, thereby capturing essential information from ID cards of diverse formats. The extracted text serves as the foundational data for downstream tasks, enabling further analysis and processing.

- **NER Subrepository**: The [NER](https://github.com/ioptime-official/ai-id-scanner/tree/main/NER) focuses on extracting valuable information from OCR (Optical Character Recognition) results obtained using PaddleOCR on various ID cards. NER enables the identification and categorization of entities such as names, dates, addresses, and more from the OCR text.

- **Text Classification Subrepository**: The [Text Classification](https://github.com/ioptime-official/ai-id-scanner/tree/main/text_classification) is responsible for classifying the pre-processed OCR text into specific ID card categories. This classification step helps determine which type of ID card the extracted information belongs to, providing valuable insights for further analysis and processing.

- **Signature Extraction Subrepository**: The [Signature Extraction](https://github.com/ioptime-official/ai-id-scanner/tree/main/Signature%20Extraction) subrepository employs a customized YOLOv5 model to detect and extract signatures from various ID cards.

Feel free to explore, contribute, and utilize the functionalities for more detailed the sub repositories from the links above

## References

https://github.com/PaddlePaddle/PaddleOCR

