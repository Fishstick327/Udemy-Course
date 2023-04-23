import os
import shutil
import filecmp
import subprocess
import re

#this function is made to find files, given the option to let the user to search through all directory and subdirectory or just the current directory.
def find_files(include_keywords, exclude_keywords, directory, search_subfolders):
    found_files = []
    if search_subfolders:
        #root is for the current directory and "_" is for any subfolder in there. os.walk() let you search for subdirectory so when it append it already have the path.
        for root, _, files in os.walk(directory):
            for file in files:
                #this check for any exclude keyword after the removing all spaces and converting to lowercases
                if any(keyword.lower() in file.lower().replace(" ", "") for keyword in exclude_keywords):
                    #this is to appends the full path of the file and join it with the root directory and added to the found_files to be access.
                    found_files.append(os.path.join(root, file))
    else:
        #os.listdir() is the list of specific directory that user want to search in.
        for file in os.listdir(directory):
            #isfile() is to check if the file is a file or not. 
            if os.path.isfile(os.path.join(directory, file)):
                if any(keyword.lower() in file.lower().replace(" ", "") for keyword in include_keywords):
                    found_files.append(os.path.join(directory, file))
    return found_files

#this function is made to find duplicates, given the option to let the user to search through all directory and subdirectory or just the current directory.
def find_duplicates(directory, search_subfolders):
    found_files = {}
    if search_subfolders:
        for root,_, files in os.walk(directory):
            for file in files:
                if file is found_files:
                    found_files[file].append(os.path.join(root, file))
                else:
                    found_files[file] = [os.path.join(root, file)]
    else:
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                if file in found_files:
                    found_files[file].append(os.path.join(directory, file))
                else:
                    found_files[file] = [os.path.join(directory, file)]
                                

def lete_smaller_duplicate(duplicates):
def write_to_txt(file_list, output_file):
def get_renamed_files(file_list, user_input):
def rename_files(file_list, user_input):
def move_files(file_list):
def scan_directory(directory):
def search_files(directory, search_subfolders)
def menu():
def main():
