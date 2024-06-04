import os


def print_directory_structure(folder_path, file, indent=""):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            file.write(indent + f"📁 {item}\n")
            print_directory_structure(item_path, file, indent + "    ")
        else:
            file.write(indent + f"📄 {item}\n")


# Get the current directory
current_directory = os.getcwd()

# Open a file to write the output
with open("directory_structure.txt", "w", encoding="utf-8") as file:
    # Call the function with the current directory and file object
    print_directory_structure(current_directory, file)

print("Directory structure has been written to directory_structure.txt")
