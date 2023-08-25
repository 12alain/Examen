import os
import nbformat
import subprocess
from nbformat.v4 import new_notebook , new_code_cell

directory = os.path.join(os.getcwd())

def create_project_structure():

    directory = os.path.join(os.getcwd())
    folders = ["data/raw", "data/cleaned", "docs",
               "models", "notebooks", "reports", "src"]


    for folder in folders:
            
            folder_path = os.path.join(directory, folder)
            os.makedirs(folder_path, exist_ok=True)
            # Crée un fichier .gitkeep dans les dossiers vides pour qu'ils soient suivis
            with open(os.path.join(folder_path, ".gitkeep"), 'w') as f:
                pass

def create_initial_files():

    files = ["LICENSE", "Makefile", "README.md", ".gitignore",
             "requirements.txt"]

    for file in files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'w') as f:
            file_content = ''
            f.write(file_content)
create_initial_files()