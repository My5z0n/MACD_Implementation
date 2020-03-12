import csv
imported_data = []
imported_price = []



def read_csv(path):
    global imported_data
    imported_data= []
    global imported_price
    imported_price= []
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            date = row[0]
            price = row[4]

            if date =='Data' or price =='Zamkniecie':
                continue
            else:
                imported_price.append(float(price))
                imported_data.append(date)
