import os
import shutil


def rollback_files(src_folder):
    subfolders = [f.path for f in os.scandir(src_folder) if f.is_dir()]

    for subfolder in subfolders:
        files = os.listdir(subfolder)
        for filename in files:
            src_file = os.path.join(subfolder, filename)
            dst_file = os.path.join(src_folder, filename)
            shutil.move(src_file, dst_file)

        os.rmdir(subfolder)


if __name__ == "__main__":
    folder_path = "./files"
    rollback_files(folder_path)
