import os

def rename_files_with_underscore(directory):
    for filename in os.listdir(directory):
        if ' ' in filename:
            new_filename = filename.replace(' ', '_')
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    rename_files_with_underscore(directory)