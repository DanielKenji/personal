# Primeiros 100 numeros de Fibonacci em lista

def fib100():
    lista = []
    a, b = 0, 1
    for i in range(0,100):
        lista.append(b)
        a, b = b, a+b
    return lista

    
if __name__ == '__main__':
    print(fib100())
    input()