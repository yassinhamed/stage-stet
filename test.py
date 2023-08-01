import pandas as pd
import os
import re

def search(file,exl):
    for i in exl:
        if i==file:
            return True
    else:
        return False


def find_file_in_folders(root_folder, target_file_name):
    
    for foldername, _, filenames in os.walk(root_folder):
        if target_file_name in filenames:
            return os.path.join(foldername, target_file_name)
    return None




test_to_read_PIL = pd.read_excel("Test suites execution (2).xlsx",sheet_name="PIL QNX")
test_to_read_HIL = pd.read_excel("Test suites execution (2).xlsx",sheet_name="HIL QNX")
colonne_HIL = pd.DataFrame(test_to_read_HIL, columns=['Test suite'])
colonne_PIL = pd.DataFrame(test_to_read_PIL, columns=['Domain'])
# Get the list of column names from the DataFrame

column_file_to_see_HIL = test_to_read_HIL.iloc[:, 1].tolist()
column_file_to_see_PIL = test_to_read_PIL.iloc[:, 1].tolist()

# no repetition
column_file_to_see_HIL = list(set(column_file_to_see_HIL))
#print(len(set(column_file_to_see_HIL))== len(column_file_to_see_HIL))
File_found=open('File_found_exel_xml.txt','w')
File_not_found=open('File_not_found_exel_xml.txt','w')
for item in column_file_to_see_HIL:
    result = find_file_in_folders('TestSeries', item)
    if result:
        #print(f"File found: {result}")
        File_found.write(result+"\n")
        df = pd.read_xml(result)
        print(df.head())
    

    else:
        #print("File not found.")
        File_not_found.write(item+"\n")
File_found.close()
File_not_found.close()




column_file_to_see = [str(exl_elem).upper() for exl_elem in column_file_to_see_PIL + column_file_to_see_HIL if isinstance(exl_elem, str)]
column_file_to_see = [item.rstrip("\xa0") for item in column_file_to_see]
#print(column_file_to_see )
file_folders=open('valide_test_folder.txt','r')
found=open('founed folder name on excell.txt','w')
not_found=open('not founed folder name on excell.txt','w')


valid_folder_list=re.split('\n',file_folders.read())
valid_test = []
invalid_test = []

for i in valid_folder_list:
    if search(i,column_file_to_see):
        valid_test.append(i)
        found.write(i+'\n')
    else:
        invalid_test.append(i)
        not_found.write(i+"\n")
not_found.close()
found.close()
#print("Valid Test Files:", valid_test)
#print("Invalid Test Files:", invalid_test)






