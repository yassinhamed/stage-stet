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
        tca_value = item.find('tca').text
        py_value = item.find('.py').text

        # Append the extracted information to the data list
        data.append({'tca': tca_value, '.py': py_value})

    # Return the data in a list of dictionaries
    return data

# Step 1: Define the path to the file.txt containing XML file paths
file_txt_path = 'File_found_exel_xml.txt'

# Step 2: Read the file.txt and process each XML file
with open(file_txt_path, 'r') as file:
    xml_file_paths = file.read().splitlines()

# Open the output files for writing
XML_file_found_tca = open('XML_file_found_tca.txt', 'w')
File_xml_not_found_tca = open('File_xml_not_found_tca.txt', 'w')

for xml_file_path in xml_file_paths:
    if os.path.exists(xml_file_path):
        print(f"Reading XML file: {xml_file_path}")
        df = read_xml_file(xml_file_path)

        # Write the extracted data to the output file (assuming you want to write the 'tca' values)
        for item in df:
            tca_value = item['tca']
            XML_file_found_tca.write(tca_value + "\n")

        print(df)  # Print the data (optional, you can remove this if not needed)
        print("\n")
    else:
        print(f"XML file not found: {xml_file_path}\n")
        File_xml_not_found_tca.write(f"XML file not found: {xml_file_path}\n")

# Close the output files after writing
XML_file_found_tca.close()
File_xml_not_found_tca.close()
