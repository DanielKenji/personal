# Usuario informa quantidade de individuos de duas populacoes e suas
# taxas de crescimento por ano.
# Programa calcula tempo para que se igualem.

a1pop = float(input("Digite valor absoluto da população 1. "))
a1cre = float(input("Digite porcentagem de crescimento. "))
a2pop = float(input("Digite valor absoluto da população 2. "))
a2cre = float(input("Digite porcentagem de crescimento. "))
anos = 0
while a1pop != a2pop:
    a1pop += a1pop * (a1cre / 100)
    a2pop += a2pop * (a2cre / 100)
    anos += 1
print("Em", anos, "as populações serão iguais.")
input()
