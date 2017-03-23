#!/usr/bin/python3
# Making Stuff Up
# When you need to make stuff up. Reformat to fit the needs of your arbitrarily-mandated-by-management records!

import random

randint = random.SystemRandom().randint

time = '{}:{:02}'.format(randint(20, 23), randint(0, 59))
pace = 6 * 60 + 30 + randint(0, 59)
distance = round(1.8 + (randint(0, 30) / 100), 2)
duration = pace * distance

# Stringify
pace = '{}:{:02}'.format(int(pace / 60), int(pace % 60))
duration = '{}:{:02}'.format(int(duration / 60), int(duration % 60))

day = input('Choose a day this record occurs on (yyyy-mm-dd format): ')
print('{}\t{}\t{}\t{}\t{}\t'.format(day, time, distance, duration, pace))
