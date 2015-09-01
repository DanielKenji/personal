# Count a text's vowels. Pretty dumb.

import sys

filename = sys.argv[1]
f = open(filename, "r")
vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
for line in f:
    for char in line:
        temp = char.lower()
        if temp in vowels:
            vowels[temp] += 1
        
print(vowels)
input()