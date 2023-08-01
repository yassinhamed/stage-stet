def remove_py_extension(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    # Remove the '.py' extension from each line
    lines_without_py = [line.strip()[:-3] for line in lines]

    # Save the modified lines to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write("\n".join(lines_without_py))

# Step 1: Define the path to the input file.txt
input_file_path = 'valide_testfiles.txt'

# Step 2: Define the path to the output file without .py extension
output_file_path = 'file_without_py_extension.txt'

# Step 3: Remove .py extension and save to the output file
remove_py_extension(input_file_path, output_file_path)
