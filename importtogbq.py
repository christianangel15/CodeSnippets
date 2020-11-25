import os
import pandas as pd
from pandas.io import gbq
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))
# From CSV - local directory
df = pd.read_csv('COVID Data Pulling\data\ETH_1hr.csv')
# From JSON - local directory
# df = pd.read_json('COVID Data Pulling\data\sample.json')


df.to_gbq(destination_table='Test.SampleTable',
          project_id='testbq-296623', if_exists='fail', credentials=credentials)
print('Data Uploaded')
