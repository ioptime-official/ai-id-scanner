# Custom Named Entity Recognition (NER) Model for OCR Data

This repository contains a custom Named Entity Recognition (NER) model trained with spaCy v3, designed to extract relevant information from OCR (Optical Character Recognition) data of South African ID Cards, Passports, and Driver's Licenses. Additionally, similar models have been trained for Zimbabwean and Kenyan documents.

## Introduction

Optical Character Recognition (OCR) is a technology that converts various types of documents, such as scanned paper documents, PDF files, or images captured by a digital camera, into editable and searchable data. However, extracting specific pieces of information from OCR data can be challenging due to the unstructured nature of the text.

To address this challenge, we have developed custom NER models using spaCy v3, which is a powerful and efficient Natural Language Processing (NLP) library. These models are trained to recognize and extract important entities, such as names, addresses, dates of birth, identification numbers, and other relevant information from OCR text.

## Data Annotation

To train the custom NER models, we utilized an online annotation tool available at [NER Annotator](https://tecoholic.github.io/ner-annotator/). The tool allowed us to perform entity labeling on the OCR data for South African, Zimbabwean, and Kenyan documents. We carefully annotated the data to ensure high-quality training for the models.

## Model Training

The training of the custom NER models was performed in a Jupyter Notebook environment. We used the annotated data to train multiple models for each document type (South African ID Cards, Passports, and Driver's Licenses; Zimbabwean documents; and Kenyan documents). The models were fine-tuned using the spaCy v3 library and appropriate configuration settings.

## Usage

If you wish to use the pre-trained NER models for extracting information from OCR data of South African, Zimbabwean, or Kenyan documents, follow these steps:

1. Install the required dependencies by running `pip install spacy` or i can be directly insalled in the jupyter notebook: [notebook](https://github.com/ioptime-official/ai-id-scanner/blob/main/NER/Spacyv3/NER_Training_with_Spacy_v3_Notebook.ipynb)
2. Base Config file can be used for configuration, the code for that is available in jupyter notebook [Base Config](https://github.com/ioptime-official/ai-id-scanner/blob/main/NER/Spacyv3/base_config.cfg)

## Acknowledgments

We would like to express our gratitude to the team at [https://tecoholic.github.io/ner-annotator/](https://tecoholic.github.io/ner-annotator/) for providing the annotation tool, which significantly streamlined the data labeling process.

## Disclaimer

Please note that while the custom NER models have been trained and evaluated to the best of our abilities, they may not be perfect and could make mistakes in certain cases. We recommend verifying the extracted information with other reliable sources before using it for critical applications.
