import os

# Get current working directory
current_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_dir)  # Affect files in current working directory

for f in os.listdir():
    file_name = os.path.basename(f)  # example: 'file.txt'
    if "test" in file_name:  # exclude files with 'test'
        continue

    new_name = f"new_{file_name}"
    print(new_name)

    os.rename(file_name, new_name)
