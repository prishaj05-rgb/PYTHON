#create a tuple with different data types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

#crate a tuple
tuplex = (4,6,2,8,3,1)
print(tuplex)

#tuples are immutable, meaning you cannot change their values after creation.
#using merge of tuples with the + operator you can add an element and it will create a new tuple

tuplex = tuplex + (9,)
print(tuplex)

#counts the number of occurrences of an element in a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

#create a tuple 
tuplex = (4, 6, 2, 8, 3, 1, 5, 3, 8, 2,5)
_slice = tuplex[3:5]
print(_slice)

_slice = tuplex[:6]
print(_slice)
