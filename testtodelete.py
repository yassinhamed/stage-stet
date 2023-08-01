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


def get_tca_name(file_path):
    with open(file_path, 'r') as file:
        file_cont = file.read()
        file_cont_list = file_cont.split("\n")
        tca_list = []
        for tca in file_cont_list:
            tca_start = tca.find("tca")
            if tca_start != -1:
                tca = tca[tca_start:tca.index(".py")]
                tca_list.append(tca)
        return tca_list

def get_tca_list_LINUX(file_without_py_extension, QNX_testfiles):
    tca_list_QNX = get_tca_name(file_without_py_extension)
    tca_list_QNX += get_tca_name(QNX_testfiles)
    return tca_list_QNX
def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2:
            common_elements.append(item)
    return common_elements

def main():
    file_without_py_extension = 'File_xml_found_tca.txt'
    LINUX_testfiles = 'QNX_testfiles.txt'
    LINUX_QNX_testfiles = 'LINUX_QNX_testfiles.txt'
    different_LINUX_QNX_testfiles = 'LINUX_QNX_testfiles.txt'

    file_xml = read_file(file_without_py_extension)
    file_qnx = get_tca_list_LINUX(LINUX_testfiles, LINUX_QNX_testfiles)

    tca_qnx = find_common_elements(file_xml,file_qnx)
    print((set(file_xml)))
    print(set(file_qnx))
    print((set(file_qnx))==file_xml)

    write_file('QNX_tca_excell.txt', tca_qnx)
with open('LINUX_QNX_testfiles.txt', 'r') as LINUX_QNX_testfiles:
    line = LINUX_QNX_testfiles.readline()
    while line:
        #print(line.strip())  
        line = LINUX_QNX_testfiles.readline()
        #print("\n")
if __name__ == "__main__":
    main()
