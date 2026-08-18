#create class
class IOString ():

    #constructor set to default value
    def __init__(self):
        self.str1 = ""

    #function to get imput from user
    def get_string(self):
        self.str1 = input("Enter a string: ")

  #function to print the string in uppercase
    def print_string(self):
        print(self.str1.upper())

    #object creation
str1 = IOString()

#Call the functions
str1.get_string()
str1.print_string()