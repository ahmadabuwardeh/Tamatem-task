import os
import shutil


def create_subfolders(src_folder):
    language_set = set(filename.split('-')[0] for filename in os.listdir(src_folder) if filename.endswith('.txt'))
    for language in language_set:
        subfolder = os.path.join(src_folder, language)
        os.makedirs(subfolder, exist_ok=True)


def group_files_into_subfolders(src_folder):
    files = [filename for filename in os.listdir(src_folder) if filename.endswith('.txt')]
    for filename in files:
        language = filename.split('-')[0]
        src_file = os.path.join(src_folder, filename)
        dst_folder = os.path.join(src_folder, language)
        dst_file = os.path.join(dst_folder, filename)

        # Check if the destination folder exists, if not, create it
        if not os.path.exists(dst_folder):
            os.makedirs(dst_folder, exist_ok=True)

        if not os.path.exists(dst_file):
            shutil.move(src_file, dst_file)
        else:
            print(f"Warning: File '{filename}' already exists in the destination folder.")


if __name__ == "__main__":
    folder_path = "./files"

    # Check if the source folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
    else:
        create_subfolders(folder_path)
        group_files_into_subfolders(folder_path)
        print("Files successfully grouped into subfolders.")
