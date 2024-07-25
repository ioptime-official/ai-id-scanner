# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import spacy

# # Initialize FastAPI app
# app = FastAPI()



# # Load the custom NER model
# nlp = spacy.load("output/model-best")  # Replace with the actual path to your model

# # Define a request model
# class TextRequest(BaseModel):
#     text: str

# # Define a response model
# class EntityResponse(BaseModel):
#     text: str
#     start: int
#     end: int
#     label: str

# @app.get("/")
# async def root():
#     return {"message": "Welcome to the NER API"}

# # Define an endpoint for NER
# @app.post("/ner", response_model=list[EntityResponse])
# async def extract_entities(request: TextRequest):
#     # Process the text using the custom NER model
#     doc = nlp(request.text)
#     entities = [
#         EntityResponse(text=ent.text, start=ent.start_char, end=ent.end_char, label=ent.label_)
#         for ent in doc.ents
#     ]
#     return entities

# # Run the application
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="192.168.110.67", port=8000)


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spacy
import os

# Initialize FastAPI app
app = FastAPI()

# Load the custom NER model
model_path = os.path.join(os.getcwd(), "output/model-best")
nlp = spacy.load(model_path)  # Load the custom model from the correct path

# Define a request model
class TextRequest(BaseModel):
    text: str

# Define a response model
class EntityResponse(BaseModel):
    text: str
    start: int
    end: int
    label: str

@app.get("/")
async def root():
    return {"message": "Welcome to the NER API"}

# # Define an endpoint for NER
# @app.post("/ner", response_model=list[EntityResponse])
# async def extract_entities(request: TextRequest):
#     # Process the text using the custom NER model
#     doc = nlp(request.text)
#     entities = [
#         EntityResponse(text=ent.text, start=ent.start_char, end=ent.end_char, label=ent.label_)
#         for ent in doc.ents
#     ]
#     return entities

# Define an endpoint for NER
@app.post("/ner", response_model=list[EntityResponse])
async def extract_entities(request: TextRequest):
    # Process the text using the custom NER model
    doc = nlp(request.text)
    entities = [
        EntityResponse(text=ent.text, start=ent.start_char, end=ent.end_char, label=ent.label_)
        for ent in doc.ents
    ]
    
    if not entities:
        raise HTTPException(status_code=404, detail="No entities found")

    return entities

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
