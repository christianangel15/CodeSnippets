
import pandas as pd
def CovidDataByDate(date):
    df_confirmed = pd.read_csv(
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', index_col='Country/Region')
    df_deaths = pd.read_csv(
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv', index_col='Country/Region')
    df_recovered = pd.read_csv(
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv', index_col='Country/Region')


    df_confirmed.rename(columns={'Province/State': 'Province'}, inplace=True)
    df_deaths.rename(columns={'Province/State': 'Province'}, inplace=True)
    df_recovered.rename(columns={'Province/State': 'Province'}, inplace=True)


    Confirmed = df_confirmed[['Province', date]]
    Deaths = df_deaths[['Province', date]]
    Recovered = df_recovered[['Province', date]]


    filt = pd.isnull(Confirmed.Province)
    filt1 = pd.isnull(Deaths.Province)
    filt2 = pd.isnull(Recovered.Province)


    Confirmed = Confirmed.loc[filt]
    Deaths = Deaths.loc[filt1]
    Recovered = Recovered.loc[filt2]


    Confirmed.rename(
        columns={Confirmed.columns[-1]: 'Confirmed_Cases'}, inplace=True)
    Deaths.rename(columns={Deaths.columns[-1]: 'Total_Deaths'}, inplace=True)
    Recovered.rename(
        columns={Recovered.columns[-1]: 'Total_Recovered'}, inplace=True)


    new = pd.concat([Confirmed, Deaths, Recovered], axis='columns')


    new.drop(['Province'], axis=1, inplace=True)


    new.nlargest(10, 'Confirmed_Cases')


    new.loc['US']


    grpC = df_confirmed.groupby(['Country/Region'])
    chinaC = grpC.get_group('China')[date].sum()
    canadaC = grpC.get_group('Canada')[date].sum()
    australiaC = grpC.get_group('Australia')[date].sum()


    grpD = df_deaths.groupby(['Country/Region'])
    chinaD = grpD.get_group('China')[date].sum()
    canadaD = grpD.get_group('Canada')[date].sum()
    australiaD = grpD.get_group('Australia')[date].sum()


    grpR = df_recovered.groupby(['Country/Region'])
    australiaR = grpR.get_group('Australia')[date].sum()
    canadaR = Recovered.loc['Canada', 'Total_Recovered']
    chinaR = grpR.get_group('China')[date].sum()


    Arow = pd.Series(data={'Confirmed_Cases': australiaC, 'Total_Deaths': australiaD,
                           'Total_Recovered': australiaR}, name='Australia')
    new = new.append(Arow, ignore_index=False)


    Chrow = pd.Series(data={'Confirmed_Cases': chinaC,
                            'Total_Deaths': chinaD, 'Total_Recovered': chinaR}, name='China')
    new = new.append(Chrow, ignore_index=False)


    new.drop(['Canada'], axis=0, inplace=True)


    Carow = pd.Series(data={'Confirmed_Cases': canadaC,
                            'Total_Deaths': canadaD, 'Total_Recovered': canadaR}, name='Canada')
    new = new.append(Carow, ignore_index=False)


    new.tail()


    new['Active_Cases'] = new['Confirmed_Cases'] - \
        new['Total_Deaths'] - new['Total_Recovered']


    new = new.astype(int)
    new.nlargest(20, 'Active_Cases')


    temp = date.replace('/', '-')
    new.to_json(f'COVID-19\\JHU_{temp}.json', indent=2)

CovidDataByDate('7/4/20')
