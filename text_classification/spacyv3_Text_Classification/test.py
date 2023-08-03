import spacy

# Load the saved model
nlp = spacy.load("model")

# Test classification
text = "DENNGEICENCE SOUTH AFRICA ZA CARTADECONDUCAO DS LUCY IDNo.: 02/8512115129083 FEMALE Birth: 21/12/1998 ZA Restriction LiconceNumber 206190052R3M No.: 8 Vaii 10/07/2017 09/07/2022 issued. Us A EC Venicierestrietion: 0 0 21/12/2000 05/03/2013 [Prot. driving permit: GP Expiry date: 09/07/2027"
categories = nlp(text)._.cats

print(categories)
