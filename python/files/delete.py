import glob


def delete_files(source_dir, pattern):
    """Delete files matching `pattern` in `source_dir`."""

    # Retrieve a list of all matching files
    matching_files = glob.glob(pattern)

    if matching_files == []:
        print("There is no file to delete.")
    else:
        print(f"Files found in {source_dir}:")

        for matching_file in matching_files:
            print(matching_file)

        for matching_file in matching_files:
            os.remove(matching_file)
        print("Files deleted.")
        return
