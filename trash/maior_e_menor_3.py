a = int(input('Digite o primeiro número '))
b = int(input('Digite o segundo número '))
c = int(input('Digite o terceiro número '))
if a > b and a > c:
    print(a, "é o maior número.")
    if b > c:
        print(c, "é o menor número.")
    else:
        print(b, "é o menor número.")
elif b > a and b > c:
    print(b, "é o maior número. ")
    if a > c:
        print(c, "é o menor número.")
    else:
        print(a, "é o menor número.")
else:
    print(c, "é o maior número. ")
    if a > b:
        print(b, "é o menor número.")
    else:
        print(a, "é o menor número.")
input()
