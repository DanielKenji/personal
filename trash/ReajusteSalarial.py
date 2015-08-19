salario = float(input("Digite seu salário "))
print("Digite a porcentagem do seu aumento. Por exemplo, para 20% de aumento, ")
aumento = float(input("Digite 20, sem o sinal de porcentagem. "))
reajuste = (aumento*salario)/100
print("seu salário era R$",salario,"e passa a ser R$",salario+reajuste)
input()