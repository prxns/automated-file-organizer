import os
import shutil
from pathlib import Path

# File type mapping
File_Categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".java", ".cpp", ".js", ".html", ".css"],
}

def get_category(file_extension):
    """Return category name based on file extension"""
    for category, extensions in File_Categories.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"

def create_folder_if_not_exists(base_path, folder_name):
    """Create folder if it does not exist"""
    folder_path = base_path / folder_name
    folder_path.mkdir(exist_ok = True)
    return folder_path

def move_file_safely(source, destination_folder):
    """Move file safely and handle duplicate names"""
    destination = destination_folder / source.name

    #Handle Duplicate Files
    counter = 1
    while destination.exists():
        name = source.stem
        extension = source.suffix
        new_name = f"{name}_{counter}{extension}"
        destination = destination_folder/new_name
        counter += 1

    shutil.move(str(source), str(destination))
    print(f"Moved: {source.name} -> {destination_folder.name}/")

def organize_folder(folder_path):
    """Main function to organize files"""
    folder = Path(folder_path)

    if not folder.exists():
        print("Error: Folder does not exist")
        return
    
    print(f"\nOrganizing folder: {folder}\n")

    for item in folder.iterdir():

        #Skip directories
        if item.is_dir():
            continue

        #Get file extension
        extension = item.suffix

        #Get category
        category = get_category(extension)

        #Create category folder
        category_folder = create_folder_if_not_exists(folder, category)

        #Move file
        try:
            move_file_safely(item, category_folder)
        except Exception as e:
            print(f"Error moving file {item.name}: {e}")

    print("\nOrganization Complete.")

if __name__ == "__main__":
    folder_to_organize = input("Enter folder path to organize: ").strip()
    organize_folder(folder_to_organize)
