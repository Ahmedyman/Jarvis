import csv
import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'Code','D:\\Microsoft VS Code\\Code.exe')"
# cursor.execute(query)
# con.commit()
# query = "DELETE FROM sys_command WHERE name = 'Command Prompt'"
# cursor.execute(query)
# con.commit()


# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name VARCHAR(255), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'youtube','https://www.youtube.com/')"
# cursor.execute(query)
# con.commit()
# query = "DELETE FROM web_command WHERE name = 'Youtube'"
# cursor.execute(query)
# con.commit()

# Create a table with the desired columns
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts_3 (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 30]





# # Read data from CSV and insert into SQLite table for the desired columns

# Re-create the CSV file with the required structure (name and mobile_no)



# file_path = "D:\\New folder (12)\\Javires\\contacts (2).csv"

# Data to be written into the CSV file
# data = [
#     ['name', 'mobile_no'],
#     ['me', '01014252854']
# ]

# # Writing to CSV
# with open("D:\\New folder (12)\\Javires\\contacts (2).csv", mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# file_path


# Specify the column indices you want to import (0-based index)
# desired_columns_indices = [0, -1]  # 0th column for names, last column for mobile numbers

# # Read data from CSV and insert into SQLite table
# with open('D:/New folder (12)/Javires/names_and_numbers.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         # Ensure the row has at least the number of columns we expect
#         if len(row) > max(desired_columns_indices):
#             # Clean and filter the selected data
#             selected_data = [row[i].strip() for i in desired_columns_indices if row[i].strip()]

#             # Ensure we have exactly 2 items (name, mobile_no) before inserting into the database
#             if len(selected_data) == 2:
#                 cursor.execute('''INSERT INTO contact_2(id, name, mobile_no) VALUES (null, ?, ?);''', tuple(selected_data))
#             else:
#                 print(f"Error: selected_data does not contain the required number of values. Selected data: {selected_data}")
#         else:
#             print(f"Error: Row does not contain enough columns: {row}")

# # Commit changes and close connection
# con.commit()
# con.close()

# print("Data insertion completed.")