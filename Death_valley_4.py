import csv
from datetime import datetime

from matplotlib import pyplot as plt

open_file = 'death_valley_2018_simple.csv'
open_file = 'sitka_weather_2018_simple.csv'
place_name = ''
with open(open_file) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print(header_row)
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        # Grab the station name, if it's not already set.
        if not place_name:
            place_name = row[name_index]
            print(place_name)
            
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = f"Daily high and low temperatures - 2018\n{place_name}"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()