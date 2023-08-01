import pandas as pd
import os

def search(name):
    folder_path = r"C:\Users\ASUS\Downloads\inputfiles (2)\TestSeries\TestSeries"
    file_path = os.path.join(folder_path, str(name))
    
    try:
        with open(file_path, "r"):
            pass  # Do nothing, just checking if the file exists
        return True
    except FileNotFoundError:
        return False


test_to_read = pd.read_excel("Test suites execution (2).xlsx",sheet_name="HIL QNX")
colonne = pd.DataFrame(test_to_read, columns=['Test suite'])

# Get the list of column names from the DataFrame
column_file_to_see = test_to_read.iloc[:, 1].tolist()
print(column_file_to_see)
valid_test = []
invalid_test = []

for i in column_file_to_see:
    if search(i):
        valid_test.append(i)
    else:
        invalid_test.append(i)
print("Valid Test Files:", valid_test)
print("Invalid Test Files:", invalid_test)

