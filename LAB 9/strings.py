#QUESTÃO 01

nome = input("DIGITE SEU PRIMEIRO NOME: ")
sobre = input("DIGITE SEU SOBRENOME: ")

print(f"BEM VINDO(A), {nome} {sobre}!")

#QUESTÃO 02

frase = input("\nDIGITE UMA FRASE: ")
espacos = frase.count(" ")
print("ESPAÇOS EM BRANCO:", espacos)

#QUESTÃO 03

nome = input("\nDIGITE SEU NOME: ")
for i in range(1, len(nome) + 1)
    print(nome[:i])

#QUESTÃO 04

numero = input("\nDIGITE O NÚMERO: ")
if len(numero) == 0:
    numero = "9" + numero
elif len(numero) == 9 and numero[0] != "9":
    numero = "9" + numero[1:]
print("NÚMERO COMPLETO:", numero[:-4] + "-" + numero[-4:])
S
#QUESTÃO 05

frase = input("\nDIGITE UMA FRASE: ")
vogais = "aeiouAEIOU"
indices = []

for i in range(len(frase)):
    if frase[i] in vogais:
        indices.append(i)
print("ÍNDICES DAS VOGAIS:", ",".join(map(str, indices)))
print("TOTAL:", len(indices), "vogais")

