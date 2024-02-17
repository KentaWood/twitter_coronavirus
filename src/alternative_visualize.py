#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')

import argparse
import json
import glob
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths', nargs='+', required=True)
parser.add_argument('--keys', nargs='+', required=True)
args = parser.parse_args()

def sum_counts(input_paths, keys):
    all_sums = defaultdict(Counter)
    for input_path in input_paths:
        expanded_paths = glob.glob(input_path)

        for expanded_path in expanded_paths:
            with open(expanded_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Extract date from the file name (considering only month and date)
            date = expanded_path.split('/')[-1].split('.')[0][-5:]
            for key in keys:
                if key in data:
                    # Sum up counts for each hashtag key
                    hashtag_count = sum(data[key].values())
                    all_sums[key][date] += hashtag_count

    return all_sums

# Call the function to sum up counts and print totals
all_sums = sum_counts(args.input_paths, args.keys)

# Plotting
print("Data points being plotted:")
for key, counts in all_sums.items():
    # Sort the dates
    sorted_dates = sorted(counts.keys())
    # Get the counts corresponding to sorted dates
    sorted_counts = [counts[date] for date in sorted_dates]
    plt.plot(sorted_dates, sorted_counts, label=key)
    for date, count in zip(sorted_dates, sorted_counts):
        print(f"Date: {date}, Count: {count}, Hashtag: {key}")

plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Hashtag Counts Over Time')
plt.legend()
plt.savefig('hashtag_counts.png')  # Save the plot as an image
plt.show()

