import os

def save_directory_structure(root_dir, output_file):
    with open(output_file, 'w') as f:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            depth = dirpath.count(os.sep)
            indent = '  ' * depth
            f.write('{}{}/\n'.format(indent, os.path.basename(dirpath)))
            sub_indent = '  ' * (depth + 1)
            for filename in filenames:
                f.write('{}{}\n'.format(sub_indent, filename))

if __name__ == "__main__":
    root_directory = os.path.dirname(os.path.abspath(__file__))
    output_file = "directory_structure.txt"
    save_directory_structure(root_directory, output_file)
    print("Directory structure saved to", output_file)
