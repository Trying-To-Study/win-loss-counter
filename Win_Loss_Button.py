# TryingToStudy's win loss buttons 1.0

from tkinter import *
import csv
import matplotlib.pyplot as plt
import numpy as np

# variables
w = 0
ls = 0


def win():
    """Defines win and updates the txt file for obs"""
    global w
    w += 1
    f = open("WinLossData.txt", 'w')
    f.write(f'W({w}) L({ls})')
    f.close()


def loss():
    """Defines loss and updates the txt file for obs"""
    global ls
    ls += 1
    f = open("WinLossData.txt", 'w')
    f.write(f'W({w}) L({ls})')
    f.close()


def getdata():
    """To properly get the data into two arrays"""
    # arrays
    totwins = []
    totlosses = []
    day = []

    # count for day
    count = 0

    # file reader
    f = open("WinLossData.csv", "r")
    data = f.read().split()
    data = [i for i in data if i != ","]

    f.close()

    # to properly divide and set up the arrays
    for i in data:

        x = i.split(",")
        x1 = int(x[0])
        x2 = int(x[1])
        totwins.append(x1)
        totlosses.append(x2)
        count += 1
        day.append(count)

    return [totwins, totlosses, day]


def reset():
    """Defines reset status and save for data collection into a csv file"""
    # put data into csv file

    # define list with values
    global w, ls
    val = [w, ls]

    # write in it
    f = open("WinLossData.csv", "a")
    writer = csv.writer(f)
    writer.writerow(val)

    f.close()
    print("Data Automatically Saved!")
    # reset values

    w = 0
    ls = 0


def call_button():
    """Calling the button into display"""
    window = Tk()

    button1 = Button(window, text="Win", command=win)
    button1.pack()

    button2 = Button(window, text="Loss", command=loss)
    button2.pack()

    button3 = Button(window, text="Reset", command=lambda: [reset(), window.destroy()])
    button3.pack()

    window.mainloop()


def dat():
    """To get and graph your past wins and loss recorded on stream"""
    total_wins = getdata()[0]
    total_losses = getdata()[1]

    # focus here
    stream_days = getdata()[2]

    x_axis = np.arange(len(stream_days))

    plt.bar(x_axis - 0.2, total_wins, 0.4, label='Wins', color="lime", edgecolor="black")
    plt.bar(x_axis + 0.2, total_losses, 0.4, label='Losses', color="red", edgecolor="black")

    plt.xticks(x_axis, stream_days)
    plt.xlabel("Stream Day Number")
    plt.ylabel("Win/Loss Bars")
    plt.title("Win/Loss Per Day Bar Chart")
    plt.legend()
    plt.show()


# run em
call_button()
dat()

