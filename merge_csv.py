#!/usr/bin/env python3
import csv
import os
import sys

out_fname = 'out.csv'
if os.path.exists(out_fname):
    sys.exit(f'"{out_fname}" already exists. Aborting...')

inputs = [file_name for file_name in os.listdir(os.getcwd()) if file_name.endswith('.csv') if not os.stat(file_name).st_size == 0]
empty_inputs = [file_name for file_name in os.listdir(os.getcwd()) if file_name.endswith('.csv') if os.stat(file_name).st_size == 0]

# First determine the field names from the top line of each input file
fieldnames = []
for filename in inputs:
    with open(filename, 'r', newline="") as f_in:
        reader = csv.reader(f_in)
        headers = next(reader)
        for h in headers:
            if h not in fieldnames:
                fieldnames.append(h)

# Then copy the data
with open(out_fname, 'w', newline="") as f_out:
    writer = csv.DictWriter(f_out, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()  # Add headers
    for filename in inputs:
        print(f'processing {filename}')
        with open(filename, 'r', newline="") as f_in:
            reader = csv.DictReader((line.replace('\0', ' ') for line in f_in))  # Uses the field names in this file. Also remove NULL bytes
            last_line = ''
            for line in reader:
                writer.writerow(line)

if empty_inputs:
    print(f'Skipped empty files: {empty_inputs}')
print(f'Merged CSV files into {out_fname}')
