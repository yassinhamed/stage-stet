import os
import xml.etree.ElementTree as ET
import re

def find_tca(file_tca_content):
    result = re.findall(r'tca.*?"', file_tca_content)
    result = [item[:-1] for item in result]
    return result

def extract_tests(xml_content):
    root = ET.fromstring(xml_content)
    test_data = []
    for group in root.findall('.//Group'):
        for test in group.findall('.//Test'):
            test_name = test.get('name')
            test_repetition = test.get('repetition')
            test_data.append({'name': test_name, 'repetition': test_repetition})
    return test_data

# Step 1: Define the path to file1.txt
file1_txt_path = 'stage02.txt'

found = open('founed tca name on xml_3.txt', 'w')
tca_file = open('tca_3_name_3.txt', 'w')

with open(file1_txt_path, 'r') as file2:
    xml_file_paths = file2.read().splitlines()

# Step 2: Read the paths to XML files from file1.txt and process them one by one
for xml_file_path in xml_file_paths:
    if xml_file_path.endswith('.xml'):
        print(f"Reading XML file: {xml_file_path}")
        if os.path.exists(xml_file_path):
            with open(xml_file_path, 'r') as xml_file:
                xml_content = xml_file.read()
                tca = find_tca(xml_content)
                print(set(tca))
                print("\n")

                # Extract Test names and their repetition attributes
                test_data = extract_tests(xml_content)

                # Print or do something with the extracted test data
                for test in test_data:
                    tca_file.write(f"{test['name']}\n")

                # Write the extracted test data to the output file
                found.write(str(test_data) + "\n")
        else:
            print(f"XML file not found: {xml_file_path}\n")
    else:
        print(f"Invalid XML file path: {xml_file_path}\n")

for test in test_data:
    tca_file.write(f"Test Name: {test['name']}, Repetition: {test['repetition']}\n")
tca_file.close()
found.close()
