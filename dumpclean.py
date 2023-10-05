import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('3d0d7e5fb2ce288813306e4d4636395e047a3d28')
cursor = conn.cursor()

# Get the headers (column names) from the message table
headers = ['handle', 'is_from_me', 'text']

# Query the top 1000 rows from the message table
cursor.execute("""
    SELECT h.id, m.is_from_me, m.text AS contact_number_or_apple_id 
    FROM message AS m 
    JOIN handle AS h ON m.handle_id = h.ROWID 
    ORDER BY h.id, m.date 
    LIMIT 1000
""")
rows = cursor.fetchall()

# Write to CSV
with open('output.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)  # Write the headers first
    csv_writer.writerows(rows)   # Write the rows

print(f"CSV file created with {len(rows)} rows")

# Close the connection
conn.close()
