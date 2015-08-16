ano = int(input("Digite o ano. "))
if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 != 0:
        print("O ano", ano, "nao e bissexto.")
    if ano % 100 == 0 and ano % 400 == 0:
        print("o ano", ano, "e bissexto.")
    elif ano % 100 != 0 and ano % 400 != 0:
        print("O ano", ano, "e bissexto.")
else:
    print("O ano", ano, "nao e bissexto.")
input()
