import os
import xml.etree.ElementTree as ET

def read_xml_file(xml_file_path):
    # Parse the XML file and extract data
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Initialize an empty list to hold data extracted from XML
    data = []

    # Iterate through the XML and extract relevant information
    for item in root.findall('item'):
        data.append({'tca': item.find('tca').text, '.py': item.find('.py').text})

    # Return the data in a list of dictionaries
    return data

def check_file1_in_xml(xml_file_path, file1_txt_path):
    # Read the content of file1.txt
    with open(file1_txt_path, 'r') as file1:
        file1_content = file1.read().strip()

    # Read the content of the XML file
    with open(xml_file_path, 'r') as file_xml:
        xml_content = file_xml.read()

    # Check if the content of file1.txt exists in the XML content
    if file1_content in xml_content:
        print(f"The content of {file1_txt_path} exists in the XML file {xml_file_path}.")
    else:
        print(f"The content of {file1_txt_path} does not exist in the XML file {xml_file_path}.")

# Step 1: Read the path to the XML file from path.xml
with open('path.xml', 'r') as path_file:
    xml_file_path = path_file.read().strip()

# Step 2: Define the path to file1.txt
file1_txt_path = 'File_found_exel_xml.txt'

# Step 3: Check if file1.txt content exists in the XML file
if os.path.exists(xml_file_path):
    print(f"Reading XML file: {xml_file_path}")
    df = read_xml_file(xml_file_path)
    check_file1_in_xml(xml_file_path, file1_txt_path)
    print("\n")
else:
    print(f"XML file not found: {xml_file_path}\n")
