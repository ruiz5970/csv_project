import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv","r")

csv_file = csv.reader(open_file,delimiter=',')

header_row = next(csv_file)
'''
print(header_row)

for index,column_header in enumerate(header_row):
    print(index,column_header)
'''

date_index = header_row.index('DATE')
high_index = header_row.index('TMAX')
low_index = header_row.index('TMIN')


highs = []
dates = []
lows = []

x = datetime.strptime('2018-07-01','%Y-%m-%d')
print(x)



for row in csv_file:
    try:
        high = int(row[high_index])
        low = int(row[low_index])
        the_date = datetime.strptime(row[date_index],'%Y-%m-%d' )
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(the_date)





open_file2 = open("sitka_weather_2018_simple.csv","r")

csv_file2 = csv.reader(open_file2,delimiter=',')

header_row2 = next(csv_file2)
'''
print(header_row)

for index,column_header in enumerate(header_row):
    print(index,column_header)
'''

date_index2 = header_row2.index('DATE')
high_index2 = header_row2.index('TMAX')
low_index2 = header_row2.index('TMIN')
name_index2 = header_row2.index('NAME')

highs2 = []
dates2 = []
lows2 = []

x = datetime.strptime('2018-07-01','%Y-%m-%d')
print(x)



for row in csv_file2:
    try:
        high2 = int(row[high_index2])
        low2 = int(row[low_index2])
        the_date2 = datetime.strptime(row[date_index2],'%Y-%m-%d' )
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs2.append(high2)
        lows2.append(low2)
        dates2.append(the_date2)










import matplotlib.pyplot as plt


fig, ax = plt.subplots(2,sharex='col')
fig.suptitle('Temperature comparison between DEATH VALLEY, CA US and SITKA AIRPORT, AK US',fontsize=12)
ax[0].plot(dates,highs,c="red",alpha=0.5)
ax[0].plot(dates,lows,c="blue",alpha=0.5)
ax[0].set_title("DEATH VALLEY, CA US",fontsize=12)

ax[1].plot(dates2,highs2,c="red",alpha=0.5)
ax[1].plot(dates2,lows2,c="blue",alpha=0.5)
ax[1].set_title("SITKA AIRPORT, AK US",fontsize=12)

'''plt.title("Daily High and Low Temperatures - 2018\nDeath Valley",fontsize=16)
plt.xlabel("", fontsize=12)

plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)



fig.autofmt_xdate()'''


ax[0].fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
ax[1].fill_between(dates2,highs2,lows2,facecolor='blue',alpha=0.1)

plt.show()
