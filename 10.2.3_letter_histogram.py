# Exercise 3: Write a program that reads a file and prints the letters in decreasing
# order of frequency.
# Your program should convert all the input to lower case and only count the letters
# a-z. Your program should not count spaces, digits, punctuation, or anything other
# than the letters a-z. Find text samples from several different languages and see
# how letter frequency varies between languages

import string

print('Build letter histogram. type in a file location, please.')
file = input('File path: ')
if file == '':
    file = './text/mbox-short.txt'

try:
    fhandle = open(file, 'r')
except FileNotFoundError:
    print('File not found. sorry!')

letters = {}    # to store letters in this variable
linestext = 0   # DISPLAY lines are we worked with
linenumb = 0

for line in fhandle:
    line = line.rstrip()
    line = line.strip('\n')
    line = line.lower()
    # Getting the letters one by one
    for letter in line:
        if letter in string.punctuation + ' ' + string.digits + '\t':    # if doesn't contain letters just
            # punctuations it skips the string or letter, also skips tabs, and digits.
            continue
        letters[letter] = letters.get(letter, 0) + 1    # itt adds to the dictionary if it's already in ads +1 to it
        #print(f'\t--> "{letter}" Added: {letters[letter]} times.')
    if line == []:
        continue

    linenumb += 1
    #print(f'{linenumb}: {line}')
    #if linenumb >= 50: break

print('\n---------------------------')
print(f'Histogram of the file: {file}.')
print(f'Lines processed: {linenumb}.')
print(f'Histogram of letters occurrences:')
letters = sorted(letters.items())
for char, count in letters:
    print(f'\t{char} : {count}')
print('---------------------------')
print(f'Top 5 letters occurrences:')
res = sorted(letters, key=lambda x: x[1], reverse=True)
for char, count in res[:5]:
    print(f'\t{char} : {count}')