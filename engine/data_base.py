import csv
import sqlite3

# Connect to SQLite database (create db file if it doesn't exist)
con = sqlite3.connect('jarvis.db')
cursor = con.cursor()

# Ensure the table exists
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS contacts (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         mobile_no TEXT NOT NULL
#     )
# ''')

# Correct column indices for the CSV: [0] for name, [1] for mobile_no
# desired_columns_indices = [0, 1]

# Read data from the CSV and insert into the SQLite table for the desired columns
# with open('D:/New folder (12)/Javires/names_and_numbers.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         if len(row) >= 2:  # Ensure we have at least two values: name and mobile_no
#             selected_data = [row[i] for i in desired_columns_indices]
#             cursor.execute('''
#                 INSERT INTO contacts_3 (name, mobile_no) 
#                 VALUES (?, ?)
#             ''', tuple(selected_data))
#         else:
#             print(f"Skipping row with insufficient data: {row}")

# # Commit changes and close the connection
# con.commit()
# con.close()

# print("Data insertion completed successfully.")

query = 'Omy'
query = query.strip().lower()

cursor.execute("SELECT mobile_no FROM contacts_3 WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
results = cursor.fetchall()
print(results[0][0])