import sqlite3

# Initiating the database and opening the file
database = 'C:\\Users\\Levente\\OneDrive\\Desktop\\database_assignment_1.db'

connector = sqlite3.connect(database)
cursor = connector.cursor()

# First read before insertion
result_before = cursor.execute("SELECT * FROM Ages;")
tables_before = result_before.fetchall()

# Insert new data
cursor.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Garry', 100))
connector.commit()  # Commit is important when writing!

# Second read after insertion
result_after = cursor.execute("SELECT * FROM Ages;")
tables_after = result_after.fetchall()

# Print both results
print('-' * 10, 'Table 1', '-' * 10)
for row in tables_before:
    print(row[0], row[1])

print('-' * 10, 'Table 2', '-' * 10)
for row in tables_after:
    print(row[0], row[1])

connector.close()
