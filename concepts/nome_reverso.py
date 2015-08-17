# Recebe um nome e reverte o nome em letras minusculas.

print("Digite seu nome. ")
nome = str(input())
nome = nome.lower()  # Deixa a str nome em caracteres minusculos
nome = nome[::-1]    #[begin:end:step] Extended slice. Com step de -1 indexa a lista de tras para frente.
# Outra possibilidade: "".join(reversed(nome)) junta uma string vazia com o reverso da string nome
print(nome)
input()
