"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730322652"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print(" Your fortune cookie says... ")

x = randint(1, 4)
if(x > 2): 
    if(x == 3):
        print(" money will come your way. ")
    else:
        print(" you will meet the love of your life tomorrow. ")
else:
    if( x == 1):
        print(" try another cookie. ")
    else:
        print(" you will have bad luck for 11 years. ")

print(" Now, go spread positive vibes! ")

