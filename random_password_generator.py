import random

length = int(input('Enter the minimum length of the password needed: '))
numbers = '0123456789'
letters = 'abcdefghijklmnopqrstuvwxyz'
upper_ = letters.upper()
special = '[](){}_.$-!*#'

All = numbers + letters + upper_ + special
password = ''.join(random.choice(All) for i in range(length))
print(password)
