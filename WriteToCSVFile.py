import requests

r = requests.get('https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/10-Subplots/data.csv')
data = r.text

with open('data.csv', 'w') as f:
    f.write(data)

