import matplotlib.pyplot as plt
import matplotlib.dates as dat
from datetime import datetime

date_in_datatime = []
plot_date = []


def prepare_date(day):
    for date in day:
        try:
            date_in_datatime.append(datetime.strptime(date, "%Y-%m-%d"))
        except ValueError:
            raise Exception("Broken CSV Data")

    for date in date_in_datatime:
        plot_date.append(dat.date2num(date))


def draw_plot(prices, day, MACD, signal, name):
    prepare_date(day)
    plt.figure(figsize=(12, 9))

    plt.gcf().autofmt_xdate()

    ax1 = plt.subplot(211)
    plt.plot(plot_date, prices, color="red")
    plt.grid(True)
    plt.ylabel("Exchange " + name)

    plt.title(name + " Exchange rate ")

    plt.subplot(212, sharex=ax1)
    plt.plot(plot_date, MACD, color="darkorange", label="macd")
    plt.plot(plot_date, signal, color="green", label="signal")
    plt.legend()
    plt.grid(True)
    plt.title("MACD Signals")
    plt.ylabel("Value")

    plt.xlabel("Date YYYY-MM")

    plt.gcf().autofmt_xdate()
    myFmt = dat.DateFormatter('%Y-%m')
    plt.gca().xaxis.set_major_formatter(myFmt)

    plt.show()
