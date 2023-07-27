import spacy
import json

# Load the saved model
model_path = "model"
nlp = spacy.load(model_path)

# Test the loaded model
text = "Passport/Passeport REPUBLIC OF SOUTHAFRICA/REPUBLIQUE D'AFRIQUE DU SUD an PA ZAF A04714890 GORNALL ANTHONY DALE SOUTHAFRICAN/SUD-AFRICAIN AFR 25 MAY 1997 9705255136082 5098 S/S M ZAF 11 MAY Z015 DEPT OF HOME AFFAIRS 10 MAY 2025 PAZAFGORNALL<<ANTHONY<DALE<<<<<<<<<<<<<<<<<< A047148903ZAF9705250M25051079705255136082<56"
doc = nlp(text)

# Create a JSON object
response = {}

# Populate the JSON object with extracted entities
for ent in doc.ents:
    response[ent.label_] = ent.text

# Convert the JSON object to a string
json_response = json.dumps(response)

# Print the JSON response
print(json_response)

