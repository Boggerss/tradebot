# Web-scraped S&P 500 data for 500+ US stocks.

import requests
import pandas as pd
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}

url = 'https://www.slickcharts.com/sp500' # Data from SlickCharts
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

table1 = soup.find('table', attrs={'class':'table table-hover table-borderless table-sm'})

for row in table1.find_all('tr'):
    all_td_tags = row.find_all('td')
    if len(all_td_tags) > 0:
        company = all_td_tags[1].text
        symbol = all_td_tags[2].text
        weight = all_td_tags[3].text
        price = all_td_tags[4].text
        chg = all_td_tags[5].text
        perChg = all_td_tags[6].text

df = pd.read_html(str(table1))[0]   # Makes data into an html readable and can output and look through data
df.drop(['#'], axis = 1, inplace = True)    # Removes an extra column of numbers

def symbol_input(userinput):
    if userinput.isupper():
        symbol = (df[df['Symbol'] == userinput])
        return symbol

def viewallSect1():
    Sect1Stocks = df.head(20)
    return Sect1Stocks

def viewallSect2():
    Sect2Stocks = df.loc[20:39]
    return Sect2Stocks

def viewallSect3():
    Sect3Stocks = df.loc[40:59]
    return Sect3Stocks

def viewallSect4():
    Sect4Stocks = df.loc[60:79]
    return Sect4Stocks

def viewallSect5():
    Sect5Stocks = df.loc[80:99]
    return Sect5Stocks

def viewallSect6():
    Sect6Stocks = df.loc[100:119]
    return Sect6Stocks

def viewallSect7():
    Sect7Stocks = df.loc[120:139]
    return Sect7Stocks

def viewallSect8():
    Sect8Stocks = df.loc[140:159]
    return Sect8Stocks

def viewallSect9():
    Sect9Stocks = df.loc[160:170]
    return Sect9Stocks

def viewallSect10():
    Sect10Stocks = df.loc[171:186]
    return Sect10Stocks

def viewallSect11():
    Sect8Stocks = df.loc[187:206]
    return Sect8Stocks

def viewallSect12():
    Sect12Stocks = df.loc[207:226]
    return Sect12Stocks

def viewallSect13():
    Sect13Stocks = df.loc[227:246]
    return Sect13Stocks

def viewallSect14():
    Sect14Stocks = df.loc[247:266]
    return Sect14Stocks

def viewallSect15():
    Sect15Stocks = df.loc[267:286]
    return Sect15Stocks

def viewallSect16():
    Sect16Stocks = df.loc[287:306]
    return Sect16Stocks

def viewallSect17():
    Sect17Stocks = df.loc[307:326]
    return Sect17Stocks

def viewallSect18():
    Sect18Stocks = df.loc[327:346]
    return Sect18Stocks

def viewallSect19():
    Sect19Stocks = df.loc[347:366]
    return Sect19Stocks

def viewallSect20():
    Sect20Stocks = df.loc[367:386]
    return Sect20Stocks

def viewallSect21():
    Sect21Stocks = df.loc[387:406]
    return Sect21Stocks

def viewallSect22():
    Sect22Stocks = df.loc[407:426]
    return Sect22Stocks

def viewallSect23():
    Sect23Stocks = df.loc[427:446]
    return Sect23Stocks

def viewallSect24():
    Sect24Stocks = df.loc[447:466]
    return Sect24Stocks

def viewallSect25():
    Sect25Stocks = df.loc[467:486]
    return Sect25Stocks

def viewallSect26():
    Sect26Stocks = df.loc[487:504]
    return Sect26Stocks