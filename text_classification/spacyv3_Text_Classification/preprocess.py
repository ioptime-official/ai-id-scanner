# Read the input text file
input_file = 'data/SA Lisence.txt'
output_file = 'data/SA Lisence_output.txt'

with open(input_file, "r") as file:
    lines = file.readlines()

modified_lines = []
for line in lines:
    line = line.strip()
    modified_line = '"' + line + '",\n'
    modified_lines.append(modified_line)

with open(output_file, "w") as file:
    file.writelines(modified_lines)
