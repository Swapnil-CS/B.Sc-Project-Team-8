import sqlite3
  
# Connecting to sqlite
conn = sqlite3.connect('entries.db')
  
# Creating a cursor object using the 
# cursor() method
cursor = conn.cursor()

print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM data''')
for row in data:
    print(row)
  
# Commit your changes in the database    
conn.commit()
  
# Closing the connection
conn.close()