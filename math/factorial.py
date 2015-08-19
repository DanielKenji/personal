# Factorial of a number


number = int(input())
fact = 1
if number < 0:
    print("Doesn't exist.")
elif number == 0 or number == 1:
    print("1")
else:
    for i in range(1, number+1):
        fact = fact * i
    print(fact)
input()