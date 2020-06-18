import requests
import json

# url = "https://api.covid19api.com/summary"

# response = requests.get(url)

# data = response.json()
# print(data['Global'])
# with open('Covid19.json', 'w') as f:
#     json.dump(data, f, indent=2)
with open('Pandas_demo/Covid19JHU.json', 'r') as f:
    data = json.load(f)

print(data['Active_Cases']['US'])
# for country in data['Countries']:
#     Active = country['TotalConfirmed'] - \
#         country['TotalDeaths'] - country['TotalRecovered']
#     if (country['Country'] == 'United States of America'):
#         print(country['Country'])
#         print(f'Active Cases - {Active}')
#         print()
