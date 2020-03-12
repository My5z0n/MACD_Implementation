from datetime import datetime

import print_chart


def create_buy_sell_signalls(data, prices, MACD, SIGNAL,wiliam):
    dif = 0
    buy_sell = []
    for i in range(len(MACD)):
        if MACD[i] is not None and SIGNAL[i] is not None:
            # set start position
            if dif == 0:
                if MACD[i] - SIGNAL[i] > 0:
                    dif = 1
                elif MACD[i] - SIGNAL[i] < 0:
                    dif = -1
                continue
        else:
            continue

        varunek=0
        if MACD[i] - SIGNAL[i] > 0:
            if dif == 1:
                pass
            elif dif == -1:
                # MACD intersects SIGNAL from below
                dif = 1
                # signals should be bellow 0 to be more reliable
                #if MACD[i] < -varunek:
                #
                buy_sell.append((data[i], 'BUY', prices[i]))
        elif MACD[i] - SIGNAL[i] < 0:
            if dif == 1:
                # MACD intersects SIGNAL from above to be more reliable
                dif = -1
                # signals should be above 0 to be more reliable
                #if MACD[i] > varunek :
                buy_sell.append((data[i], 'SEL', prices[i]))
            elif dif == -1:
                pass

        else:
            continue
    return buy_sell


def perform_simulation(data, prices, MACD, SIGNAL, wiliam,xname="",start_day=1, end_day=1000, money=1000.0,):
    buy_sell = create_buy_sell_signalls(data, prices, MACD, SIGNAL,wiliam)
    points = 0.0
  #  print('Start Point:')
  #  print(f'Money: {money}')
  #  print(f'Points: {points}')
    k = 0
    if len(buy_sell)>0:

        for a in range(start_day-1, end_day-1):
            if data[a] == buy_sell[k][0] :

                if buy_sell[k][1] == 'BUY' and money != 0.0 and wiliam[a] is not None and wiliam[a]<=-79.0:
                    points += money / buy_sell[k][2]
                    money = 0.0
                    last_event=datetime.strptime(data[a], "%Y-%m-%d")
                  #  print('-------------')
                   # print(f'Date: {data[a]}')
                   # print(f'Price: {prices[a]}')
                   # print(f'SIGNAL: {buy_sell[k][1]}')
                   # print(f'Money: {money}')
                   # print(f'Points: {points}')
                if buy_sell[k][1] == 'SEL' and points != 0.0 and wiliam[a] is not None  and wiliam[a]>=-19.0:
                    money += points * buy_sell[k][2]
                    points = points-1*points
                   # print('-------------')
                  #  print(f'Date: {data[a]}')
                 #   print(f'Price: {prices[a]}')
                  #  print(f'SIGNAL: {buy_sell[k][1]}')
                #    print(f'Money: {money}')
                 #   print(f'Points: {points}')
                if len(buy_sell) - 1 == k:
                    break
                else:
                    k += 1

        # sell everything:
        money += points * prices[-1]
        points = 0.0
       # print('************')
        #print('End Point:')
       # print(f'Money: {money}')
      #  print(f'Points: {points}')
        print('{0}: {1:2.2f}'.format(xname, money / 1000.0 * 100))
        return money / 1000.0 * 100
    print('{0}: {1:2.2f}'.format(xname, money / 1000.0 * 100))
    return 100
