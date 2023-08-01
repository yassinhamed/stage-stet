def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    return content

def compare_files(file1_content, file2_content):
    file1_lines = set(file1_content)
    file2_lines = set(file2_content)

    unique_to_file1 = file1_lines - file2_lines
    unique_to_file2 = file2_lines - file1_lines

    return unique_to_file1, unique_to_file2

def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

def main():
    file1_path = 'file_without_py_extension.txt'
    file2_path = 'tca name .txt'
    file3_path = 'not_same_tca_name.txt'

    file1_content = read_file(file1_path)
    file2_content = read_file(file2_path)

    unique_file1, unique_file2 = compare_files(file1_content, file2_content)

    unique_lines = unique_file1.union(unique_file2)
    write_file(file3_path, unique_lines)

if __name__ == "__main__":
    main()
