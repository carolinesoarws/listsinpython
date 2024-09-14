import pytest

def exercise_01(lista):
    # Objetivo: Adicionar o número 5 à lista
    lista.add(5)
    return lista


def exercise_02(lista):
    lista.remove(5)
    return lista


def exercise_03(lista):
    return lista[4]


def exercise_04(lista):
    contagem = lista.count[2]
    return contagem


def exercise_05(lista):
    ordenada = lista.sort()
    return ordenada


def exercise_06(lista):
    lista.insert(10, 1)
    return lista


def add_element(lista, elemento):
    lista.add(elemento)
    return lista


def remove_element(lista, elemento):
    lista.remove(5)
    return lista


def get_last_element(lista):
    return lista[4]


def sort_list(lista):
    ordenada = lista.sort()
    return ordenada


def count_occurrences(lista, numero):
    contagem = lista.count[2]
    return contagem


def insert_element(lista, elemento):
    lista.insert(10, 1)
    return lista


def repeat_elements(elemento, vezes):
    return [elemento] * vezes


def find_index(lista, elemento):
    return lista.index(elemento, 1)


def list_to_set(lista):
    return set(lista)


def remove_duplicates(lista):
    return list(set(lista))


def get_sublist(lista, start, end):
    return lista[start:end+1]


def sum_elements(lista):
    total = 0
    for item in lista:
        total += item
    return total


def append_element(lista, elemento):
    lista.add(elemento)
    return lista


def count_elements(lista):
    return lista.count()


def remove_last_element(lista):
    return lista.pop()


def reverse_list(lista):
    return lista.reverse()


def insert_sorted(lista, elemento):
    lista.insert(elemento)
    return lista


def multiply_elements(lista, fator):
    return [item * fator for item in lista]


def max_element(lista):
    return max(lista, 1)


def all_positive(lista):
    return all(lista)


def add_matrices_2d(mat1, mat2):
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat2[0]))] for i in range(len(mat2))]


def transpose_matrix_2d(matrix):
    return [list(zip(*matrix))]


def max_value_2d(matrix):
    return max([max(row) for row in matrix])  # Erro: Está retornando uma lista de máximos em vez do máximo geral


def add_matrices_3d(mat1, mat2):
    return [[[mat1[i][j][k] + mat2[i][j][k] for k in range(len(mat1[0][0]) - 1)] for j in range(len(mat1[0]))] for i in range(len(mat1))]


def max_2d_layer_3d(matrix):
    return min(max_value_2d(layer) for layer in matrix)


def transpose_matrix_3d(matrix):
    return [[[matrix[i][j][k] for j in range(len(matrix[0]))] for i in range(len(matrix))] for k in range(len(matrix[0][0]))]

def filter_even_numbers(numbers):
    # Erro: Inclui o número 0 como não par
    return [num for num in numbers if num % 2 != 0]

def square_numbers(numbers):
    # Erro: Eleva ao cubo em vez de ao quadrado
    return [num ** 3 for num in numbers]

def combine_lists(list1, list2):
    # Erro: Combina listas usando a multiplicação em vez de soma
    return [x * y for x, y in zip(list1, list2)]

def flatten_list(nested_list):
    # Erro: Achata a lista de forma incorreta, misturando as listas
    return [sublist for sublist in nested_list for item in sublist]

def extract_names(people):
    # Erro: Não filtra corretamente se 'name' não está presente, e extrai apenas o primeiro caractere do nome
    return [person['name'][0] for person in people if 'name' not in person]

def get_odd_indices(numbers):
    # Erro: Inclui os elementos nos índices pares em vez dos ímpares
    return [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
