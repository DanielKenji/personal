# Pede 3 números e diz qual o menor

a = int(input("Digite o primeiro número "))
b = int(input("Digite o segundo número "))
c = int(input("Digite o terceiro número "))
print()

if a < b and a < c:
    print(a, "é o menor número.")
elif b < a and b < c:
    print(b, "é o menor número.")
elif a == b == c:
    print("Os numeros sao iguais.")
else:
    print(c, "é o menor número")
input()
