import csv

# Open the CSV file
with open('LebronData/lebron_james_2004_gamelog.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Read the header row
    print(f"Header: {header}")

    # Iterate through the rows
    skip_six = 6
    skip_zero = 0

    for row in csv_reader:

        row_number = row[0]

        row_without_skipped_column = [value for index, value in enumerate(row) if index != skip_six and index != skip_zero]
        

        print(f"Game {row_number}")
        print(f"Date: {row_without_skipped_column[0]}")
        print(f"Age: {row_without_skipped_column[1]}")
        print(f"Team: {row_without_skipped_column[2]}")
        if row_without_skipped_column[3] == "@":
            print("Away")
        else:
            print("Home")
        print(f"Opponent: {row_without_skipped_column[4]}\n")