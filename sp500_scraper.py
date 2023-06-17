import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
# scrapes this wiki for dataframe objects

sp = tables[0].iloc[:, 0]
# takes first column of first wiki data frame object (i.e: symbols of sp500)

sp_list = sp.values.tolist()
sp_data = []

output_file_path = "/Users/yourname/downloads/sp_data.json"
#replace yourname with your actual name or replace with desired filepath

def getData(ticker):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0'}
    #headers contain more information about the client requesting the resource

    url = f'https://finance.yahoo.com/quote/{ticker}'

    r = requests.get(url, headers=headers)
    #creates response object called r

    soup = BeautifulSoup(r.text, 'html.parser')

    price = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text
    change = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text
    percent_change = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text
    percent_change =  percent_change[:-1]
    percent_change =  percent_change[1:]


    stock = {
        'stock': ticker, 
        'price': price,
        'change': change,
        'percent change': percent_change,

    }
    return(stock)

for i in sp_list:
    sp_data.append(getData(i))
    print('getting: ', i) 

with open(output_file_path, 'w') as f:
    json.dump(sp_data, f)

print('finished')