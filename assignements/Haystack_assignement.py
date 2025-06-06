# Handling The Data The basic outline of this problem is to read the file, look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up
# the integers.

import re

file = '../text/regex_sum_2223026.txt'

# Read and process the file in one go
with open(file) as f:
    numbers = [int(match) for line in f for match in re.findall(r'\d+', line.strip())]

# Compute the sum
totalsum = sum(numbers)

# Print results
print(f'There are a total of {len(numbers)} items. Total lines processed: {sum(1 for _ in open(file))}')
print(f'\033[91mThe items found: {numbers}\033[0m')
print(f'The resulting sum is {totalsum}')

