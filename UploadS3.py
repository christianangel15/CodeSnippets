import pyodbc
import boto3
import json
s3 = boto3.client('s3')

driver = 'ODBC Driver 17 for SQL Server'
server = 'tdudcza2cgfmjt.c4lhiwtmcwzw.us-east-1.rds.amazonaws.com'
database = 'TestingCDB'
user = 'TestingCUID'
password = 'TestingCPWD'
conn = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password}')
cursor = conn.cursor()
print(f'Connected to Database {database}')

cursor.execute('SELECT * FROM Table1')
d = []
for row in cursor:
    d.append(row)

jsonlist = []
for i in range(len(d)):
    jsonlist.append({'ID': d[i][0], 'Name': d[i][1], 'Last': d[i][2]})
# print(jsonlist)
jsondata = json.dumps(jsonlist, indent=2)
print(jsondata)
#s3.put_object(Body=jsondata, Bucket='testingcs3', Key='Db.json')
print('Data Uploaded')

cursor.close()
conn.close()
