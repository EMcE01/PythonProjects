import csv
import time
import csv

def update_clock():
    current_time = time.time_ns()
    nanoseconds = current_time % 1_000_000_000

with open('pokemon_extract.py', 'r') as file:
    # Create a CSV reader with a dictionary format
    csv_reader = csv.DictReader(file)

    # Read and process the CSV data
    for row in csv_reader:
        # Each row is a dictionary
        name = row['Name']
        type = row['Type']
        generation = row['generation']
        print(f"Name: {name}, Age: {type}, generation: {generation}")


if __name__ == '__main__':
    print("Running")