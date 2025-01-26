import csv
import json
import os

# Path to the output JSON file
output_file = 'LebronData/lebron_james_processed.json'

# Remove existing JSON file if it exists
if os.path.exists(output_file):
    os.remove(output_file)
    print(f"Removed existing file: {output_file}")

# Master list to store all processed game data
all_games = []

# Loop through each year from 2004 to 2024
for i in range(2004, 2025):
    # Input file path for the current year
    input_file = f'LebronData/lebron_james_{i}_gamelog.csv'
    print(f"Processing {i}'s data...")

    # Check if the input file exists before processing
    if os.path.exists(input_file):
        with open(input_file, mode='r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Read the header row

            # Define the indices of columns to skip
            skip_indices = {0}

            # Process each row in the CSV
            for row in csv_reader:
                # Remove the specified columns
                row_without_skipped_column = [
                    value for index, value in enumerate(row) if index not in skip_indices
                ]

                # Create a dictionary for each game's data
                game_data = {
                    "Date": row_without_skipped_column[0],
                    "Minutes": row_without_skipped_column[7],
                    "FG": row_without_skipped_column[8],
                    "FGA": row_without_skipped_column[9],
                    "FG Percentage": row_without_skipped_column[10],
                    "3P": row_without_skipped_column[11],
                    "3PA": row_without_skipped_column[12],
                    "3P Percentage": row_without_skipped_column[13],
                    "FT Percentage": row_without_skipped_column[16],
                    "Rebounds": row_without_skipped_column[19],
                    "Assists": row_without_skipped_column[20],
                    "Steals": row_without_skipped_column[21],
                    "Blocks": row_without_skipped_column[22],
                    "Points": row_without_skipped_column[25], 
                    "Age": row_without_skipped_column[1],
                    "Team": row_without_skipped_column[2],
                    "Location": "Away" if row_without_skipped_column[3] == "@" else "Home",
                    "Opponent": row_without_skipped_column[4],
                }

                # Append the processed game data to the master list
                all_games.append(game_data)
        print(f"Data for {i} processed successfully.")
    else:
        print(f"File not found for {i}: {input_file}")

# Write all processed data to the output file as a single array
with open(output_file, mode='w') as json_file:
    json.dump(all_games, json_file, indent=4)

print(f"All data processed and saved to {output_file}")
