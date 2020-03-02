import MACD
import data_load as dl
import print_chart as pch
import  Simulation
def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("fname", help="file path containing stock data",
                        type=str)
    parser.add_argument("name", help="name of stock market shares",
                        type=str)
    parser.add_argument("-plot", help="type of displayed plot",type=int,
                        default=1)
    parser.add_argument("-begin", help="day when buy/sell simulation starts", type=int,
                        default=1)
    parser.add_argument("-end", help="day when buy/sell simulation stops", type=int,
                        default=1000)
    args = parser.parse_args()
    dl.read_csv(args.fname)
    MACD.make_macd(dl.imported_price)
    MACD.make_signal()
    print("Simulation")
    Simulation.perform_simulation(dl.imported_data, dl.imported_price, MACD.macd, MACD.signal)
    print("Drawing plot")
    pch.draw_plot(dl.imported_price,dl.imported_data,MACD.macd,MACD.signal,args.name,args.plot)
    print("Closing Script...")

if __name__ == "__main__":
    main()
