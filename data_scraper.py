from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

"""
df_hmc = pd.read_csv("/Users/OliverM/Code/New Home/Data/HMC_Schools.csv")
links = df_hmc['wikipedia link'].values.tolist()

def get_hmc_postcode(links):
    results = []

    for i in links:
        response = requests.get(i)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        try:
            postcode = soup.select_one("span[class*=postal]").text
            results.append((i, postcode))
            print(i, postcode)
        except AttributeError:
            pass

    df = pd.DataFrame(results, columns=['wikipedia_link', 'postcode'])
    df.to_csv('/Data/hmc_schools_postcode')
    return df

print(get_hmc_postcode(links))



df_waitrose = pd.read_csv("/Users/OliverM/Code/New Home/Data/waitrose.csv")
links = df_waitrose['store link'].values.tolist()

def get_waitrose_postcode(links):
    results = []

    for i in links:
        response = requests.get(i)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        try:
            address = soup.select_one("div[class*=branch-details]").text
            results.append((i, address))
            print(i, address)
        except AttributeError:
            pass

    df = pd.DataFrame(results, columns=['waitrose link', 'address'])
    df.to_csv('waitrose_postcode.csv')
    return df

get_waitrose_postcode(links)



df_crossrail = pd.read_csv("/Users/OliverM/Code/New Home/Data/crossrail.csv")
links = df_crossrail['railway_link'].values.tolist()

def get_crossrail_locations(links):
    results = []

    for i in links:
        response = requests.get(i)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        try:
            location = soup.select_one("span[class*=geo-dec]").text
            results.append((i, location))
            print(i, location)
        except AttributeError:
            pass

    df = pd.DataFrame(results, columns=['station_link', 'location'])
    df.to_csv('crossrail_locations2.csv')
    return df

get_crossrail_locations(links)



df_airports = pd.read_csv("/Users/OliverM/Code/New Home/Data/international_airports.csv")
links = df_airports['link'].values.tolist()

def get_airports(links):
    results = []

    for i in links:
        response = requests.get(i)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        try:
            location = soup.select_one("span[class*=geo-dec]").text
            results.append((i, location))
            print(i, location)
        except AttributeError:
            pass

    df = pd.DataFrame(results, columns=['airport_link', 'location'])
    df.to_csv('international_airports2.csv')
    return df

get_airports(links)


df_qol = pd.read_csv("/Users/OliverM/Code/New Home/Data/Halifax_quality_of_life.csv")
links = df_qol['link'].values.tolist()

def get_qol_locations(links):
    results = []

    for i in links:
        response = requests.get(i)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        try:
            location = soup.select_one("span[class*=geo-dec]").text
            results.append((i, location))
            print(i, location)
        except AttributeError:
            pass

    df = pd.DataFrame(results, columns=['link', 'location'])
    df.to_csv('halifax_qol.csv')
    return df

get_qol_locations(links)


df_times = pd.read_csv("/Users/OliverM/Code/PlacesToLive/data/Times_places_to_live.csv")
links = df_times['Link'].values.tolist()
links2 = df_times['Link2'].values.tolist()

def get_times_locations(links):
    results = []

    for i in links:
        response = requests.get(i)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        try:
            location = soup.select_one("span[class*=geo-dec]").text
            results.append((i, location))
            print(i, location)
        except AttributeError:
            pass

    df = pd.DataFrame(results, columns=['link', 'location'])
    df.to_csv('times_places2.csv')
    return df

get_times_locations(links2)

"""

df_stations = pd.read_csv("/Users/OliverM/Code/PlacesToLive/data/Base_data/station_data.csv")
tlc = df_stations['TLC'].values.tolist()
#tlc = ['SMD', 'BAN']

def get_train_times(tlc):
    links = []
    df_train_master = pd.DataFrame(columns=['station', 'to', 'time', 'changes'])

    for station in tlc:
        url = 'http://ojp.nationalrail.co.uk/service/timesandfares/'+station+'/London/today/0800/dep?excludeslowertrains'
        print(url)
        links.append(url)

    for i in links:
        df_station_times = pd.DataFrame(columns=['station', 'to', 'time', 'changes'])
        response = requests.get(i)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        try:
            dep = soup.select("table td[class*=from]")
            dest = soup.select("table td[class*=to]")
            time = soup.select("table td[class*=dur]")
            changes = soup.select("table td[class*=chg]")
            time_list = []
            change_list = []
            dest_list = []
            dep_list = []

            for a in dest:
                dest_list.append(a.text.strip())

            for b in dep:
                dep_list.append(b.text.strip())

            for c in time:
                time_list.append(c.text.strip())

            for d in changes:
                change_list.append(d.text.strip())

            df_station_times['changes'] = change_list
            df_station_times['time'] = time_list
            df_station_times['station'] = dep_list
            df_station_times['to'] = dest_list

            print(df_station_times)
            df_train_master = df_train_master.append(df_station_times, ignore_index=True)

        except AttributeError:
            pass

    df_train_master['time'] = df_train_master['time'].replace(to_replace=r'\n\t.', value="", regex=True)
    df_train_master[['station', 'to']] = df_train_master[['station', 'to']].replace(to_replace=r'Platform\n\t.*', value="", regex=True)

    df_train_master.to_csv('/Users/OliverM/Code/PlacesToLive/data/train_times.csv')
    return df_train_master

print(get_train_times(tlc))

# One off test

"""
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'http://ojp.nationalrail.co.uk/service/timesandfares/London/SMD/today/0800/dep?excludeslowertrains'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'lxml')

time = soup.select("table td[class*=dur]")
changes = soup.select("table a[class*=changestip-link]")
strip_list = []
clean_list = []
change_list = []

for i in time:
    strip_list.append(i.text.strip())

for n in strip_list:
    clean_list.append(n.replace('\n\t\t',''))

for i in changes:
    change_list.append(i.text.strip())
"""
