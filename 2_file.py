import os
import re
import xml.etree.ElementTree as ET
# Creating a dictionary with some key-value pairs
files = {
    'name': '',
    'repitetion': 0,
    'file': ''
}
def find_tca(file_tca):
    file_tca=open(file_tca,'r')
    file_cont=file_tca.read()

    result=re.findall(r'tca.*?"',file_cont)
    result=[item[:-1] for item in result]
    return result

def split_file(file_tca):
    file_tca=open(file_tca,'r')
    file_cont=file_tca.read()
    results=re.split(r'<?xml version="1.0" ?> \n',file_cont)
    file_tca.close()
    return results




def check_line_in_xml(file_txt_path, xml_file_path):
    # Read the lines from file1.txt
    with open(file_txt_path, 'r') as file1:
        lines = file1.read().splitlines()

    # Read the content of the XML file
    with open(xml_file_path, 'r') as file_xml:
        xml_content = file_xml.read()

    # Check if any line from file1.txt exists in the XML content
    for line in lines:
        if line in xml_content:
            print(f"The line '{line}' from {file_txt_path} exists in the XML file {xml_file_path}.")
        else:
            print(f"The line '{line}' from {file_txt_path} does not exist in the XML file {xml_file_path}.")

# Step 1: Define the path to file1.txt and file2.txt
file1_txt_path = 'File_found_exel_xml.txt'
file2_txt_path = 'file_without_py_extension.txt'
found=open('founed tca name on xml.txt','w')
tca_file=open('tca name .txt','w')
with open(file1_txt_path, 'r') as file2:
    xml_file_paths = file2.read().splitlines()
# Step 2: Read the paths to XML files from file1.txt and process them one by one

with open(file2_txt_path, 'r') as file1:
    txt_file_paths = file1.read().splitlines()

for xml_file_path in xml_file_paths:
    if xml_file_path.endswith('.xml'):
        print(f"Reading XML file: {xml_file_path}")
        if os.path.exists(xml_file_path):
            with open(xml_file_path, 'r') as xml_file:
                xml_content = xml_file.read()
                tca=find_tca('founed tca name on xml.txt')
                #print(set(find_tca('founed tca name on xml.txt')))
                print("\n")

     
                 
                


                found.write(xml_content + "\n")
                
                    
                    
            



            # Here you can perform any operations with the xml_content
            print("Content of the XML file:")
            #print(xml_content)
            print("\n")
        else:
            print(f"XML file not found: {xml_file_path}\n")
    else:
        print(f"Invalid XML file path: {xml_file_path}\n")
print(set(find_tca('founed tca name on xml.txt')))
for name in find_tca('founed tca name on xml.txt'):
    tca_file.write(str(name) + "\n")
tca_file.close()
found.close()

#print(set(find_tca('founed tca name on xml.txt')))
    
