import sqlite3

conn = sqlite3.connect('Data//vacancies.db')
cursor = conn.cursor()


cursor.execute('SELECT * FROM vacancies ORDER BY id DESC LIMIT 5') 
rows = cursor.fetchall()

if rows:
    print("Data from DB:")
    for row in rows:
        print(row)  
else:
    print("No Data found")

conn.close()
