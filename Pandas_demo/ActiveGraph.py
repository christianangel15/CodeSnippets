import os
import json
from datetime import datetime, date
from matplotlib import pyplot as plt
plt.style.use('seaborn')
Path = 'COVID-19'
Date = []
Active = []
for filename in os.listdir(Path):
    nm, ext = filename.split('.')
    jhu, dt = nm.split('_')
    dtpr = datetime.strptime(dt, '%m-%d-%y').date()
    Date.append(dtpr)
    with open(f'{Path}/{filename}') as f:
        data = json.load(f)
        Active.append(data['Active_Cases']['Italy'])
plt.bar(Date, Active, edgecolor='red')

plt.gcf().autofmt_xdate()
plt.title('Active Cases in Italy')
plt.xlabel('Date')
plt.ylabel('Cases')

plt.tight_layout()
plt.show()
plt.gcf()
