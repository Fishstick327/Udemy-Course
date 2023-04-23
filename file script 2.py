import os
import shutil
import filecmp
import subprocess
import re


def find_files(include_keywords, exclude_keywords, directory, search_subfolders):
    found_files = []
    if search_subfolders:
        for root, _, files in os.walk(directory):
            for file in files:
                if any(keyword.lower() in file.lower().replace(" ", "") for keyword in include_keywords) and not any(keyword.lower() in file.lower().replace(" ", "") for keyword in exclude_keywords):
                    found_files.append(os.path.join(root, file))
    else:
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                if any(keyword.lower() in file.lower().replace(" ", "") for keyword in include_keywords) and not any(keyword.lower() in file.lower().replace(" ", "") for keyword in exclude_keywords):
                    found_files.append(os.path.join(directory, file))
    return found_files

def find_duplicates(directory, search_subfolders):
    found_files = {}
    if search_subfolders:
        for root, _, files in os.walk(directory):
            for file in files:
                if file in found_files:
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

    duplicates = [(found_files[file][i], found_files[file][j]) for file in found_files for i in range(len(found_files[file])) for j in range(i + 1, len(found_files[file]))]

    return duplicates

def delete_smaller_duplicate(duplicates):
    for duplicate in duplicates:
        file1_size = os.path.getsize(duplicate[0])
        file2_size = os.path.getsize(duplicate[1])

        if file1_size <= file2_size:
            os.remove(duplicate[0])
            print(f"Deleted {duplicate[0]}")
        else:
            os.remove(duplicate[1])
            print(f"Deleted {duplicate[1]}")

def write_to_txt(file_list, output_file):
    try:
        with open(output_file, "w", encoding='utf-8') as f:
            for file in file_list:
                f.write(file + "\n")
        print(f"Output written to {output_file}")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")



def get_renamed_files(file_list, user_input):
    renamed_files = []
    name_count = {}
    for file in file_list:
        dirname, filename = os.path.split(file)
        name, ext = os.path.splitext(filename)
        filename_parts = re.split(r'(\s+)', name)
        new_filename_parts = [user_input if "#" in part else part for part in filename_parts]
        new_name = "".join(new_filename_parts)

        if not any("#" in part for part in filename_parts):
            new_name = name + " " + user_input

        new_filename = f"{new_name}{ext}"

        # Check for duplicate names and append a unique number if necessary
        if new_filename in name_count:
            name_count[new_filename] += 1
            new_filename = f"{new_name}_{name_count[new_filename]}{ext}"
        else:
            name_count[new_filename] = 0

        new_file = os.path.join(dirname, new_filename)
        renamed_files.append(new_file)
    return renamed_files

def rename_files(file_list, user_input):
    for old_file, new_file in zip(file_list, get_renamed_files(file_list, user_input)):
        os.rename(old_file, new_file)

def move_files(file_list):
    move_keywords = input("Enter keywords to filter files to move (separated by spaces): ").split()
    filtered_files = [file for file in file_list if all(keyword.lower() in file.lower().replace(" ", "") for keyword in move_keywords)]

    new_directory = input("Enter the new directory path: ")
    new_directory = new_directory.strip('"')  # Remove quotes from the input
    new_directory = os.path.normpath(new_directory)  # Normalize the directory path
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    for file in filtered_files:
        shutil.move(file, new_directory)

def scan_directory(directory):
    total_files = 0
    total_folder = 0
    scanned_files = []

    for root, dir, files in os.walk(directory):
        total_files += len(files)
        total_folder += len(dir)
        for file in files:
            scanned_files.append(os.path.join(root, file))

    output_file = os.path.join(os.path.expanduser("~"), "Desktop", "scanned_file.txt")
    write_to_txt(scanned_files, output_file)

    return scanned_files, total_files, total_folder

def menu():
    print("\nMenu:")
    print("1. Search for files")
    print("2. Move files")
    print("3. Rename files")
    print("4. Scan directory")
    print("5. Exit")
    choice = input("Enter the number of your choice: ")
    return choice

def main():
    directory = r"C:\\"  #Replace with your desired directory path as a raw string or with double backslashes
    found_files = []

    while True:
        choice = menu()

        if choice == "1":
            search_subfolders_option = input("Do you want to search in subfolders? (yes/no) ")
            search_subfolders = search_subfolders_option.lower() == "yes"
            found_files = search_files(directory, search_subfolders)
        elif choice == "2":
            if found_files:
                move_files(found_files)
            else:
                print("No files found. Please run the search first.")
        elif choice == "3":
            if found_files:
                user_input = input("Enter the text to replace '#' with: ")
                renamed_files = get_renamed_files(found_files, user_input)
                preview_file = os.path.join(os.path.expanduser("~"), "Desktop", "rename_preview.txt")
                write_to_txt(renamed_files, preview_file)

                print("Edit the rename_preview.txt file to make changes to the file names.")
                input("Press Enter to continue after you have saved the changes in the rename_preview.txt file.")

                with open(preview_file, "r", encoding='utf-8') as f:
                    edited_renamed_files = [line.strip() for line in f.readlines()]

                for old_file, new_file in zip(found_files, edited_renamed_files):
                    os.rename(old_file, new_file)

                print("Files have been renamed.")
                open_txt_file = input("Do you want to open the rename_preview.txt file? (yes/no) ")
                if open_txt_file.lower() == "yes":
                    if os.name == 'nt':  # For Windows
                        os.startfile(preview_file)
                    elif os.name == 'posix':  # For macOS and Linux
                        subprocess.call(('open', preview_file))
            else:
                print("No files found. Please run the search first.")
        
        elif choice == "4":
            scan_directory_option = input("Enter the Directory path to scan: ")
            scan_directory_option = scan_directory_option.strip('"') #remove the quotes from input so u dont need quotes
            scan_directory_option = os.path.normpath(scan_directory_option) #normalize the dir path
            found_files, total_files, total_folders = scan_directory(scan_directory_option)
            print(f"Total number of files: {total_files}")
            print(f"Total number of folders: {total_folders}")

        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def search_files(directory, search_subfolders):
    search_option = input("Do you want to search for keywords or duplicates? (keywords/duplicates) ")

    input_directory = input("Enter the directory path to search: ")
    input_directory = input_directory.strip('"')
    input_directory = os.path.normpath(input_directory)

    if search_option.lower() == "keywords":
        include_keywords = input("Enter keywords to INCLUDE in the search (separated by spaces): ").split()
        exclude_keywords = input("Enter keywords to EXCLUDE from the search (separated by spaces): ").split()
        found_files = find_files(include_keywords, exclude_keywords, directory, search_subfolders)
        output_file = os.path.join(os.path.expanduser("~"), "Desktop", "found_files.txt")
        write_to_txt(found_files, output_file)
        return found_files
    elif search_option.lower() == "duplicates":
        duplicates = find_duplicates(directory, search_subfolders)
        output_file = os.path.join(os.path.expanduser("~"), "Desktop", "duplicate_files.txt")
        write_to_txt([" - ".join(pair) for pair in duplicates], output_file)
        print("Duplicate files found:")
        for pair in duplicates:
            print(f"{pair[0]} - {pair[1]}")
        delete_option = input("Do you want to delete the smaller file size duplicate? (yes/no) ")
        if delete_option.lower() == "yes":
            delete_smaller_duplicate(duplicates)
        return []
    else:
        print("Invalid search option. Please try again.")
        return []

if __name__ == "__main__":
    main()