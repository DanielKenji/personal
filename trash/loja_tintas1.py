# Loja de tintas: 1 litro de tinta para 3 metros quadrados. 1 lata de 18 litros custa R$ 80,00.
# Pedir tamanho em metros e dar quantidade de latas e preço.

preco_lata = 80
area_lata = 54
quantidade = 0
area = int(input("Qual a area a ser pintada? "))

if area <= 54:
    print("Vc vai precisar de uma lata de tinta, R$ 80,00")
else:
    total = area//54
    if area % 54 != 0:
        total += 1
    print("Voce vai precisar de", total, "latas, R$ ", total*80)
input()
