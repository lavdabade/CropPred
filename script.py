# # import pandas as pd
# # import numpy as np

# # data = pd.read_csv('data/rainfall-india.csv')

# # data = data.drop(['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC','Jan-Feb','Mar-May','Jun-Sep','Oct-Dec'],axis=1)
# # for i in range(0,641):
# #     data['ANNUAL'][i] = int(data['ANNUAL'][i]) / 12


# # data.to_csv('data/rainfall-cleaned.csv')
# # from geopy.geocoders import Nominatim

# # geolocator = Nominatim(user_agent="geoapiExercises")
# # lat = geolocator.geocode('Ulhasnagar, India').raw['lat']
# # lon = geolocator.geocode('Ulhasnagar, India').raw['lon']
# # location = geolocator.reverse(lat+","+lon)
# # print( 'location',location.raw['address'])s

# import pandas as pd

# data = pd.read_csv('data/rainfall-cleaned.csv')

# state = {'ANDAMAN And NICOBAR ISLANDS': [], 'ARUNACHAL PRADESH': [], 'ASSAM': [], 'MEGHALAYA': [], 'MANIPUR': [], 'MIZORAM': [], 'NAGALAND': [], 'TRIPURA': [], 'WEST BENGAL': [], 'SIKKIM': [], 'ORISSA': [], 'JHARKHAND': [], 'BIHAR': [], 'UTTAR PRADESH': [], 'UTTARANCHAL': [], 'HARYANA': [], 'CHANDIGARH': [], 'DELHI': [], 'PUNJAB': [], 'HIMACHAL': [], 'JAMMU AND KASHMIR': [], 'RAJASTHAN': [], 'MADHYA PRADESH': [], 'GUJARAT': [], 'DADAR NAGAR HAVELI': [], 'DAMAN AND DUI': [], 'MAHARASHTRA': [], 'GOA': [], 'CHATISGARH': [], 'ANDHRA PRADESH': [], 'TAMIL NADU': [], 'PONDICHERRY': [], 'KARNATAKA': [], 'KERALA': [], 'LAKSHADWEEP': []}

# for i in range(0,641):
#      state[data['state'][i]].append(f"{data['district'][i]}")

# for x,y in zip(state.keys(),state.values()):
#     # print(x,y)
#     # print(',\n')
#     print(f'<option>{x}</option>')
#     print('\n')
# # print(state) 

import pandas as pd
from urllib import request
import requests 
from urllib.request import urlopen
import json 
import urllib 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from geopy.geocoders import Nominatim


KEY = 'C8KWK70N2FFC4P6H'
HEADER = '&results=7'


URL_T = 'https://api.thingspeak.com/channels/1657669/fields/1.json?'
NEW_URL_T = URL_T + KEY + HEADER
get_data = requests.get(NEW_URL_T).json()
ft = get_data['feeds']
t = []
for x in ft:
    t.append(x['field1'])
print(t)

URL_H = 'https://api.thingspeak.com/channels/1657669/fields/2.json?'
NEW_URL_H = URL_H + KEY + HEADER
get_data = requests.get(NEW_URL_H).json()
fh = get_data['feeds']
h = []
for x in fh:
    h.append(x['field2'])
print(h)