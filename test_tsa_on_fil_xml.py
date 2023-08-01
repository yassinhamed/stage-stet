"""def check_tca_in_xml(xml_file_path):
    # Read the content of the XML file
    with open(xml_file_path, 'r') as xml_file:
        xml_content = xml_file.read()

    # Check if "tca" exists in the XML content
    return "tca" in xml_content

# Step 1: Define the paths to the files
file_txt_path = 'valide_testfiles.txt'
file_xml_path = 'TestSeries\TestSeries\TS_Diag_IPSEC_QNX.xml'

# Step 2: Read the content of file1.txt
with open(file_txt_path, 'r') as file1:
    file1_content = file1.read()

# Step 3: Check if "tca" exists in file1_content
if "tca" in file1_content:
    # Step 4: If "tca" exists, read and check the content of file2.xml
    tca_exists_in_xml = check_tca_in_xml(file_xml_path)
    if tca_exists_in_xml:
        print("File2.xml contains 'tca'.")
    else:
        print("File2.xml does not contain 'tca'.")
else:
    print("The file1.txt does not contain 'tca'.")"""
"""import xml.etree.ElementTree as ET

def compare_first_line_with_xml(first_file_path, xml_file_path):
    # Read the first line of the first file (file1.txt)
    with open(first_file_path, 'r') as file1:
        first_line = file1.readline().strip()

    # Read the content of the XML file (file2.xml)
    with open(xml_file_path, 'r') as file2:
        xml_content = file2.read()

    # Compare the first line with the XML content
    if first_line in xml_content:
        print(f"The content of the first line '{first_line}' from file1.txt exists in file2.xml.")
    else:
        print(f"The content of the first line '{first_line}' from file1.txt does not exist in file2.xml.")

# Step 1: Define the paths to file1.txt and file2.xml
file1_path = 'file_without_py_extension.txt'
file2_path = 'TestSeries\TestSeries\TS_Application_QNX.xml'

# Step 2: Compare the content
compare_first_line_with_xml(file1_path, file2_path)"""
import xml.etree.ElementTree as ET

def compare_lines_with_xml(file_txt_path, xml_file_path):
    # Read the content of file_without_py_extension.txt
    with open(file_txt_path, 'r') as file_txt:
        lines_without_py = file_txt.read().splitlines()

    # Read the content of the XML file
    with open(xml_file_path, 'r') as file_xml:
        xml_content = file_xml.read()

    # Compare the content of each line with the XML content
    for line in lines_without_py:
        if line in xml_content:
            print(f"The content of '{line}' from file_without_py_extension.txt exists in file2.xml.")
        else:
            print(f"  does not exist .")
            

# Step 1: Define the paths to file_without_py_extension.txt and file2.xml
file_txt_path = 'file_without_py_extension.txt'
xml_file_path = r'TestSeries\TestSeries\TS_Application_QNX_ProxyApp.xml'

# Step 2: Compare the content of each line
compare_lines_with_xml(file_txt_path, xml_file_path)
