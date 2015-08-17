# Gera a sequencia de Fibonacci com termo final dado pelo usuario

a,b = 0,1
n = int(input("Digite ultimo termo da sequencia. "))
while n!= 0:
    fib = a + b
    n = n-1
    a,b = b,fib
    print(fib,end= ',') # Em vez de newline, termina com virgula
input()
