import csv
from Model.Sale import Sale

class SaleModel():
    file = './data/sales.csv'

    def __init__(self):
        # Lo primero que hago cuando me instancian es mapear los datos a una lista de objetos Sale
        self.data = self.readData()

    # Esta funcion lee el scv y retorna una lista de objetos Model.Sale
    def readData(self):
        ifile = open(self.file, 'r')
        reader = csv.reader(ifile)
        rowNumber = 0
        data = []
        
        for row in reader:
            if rowNumber == 0:
                header = row
            else:
                indexOfClient = header.index('CLIENT')
                indexOfCode = header.index('CODE')
                indexOfProduct = header.index('PRODUCT')
                indexOfQuantity = header.index('QUANTITY')
                indexOfPrice = header.index('PRICE')

                sale = Sale(client=row[indexOfClient], code=row[indexOfCode], product=row[indexOfProduct], quantity=row[indexOfQuantity], price=row[indexOfPrice])
                data.append(sale)
            rowNumber += 1
        
        return data

    def byClient(self, client):
        products = []

        for sale in self.data:
            if sale.client == client:
                products.append(sale.product)

        return products

    def byProduct(self, product):
        clients = []

        for sale in self.data:
            if sale.product == product:
                clients.append(sale.clients)

        return clients

    def mostSold(self):
        

    # def groupBy(self, field):
    #     ifile = open(self.file, 'r')
    #     reader = csv.reader(ifile)
    #     rowNumber = 0
    #     toSort = []

    #     for row in reader:
    #         if (rowNumber == 0):
    #             header = row
    #         else:
    #             indexOfClient = header.index('PRODUCT')
    #             indexOfQuantity = header.index('QUANTITY')
    #             element = {'product': row[indexOfClient], 'quantity': row[indexOfQuantity]}
    #             toSort.append(element)
            
    #         rowNumber += 1

    #     return toSort


    # def groupProductByClient(client, product):
    #     # if (client )

    # def byProduct(self, product):
    #     return []

    # def mostSold(self):
    #     return []

    # def bestClients(self):
    #     return []