import pyodbc


driver = 'ODBC Driver 17 for SQL Server'
server = 'tdudcza2cgfmjt.c4lhiwtmcwzw.us-east-1.rds.amazonaws.com'
database = 'TestingCDB'
user = 'TestingCUID'
password = 'TestingCPWD'
conn = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password}')
cursor = conn.cursor()
print(f'Connected to Database {database}')

# query = '''INSERT INTO sample (id, name, phone) VALUES (?, ?, ?);  '''
# values = (1, 'Angel', '7735161357')
# cursor.execute(query, values)

# conn.commit()
# print('Inserted data into table')
cursor.execute('SELECT * FROM Table1')

for row in cursor:
    print(row)


cursor.close()
conn.close()
