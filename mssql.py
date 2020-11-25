import pyodbc

driver = 'ODBC Driver 17 for SQL Server'
server = 'DESKTOP-EIG2M9I\SQLEXPRESS'
database = 'test'
user = 'Angel'
password = '123'
conn = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password}')
cursor = conn.cursor()
print(f'Connected to Database {database}')

# query = '''INSERT INTO sample (id, name, phone) VALUES (?, ?, ?);  '''
# values = (1, 'Angel', '7735161357')
# cursor.execute(query, values)

# conn.commit()
# print('Inserted data into table')
cursor.execute('SELECT * FROM sample')

for row in cursor:
    print(row)
cursor.close()
conn.close()
