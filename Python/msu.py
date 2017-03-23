#!/usr/bin/python3
# Making Stuff Up
# When you need to make stuff up. Reformat to fit the needs of your arbitrarily-mandated-by-management records!

import random
import requests
from bs4 import BeautifulSoup

randint = random.SystemRandom().randint

# Time

time = '{:02}:{:02}'.format(randint(20, 23), randint(0, 59))
pace = 6 * 60 + 45 + randint(0, 59)
distance = round(1.8 + (randint(0, 30) / 100), 2)
duration = pace * distance
# Stringify
pace = '{:02}:{:02}'.format(int(pace / 60), int(pace % 60))
duration = '{:02}:{:02}'.format(int(duration / 60), int(duration % 60))

# Date

day = input('Choose a day this record occurs on (ISO format, yyyy-mm-dd): ')

# Weather

r = requests.get('https://www.wunderground.com/history/airport/KSJC/{}/{}/{}/DailyHistory.html?req_city=San+Jose&req_state=CA&req_statename=&reqdb.zip=95101&reqdb.magic=1&reqdb.wmo=99999&MR=1'.format(*day.split('-')))
bsoup = BeautifulSoup(r.text, 'lxml')
hist = bsoup.find('table', {'class': 'obs-table responsive'}).find_all('tr', {'class': True})
for row in hist:
    rowtime = row.text.split('\n')[1]
    if 'PM' in rowtime:
        if int(rowtime.split(':')[0]) == int(time.split(':')[0]) % 12:  # Same hour, close enough
            break  # oh no a break statement
weather = row.text.split('\n')[-2]

print('{}\t{}\t{}\t{}\t{}\t{}'.format(day, time, distance, duration, pace, weather))
