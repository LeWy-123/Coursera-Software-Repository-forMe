import sqlite3
import re

# reading in the file
with open('../text/mbox.txt', 'r') as f:
    text = f.read().split('\n')

# counting the email received and sorting out by organizations

email_histogram = dict()    # will store the emails extracted :D
table_name = 'Counts'

for line in text:
    y = re.findall(r'^From\s.*?@(.*?)\s', line)
    if not y: continue
    z = str(y[-1])
    email_histogram[z] = email_histogram.get(z, 0) + 1

# creating a tuple for the sqlite3 executemany() command

domain_histogram = tuple(email_histogram.items())

# initiating the SQLITE3 cursor and connector
conn = sqlite3.connect('../text/mbox.db')
c = conn.cursor()

# executing the first command to create the database :D so exciting part

# Delete the table if already exists coz is just assignment and need clean data
c.execute(f'DROP TABLE IF EXISTS {table_name};')
c.execute(f'CREATE TABLE IF NOT EXISTS {table_name} (org VARCHAR(64), count INTEGER);')

# inserting onto the database :D my fresh stuff
c.executemany(f'INSERT INTO {table_name} VALUES (?, ?)', domain_histogram)  # this is repeatedly inserting all
# elements onto the database
conn.commit() # uploading it onto the database

Testing = c.execute(f'SELECT * FROM {table_name};').fetchall()
print('THIS IS THE REAL RESULT:', Testing)

c.close()   # closing the database or disconnect from it