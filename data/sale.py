import csv
from Model.Sale import Sale

class SaleModel():
    file = './data/sales.csv'

    def __init__(self):
        self.headers = []
        # Lo primero que hago cuando me instancian es mapear los datos a una lista de objetos Sale
        self.data = self.readData()

    # Esta funcion lee el scv y retorna una lista de objetos Model.Sale
    def readData(self):
        ifile = open(self.file, 'r')
        reader = csv.reader(ifile)
        rowNumber = 0
        data = []

        try:
            for row in reader:
                if rowNumber == 0:
                    header = row
                    self.headers = header
                else:
                    indexOfClient = header.index('CLIENTE')
                    indexOfCode = header.index('CODIGO')
                    indexOfProduct = header.index('PRODUCTO')
                    indexOfQuantity = header.index('CANTIDAD')
                    indexOfPrice = header.index('PRECIO')

                    sale = Sale(client=row[indexOfClient], code=row[indexOfCode], product=row[indexOfProduct], quantity=row[indexOfQuantity], price=row[indexOfPrice])
                    data.append(sale)
                rowNumber += 1
        except FileNotFoundError:
            raise FileNotFoundError
        
        return data

    def clients(self):
        clients = []

        # por cada venta voy a armar un arreglo de clientes NO repetidos
        for sale in self.data:
            clients.append(sale.cliente)

        return set(clients)

    def products():
        products = []

        # por cada venta voy a armar un arreglo de productos NO repetidos
        for sale in self.data:
            products.append(sale.producto)

        return set(products)
        

    def byClient(self, client):
        products = []

        for sale in self.data:
            if sale.cliente == client:
                products.append(sale.producto)

        return products

    def byProduct(self, product):
        clients = []

        for sale in self.data:
            if sale.producto == product:
                clients.append(sale.cliente)

        return clients

    def bestClients(self):
        best = []
        clients = self.clients()
        
        # por cada cliente de ese arreglo, voy a revisar cada sale y armar el array de bests
        for client in clients:
            bestClient = {'name': client, 'amount': 0}
            for sale in self.data:
                if sale.cliente == client:
                    bestClient['amount'] += int(sale.precio)
            best.append(bestClient)
        
        return best

    def mostSold(self):
        most = []
        products = self.products()
        
        for product in products:
            mostSold = {'name': product, 'quantity': 0}
            for sale in self.data:
                if sale.producto == product:
                    mostSold['quantity'] += int(sale.cantidad)
            most.append(mostSold)
        
        return most