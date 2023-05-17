"""
E.g., input (as CSV):

COL1  COL2  COL3
A     B     C
A     B     D
A     B     E
A     B     F

Output:
COL1  COL2  COL3
A     B     C
            D
            E
            F

Or merge on COL1 and COL2:
MERGED_COL COL3
A          C
B          D
           E
           F
"""

import csv

COLUMNS_TO_TRACK_UNIQUE_VALUES = [
    "COL1",
    "COL2",
    "COL3",
]

FILE_TO_OPEN = "file.csv"
FILE_TO_SAVE = "save_path.csv"


def store_unique_values_from_columns(
    columns: list[str] = COLUMNS_TO_TRACK_UNIQUE_VALUES,
) -> None:
    # Get unique values from the columns
    results = {}
    with open(FILE_TO_OPEN, newline="") as file_to_open:
        reader = csv.DictReader(file_to_open)
        for row in reader:
            for key, value in row.items():
                if key in columns:
                    # E.g., merge all columns with the same kind of data
                    if "part of the column name" in key:
                        key = "COLUMN NAME"
                    # E.g., merge COL1 and COL2 into MERGED_COL
                    elif key in ["COL1", "COL2"]:
                        key = "MERGED_COL"

                    # Eliminate duplicates with sets, then eliminate some more with
                    # string manipulations
                    results.setdefault(key, set()).add(
                        value.upper().replace("-", " ")
                    )

    # cast the sets to lists
    for key, value in results.items():
        results[key] = list(value)

    # Extract keys and values from the dictionary
    keys = list(results.keys())
    values = list(results.values())

    # Determine the maximum length of the value lists
    max_length = max(len(lst) for lst in values)

    # Fill any shorter lists with empty strings
    values = [lst + [""] * (max_length - len(lst)) for lst in values]

    # Sort the values lists so that all non-empty strings appear first and sort
    # alphabetically
    transformed_lists = [
        sorted(lst, key=lambda x: (x == "", x)) for lst in values
    ]

    # Transpose the values list so that each row is a column
    # (i.e., all unique values for a given column)
    transposed_values = list(map(list, zip(*transformed_lists)))

    with open(FILE_TO_SAVE, "w", newline="") as csv_output:
        writer = csv.writer(csv_output)
        writer.writerow(keys)  # Write the header row
        writer.writerows(transposed_values)  # Write the data rows


if __name__ == "__main__":
    store_unique_values_from_columns()
