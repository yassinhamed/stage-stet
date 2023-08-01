import os
import re
import ast
import astor
def find_variable(file_path, variable_name):
    file=open(file_path, "r")
    tree = ast.parse(file.read(), filename=file_path)

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == variable_name:
                    return node.value
    return None

def eval_variable_value(value_node):
    return ast.literal_eval(value_node)


def status_contain(path):

    file_path = os.path.normpath(path)
    variable_name_to_search = "STATUS"

    variable_value = find_variable(file_path, variable_name_to_search)
    if variable_value:
        value = eval_variable_value(variable_value)
        variable_source = astor.to_source(variable_value).strip()
        return(variable_source)
    else:
        return ('')

def unique_list (folders_file):
    file_folder=open(folders_file,"r")
    new_file=(file_folder.read())
    new_file=set(re.split('\n',new_file))
    new_file=[folder_name.upper() for folder_name in new_file]
    file_folder.close()
    file_folder=open(folders_file,"w")
    
    for i in new_file:
        file_folder.write(i+'\n')
    file_folder.close()

def path_to_name(path):
    tca=path.index('tca')
    path=path[tca:]
    return path
def path_to_folder(path):
    tca = path.index("tca")
    folder = tca - 2
    while True:
        if path[folder] == '\\':
            break
        else:
            folder -= 1
    return path[folder+1:tca-1]
  
    
folder_path = "trainee"  

# List all Python files (files with .py extension) in the folder and its subfolders
python_files = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".py") and file.startswith("tca"):
            python_files.append(os.path.join(root, file))

#print(len(python_files))

#python_files=['trainee\trainee\SOP_2207_2311\Hil\Automated\TDFNext\TDFXPadAutomationTool\Tests\INFRA_SAMPLES\tca_INFRA_SAMPLES_MediaGatewayUpdate.py']
valide_testfiles=open('valide_testfiles.txt','w')
valide_test_folder=open('valide_test_folder.txt','w')
valid_test = []
valid_unique_folders=[]
i = 1
j = 1
e = None  # Initialize the variable 'e' to None

for python_file in python_files:
    try:
        j = j + 1
        if status_contain(python_file) == '"""Ready"""':
            i += 1
            valid_test.append(python_file)
            valide_testfiles.write(path_to_name(python_file)+'\n')
            folder = path_to_folder(python_file)
            if folder not in valid_unique_folders: 
                valid_unique_folders.append(folder)
                valide_test_folder.write(folder+'\n')
            
            
    except Exception as ex:
        """e = ex  # Capture the exception and assign it to the variable 'e'
        print(f"Exception occurred in file: {python_file}")"""
        pass
print(f"Current values of i and j: {i}, {j}")
    
 
valide_testfiles.close()
unique_list ('valide_test_folder.txt')
print(len(valid_test))
print(valid_unique_folders)
