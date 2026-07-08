class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def __str__(self):
        return f"{self.nome} - {self.altura}m"

    def __gt__(self, other):
        return self.altura > other.altura

    def __lt__(self, other):
        return self.altura < other.altura

lst = []

quantidade = int(input("QUANTAS PESSOAS SERÃO CADASTRADAS? "))
for i in range(quantidade):
    nome = input("NOME: ")
    altura = float(input("ALTURA: "))

    pessoa = Pessoa(nome, altura)
    lst.append(pessoa)

print("\nPESSOA MAIS ALTA:")
print(max(lst))

print("\nPESSOA MAIS BAIXA:")
print(min(lst))

print("\nPESSOAS ORDENADAS POR ALTURA:")
for pessoa in sorted(lst):
    print(pessoa)