import sqlite3 

conn=sqlite3.connect("biblioteka.db")

conn.execute("""CREATE TABLE IF NOT EXISTS dati (nosaukums TEXT , autors TEXT ,gads INT)""")
conn.commit()