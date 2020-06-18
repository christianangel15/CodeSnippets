import csv
import numpy as np
import pandas as pd
from  collections import Counter
from matplotlib import pyplot as plt
# Comic Plot Style
# plt.xkcd()
plt.style.use('fivethirtyeight')

# Without using Pandas
# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang = data['LanguagesWorkedWith']

lang_counter = Counter()

for row in lang:
    lang_counter.update(row.split(';'))

languages = []
popularity = []

for items in lang_counter.most_common(15):
    languages.append(items[0])
    popularity.append(items[1])

languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)

plt.title('Most Popular Languages')
# plt.ylabel('Programming Languages')
plt.xlabel('Number of People using it')
plt.tight_layout()
plt.show()
print(languages)
print(popularity)
