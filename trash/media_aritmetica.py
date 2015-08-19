# Média aritmética. Implementado com listas.

print("Digite quantos elementos tem a média aritmética: ")
n = int(input())
notas = [0]*n
soma = 0
for i in range(0,n,1):
    notas[i] = float(input("Digite a nota. "))
    soma = soma + notas[i]
media = soma/n
print("A média aritmética dos elementos é",media)

input()