# Nome na vertical em escada. Letras maiusculas.
#  Strings aceitam indexing.

print("Digite seu nome: ")
nome = input()
upper = nome.upper()
for i in range(0,len(upper)+1):
    print(upper[:i])
input()