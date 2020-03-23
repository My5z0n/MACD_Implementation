import print_chart


def create_buy_sell_signalls(data, prices, MACD, SIGNAL):
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

        if MACD[i] - SIGNAL[i] > 0:
            if dif == 1:
                pass
            elif dif == -1:
                # MACD intersects SIGNAL from below
                dif = 1
                # signals should be bellow 0 to be more reliable
                #if MACD[i] < 0 and SIGNAL[i] < 0:
                buy_sell.append((data[i], 'BUY', prices[i]))
        elif MACD[i] - SIGNAL[i] < 0:
            if dif == 1:
                # MACD intersects SIGNAL from above to be more reliable
                dif = -1
                # signals should be above 0 to be more reliable
                #if MACD[i] > 0 and SIGNAL[i] > 0:
                buy_sell.append((data[i], 'SEL', prices[i]))
            elif dif == -1:
                pass

        else:
            continue
    return buy_sell


def perform_simulation(data, prices, MACD, SIGNAL,wiliam, start_day=1, end_day=1000,mytype=1, money=1000.0):
    buy_sell = create_buy_sell_signalls(data, prices, MACD, SIGNAL)
    points = 0.0
    print('Start Point:')
    print(f'Money: {money}')
    print(f'Points: {points}')
    k = 0
    for a in range(start_day-1, end_day-1):
        if data[a] == buy_sell[k][0]:
            print('-------------')
            print(f'Date: {data[a]}')
            print(f'Price: {prices[a]}')
            print(f'Money: {money}')
            print(f'Points: {points}')
            print(f'SIGNAL: {buy_sell[k][1]}')
            if wiliam is None or mytype ==1:

                if buy_sell[k][1] == 'BUY' and money != 0.0 :
                    points += money / buy_sell[k][2]
                    money = 0.0
                if buy_sell[k][1] == 'SEL' and points != 0.0:
                    money += points * buy_sell[k][2]
                    points = 0.0
            else:
                if buy_sell[k][1] == 'BUY' and money != 0.0 and wiliam[a]<=-79.0:
                    points += money / buy_sell[k][2]
                    money = 0.0
                if buy_sell[k][1] == 'SEL' and points != 0.0 and wiliam[a]>=-19.0:
                    money += points * buy_sell[k][2]
                    points = 0.0
            print(f'Money: {money}')
            print(f'Points: {points}')
            if len(buy_sell) - 1 == k:
                break
            else:
                k += 1

    # sell everything:
    money += points * prices[-1]
    points = 0.0
    print('************')
    print('End Point:')
    print(f'Money: {money}')
    print(f'Points: {points}')
    print('Percentage: {0:2.2f}%'.format(money / 1000.0 * 100))
