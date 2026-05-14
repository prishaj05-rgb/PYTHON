price = 2.50

#define a function that calculates the differnce between the amount paid and the price of the item
def calcu_change(amount_paid):
   return amount_paid - price

c = calcu_change(4.00)
print("change: ", c)