import MACD
import data_load as dl
import argparse
import  Simulation
import statistics
import print_chart as pch
def main():
    pusta=[]
    tablica=["data/11b_d.csv","data/bft_d.csv","data/cdr_d.csv",
             "data/jsw_d.csv","data/kgh_d.csv","data/kty_d.csv",
             "data/lpp_d.csv","data/mbk_d.csv","data/neu_d.csv",
             "data/pkn_d.csv","data/WIG_20.csv","data/wwl_d.csv",
             "data/pko_d.csv", "data/peo_d.csv", "data/pge_d.csv",
             "data/ccc_d.csv", "data/lts_d.csv", "data/opl_d.csv",
             "data/gpw_d.csv", "data/mil_d.csv"
             ]
    parser = argparse.ArgumentParser()
    parser.add_argument("fname", help="file path containing stock data",
                        type=str)
    parser.add_argument("name", help="name of stock market shares",
                        type=str)
    parser.add_argument("-plot", help="type of displayed plot", type=int,
                        default=1)
    parser.add_argument("-begin", help="day when buy/sell simulation starts", type=int,
                        default=1)
    parser.add_argument("-end", help="day when buy/sell simulation stops", type=int,
                        default=1000)
    args = parser.parse_args()
    final=0
    for x in tablica:


        dl.read_csv(x)
        MACD.make_macd(dl.imported_price)
        MACD.make_signal()
        MACD.make_wiliams(dl.imported_price)
        #print("Simulation")
        var = Simulation.perform_simulation(dl.imported_data, dl.imported_price, MACD.macd, MACD.signal,x)
        final=final+var
        pusta.append(var)
      #  print("Drawing plot")
      #  pch.draw_plot(dl.imported_price,dl.imported_data,MACD.macd,MACD.signal,x,args.plot)
        # print("Closing Script...")
    print('{0:4.4f}'.format(final ))
    print('{0:4.4f}'.format(statistics.median(pusta)))
    print('{0:2.2f}'.format(final/20.0))
if __name__ == "__main__":
    main()
