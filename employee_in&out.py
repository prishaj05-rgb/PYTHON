<<<<<<< HEAD
#create class
class employee:

    #initialising
    def __init__(self):
        print("Employee created")

    #calling destructor
    def __del__(self):
        print("Destructor called")

def Create_obj ():
    print("making object...")
    obj = employee()
    return obj

print ("Calling Create_obj() function...")
obj = Create_obj()
=======
#create class
class employee:

    #initialising
    def __init__(self)
        print("Employee created")

    #calling destructor
    def __del__(self):
        print("Destructor called")

def Create_obj ():
    print("making object...")
    obj = employee()
    return obj

print ("Calling Create_obj() function...")
obj = Create_obj()
>>>>>>> 95d5b28df1df032a0d148cc61d31d3cae18bb389
print ("Program End...")