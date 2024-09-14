print("##############################################")
print("##############################################")
print("")
print(" Capitulo 02 - Consultas, manipulações e função com listas")
print("")
print("##############################################")
print("##############################################")
print("")

# Exemplo 01 - Consulta com index positivo
print("Exemplo 01 - Consulta com index positivo")
lista = [10, 20, 30, 40, 50]
print(lista[2])   # Saída: 30
print(lista[0])   # Saída: 10
print(lista[4])   # Saída: 50

print("#########################################")
print("")

# Exemplo 02 - Consulta com index negativo
print("Exemplo 02 - Consulta com index negativo")
lista = [1, 2, 3, 4, 10, 30]
print(lista[-1])   # Saída: 30
print(lista[-2])   # Saída: 10
print(lista[-4])   # Saída: 3

print("#########################################")
print("")

# Exemplo 03  - Consultando o último elemento da lista
print("Exemplo 03  - Consultando  o último elemento da lista")
lista = [10, 20, 30, 40, 50]
print(lista[-1])  # Saída: 50

print("#########################################")
print("")

# Exemplo 04 - Consultando o penúltimo ou outros elementos a partir do fim
print("Exemplo 04 - Consultando o penúltimo ou outros elementos a partir do fim")
print(lista[-2])  # Saída: 40 (penúltimo)
print(lista[-3])  # Saída: 30 (antepenúltimo)

print("#########################################")
print("")

# Exemplo 05 - Revertendo a lista com índices negativos
print("Exemplo 05 - Revertendo a lista com índices negativos")
print(lista[::-1])  # Saída: [50, 40, 30, 20, 10] (lista invertida)

print("#########################################")
print("")


# Exemplo 06 - Verificar presença de elemento a partir do final
print("Verificar presença de elemento a partir do final")
if lista[-1] == 50:
    print("O último elemento é 50.")

print("#########################################")
print("")

# Exemplo 07 - Slicing / Fatiamento com intervalo de indices
print("Exemplo 07 - Slicing / Fatiamento com intervalo de indices")
lista = [10, 20, 30, 40, 50]
print(lista[1:4])  # Saída: [20, 30, 40]
print(lista[0:3])  # Saída: [10, 20, 30]
print(lista[0:-2]) # Saída: [10, 20, 30]

print("#########################################")
print("")

# Exemplo 08 - Coerência com a indexação com slicing
print("Exemplo 08 - Coerência com a indexação com slicing")
lista = [10, 20, 30, 40, 50]
print(lista[:3])

print("#########################################")
print("")

# Exemplo 09 - Exemplo de facilidade na concatenação de slice
print("Exemplo 09 - Exemplo de facilidade na concatenação de slice")
lista = [1, 2, 3, 4, 5, 6]

nova_lista = lista[:3]
nova_lista_2 = lista[3:]
print(nova_lista + nova_lista_2)
print("#########################################")
print("")

# Exemplo 10 - Exemplo último valor da lista
print("Exemplo 10 - Exemplo último valor da lista")

lista = [1, 2, 3, 4, 5]
print(lista[1:])  # [2, 3, 4, 5]
print("#########################################")
print("")

# Exemplo 11 - Usando o elemento + 1
print("Exemplo 11 - Usando o elemento + 1")
lista = [1, 2, 3, 4, 5]
print(lista[1:5])

lista = [10, 20, 30, 40, 50]
print(lista[1:4])  # Saída: [20, 30, 40]
print(lista[0:3])  # Saída: [10, 20, 30]
print(lista[0:-2]) # Saída: [10, 20, 30]
print("#########################################")
print("")

# Exemplo 12 - Slicing exemplo passo
print("Exemplo 12 - Slicing exemplo passo")
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
print(lista[0:5:2])  # Saída: [10, 30, 50]
print(lista[1:5:3])  # Saída: [20, 50]
print(lista[5:10:2])  # Saída: [60, 80, 100]

