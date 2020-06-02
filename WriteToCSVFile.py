import requests

r = requests.get('https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Pandas/10-Datetime-Timeseries/ETH_1h.csv')
data = r.text

with open('data.csv', 'w') as f:
    f.write(data)

