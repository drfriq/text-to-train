import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('3d0d7e5fb2ce288813306e4d4636395e047a3d28')
cursor = conn.cursor()

# Get the headers (column names) from the message table
cursor.execute("PRAGMA table_info(message)")
headers = [column[1] for column in cursor.fetchall()]

# Query the top 1000 rows from the message table
cursor.execute("SELECT * FROM message")
rows = cursor.fetchall()

# Write to CSV
with open('texts.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)  # Write the headers first
    csv_writer.writerows(rows)   # Write the rows

print(f"texts created with {len(rows)} rows")

# Get the headers (column names) from the message table
cursor.execute("PRAGMA table_info(handle)")
headers = [column[1] for column in cursor.fetchall()]

# Query the top 1000 rows from the message table
cursor.execute("SELECT * FROM handle")
rows = cursor.fetchall()

# Write to CSV
with open('text_handles.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)  # Write the headers first
    csv_writer.writerows(rows)   # Write the rows

print(f"handles file created with {len(rows)} rows")


# Close the connection
conn.close()
