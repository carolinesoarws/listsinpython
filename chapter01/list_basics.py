from linked_lists import LinkedList

print("##############################################")
print("##############################################")
print("")
print(" Capitulo 01 - Uso básicos de listas em Python")
print("")
print("##############################################")
print("##############################################")
print("")

# Exemplo 01 - lista vazia com colchetes
print("Exemplo 01 - lista vazia com colchetes")
lista = []
print(type(lista))
print("#########################################")
print("")

# Exemplo 02 - lista simples com 5 elementos
print("Exemplo 02 - lista simples com 5 elementos")
lista = [10, 20, 30, 40, 50]
print(lista)
print(type(lista))
print("#########################################")
print("")

# Exemplo 03 - lista criada com a função list
print("Exemplo 03 - lista criada com a função list")
txt = list("python is fun")
print(txt)
print(type(txt))
print("#########################################")
print("")

# Exemplo 04 - Convertendo uma tupla para lista com função list
print("Exemplo 04 - Convertendo uma tupla para lista com função list")
minha_tupla = (1, 2, 3, 4)
minha_lista = list(minha_tupla)
print(minha_lista)
print(type(minha_lista))
print("#########################################")
print("")

# Exemplo 05 - Erro na lista com valore inteiros
print("Exemplo 05 - Erro na lista com valore inteiros")
# print(list(145783764))

# Exemplo 06 - Revertendo os elementos da lista com a função reverse
print("Exemplo 06 - Revertendo os elementos da lista com a função reverse")
minha_lista = [1, 2, 3, 4, 5]
print(f"Minha lista: {minha_lista}")

minha_lista.reverse()  # Inverte a lista original
print(f"Minha lista revertida: {minha_lista}")
print("#########################################")
print("")

# Exemplo 07 - Revertendo os elementos da lista com a função reversed
print("Exemplo 07 - Revertendo os elementos da lista com a função reversed")
minha_lista_01 = [1, 2, 3, 4, 5]
print(f"minha lista: {minha_lista_01}")

# Criando uma nova lista com a ordem invertida
nova_lista = list(reversed(minha_lista))
print(f"Minha nova lista: {nova_lista}")
print(nova_lista)
print("#########################################")
print("")

# Exemplo 08 - Ordenando a lista com a função sort
print("Exemplo 08 - Ordenando a lista com a função sort")
lista_01 = [3, 1, 4, 2, 5]
# Ordena a lista em ordem crescente
lista_01.sort()
print(lista_01)
print("#########################################")
print("")

# Exemplo 09 - Ordenando a lista com a função sorted
print("Exemplo 09 - Ordenando a lista com a função sorted")
lista_02 = [3, 1, 4, 2, 5, 9, 18, 23, 3]

nova_lista = sorted(lista_02) # Retorna uma nova lista ordenada
print(nova_lista)
print("#########################################")
print("")

# Exemplo 10 - Segundo exemplo ordenando lista com a função sorted
print("Exemplo 10 - Segundo exemplo ordenando lista com a função sorted")
numeros = [5, 2, 9, 1, 5, 6]

# Ordenar em ordem decrescente
numeros_ordenados = sorted(numeros, reverse=True)
print(numeros_ordenados)
print("#########################################")
print("")

# Exemplo 11 - Reordenando a lista de forma manual
print("Exemplo 11 - Reordenando a lista de forma manual")
lista_03 = [1, 2, 3, 4, 5]
lista_03[0],lista_03[4] = lista_03[4], lista_03[0]

# Troca o primeiro e o último elemento
print(lista_03)
print("#########################################")
print("")

# Exemplo 12 - Lista com valores duplicados
print("Exemplo 12 - Lista com valores duplicados")
lista = [1, 3, 4, 6, 7, 5, 4, 77, 54, 3, 22, 4, 77, 4]

print(lista)
print(type(lista))
print("#########################################")
print("")

# Exemplo 13 - Exemplo de lista como iterável
print("Exemplo 13 - Exemplo de lista como iterável")
lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item)
print("#########################################")
print("")

# Exemplo 14 - Exemplo de lista homogêneas
print("Exemplo 14 - Exemplo de lista homogêneass")
# Lista de inteirosrr
lista_inteiros = [1, 2, 3, 4, 5]
# Lista de strings
lista_strings = ["a", "b", "c", "d"]
# Lista de floats
lista_floats = [1.1, 2.2, 3.3, 4.4]

print(lista_inteiros, lista_strings, lista_floats)
print("#########################################")
print("")

# Exemplo 15 - Exemplo Lista Heterogênea
print("Exemplo 15 - Exemplo Lista Heterogênea")
# Lista contendo inteiro, string, float e booleano
lista_heterogenea = [1, "dois", 3.0, True]
print(lista_heterogenea)
print("#########################################")
print("")

# Exemplo 16 - Matriz 2d
print("Exemplo 16 - Matriz 2d")
matriz = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
print(matriz)
print("#########################################")
print("")

# Exemplo 17 - Acessando elementos da lista 2D
print("Exemplo 17 - Acessando elementos da lista 2D")

lista_2d = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
for linha in lista_2d:
    for elemento in linha:
        print(elemento)
print("#########################################")
print("")

# Exemplo 18 - Lista Matriz 3D
print("Exemplo 18 - Lista Matriz 3DD")
matriz_3d = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]
print(matriz_3d)
print("#########################################")
print("")

# Exemplo 19 - Listas com tipos complexos
print("Exemplo 19 - Listas com tipos complexos")
# Lista de dicionários
lista_dicionarios = [
 {"nome": "Alice", "idade": 25},
 {"nome": "Bob", "idade": 30}
]
# Lista de tuplas
lista_tuplas = [(1, 2), (3, 4), (5, 6)]

print(lista_dicionarios)
print(lista_tuplas)
print("#########################################")
print("")

# Exemplo 20 - Lista de funções
print("Exemplo 20 - Lista de funções")


def soma(a, b):
    return a + b


def multiplicacao(a, b):
    return a * b


lista_funcoes = [soma, multiplicacao]
# Usar funções da lista
print(lista_funcoes[0](2, 3))
print(lista_funcoes[1](2, 3))
print("#########################################")
print("")

# Exemplo 21 - Linked Lists
print("Exemplo 21 - Linked Lists")

print("Criando uma lista encadeada")
llist = LinkedList()

print("Adicionando elementos à lista")
llist.append(1)
llist.append(2)
llist.append(3)

print("Imprimindo a lista")
llist.print_list()  # Saída: 1 -> 2 -> 3 -> None

print("Inserindo um elemento no início da lista")
llist.prepend(0)
llist.print_list()  # Saída: 0 -> 1 -> 2 -> 3 -> None

print("Removendo um elemento da lista")
llist.delete(2)
llist.print_list()  # Saída: 0 -> 1 -> 3 -> None
print("#########################################")
print("")
