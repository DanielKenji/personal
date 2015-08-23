# Takes a list of integers and prints a histogram.
# Random testing implemented.

import random

def histogram(intlist):
    for number in intlist:
        print(number * "*")
    

if __name__ == "__main__":
    intlist = random.sample(range(1, 12), 3)
    histogram(intlist)
    