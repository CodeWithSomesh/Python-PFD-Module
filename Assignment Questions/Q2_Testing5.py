from tabulate import tabulate

# Sample data from the image
data = [
    [1, 3696, 2115],
    [2, 3678, 2177],
    [3, 3694, 2136],
    [4, 3683, 2209],
    [5, 3696, 2163],
    [6, 3687, 2185],
    [7, 3686, 2171],
    [8, 3692, 2148],
    [9, 3687, 2171],
    [10, 3681, 2101],
]

# Calculate totals and averages
total_hash1 = sum(row[1] for row in data)
total_hash2 = sum(row[2] for row in data)
average_hash1 = total_hash1 / len(data)
average_hash2 = total_hash2 / len(data)

# Append totals and averages to the data
data.append(['Total', total_hash1, total_hash2])
data.append(['Average', f'{average_hash1:.2f}', f'{average_hash2:.2f}'])

# Define headersIa
headers = ['Experiment', 'Hash function 1', 'Hash function 2']

# Print the table
print(tabulate(data, headers=headers, tablefmt='grid', stralign='center', numalign="center"))
