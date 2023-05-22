import sqlite3
  
file = "entries.db"
  
try:
  conn = sqlite3.connect(file)
  print("Database formed.")
except:
  print("Database not formed.")