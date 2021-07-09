# coding: utf-8

from datetime import datetime
import time
import matplotlib.pyplot as plt
import os
import catch_exchange_scrapper as ces


# ---------------------	ATTENTION !!!!! -----------------
# Removing the comment from the next line will erase perma-
# nentily all our data!! Be carefull.

#clean_data_json()

# The following 2 functions aren't tested because there aren't
# enought data to do so.

def plot_data(period):
    period = int(period)
    
    data = ces.read_data()

    timeline = data["timeline"][-period:]

    timeline = list(map(lambda t: datetime.utcfromtimestamp(t).strftime('%d-%m-%Y'), timeline))

    for country in data['values']:
        balance = data['values'][country][-period:]
        base = balance[0]
        if base == 0:
            base = 0.001
        for i in range(len(balance)):
            if balance[i] == 0:
                balance[i] = 0.001
            #if balance[i]/base >= 2:
            #    print(country + str(balance) + str(i))
            balance[i] = round(balance[i]/base, 2)
        l = country
        if balance[len(balance)-1] != 1:
            l = l + f" {balance[len(balance)-1]}" 
        plt.plot(timeline, balance, label = l)
	
    plt.xlabel('Timeline')
    plt.ylabel('Balance')
    plt.legend(loc='center', bbox_to_anchor=(0.5,-0.6), ncol=10)
    plt.title(f'Currency value variation in the last {period} days')

    if period >= 7:
        every_nth = int(5)
        ax = plt.subplot()
        plt.axes().xaxis.set_major_locator(plt.MaxNLocator(every_nth))

    plt.rcParams['figure.figsize'] = [15, 5]

    plt.savefig(f'balance_{period}.png', bbox_inches='tight')

    plt.close()

def try_plot():
    data = ces.read_data()

    size = len(data['values']['USD'])

    periods = [2, 2, 3, 7, 7, 15, 30, 90, 180, 365, 730, 1095, 1460, 1825, 3650]

    for p in periods:
        if size >= p:
            plot_data(p)
        else:
            break

    if size >= periods[0]:
        print("New data available!")

def run():
    while True:
        if ces.updated():
            print("UPDATED!")
            try_plot()
            os.system('git add *.png')
            os.system('git commit -m "updated charts"')
            os.system('git push')
        else:
            print(f"Dormindo desde: {datetime.now()}")
            time.sleep(1*60*60)
