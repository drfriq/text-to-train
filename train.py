import sqlite3
import json
import re

# Function to clean the text and remove special characters
def clean_text(text):
    return re.sub(r'[^\w\s]', '', text)

# Connect to the SQLite database
conn = sqlite3.connect('3d0d7e5fb2ce288813306e4d4636395e047a3d28')
cursor = conn.cursor()

# Query the message table
cursor.execute("SELECT is_from_me, text FROM message order by handle_id, date")
rows = cursor.fetchall()

# Process the rows into alpaca-chatbot-format.json format
data_entries = []
buffered_messages = []
buffered_responses = []

for row in rows:
    message_text = row[1]
    if message_text is None:  # skip None messages
        continue

    if row[0] == 0:  # message from friends
        if buffered_responses:  # check if there are buffered responses from the previous set
            combined_responses = clean_text(" ".join(buffered_responses))
            combined_messages = clean_text(" ".join(buffered_messages))

            # Only add if both are present and not just whitespace
            if combined_messages.strip() and combined_responses.strip():
                # Create a dictionary entry with the required format
                data_entries.append({
                    "instruction": combined_messages,
                    "output": combined_responses
                })

            buffered_responses = []  # clear the buffered responses
            buffered_messages = []  # clear the buffered messages

        buffered_messages.append(message_text)
    else:  # your message
        buffered_responses.append(message_text)

# I doubt the last message is important enough to repeat all that code

# Convert the list to JSON and write to a file
with open('training_data.json', 'w') as file:
    json.dump(data_entries, file, indent=4)

# Close the database connection
conn.close()
