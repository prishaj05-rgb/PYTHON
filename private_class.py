#class creation
class myClass:

    #private variable
    __myPrivateVar = 27

    #private method
    def __privMeth(self):
        print("I am inside the class myClass")

    #function to print value of private variable
    def hello (self):
        print("Private variable value: " ,myClass.__myPrivateVar)

#object creation and method call

foo = myClass()
foo.hello()
foo.__privMeth()  # This will raise an AttributeError since __privMeth is private
    