print("negative indexes")
print(lista[0:-1:2])    # Saída: [10, 30, 50, 70, 90]
print(lista[-10:-4:3])  # Saída: [20, 50]
print("#########################################")
print("")

# Exemplo 13 - Consulta de existência do elemento na lista
print("Exemplo 13 - Consulta de existência do elemento na lista")
lista = [10, 20, 30, 40, 50]
print(20 in lista)  # Saída: True
print(60 in lista)  # Saída: False

print("#########################################")
print("")


# Exemplo 14 - Consultando cumprimento da lista
print("Exemplo 14 - Consultando cumprimento da lista")

lista = [10, 20, 30, 40, 50]
print(len(lista))  # Saída: 5
print("#########################################")
print("")

# Exemplo 15 - Consultando ocorrencia dos elementos da lista
print("Exemplo 15 - Consultando ocorrencia dos elementos da lista")

lista = [10, 20, 30, 20, 40, 50]
print(lista.count(20))  # Saída: 2
print("#########################################")
print("")

# Exemplo 16 - Consultando índice de um elemento da lista
print("Exemplo 16 - Consultando índice de um elemento da lista")

lista = [10, 20, 30, 20, 40, 50]
print(lista.index(10))  # Saída: 0
print("#########################################")
print("")

# Exemplo 17 - Função agregada Sum
print("Exemplo 17 - Função agregada Sum")

lista = [10, 20, 30, 40, 50]
print(sum(lista))   # Saída: 150
print("#########################################")
print("")

# Exemplo 18 - Função agregada Max
print("Exemplo 18 - Função agregada Max")
lista = [10, 20, 30, 40, 50]
print(max(lista)) # Saída: 50

print("#########################################")
print("")

# Exemplo 19 - Função agregada Min
print("Exemplo 19 - Função agregada Min")
lista = [10, 20, 30, 40, 50]
print(min(lista))   # Saída: 10

print("#########################################")
print("")

# Exemplo 20 - Função agregada All
print("Exemplo 20 - Função agregada All")
lista = [True, True, True]
resultado = all(lista)
print(resultado)  # Saída: True

print("#########################################")
print("")

# Exemplo 21 - Função agregada Any
print("Exemplo 21 - Função agregada Any")
lista = [False, False, True]
resultado = any(lista)
print(resultado)  # Saída: True

print("#########################################")
print("")

# Exemplo 22 - Manipulando listas com função append
print("Exemplo 22 - Manipulando listas com função append")

lista = [1, 2, 3]
lista.append(4)
print(lista)  # Saída: [1, 2, 3, 4]
print("#########################################")
print("")

# Exemplo 23 - Manipulando lista com função Insert
print("Exemplo 23 - Manipulando lista com função Insert")

lista = [1, 2, 3]
lista.insert(1, 1.5)
print(lista)  # Saída: [1, 1.5, 2, 3]
print("#########################################")
print("")

# Exemplo 24 - Manipulando lista com função Extend
print("Exemplo 24 - Manipulando lista com função Extend")
lista_atual = [1, 2, 3] # lista atual
print(f"Lista atual: {lista_atual}")

outra_lista = [4, 5]
print(f"Outra lista: {outra_lista}")

lista_atual.extend(outra_lista) # outra lista
print(f"lista atualizada: {lista_atual}")  # Saída: [1, 2, 3, 4, 5]
print("#########################################")
print("")

# Exemplo 25 - Removendo elementos da lista com a função remove
print("Exemplo 25 - Removendo elementos da lista com a função remove")
lista = [1, 2, 3, 2]
print(f"Lista: {lista}")
lista.remove(2)
print(f"Nova lista: {lista}")  # Saída: [1, 3, 2]

print("#########################################")
print("")

# Exemplo 26 - Removendo elementos da lista com a função pop
print("Exemplo 26 - Removendo elementos da lista com a função pop")
lista = [1, 2, 3]
print(f"Lista: {lista}")

item = lista.pop()
print(f"Elemento removido: {item}")  # Saída: 3
print(f"Lista atualizada: {lista}")
print("#########################################")
print("")

