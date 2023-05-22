import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('entries.db')
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")
 
# Creating table
table = """ CREATE TABLE data (

            'age' INT
            ,'sex' INT
            ,'cp' INT
            ,'trestbps' INT
            ,'chol' INT
            ,'fbs' INT
            ,'restecg' INT
            ,'thalach' INT
            ,'exang' INT
            ,'oldpeak' INT
            ,'slope' INT
            ,'target' INT       
        ); """
 
cursor_obj.execute(table)
 
print("Table is Ready")

connection_obj.close()