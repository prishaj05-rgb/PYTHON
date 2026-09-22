<<<<<<< HEAD
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #method to print points in coordinate format
    def __str__(self):
        return "({0},{1})" .format(self.x, self.y)

#create object

p1 = Point(2,3)
=======
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #method to print points in coordinate format
    def __str__(self):
        return "({0},{1})" .format(self.x, self.y)

#create object

p1 = Point(2,3)
>>>>>>> d67f225df264a7e2c6739ceb0a28f848ae4a7b63
print(p1)