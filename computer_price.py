<<<<<<< HEAD
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

#change the price
c.__maxprice = 1000
c.sell()

#using setter function
c.setMaxPrice(1000)
=======
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

#change the price
c.__maxprice = 1000
c.sell()

#using setter function
c.setMaxPrice(1000)
>>>>>>> d67f225df264a7e2c6739ceb0a28f848ae4a7b63
c.sell()    