import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv","r")
open_file = open("sitka_weather_07-2018_simple.csv","r")

csv_file = csv.reader(open_file,delimiter=',')
place_name = ''

header_row = next(csv_file)
'''
print(header_row)

for index,column_header in enumerate(header_row):
    print(index,column_header)
'''
date_index = header_row.index('DATE')
high_index = header_row.index('TMAX')
low_index = header_row.index('TMIN')
name_index = header_row.index('NAME')


highs = []
dates = []
lows = []

x = datetime.strptime('2018-07-01','%Y-%m-%d')
print(x)

for row in csv_file:
    if not place_name:
            place_name = row[name_index]
            print(place_name)
    try:
        high = int(row[high_index])
        low = int(row[low_index])
        the_date = datetime.strptime(row[2],'%Y-%m-%d' )
    except ValueError:
            print(f"Missing data for {the_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(the_date)



import matplotlib.pyplot as plt

fig, ax = plt.subplots(2) 

ax[0].plot(dates,highs,c="red",alpha=0.5)
plt.plot(dates,lows,c="blue",alpha=0.5)

plt.title("Daily High and Low Temperatures - 2018\nDeath Valley",fontsize=16)
plt.xlabel("", fontsize=12)

plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)



fig.autofmt_xdate()

plt.ylabel("Temperature(F)",fontsize=12)
plt.tick_params(axis="both",labelsize=12)

plt.show()

