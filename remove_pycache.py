import os
import shutil

def delete_pycache(directory):
    for root, dirs, files in os.walk(directory):
        for d in dirs:
            if d == "__pycache__":
                pycache_path = os.path.join(root, d)
                print(f"Deleting {pycache_path}")
                shutil.rmtree(pycache_path)

if __name__ == "__main__":
    target_directory = input("Enter the target directory path: ")

    if os.path.exists(target_directory):
        delete_pycache(target_directory)
        print("__pycache__ directories deleted successfully.")
    else:
        print("The specified directory does not exist.")