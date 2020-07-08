import os
import json
from datetime import datetime
from matplotlib import pyplot as plt


def PlotCovidGraph(Path, param, Country):
    # Path - Folder that has all json files consisting actual data.
    # param - Any one from (Active_Cases, Confirmed_Cases, Total_Deaths, Total_Recovered)
    Date = []
    Parameter = []
    for filename in os.listdir(Path):
        nm = filename.split('.')
        dt = nm[0].split('_')
        dtpr = datetime.strptime(dt[1], '%m-%d-%y').date()
        Date.append(dtpr)
        with open(f'{Path}/{filename}') as f:
            data = json.load(f)
            Parameter.append(data[param][Country])

    plt.style.use('seaborn')
    plt.bar(Date, Parameter, edgecolor='red')

    plt.gcf().autofmt_xdate()
    plt.title(f'{param} in {Country}')
    plt.xlabel('Date')
    plt.ylabel('Cases')
    plt.tight_layout()
    plt.show()
    plt.gcf()

def PlotCovidGraphByDate(Path, param, date):
    d={}
    country=[]
    countries=[]
    case=[]
    for filename in os.listdir(Path):
        if date in filename:
            nm = filename.split('.')
            dt = nm[0].split('_')
            with open(f'{Path}/{filename}') as f:
                data = json.load(f)
                data = data[param]
                for key, val in data.items():
                    d[val]=key
                    country.append(key)
                    case.append(val)
    case=sorted(case, reverse=True)
    for ele in case:
        countries.append(d[ele])
    plt.style.use('seaborn')
    plt.bar(countries[:10], case[:10], edgecolor='red')
    plt.ticklabel_format(axis= 'y', style='plain')
    ax=plt.gca()
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.gcf().autofmt_xdate()
    p1, p2 = param.split('_')
    plt.title(f'{p1} {p2} on {dt[1]}')
    plt.xlabel('Countries')
    plt.ylabel('Cases')
    plt.tight_layout()
    plt.show()
    plt.gcf()
PlotCovidGraphByDate('COVID-19', 'Total_Recovered', '7-7-20')
# Path = 'COVID-19'
