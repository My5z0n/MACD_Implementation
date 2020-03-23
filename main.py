import MACD
import data_load as dl
import print_chart as pch
import  Simulation
import argparse
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("fname", help="file path containing stock data",
                        type=str)
    parser.add_argument("name", help="name of stock market shares",
                        type=str)
    parser.add_argument("-begin", help="day when buy/sell simulation starts", type=int,
                        default=1)
    parser.add_argument("-end", help="day when buy/sell simulation stops", type=int,
                        default=1000)
    parser.add_argument("-mytype", help="select algorithm 1 normal 2 advanced", type=int,
                        default=1)
    args = parser.parse_args()
    dl.read_csv(args.fname)
    MACD.make_macd(dl.imported_price)
    MACD.make_signal()

    print("Simulation")
    if args.mytype==1:
        Simulation.perform_simulation(dl.imported_data, dl.imported_price, MACD.macd, MACD.signal, MACD.rwiliams,
                                      args.begin, args.end,1)
    elif args.mytype==2:
        MACD.make_wiliams(dl.imported_price)
        Simulation.perform_simulation(dl.imported_data, dl.imported_price, MACD.macd, MACD.signal, MACD.rwiliams,
                                      args.begin, args.end,2)

    print("Drawing plot")
    pch.draw_plot(dl.imported_price,dl.imported_data,MACD.macd,MACD.signal,args.name)
    print("Closing Script...")

if __name__ == "__main__":
    main()
