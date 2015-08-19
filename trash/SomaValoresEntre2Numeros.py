print("Esse programa recebe dois números inteiros, um maior que o outro")
print("e retorna os números entre eles e a soma desses números.")

num1 = int(input("Digite o número 1. "))
num2 = int(input("Digite o número 2. "))
soma = 0
if num1 == num2:
    print("Números iguais")
elif num1 < 0 or num2 < 0:
    print("Números negativos. ")
else:
    maior = max(num1,num2)
    menor = min(num1,num2)
    while menor < maior-1:
        menor = menor + 1
        soma = soma + menor
        print(menor)
print("A soma dos numeros entre os números equivale a ",soma)
input()