import spacy
from spacy.util import minibatch, compounding
import random
import json

# Load the training data
def load_data(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            example = json.loads(line)
            data.append((example['text'], example['cats']))
    return data

# Define the paths to the training data and the output directory
train_data = load_data('data/passporttrain.spacy')
output_dir = 'model'

# Define the number of training iterations
n_iter = 10

# Load the blank English model
nlp = spacy.blank('en')

# Create the text categorizer pipe and add it to the pipeline
textcat = nlp.create_pipe('textcat')
nlp.add_pipe(textcat, last=True)

# Add the labels to the text categorizer
textcat.add_label('passport')
textcat.add_label('SA_ID_CARD')

# Disable unnecessary pipeline components
pipe_exceptions = ['textcat']
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
with nlp.disable_pipes(*unaffected_pipes):
    # Training loop
    optimizer = nlp.begin_training()
    for iteration in range(n_iter):
        # Shuffle the training data
        random.shuffle(train_data)
        losses = {}
        # Create mini-batches
        batches = minibatch(train_data, size=compounding(4.0, 32.0, 1.001))
        # Iterate over the mini-batches
        for batch in batches:
            texts, annotations = zip(*batch)
            # Update the model with the current batch
            nlp.update(texts, annotations, sgd=optimizer, drop=0.2, losses=losses)
        print(f'Iteration {iteration+1}: Losses - {losses}')

# Save the trained model to the output directory
nlp.to_disk(output_dir)
