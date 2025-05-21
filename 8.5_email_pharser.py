fname = input("Enter file name: ")
fname = './text/mbox-short.txt'

count = 0
file = open(fname)
for line in file:
    if line.startswith('From '):
        email = line.split()[1]
        count += 1
        print(f'{count}. Emails from: {email}')

print("There were", count, "lines in the file with From as the first word")
