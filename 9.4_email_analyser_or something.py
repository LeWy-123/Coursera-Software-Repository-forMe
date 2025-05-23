# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
# loop to find the most prolific committer.

# initialization
filePath = './text/mbox-short.txt'

fname = input('Enter file name: ')
fhandle = open(filePath, 'r')
count = 0
senders = {}
lineN = 0
# reading file
for line in fhandle:
    lineN += 1
    line = line.rstrip()   # stripping off the extra new line character
    if not line.startswith('From'):     # skipping the lines that dont contain 'from:'
        continue
    # Snipping out the email address
    count += 1
    emailsender = line.split()
    emailsender = emailsender[1]
    print(f'Added: {emailsender}, count: {count}, lineN: {lineN}')
    senders[emailsender] = senders.get(emailsender, 0) + 1

# finding the most active senders email
prev = None
for sender, count in senders.items():
    if prev is None:
        prev = count
        continue
    if count > prev:
        prev = count

# findig who sent the email
for sender, c in senders.items():
    if c == prev:
        print(sender, c)

