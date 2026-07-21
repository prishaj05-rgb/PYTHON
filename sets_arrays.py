#PART 1: Create two fruit baskets as sets
basket1 = {"apple","banana", "mango", "apple","grape"}
basket2 = {"mango", "kiwi", "banana", "kiwi"}

print("Basket 1:", basket1)
print("Basket 2:", basket2)

#PART 2: Add a new fruit to basket1

basket1.add("orange")
print("Basket 1 after adding orange:", basket1)

#PART 3: Find fruits in common to both baskets
common_fruits = basket1.intersection(basket2)
print("Fruits in common:", common_fruits)

#PART 4: Create an array of fruit counts using the array module
import array as arr
fruit_counts = arr.array('i', [3, 5, 2, 4])
print("Fruit counts array:", fruit_counts)  

#PART 5: Add new fruits counts to the array
fruit_counts.insert(0,1)
fruit_counts.append(6)
print("Fruit counts array after adding new counts:", fruit_counts)

#PART 6: Count how many times the number 4 appears in the array
count_of_4 = fruit_counts.count(4)
print("Count of 4 in fruit counts array:", count_of_4)

#PART 7: Reversethe order of the fruit counts array
fruit_counts.reverse()
print("Fruit counts array after reversing:", fruit_counts)


#PART 8: Print the final class fuit basket organiser summary
print('')
print("==== CLASS FRUIT BASKET ORGANISER ====")
print("Basket 1:", basket1)
print("Basket 2:", basket2)
print("Fruits in common:", common_fruits)
print("Fruit counts array:", fruit_counts)
print("=========================================")
