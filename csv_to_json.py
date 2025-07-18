import csv
import json
import sys

csv_file_path = sys.argv[1]
json_file_path = sys.argv[2]

# Read the CSV and add data to a list
data = []
with open(csv_file_path, encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

# Write the data to a JSON file
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    for record in data:
        json_file.write(json.dumps({"index": {}}) + '\n')
        json_file.write(json.dumps(record) + '\n')
