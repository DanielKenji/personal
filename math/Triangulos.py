# Verifica pelos lados de um triângulo se ele é mesmo um triângulo.
# E se ele é escaleno, isósceles ou equilátero

a = float(input("Digite o tamanho do primeiro lado "))
b = float(input("Digite o tamanho do segundo lado "))
c = float(input("Digite o tamanho do terceiro lado "))

if a+b > c and a+c > b and b+c > a:
    print("É um triângulo.")
    if a == b and a == c:
        print("É um triângulo equilátero, pois seus lados são iguais.")
    elif a == b and a != c:
        print("É um triângulo isósceles, pois tem dois lados iguais.")
    elif a == c and a != b:
        print("É um triângulo isósceles, pois tem dois lados iguais.")
    elif b == c and a != c:
        print("É um triângulo isósceles, pois tem dois lados iguais.")
    else:
        print("É um triângulo escaleno, pois seus lados são diferentes.")
else:
    print("Não é um triângulo.")
input()
