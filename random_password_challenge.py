import random
import string
print('hello, welcome to password generator')
#input the length of password
length = int(input('Enter the length of password: '))
#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
#string.ascii_letters = lower + upper
#combine the data
all = lower + upper + digits + symbols
#use random to generate password
temp = random.sample(all, length)
#create password
password = "".join(temp)
print('Your password is: ', password)