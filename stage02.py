import pandas as pd
import os
test_to_read = pd.read_excel("Test suites execution (3).xlsx", sheet_name="PIL Linux")
colonne = pd.DataFrame(test_to_read, columns=['Test series New folder'])

# Get the list of column names from the DataFrame
column_file_to_see = test_to_read.iloc[:, 2].tolist()

# Example of using the search function to check if a file exists in the "trainee" folder
file_name_to_search = "example.txt"
f=open('stage02.txt', 'w')
for iteam in column_file_to_see:
    f.write('trainee\trainee\\'+iteam.strip() +"\n")
f.close()
with open('stage02.txt', 'r') as g:
    line = g.readline()
    while line:
        print(line)  
        line = g.readline()
        



