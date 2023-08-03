import json

def convert_data(input_file, output_file):
    data = []
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                segments = line.split(' ')
                text = ' '.join(segments[:-1])
                labels = segments[-1].split('/')
                labels_dict = {"SA_ID_CARD": True}  # Category name is "passport"
                data.append({"text": text, "cats": labels_dict})

    with open(output_file, 'w') as f:
        for example in data:
            f.write(json.dumps(example) + '\n')

# Provide the path to your input file and the desired output file
input_file = 'data/SA_ID Card.txt'
output_file = 'data/SA_ID Card_train.spacy'

# Convert the data to the required format
convert_data(input_file, output_file)
