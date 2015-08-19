# Lê n números e imprime a soma dos seus quadrados

print("Digite quantos numeros gostaria de usar. ")
n = int(input())
lista = []
soma = 0

for i in range(n):
    print("Digite um numero. ")
    num = int(input())
    lista.append(num)

lista_quad = [n**2 for n in lista] # List comprehension

for quadrado in lista_quad:
    soma += quadrado

print("Quadrado dos números:",lista_quad)
print("Soma dos quadrados:",soma)
input()