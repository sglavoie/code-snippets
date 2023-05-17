"""
Take in a bunch of CSV files and merge them into one CSV file without repeating
the header row.

Very fast for relatively small files, but must fit in memory.
Could optimize writing to disk. Left as an exercise for the reader.
"""
from pathlib import Path

DATA_PATH = Path("data")
HEADER_ROW = "COL1,COL2,COL3\n"
MERGE_FILEPATH = Path("merged_data.csv")


def merge_data(self) -> None:
    csv_files = list(DATA_PATH.glob("*.csv"))
    if not csv_files:
        raise ValueError("No CSV files found in data folder")

    # Manually set the header row, we're not guaranteed to get data back from all files
    merged_data = HEADER_ROW
    for csv_file in csv_files:
        with open(csv_file, "r") as f:
            # don't repeat the header row in the output
            data = "".join(f.readlines()[1:])
        merged_data += data

    with open(MERGE_FILEPATH, "w") as f:
        f.write(merged_data)

    print(f"Merged data saved to {MERGE_FILEPATH.as_posix()}")
