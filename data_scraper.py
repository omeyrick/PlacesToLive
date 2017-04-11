from bs4 import BeautifulSoup
import requests
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

#df_stations = pd.read_csv("/Users/OliverM/Code/PlacesToLive/data/Base_data/station_data_test.csv")
#tlc = df_stations['TLC'].values.tolist()
tlc = ['SMD', 'BAN']

def get_train_times(tlc):
    links = []
    df_train_master = pd.DataFrame(columns=['station', 'time', 'changes'])

    for station in tlc:
        url = 'http://ojp.nationalrail.co.uk/service/timesandfares/London/'+station+'/today/1400/dep?excludeslowertrains'
        links.append[url]

    for i in links:
        df_station_times = pd.DataFrame(columns=['station', 'time', 'changes'])
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        try:
            time = soup.select("table td[class*=dur]")
            changes = soup.select("table a[class*=changestip-link]")
            strip_list = []
            clean_list = []
            change_list = []

            for i in time:
                strip_list.append(i.text.strip())

            for n in strip_list:
                clean_list.append(n.replace('h\n\t\t','.'))

            for i in changes:
                change_list.append(i.text.strip())

            print(clean_list)
            print(change_list)

            df_station_times['station'] = station
            df_station_times['changes'] = change_list
            df_station_times['time'] = clean_list

            print(df_station_times)

            result = pd.concat([df_train_master, df_station_times])

        except AttributeError:
            pass

        return result

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
