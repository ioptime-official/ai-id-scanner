# Custom Named Entity Recognition (NER) Model for OCR Data (spaCy v2.2.3)

This repository contains a custom Named Entity Recognition (NER) model trained with spaCy v2.2.3, designed to extract relevant information from OCR (Optical Character Recognition) data of various documents, including South African ID Cards, Passports, and Driver's Licenses, as well as documents from Zimbabwe and Kenya. The reason for using an older version of spaCy is to ensure compatibility with the Chaquopy library in Android.

## Introduction

Optical Character Recognition (OCR) technology has proven to be valuable for converting scanned documents and images into editable and searchable data. However, extracting specific entities from OCR data can be challenging due to the unstructured nature of the text.

To tackle this challenge, we have developed custom NER models using spaCy v2.2.3, a powerful NLP library with Python support. These models are trained to recognize and extract important entities, such as names, addresses, dates of birth, identification numbers, and other relevant information from OCR text.

## Data Annotation

The training data used to train the custom NER models was annotated using an online annotation tool [NER Annotator](https://tecoholic.github.io/ner-annotator/). The tool allowed us to label entities in the OCR data for various document types, including South African, Zimbabwean, and Kenyan documents. The labeled entities were used for training the models effectively.

## Model Training

To train the custom NER models, we utilized the `ner.py` script provided in this repository. This script is specifically designed to train the models using spaCy v2.2.3 and update the labeled entities directly within the script.

The training process involves:
1. Loading the annotated data.
2. Loading a pre trained spaCy NER model.
3. Updating the model with the labeled entities.
4. Fine-tuning the model on the annotated data.
5. Saving the trained model for future use.

## Model Testing

After training the models using `ner.py`, we can perform model testing using the `test.py` script provided in this repository. The testing script allows us to input OCR text and obtain extracted entities using the trained models. This helps us evaluate the model's performance and identify areas for improvement.

## Usage

To train and use the custom NER models for extracting information from OCR data, follow these steps:

1. Install the required dependencies, including spaCy v2.2.3 and any additional libraries, by running `pip install spacy==2.2.3` with `python=3.8`

2. Run the `ner.py` script to train the models and update labeled entities along with data and model save path:
   ```
   python ner.py
   ```

3. Use the `test.py` script to test the trained models on new OCR text:
   ```
   python test.py
   ```

   The script will prompt you to input OCR text, and it will display the extracted entities.

## Acknowledgments

We would like to acknowledge the creators of spaCy for providing an excellent NLP library, and the authors of the Chaquopy library for enabling seamless Python integration in Android applications.

## Disclaimer

While we have made efforts to train accurate and reliable NER models, please note that they may not be perfect and may have limitations. We recommend validating the extracted information from OCR data with other reliable sources before using it for critical applications.
