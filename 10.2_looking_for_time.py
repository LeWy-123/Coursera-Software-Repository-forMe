# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each
# of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string
# a second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 Once you have accumulated the
# counts for each hour, print out the counts, sorted by hour as shown below.

# setting up the variables
filepath = './text/mbox-short.txt'
occurrence = {}

fhandle = open(filepath, 'r')

# reading in the file line by line
for line in fhandle:
    line = line.rstrip()
    # finding where emails received
    if not line.startswith('From '):
        continue
    # splitting the words
    line = line.split()
    sender = line[1]
    time = line[5]
    year = line[6]
    hour = time.split(':')[0]
    # adding to a dictionary the occurrence
    occurrence[hour] = occurrence.get(hour, 0) + 1
    # print(f'The hour: {time}, hour: {hour}') # debug code

#print(f'There are {len(occurrence)} occurrences of the following:')
# sorting by hour
templist = sorted(occurrence.items())
# Printing the result sorted by hour ascending
for hour, occurrence in templist:
    print(f'{hour} {occurrence}')