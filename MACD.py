macd = []
signal = []


#Calculates ema
def make_ema(n, data, day):
    tmp_vector = data[day - n: day + 1] # vector of intresting prices in this calculation
    alpha = 2 / (n + 1)  # declaring smoothing factor
    sum = 0.0
    weights = 0.0
    var=1.0 #(1-alhpa)^N
    for i in range(n + 1):
        sum += var * tmp_vector[i]
        weights += var
        var *=( 1 - alpha)

    return sum / weights

#Calculates macd rate
def make_macd(exchange_rate):

    for i in range(len(exchange_rate)):
        if i < 26:
            macd.append(None)
        elif i>=26:
            ema12 = make_ema(12, exchange_rate, i)
            ema26 = make_ema(26, exchange_rate, i)
            result = ema12 - ema26
            macd.append(result)



#Calculate Signal
def make_signal():
    for i in range(35):
        signal.append(None)
    for i in range(35, len(macd)):
        signal.append(make_ema(9, macd, i))