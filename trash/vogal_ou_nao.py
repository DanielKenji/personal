# Testa se um caracter é vogal.

def vogal(char):
    if char in 'aeiouAEIOU':
        return "vogal"
    else:
        return "consoante"


if __name__ == "__main__":
    oi = input('Digite uma letra. ')
    print(vogal(oi))
input()
