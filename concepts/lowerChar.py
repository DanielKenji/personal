# Retorna uma letra em minusculo.

def lowerChar(char):
    if ord(char) >= 65 and ord(char) <= 90:
        num = ord(char)+32
        lower = chr(num)
        return lower
    else:
        return char

if __name__ == '__main__':
    a = input()
    print(lowerChar(a))
input()