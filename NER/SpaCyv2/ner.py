import spacy
import json
import random

def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    annotations = data["annotations"]
    TRAIN_DATA = []
    for item in annotations:
        text = item[0]
        entities = item[1]["entities"]
        TRAIN_DATA.append((text, {"entities": entities}))

    return TRAIN_DATA

def train_spacy(TRAIN_DATA, iterations, model_output_dir):
    nlp = spacy.blank("en")
    ner = nlp.create_pipe("ner")
    ner.add_label("MRZ")
    nlp.add_pipe(ner, name="mrz_ner")

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "mrz_ner"]
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()
        for itn in range(iterations):
            print("Starting Iteration {}".format(str(itn)))
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                nlp.update(
                    [text],
                    [annotations],
                    drop=0.2,
                    sgd=optimizer,
                    losses=losses
                )
            print(losses)

    # Save the trained model to disk
    nlp.to_disk(model_output_dir)
    print("Trained model saved to:", model_output_dir)

TRAIN_DATA = load_data("data/annotations.json")
random.shuffle(TRAIN_DATA)
TRAIN_DATA = TRAIN_DATA[0:6]

model_output_dir = "model/"
trained = train_spacy(TRAIN_DATA, 100, model_output_dir)

# Load the saved model
loaded_model = spacy.load(model_output_dir)

# Process text using the loaded model
doc = loaded_model("REPUBLIC-OF 71 PASSPORT TYPE STATE OFP PN ZIM AN016592 SURNAME/ZITAREMHURI/ISIBOR ROBINSON OTHER NAMES/ZITABIZO FRANK NATIONALTY DENTITYNUMBER ZIMBABWEAN 15-084163D-00 SEXE KERWA/OWAZALELWAKHON M HARARE BIRTH DATEIZUWAREKUBEREKW 11/02/1961 ISSUEDATE COUNTRYOFPES 21/08/2009 ZIMBABWE EXPIRYDATE TUTHORITY 20/08/2019 REGISTRARGENERAL-HRE fobrason PROFESSICH SIGNAfURE FINGER PRINT PNZIMROBINSON<<FRANK<<<<<<<<<<<<<<<<<<<< AN016592<5ZIM6102113M190820315084163D00<<08")

# Print the extracted entities
for ent in doc.ents:
    print(ent.text, ent.label_)
