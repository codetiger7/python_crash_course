from matplotlib import pyplot as plt

import csv


# get high temps from file
filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row[1])

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)

    # plot data
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(highs, c='red')

    # format plot
    plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()




