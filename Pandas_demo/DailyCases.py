import os
import json
from datetime import datetime
from matplotlib import pyplot as plt


def PlotDailyCases(Path, Country):
    Date = []
    Confirmed = []
    Daily = []
    for filename in os.listdir(Path):
        nm = filename.split('.')
        dt = nm[0].split('_')
        dtpr = datetime.strptime(dt[1], '%m-%d-%y').date()
        with open(f'{Path}/{filename}') as f:
            data = json.load(f)
            ConfCas = data['Active_Cases'][Country]
            Confirmed.append(ConfCas)
        if len(Confirmed) < 2:
            Daily.append(ConfCas)
            Date.append(dtpr)
        elif(ConfCas > Confirmed[-2]):
            DailyCas = ConfCas - Confirmed[-2]
            Daily.append(DailyCas)
            Date.append(dtpr)

    plt.style.use('fivethirtyeight')
    plt.bar(Date, Daily, edgecolor='red')

    plt.gcf().autofmt_xdate()
    plt.title(f'Daily New Active cases in {Country}')
    plt.xlabel('Date')
    plt.ylabel('Daily Cases')
    plt.tight_layout()
    plt.show()
    plt.gcf()
    # print(Daily)


PlotDailyCases('COVID-19', 'India')
