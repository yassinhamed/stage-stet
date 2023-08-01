import pandas as pd
import os
import re
def search(file,exl):
    for i in exl:
        if i==file:
            return True
    else:
        return False
    


test_to_read_PIL = pd.read_excel("Test suites execution (2).xlsx",sheet_name="PIL QNX")
test_to_read_HIL = pd.read_excel("Test suites execution (2).xlsx",sheet_name="HIL QNX")
colonne_HIL = pd.DataFrame(test_to_read_HIL, columns=['Domain'])
colonne_PIL = pd.DataFrame(test_to_read_PIL, columns=['Domain'])
# Get the list of column names from the DataFrame

column_file_to_see_HIL = test_to_read_HIL.iloc[:, 0].tolist()
column_file_to_see_PIL = test_to_read_PIL.iloc[:, 1].tolist()

column_file_to_see = [str(exl_elem).upper() for exl_elem in column_file_to_see_PIL + column_file_to_see_HIL if isinstance(exl_elem, str)]
column_file_to_see = [item.rstrip("\xa0") for item in column_file_to_see]
print(column_file_to_see )
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
print("Valid Test Files:", valid_test)
print("Invalid Test Files:", invalid_test)


"""import pandas as pd
import re

def search(file, exl):
    matching_test_suites = [test_suite_name for test_suite_name in exl if file in test_suite_name]
    return matching_test_suites

test_to_read = pd.read_excel("Test suites execution (2).xlsx", sheet_name="HIL QNX")
column_file_to_see = test_to_read['Test suite'].tolist()

file_folders = open('valide_test_folder.txt', 'r')
valid_folder_list = re.split('\n', file_folders.read())

valid_test = []
invalid_test = []

for file in valid_folder_list:
    matches = search(file, column_file_to_see)
    if matches:
        valid_test.extend(matches)  # Add to the list
    else:
        invalid_test.append(file)

print("Valid Test Suite Names:", valid_test)
print("Invalid Test Files:", invalid_test)"""



