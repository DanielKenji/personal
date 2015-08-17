# Procura uma palavra no dicionario. Retorna True para palavra no dicionario.
# False em caso contrario

def dicionario(palavra):
    f = open("portugues.txt", "r")
    for line in f:
        if palavra in line:
            return True
    return False

if __name__ == "__main__":
    palavra = input('Digite a palavra a procurar: ')
    print(dicionario(palavra))
input()
