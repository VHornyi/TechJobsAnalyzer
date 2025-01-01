import sqlite3
import csv
import os


db_folder = 'Data'
if not os.path.exists(db_folder):
    os.makedirs(db_folder)


db_path = os.path.join(db_folder, 'vacancies.db')


conn = sqlite3.connect(db_path)  
cursor = conn.cursor()

# min_salary and max_salary are in str format because they can have "Not Specified" values.
cursor.execute('''
CREATE TABLE IF NOT EXISTS vacancies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT,
    location TEXT,
    min_salary TEXT,
    max_salary TEXT,
    technologies TEXT,
    company TEXT,
    seniority_level TEXT,
    job_link TEXT
)
''')


with open('Data\\nofluffjobs.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  
    for row in reader:
        
        min_salary = row['Minimum Salary'].strip()  
        max_salary = row['Maximum Salary'].strip()  

        
        cursor.execute('''
        INSERT INTO vacancies (job_title, location, min_salary, max_salary, technologies, company, seniority_level, job_link)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (row['Job Title'], row['Location'], min_salary, max_salary, row['Technologies'], row['Company'], row['Seniority Level'], row['Job Link']))


conn.commit()
conn.close()
