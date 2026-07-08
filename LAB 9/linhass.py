import random

#QUESTÃO 01

lista = []

while True:
    n = int(input("DIGITE UM NÚMERO (0 PARA PARAR): "))
    if n == 0:
        break
    lista.append(n)

if len(lista) < 4:
    print("A LISTA DEVE POSSUIR PELO MENOS 4 VALORES.")
else:
    print("Lista original:", lista)
    print("3 primeiros:", lista[:3])
    print("2 últimos:", lista[-2:])
    print("Lista invertida:", lista[::-1])
    print("Índices pares:", lista[::2])
    print("Índices ímpares:", lista[1::2])

#QUESTÃO 02     

urls = [
    "www.google.com",
    "www.gmail.com",
    "www.github.com",
    "www.reddit.com",
    "www.yahoo.com"
]

dominios = []

for url in urls:
    dominios.append(url[4:-4])

print("\nURLs:", urls)
print("Domínios:", dominios)

#QUESTÃO 03

lista = []

for i in range(10):
    lista.append(random.randint(-100, 100))

ordenada = sorted(lista)

print("\nLista ordenada:", ordenada)
print("Lista original:", lista)
print("Índice do maior valor:", lista.index(max(lista)))
print("Índice do menor valor:", lista.index(min(lista)))
print("Soma:", sum(lista))
print("Média:", sum(lista)/len(lista))

#QUESTÃO 04

lista1 = []
lista2 = []

qtd1 = int(input("\nQuantidade da lista 1: "))

for i in range(qtd1):
    lista1.append(int(input()))

qtd2 = int(input("Quantidade da lista 2: "))

for i in range(qtd2):
    lista2.append(int(input()))

intercalada = []

menor = min(len(lista1), len(lista2))

for i in range(menor):
    intercalada.append(lista1[i])
    intercalada.append(lista2[i])

intercalada.extend(lista1[menor:])
intercalada.extend(lista2[menor:])

print("Lista intercalada:", intercalada)

#QUESTÃO 05

lista1 = []
lista2 = []

for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))

intersecao = sorted(list(set(lista1) & set(lista2)))

print("\nLista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção:", intersecao)

#QUESTÃO 06

lista = []

for i in range(20):
    lista.append(random.randint(0, 100))

print("\nLista original:", lista)

tam = int(input("Tamanho das sublistas: "))

sublistas = []

for i in range(0, len(lista), tam):
    sublistas.append(lista[i:i+tam])

print("Sublistas:")
print(sublistas)

#QUESTÃO 07

n = int(input("\nDigite n: "))

matriz = []

for i in range(n):
    linha = [i] * n
    matriz.append(linha)

print("Resultado:")
for linha in matriz:
    print(linha)