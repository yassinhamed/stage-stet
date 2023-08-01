import os
import glob

def read_xml_files_from_folder(xml_folder):
    xml_data_list = []

    # Find all XML files in the xml_folder and its subdirectories
    xml_files = glob.glob(os.path.join(xml_folder, '**/*.xml'), recursive=True)

    for xml_filepath in xml_files:
        try:
            with open(xml_filepath, 'r') as xml_file:
                xml_filename = os.path.basename(xml_filepath)
                xml_data = xml_file.read()
                xml_data_list.append((xml_filename, xml_data))
        except FileNotFoundError:
            print(f"File not found: {xml_filepath}")
        except Exception as ex:
            print(f"Error reading XML file: {xml_filepath}, Error: {ex}")

    return xml_data_list

def main():
    xml_folder_path = "trainee"
    xml_data_list = read_xml_files_from_folder(xml_folder_path)

    # Process the XML data
    for xml_filename, xml_data in xml_data_list:
        # Now you have the XML file name and the XML data as strings, you can further process it as needed.
        print(f"File: {xml_filename}")
        print("XML Data:")
        print(xml_data)
        print()

if __name__ == "__main__":
    main()