# Exemplo 27 - Limpando a lista com a função clear
print("Exemplo 27 - Limpando a lista com a função clear")

lista = [1, 2, 3]
print(f"Lista: {lista}")
lista.clear()
print(f"Lista atualizada: {lista}")  # Saída: []
print("#########################################")
print("")

# Exemplo 28 - Modificando lista por index
print("Exemplo 28 - Modificando lista por index")
lista = [1, 2, 3]
print(f"lista: {lista}")

lista[1] = 10
print(f"Lista atualizada: {lista}")  # Saída: [1, 10, 3]
print("#########################################")
print("")

# Exemplo 29 - Modificando a lista com slicing
print("Exemplo 29 - Modificando a lista com slicing")
lista = [1, 2, 3]
print(f"lista: {lista}")

lista[1:2] = [10, 20]
print(f"Lista atualizada: {lista}")  # Saída: [1, 10, 20, 3]
print("#########################################")
print("")

# Exemplo 30 - Ordenando os elementos da lista com sort
print("Exemplo 30 - Ordenando os elementos da lista com a função sort")
lista = [3, 1, 2]
print(f"lista: {lista}")

lista.sort()
print(f"Lista em ordem crescente: {lista}")  # Saída: [1, 2, 3]

#decrescente
lista.sort(reverse=True)
print(f"Lista em ordem decrescente: {lista}")  # Saída: [3, 2, 1]
print("#########################################")
print("")

# Exemplo 31 - Ordenando os elementos da lista com a função sorted
print("Exemplo 31 - Ordenando os elementos da lista com a função sorted")
lista = [3, 1, 2]
print(f"lista: {lista}")

nova_lista = sorted(lista)
print(f"Nova lista {nova_lista}")  # Saída: [1, 2, 3]
print(f"Lista original {lista}")  # Saída: [3, 1, 2]

# Exemplo 32 - Concatenando a listas com o +
print("Exemplo 32 - Concatenando a listas com o +")
lista1 = [1, 2]
print(f"Lista 01: {lista1}")

lista2 = [3, 4]
print(f"Lista 02: {lista2}")

lista3 = lista1 + lista2  # concatenaçãp
print(f"Lista concatenada: {lista3}")
print(lista3)  # Saída: [1, 2, 3, 4]
print("#########################################")
print("")

# Exemplo 33 - Multiplando listas
print("Exemplo 33 - Multiplando listas")
lista = [1, 2]
print(f"Lista: {lista}")

lista_repetida = lista * 3
print(f"Lista repetida: {lista_repetida}")  # Saída: [1, 2, 1, 2, 1, 2]
print("#########################################")
print("")

# Exemplo 34 - Iterando com a lista com o loop for
print("Exemplo 34 - Iterando com a lista com o loop for")
lista = [1, 2, 3]
print(f"Lista: {lista}")

for item in lista:
    print(item)

print("#########################################")
print("")

# Exemplo 35 - Iterando com a lista com o loop while
print("Exemplo 35 - Iterando com a lista com o loop while")
# Exemplo de lista
minha_lista = [1, 2, 3, 4, 5]

# Índice inicial
i = 0

# Loop while para iterar sobre a lista
while i < len(minha_lista):
    print(minha_lista[i])
    i += 1

# Exemplo 36 - List comprehension
print("Exemplo 36 - List comprehension")
lista = [1, 2, 3]
print(f"Lista {lista}")

nova_lista = [x * 2 for x in lista]
print(f"Nova lista: {nova_lista}")  # Saída: [2, 4, 6]
print("#########################################")
print("")

# Exemplo 37 - List comprehension com condições multiplas
print("Exemplo 37 - List comprehension com condições multiplas")
lista = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
print(lista)  # Saída: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

print("#########################################")
print("")

# Exemplo 38 - List comprehesion nested
print("Exemplo 38 - List comprehesion nested")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposta = [[linha[i] for linha in matriz] for i in range(len(matriz[0]))]

print(transposta)  # Saída: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print("#########################################")
print("")
