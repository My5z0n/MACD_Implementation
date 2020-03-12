import matplotlib.pyplot as plt
import matplotlib.dates as dat
from datetime import datetime

date_in_datatime = []
plot_date = []


def prepare_date(day):
    global date_in_datatime
    date_in_datatime= []
    global  plot_date
    plot_date= []
    for date in day:
        try:
            date_in_datatime.append(datetime.strptime(date, "%Y-%m-%d"))
        except ValueError:
            raise Exception("Broken CSV Data")

    for date in date_in_datatime:
        plot_date.append(dat.date2num(date))


def draw_plot(prices, day, MACD, signal, name,type=1):
    prepare_date(day)
    fig, ax1 = plt.subplots(figsize=(14,5))
    plt.grid(True)

    if type == 1:
        color = 'tab:red'

        ax1.set_xlabel('Date')
        ax1.set_ylabel(name, color=color)
        ax1.plot(plot_date, prices, color=color, label=name)
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

        color = 'tab:orange'
        color2 = 'tab:green'
        ax2.set_ylabel('MACD VALUES', color=color)  # we already handled the x-label with ax1
        ax2.plot(plot_date, MACD, color=color, label='MACD ')
        ax2.plot(plot_date, signal, color=color2, label='SIGNAL')
        ax2.tick_params(axis='y', labelcolor=color)


    elif type == 2:
        color = 'tab:red'
        ax1.set_xlabel('Date')
        ax1.plot(plot_date, signal, color=color, label='SIGNAL')

        color = 'tab:green'
        ax1.plot(plot_date, MACD, color=color, label='MACD')

    # Prepare to show
    plt.gcf().autofmt_xdate()
    myFmt = dat.DateFormatter('%Y-%m')
    plt.gca().xaxis.set_major_formatter(myFmt)
    fig.tight_layout()
    fig.legend(loc='upper left', bbox_to_anchor=(0.06, 0.97))

    plt.show()
