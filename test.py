import csv

csv_files = ["distance.csv", "addresses.csv", "packages.csv"]

for csv_file in csv_files:
    print(f"\nContents of {csv_file}:")

    try:
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                print(row)
                if i >= 5:  # Print only the first 5 rows
                    break
    except FileNotFoundError:
        print(f"File {csv_file} not found.")