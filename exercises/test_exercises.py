from exercises_list import *
import pytest

def test_exercise_01():
    # Teste 1: Adicionar 5 a uma lista vazia
    lista = []
    resultado = exercise_01(lista)
    assert resultado == [5], f"Esperado [5], mas obteve {resultado}"

    # Teste 2: Adicionar 5 a uma lista já com elementos
    lista = [1, 2, 3]
    resultado = exercise_01(lista)
    assert resultado == [1, 2, 3, 5], f"Esperado [1, 2, 3, 5], mas obteve {resultado}"

    # Teste 3: Adicionar 5 a uma lista que já contém o número 5
    lista = [5]
    resultado = exercise_01(lista)
    assert resultado == [5, 5], f"Esperado [5, 5], mas obteve {resultado}"


def test_exercise_02():
    # Teste 1: Remover o número 3 de uma lista que contém 3
    lista = [1, 2, 3, 4]
    resultado = exercise_02(lista)
    assert resultado == [1, 2, 4], f"Esperado [1, 2, 4], mas obteve {resultado}"

    # Teste 2: Remover o número 3 de uma lista que não contém 3
    lista = [1, 2, 4]
    resultado = exercise_02(lista)
    assert resultado == [1, 2, 4], f"Esperado [1, 2, 4], mas obteve {resultado}"

    # Teste 3: Remover o número 3 de uma lista vazia
    lista = []
    resultado = exercise_02(lista)
    assert resultado == [], f"Esperado [], mas obteve {resultado}"


def test_exercise_03():
    # Teste 1: Exibir o último elemento de uma lista com várias frutas
    lista = ["maçã", "banana", "laranja"]
    resultado = exercise_03(lista)
    assert resultado == "laranja", f"Esperado 'laranja', mas obteve {resultado}"

    # Teste 2: Exibir o último elemento de uma lista com apenas um elemento
    lista = ["maçã"]
    resultado = exercise_03(lista)
    assert resultado == "maçã", f"Esperado 'maçã', mas obteve {resultado}"

    # Teste 3: Exibir o último elemento de uma lista vazia (deve retornar None)
    lista = []
    resultado = exercise_03(lista)
    assert resultado is None, f"Esperado None, mas obteve {resultado}"


def test_exercise_04():
    # Teste 1: Lista com vários números 2
    lista = [2, 3, 2, 4, 2, 5]
    resultado = exercise_04(lista)
    assert resultado == 3, f"Esperado 3, mas obteve {resultado}"

    # Teste 2: Lista sem nenhum número 2
    lista = [1, 3, 4, 5]
    resultado = exercise_04(lista)
    assert resultado == 0, f"Esperado 0, mas obteve {resultado}"

    # Teste 3: Lista com apenas um número 2
    lista = [2]
    resultado = exercise_04(lista)
    assert resultado == 1, f"Esperado 1, mas obteve {resultado}"

    # Teste 4: Lista vazia
    lista = []
    resultado = exercise_04(lista)
    assert resultado == 0, f"Esperado 0, mas obteve {resultado}"

    # Teste 5: Lista com números que não incluem o 2, mas incluem números parecidos
    lista = [12, 22, 32]
    resultado = exercise_04(lista)
    assert resultado == 0, f"Esperado 0, mas obteve {resultado}"


def test_exercise_05():
    # Teste 1: Lista com números inteiros desordenados
    lista = [5, 3, 1, 4, 2]
    resultado = exercise_05(lista)
    assert resultado == [1, 2, 3, 4, 5], f"Esperado [1, 2, 3, 4, 5], mas obteve {resultado}"

    # Teste 2: Lista já ordenada
    lista = [1, 2, 3, 4, 5]
    resultado = exercise_05(lista)
    assert resultado == [1, 2, 3, 4, 5], f"Esperado [1, 2, 3, 4, 5], mas obteve {resultado}"

    # Teste 3: Lista com números repetidos
    lista = [3, 1, 3, 2, 2]
    resultado = exercise_05(lista)
    assert resultado == [1, 2, 2, 3, 3], f"Esperado [1, 2, 2, 3, 3], mas obteve {resultado}"

    # Teste 4: Lista com um único elemento
    lista = [1]
    resultado = exercise_05(lista)
    assert resultado == [1], f"Esperado [1], mas obteve {resultado}"

    # Teste 5: Lista vazia
    lista = []
    resultado = exercise_05(lista)
    assert resultado == [], f"Esperado [], mas obteve {resultado}"


def test_exercise_06():
    # Teste 1: Lista com vários números
    lista = [1, 2, 3, 4]
    resultado = exercise_06(lista)
    assert resultado == [1, 10, 2, 3, 4], f"Esperado [1, 10, 2, 3, 4], mas obteve {resultado}"

    # Teste 2: Lista com apenas um elemento
    lista = [1]
    resultado = exercise_06(lista)
    assert resultado == [1, 10], f"Esperado [1, 10], mas obteve {resultado}"

    # Teste 3: Lista vazia (deve inserir o número 10 na segunda posição, o que é impossível, então será na primeira)
    lista = []
    resultado = exercise_06(lista)
    assert resultado == [10], f"Esperado [10], mas obteve {resultado}"

    # Teste 4: Lista com múltiplos tipos de dados
    lista = [1, "a", 3.5]
    resultado = exercise_06(lista)
    assert resultado == [1, 10, "a", 3.5], f"Esperado [1, 10, 'a', 3.5], mas obteve {resultado}"

    # Teste 5: Lista já contendo o número 10 (deve adicionar outro na segunda posição)
    lista = [10, 20, 30]
    resultado = exercise_06(lista)
    assert resultado == [10, 10, 20, 30], f"Esperado [10, 10, 20, 30], mas obteve {resultado}"


def test_add_element():
    # Caso 1: Adicionando um novo elemento
    lista = [1, 2, 3]
    resultado = add_element(lista, 4)
    assert resultado == [1, 2, 3, 4], f"Esperado [1, 2, 3, 4], mas obteve {resultado}"

    # Caso 2: Adicionando um elemento já presente na lista
    lista = [1, 2, 3]
    resultado = add_element(lista, 3)
    assert resultado == [1, 2, 3, 3], f"Esperado [1, 2, 3, 3], mas obteve {resultado}"

    # Caso 3: Adicionando um elemento em uma lista vazia
    lista = []
    resultado = add_element(lista, 10)
    assert resultado == [10], f"Esperado [10], mas obteve {resultado}"

    # Caso 4: Adicionando múltiplos elementos
    lista = [1, 2]
    resultado = add_element(lista, 3)
    resultado = add_element(resultado, 4)
    assert resultado == [1, 2, 3, 4], f"Esperado [1, 2, 3, 4], mas obteve {resultado}"


def test_remove_element():
    # Caso 1: Remover um elemento presente na lista
    lista = [1, 2, 3, 5]
    resultado = remove_element(lista, 5)
    assert resultado == [1, 2, 3], f"Esperado [1, 2, 3], mas obteve {resultado}"

    # Caso 2: Remover um elemento não presente na lista
    lista = [1, 2, 3]
    resultado = remove_element(lista, 4)
    assert resultado == [1, 2, 3], f"Esperado [1, 2, 3], mas obteve {resultado}"

    # Caso 3: Remover um elemento que aparece mais de uma vez
    lista = [1, 2, 2, 3]
    resultado = remove_element(lista, 2)
    assert resultado == [1, 2, 3], f"Esperado [1, 2, 3], mas obteve {resultado}"

    # Caso 4: Remover o único elemento da lista
    lista = [1]
    resultado = remove_element(lista, 1)
    assert resultado == [], f"Esperado [], mas obteve {resultado}"


def test_get_last_element():
    # Caso 1: Lista com múltiplos elementos
    lista = [1, 2, 3]
    resultado = get_last_element(lista)
    assert resultado == 3, f"Esperado 3, mas obteve {resultado}"

    # Caso 2: Lista com um único elemento
    lista = [10]
    resultado = get_last_element(lista)
    assert resultado == 10, f"Esperado 10, mas obteve {resultado}"

    # Caso 3: Lista vazia
    lista = []
    with pytest.raises(IndexError):
        get_last_element(lista)  # Espera-se um erro de índice


def test_count_occurrences():
    # Caso 1: Contar ocorrências de um número presente várias vezes
    lista = [1, 2, 2, 3, 2]
    resultado = count_occurrences(lista, 2)
    assert resultado == 3, f"Esperado 3, mas obteve {resultado}"

    # Caso 2: Contar ocorrências de um número que não está presente
    lista = [1, 2, 3]
    resultado = count_occurrences(lista, 4)
    assert resultado == 0, f"Esperado 0, mas obteve {resultado}"

    # Caso 3: Contar ocorrências de um número em uma lista vazia
    lista = []
    resultado = count_occurrences(lista, 2)
    assert resultado == 0, f"Esperado 0, mas obteve {resultado}"

    # Caso 4: Contar ocorrências de um número que aparece apenas uma vez
    lista = [1, 2, 3]
    resultado = count_occurrences(lista, 1)
    assert resultado == 1, f"Esperado 1, mas obteve {resultado}"


def test_sort_list():
    # Caso 1: Lista desordenada
    lista = [3, 1, 2]
    resultado = sort_list(lista)
    assert resultado == [1, 2, 3], f"Esperado [1, 2, 3], mas obteve {resultado}"

    # Caso 2: Lista já ordenada
    lista = [1, 2, 3]
    resultado = sort_list(lista)
    assert resultado == [1, 2, 3], f"Esperado [1, 2, 3], mas obteve {resultado}"

    # Caso 3: Lista com todos os elementos iguais
    lista = [2, 2, 2]
    resultado = sort_list(lista)
    assert resultado == [2, 2, 2], f"Esperado [2, 2, 2], mas obteve {resultado}"

    # Caso 4: Lista vazia
    lista = []
    resultado = sort_list(lista)
    assert resultado == [], f"Esperado [], mas obteve {resultado}"

    # Caso 5: Lista com elementos negativos
    lista = [0, -1, 2, -3]
    resultado = sort_list(lista)
    assert resultado == [-3, -1, 0, 2], f"Esperado [-3, -1, 0, 2], mas obteve {resultado}"


def test_insert_element():
    # Caso 1: Inserir no início da lista
    lista = [1, 2, 3]
    resultado = insert_element(lista, 10, 0)  # Inserir 10 na posição 0
    assert resultado == [10, 1, 2, 3], f"Esperado [10, 1, 2, 3], mas obteve {resultado}"

    # Caso 2: Inserir no meio da lista
    lista = [1, 2, 3]
    resultado = insert_element(lista, 10, 1)  # Inserir 10 na posição 1
    assert resultado == [1, 10, 2, 3], f"Esperado [1, 10, 2, 3], mas obteve {resultado}"

    # Caso 3: Inserir no final da lista
    lista = [1, 2, 3]
    resultado = insert_element(lista, 10, 3)  # Inserir 10 na posição 3
    assert resultado == [1, 2, 3, 10], f"Esperado [1, 2, 3, 10], mas obteve {resultado}"

    # Caso 4: Inserir em uma lista vazia
    lista = []
    resultado = insert_element(lista, 10, 0)  # Inserir 10 na posição 0
    assert resultado == [10], f"Esperado [10], mas obteve {resultado}"

    # Caso 5: Inserir em posição inválida (deve lançar IndexError)
    lista = [1, 2, 3]
    with pytest.raises(IndexError, match="Index out of range"):
        insert_element(lista, 10, 5)  # Inserir em uma posição inválida



def test_repeat_elements():
    # Caso 1: Repetir um elemento várias vezes
    resultado = repeat_elements(2, 3)
    assert resultado == [2, 2, 2], f"Esperado [2, 2, 2], mas obteve {resultado}"

    # Caso 2: Repetir um elemento uma vez
    resultado = repeat_elements(2, 1)
    assert resultado == [2], f"Esperado [2], mas obteve {resultado}"

    # Caso 3: Repetir elemento com contagem zero
    resultado = repeat_elements(2, 0)
    assert resultado == [], f"Esperado [], mas obteve {resultado}"

    # Caso 4: Repetir elemento com contagem negativa (deve lançar ValueError)
    with pytest.raises(ValueError, match="Count must be non-negative"):
        repeat_elements(2, -1)

    # Caso 5: Repetir um string
    resultado = repeat_elements('a', 4)
    assert resultado == ['a', 'a', 'a', 'a'], f"Esperado ['a', 'a', 'a', 'a'], mas obteve {resultado}"


def test_find_index():
    # Caso 1: Elemento presente na lista
    lista = [10, 20, 30]
    resultado = find_index(lista, 20)
    assert resultado == 1, f"Esperado 1, mas obteve {resultado}"

    # Caso 2: Elemento não presente na lista
    lista = [10, 20, 30]
    resultado = find_index(lista, 40)
    assert resultado == -1, f"Esperado -1, mas obteve {resultado}"

    # Caso 3: Elemento no início da lista
    lista = [10, 20, 30]
    resultado = find_index(lista, 10)
    assert resultado == 0, f"Esperado 0, mas obteve {resultado}"

    # Caso 4: Elemento no final da lista
    lista = [10, 20, 30]
    resultado = find_index(lista, 30)
    assert resultado == 2, f"Esperado 2, mas obteve {resultado}"

    # Caso 5: Lista vazia
    lista = []
    resultado = find_index(lista, 10)
    assert resultado == -1, f"Esperado -1, mas obteve {resultado}"

    # Caso 6: Elemento presente mais de uma vez
    lista = [10, 20, 20, 30]
    resultado = find_index(lista, 20)
    assert resultado == 1, f"Esperado 1, mas obteve {resultado}"  # Esperado o índice da primeira ocorrência

    # Caso 7: Lista com elementos de diferentes tipos
    lista = [10, "hello", 30]
    resultado = find_index(lista, "hello")
    assert resultado == 1, f"Esperado 1, mas obteve {resultado}"

    # Caso 8: Elemento é None
    lista = [None, 20, 30]
    resultado = find_index(lista, None)
    assert resultado == 0, f"Esperado 0, mas obteve {resultado}"

    # Caso 9: Elemento não é comparável (para verificar como a função lida com erros)
    lista = [10, 20, 30]
    with pytest.raises(TypeError):
        find_index(lista, [10, 20])  # Comparando com uma lista, o que deve causar um erro


def test_remove_duplicates():
    # Caso 1: Lista com duplicatas
    lista = [1, 2, 2, 3, 3]
    resultado = remove_duplicates(lista)
    assert sorted(resultado) == [1, 2, 3], f"Esperado [1, 2, 3], mas obteve {resultado}"

    # Caso 2: Lista vazia
    lista = []
    resultado = remove_duplicates(lista)
    assert resultado == [], f"Esperado [], mas obteve {resultado}"

    # Caso 3: Lista com todos os elementos únicos
    lista = [4, 5, 6]
    resultado = remove_duplicates(lista)
    assert resultado == [4, 5, 6], f"Esperado [4, 5, 6], mas obteve {resultado}"

    # Caso 4: Lista com elementos não numéricos
    lista = ['a', 'b', 'a', 'c']
    resultado = remove_duplicates(lista)
    assert resultado == ['a', 'b', 'c'], f"Esperado ['a', 'b', 'c'], mas obteve {resultado}"

    # Caso 5: Lista com diferentes tipos de dados (deve lançar TypeError se a função não for compatível)
    lista = [1, 2, '2']
    with pytest.raises(TypeError, match="Unsupported type"):
        remove_duplicates(lista)


def test_get_sublist():
    # Caso 1: Sublista dentro dos limites da lista
    lista = [1, 2, 3, 4, 5]
    resultado = get_sublist(lista, 1, 3)
    assert resultado == [2, 3, 4], f"Esperado [2, 3, 4], mas obteve {resultado}"

    # Caso 2: Índices iguais
    lista = [1, 2, 3, 4, 5]
    resultado = get_sublist(lista, 2, 2)
    assert resultado == [3], f"Esperado [3], mas obteve {resultado}"

    # Caso 3: Índice inicial maior que o final
    lista = [1, 2, 3, 4, 5]
    resultado = get_sublist(lista, 4, 1)
    assert resultado == [], f"Esperado [], mas obteve {resultado}"

    # Caso 4: Índice final fora dos limites da lista
    lista = [1, 2, 3, 4, 5]
    resultado = get_sublist(lista, 1, 10)
    assert resultado == [2, 3, 4, 5], f"Esperado [2, 3, 4, 5], mas obteve {resultado}"

    # Caso 5: Índice inicial fora dos limites da lista
    lista = [1, 2, 3, 4, 5]
    resultado = get_sublist(lista, -10, 3)
    assert resultado == [1, 2, 3], f"Esperado [1, 2, 3], mas obteve {resultado}"


def test_sum_elements():
    # Caso 1: Lista com números inteiros positivos
    lista = [1, 2, 3]
    resultado = sum_elements(lista)
    assert resultado == 6, f"Esperado 6, mas obteve {resultado}"

    # Caso 2: Lista com um único número
    lista = [10]
    resultado = sum_elements(lista)
    assert resultado == 10, f"Esperado 10, mas obteve {resultado}"

    # Caso 3: Lista vazia
    lista = []
    resultado = sum_elements(lista)
    assert resultado == 0, f"Esperado 0, mas obteve {resultado}"

    # Caso 4: Lista com números negativos
    lista = [-1, -2, -3]
    resultado = sum_elements(lista)
    assert resultado == -6, f"Esperado -6, mas obteve {resultado}"

    # Caso 5: Lista com números positivos e negativos
    lista = [1, -2, 3]
    resultado = sum_elements(lista)
    assert resultado == 2, f"Esperado 2, mas obteve {resultado}"

    # Caso 6: Lista com números flutuantes
    lista = [1.5, 2.5, 3.0]
    resultado = sum_elements(lista)
    assert resultado == 7.0, f"Esperado 7.0, mas obteve {resultado}"

    # Caso 7: Lista com misturas de inteiros e flutuantes
    lista = [1, 2.5, 3]
    resultado = sum_elements(lista)
    assert resultado == 6.5, f"Esperado 6.5, mas obteve {resultado}"

    # Caso 8: Lista com todos os elementos iguais
    lista = [7, 7, 7]
    resultado = sum_elements(lista)
    assert resultado == 21, f"Esperado 21, mas obteve {resultado}"

    # Caso 9: Lista com elementos não numéricos (deve lançar TypeError se a função não for compatível)
    lista = [1, 'a', 3]
    with pytest.raises(TypeError, match="Unsupported type"):
        sum_elements(lista)

    # Caso 10: Lista com uma combinação de tipos numéricos e strings (deve lançar TypeError se a função não for compatível)
    lista = [1, 2, '3']
    with pytest.raises(TypeError, match="Unsupported type"):
        sum_elements(lista)


def test_append_element():
    # Caso 1: Adicionar um elemento a uma lista com vários elementos
    lista = [1, 2, 3]
    resultado = append_element(lista, 4)
    assert resultado == [1, 2, 3, 4], f"Esperado [1, 2, 3, 4], mas obteve {resultado}"

    # Caso 2: Adicionar um elemento a uma lista vazia
    lista = []
    resultado = append_element(lista, 10)
    assert resultado == [10], f"Esperado [10], mas obteve {resultado}"

    # Caso 3: Adicionar um elemento a uma lista com um único elemento
    lista = [5]
    resultado = append_element(lista, 6)
    assert resultado == [5, 6], f"Esperado [5, 6], mas obteve {resultado}"

    # Caso 4: Adicionar um elemento duplicado
    lista = [1, 2, 2, 3]
    resultado = append_element(lista, 2)
    assert resultado == [1, 2, 2, 3, 2], f"Esperado [1, 2, 2, 3, 2], mas obteve {resultado}"

    # Caso 5: Adicionar um elemento negativo
    lista = [1, -2, 3]
    resultado = append_element(lista, -4)
    assert resultado == [1, -2, 3, -4], f"Esperado [1, -2, 3, -4], mas obteve {resultado}"

    # Caso 6: Adicionar um elemento flutuante
    lista = [1, 2, 3]
    resultado = append_element(lista, 2.5)
    assert resultado == [1, 2, 3, 2.5], f"Esperado [1, 2, 3, 2.5], mas obteve {resultado}"

    # Caso 7: Adicionar uma string
    lista = ['a', 'b', 'c']
    resultado = append_element(lista, 'd')
    assert resultado == ['a', 'b', 'c', 'd'], f"Esperado ['a', 'b', 'c', 'd'], mas obteve {resultado}"

    # Caso 8: Adicionar uma lista (deve adicionar a lista como um elemento)
    lista = [1, 2]
    resultado = append_element(lista, [3, 4])
    assert resultado == [1, 2, [3, 4]], f"Esperado [1, 2, [3, 4]], mas obteve {resultado}"

    # Caso 9: Adicionar um caractere especial
    lista = ['!', '@']
    resultado = append_element(lista, '#')
    assert resultado == ['!', '@', '#'], f"Esperado ['!', '@', '#'], mas obteve {resultado}"

    # Caso 10: Adicionar um tipo não suportado (deve lançar TypeError se a função não for compatível)
    lista = [1, 'a']
    with pytest.raises(TypeError, match="Unsupported type"):
        append_element(lista, {1: 'a'})


def test_count_elements():
    # Caso 1: Lista com elementos repetidos
    lista = [1, 2, 2, 3]
    resultado = count_elements(lista)
    assert resultado == 4, f"Esperado 4, mas obteve {resultado}"

    # Caso 2: Lista com um único elemento
    lista = [10]
    resultado = count_elements(lista)
    assert resultado == 1, f"Esperado 1, mas obteve {resultado}"

    # Caso 3: Lista vazia
    lista = []
    resultado = count_elements(lista)
    assert resultado == 0, f"Esperado 0, mas obteve {resultado}"

    # Caso 4: Lista com todos os elementos iguais
    lista = [5, 5, 5, 5]
    resultado = count_elements(lista)
    assert resultado == 4, f"Esperado 4, mas obteve {resultado}"

    # Caso 5: Lista com elementos negativos
    lista = [-1, -2, -2, -3]
    resultado = count_elements(lista)
    assert resultado == 4, f"Esperado 4, mas obteve {resultado}"

    # Caso 6: Lista com elementos mistos (inteiros e flutuantes)
    lista = [1, 2.5, 2.5, 3]
    resultado = count_elements(lista)
    assert resultado == 4, f"Esperado 4, mas obteve {resultado}"

    # Caso 7: Lista com strings
    lista = ['a', 'b', 'b', 'c']
    resultado = count_elements(lista)
    assert resultado == 4, f"Esperado 4, mas obteve {resultado}"

    # Caso 8: Lista com strings e números
    lista = ['x', 1, 'y', 2]
    resultado = count_elements(lista)
    assert resultado == 4, f"Esperado 4, mas obteve {resultado}"

    # Caso 9: Lista com caracteres especiais e espaços em branco
    lista = [' ', '!', '@', '@']
    resultado = count_elements(lista)
    assert resultado == 4, f"Esperado 4, mas obteve {resultado}"

    # Caso 10: Lista com tipos não suportados (deve lançar TypeError se count_elements não for compatível)
    lista = [1, 'a', [1, 2]]
    with pytest.raises(TypeError, match="Unsupported type"):
        count_elements(lista)


def test_remove_last_element():
    # Caso 1: Lista com vários elementos
    lista = [1, 2, 3]
    resultado = remove_last_element(lista)
    assert resultado == 3, f"Esperado 3, mas obteve {resultado}"
    assert lista == [1, 2], f"Esperado [1, 2], mas obteve {lista}"

    # Caso 2: Lista com um único elemento
    lista = [10]
    resultado = remove_last_element(lista)
    assert resultado == 10, f"Esperado 10, mas obteve {resultado}"
    assert lista == [], f"Esperado [], mas obteve {lista}"

    # Caso 3: Lista vazia (deve lançar IndexError)
    lista = []
    with pytest.raises(IndexError, match="pop from empty list"):
        remove_last_element(lista)

    # Caso 4: Lista com elementos duplicados
    lista = [5, 5, 5]
    resultado = remove_last_element(lista)
    assert resultado == 5, f"Esperado 5, mas obteve {resultado}"
    assert lista == [5, 5], f"Esperado [5, 5], mas obteve {lista}"

    # Caso 5: Lista com elementos negativos
    lista = [-1, -2, -3]
    resultado = remove_last_element(lista)
    assert resultado == -3, f"Esperado -3, mas obteve {resultado}"
    assert lista == [-1, -2], f"Esperado [-1, -2], mas obteve {lista}"

    # Caso 6: Lista com elementos mistos (inteiros e flutuantes)
    lista = [1, 2.5, 3]
    resultado = remove_last_element(lista)
    assert resultado == 3, f"Esperado 3, mas obteve {resultado}"
    assert lista == [1, 2.5], f"Esperado [1, 2.5], mas obteve {lista}"

    # Caso 7: Lista com strings
    lista = ['a', 'b', 'c']
    resultado = remove_last_element(lista)
    assert resultado == 'c', f"Esperado 'c', mas obteve {resultado}"
    assert lista == ['a', 'b'], f"Esperado ['a', 'b'], mas obteve {lista}"

    # Caso 8: Lista com strings e números
    lista = ['x', 1, 'y', 2]
    resultado = remove_last_element(lista)
    assert resultado == 2, f"Esperado 2, mas obteve {resultado}"
    assert lista == ['x', 1, 'y'], f"Esperado ['x', 1, 'y'], mas obteve {lista}"

    # Caso 9: Lista com espaços em branco e caracteres especiais
    lista = [' ', '!', '@']
    resultado = remove_last_element(lista)
    assert resultado == '@', f"Esperado '@', mas obteve {resultado}"
    assert lista == [' ', '!'], f"Esperado [' ', '!'], mas obteve {lista}"

    # Caso 10: Lista com elementos não suportados (deve lançar TypeError)
    lista = [1, 'a', [1, 2]]
    with pytest.raises(TypeError, match="Unsupported type"):
        remove_last_element(lista)


def test_reverse_list():
    # Caso 1: Lista com elementos inteiros
    lista = [1, 2, 3]
    resultado = reverse_list(lista)
    assert resultado == [3, 2, 1], f"Esperado [3, 2, 1], mas obteve {resultado}"

    # Caso 2: Lista com apenas um elemento
    lista = [1]
    resultado = reverse_list(lista)
    assert resultado == [1], f"Esperado [1], mas obteve {resultado}"

    # Caso 3: Lista vazia
    lista = []
    resultado = reverse_list(lista)
    assert resultado == [], f"Esperado [], mas obteve {resultado}"

    # Caso 4: Lista com elementos duplicados
    lista = [1, 2, 2, 3]
    resultado = reverse_list(lista)
    assert resultado == [3, 2, 2, 1], f"Esperado [3, 2, 2, 1], mas obteve {resultado}"

    # Caso 5: Lista com elementos negativos
    lista = [-1, -2, -3]
    resultado = reverse_list(lista)
    assert resultado == [-3, -2, -1], f"Esperado [-3, -2, -1], mas obteve {resultado}"

    # Caso 6: Lista com elementos mistos (inteiros e flutuantes)
    lista = [1, 2.5, 3]
    resultado = reverse_list(lista)
    assert resultado == [3, 2.5, 1], f"Esperado [3, 2.5, 1], mas obteve {resultado}"

    # Caso 7: Lista com elementos de diferentes tipos (deve lançar TypeError)
    lista = [1, 'a', 3]
    with pytest.raises(TypeError, match="Unsupported type for reverse"):
        reverse_list(lista)

    # Caso 8: Lista com strings
    lista = ['a', 'b', 'c']
    resultado = reverse_list(lista)
    assert resultado == ['c', 'b', 'a'], f"Esperado ['c', 'b', 'a'], mas obteve {resultado}"

    # Caso 9: Lista com strings e números
    lista = ['a', 1, 'b', 2]
    resultado = reverse_list(lista)
    assert resultado == [2, 'b', 1, 'a'], f"Esperado [2, 'b', 1, 'a'], mas obteve {resultado}"

    # Caso 10: Lista com espaços em branco e caracteres especiais
    lista = [' ', '!', '@']
    resultado = reverse_list(lista)
    assert resultado == ['@', '!', ' '], f"Esperado ['@', '!', ' '], mas obteve {resultado}"


def test_insert_sorted():
    # Caso 1: Lista já ordenada e inserção no meio
    lista = [1, 3, 4]
    resultado = insert_sorted(lista, 2)
    assert resultado == [1, 2, 3, 4], f"Esperado [1, 2, 3, 4], mas obteve {resultado}"

    # Caso 2: Lista com apenas um elemento e inserção menor que o elemento existente
    lista = [5]
    resultado = insert_sorted(lista, 3)
    assert resultado == [3, 5], f"Esperado [3, 5], mas obteve {resultado}"

    # Caso 3: Lista com apenas um elemento e inserção maior que o elemento existente
    lista = [1]
    resultado = insert_sorted(lista, 2)
    assert resultado == [1, 2], f"Esperado [1, 2], mas obteve {resultado}"

    # Caso 4: Lista vazia e inserção de um elemento
    lista = []
    resultado = insert_sorted(lista, 10)
    assert resultado == [10], f"Esperado [10], mas obteve {resultado}"

    # Caso 5: Lista com todos os elementos iguais e inserção de um elemento igual
    lista = [2, 2, 2]
    resultado = insert_sorted(lista, 2)
    assert resultado == [2, 2, 2, 2], f"Esperado [2, 2, 2, 2], mas obteve {resultado}"

    # Caso 6: Lista com elementos negativos e inserção de um número negativo
    lista = [-5, -3, -1]
    resultado = insert_sorted(lista, -4)
    assert resultado == [-5, -4, -3, -1], f"Esperado [-5, -4, -3, -1], mas obteve {resultado}"

    # Caso 7: Lista com elementos mistos (negativos e positivos) e inserção de um número positivo
    lista = [-5, 0, 5]
    resultado = insert_sorted(lista, 3)
    assert resultado == [-5, 0, 3, 5], f"Esperado [-5, 0, 3, 5], mas obteve {resultado}"

    # Caso 8: Inserção de um número muito pequeno em uma lista com números grandes
    lista = [10, 20, 30]
    resultado = insert_sorted(lista, 1)
    assert resultado == [1, 10, 20, 30], f"Esperado [1, 10, 20, 30], mas obteve {resultado}"

    # Caso 9: Inserção de um número muito grande em uma lista com números pequenos
    lista = [1, 2, 3]
    resultado = insert_sorted(lista, 1000)
    assert resultado == [1, 2, 3, 1000], f"Esperado [1, 2, 3, 1000], mas obteve {resultado}"

    # Caso 10: Lista com elementos não numéricos (deve lançar TypeError)
    lista = ['a', 'c', 'e']
    with pytest.raises(TypeError, match="'<=' not supported between instances of 'str' and 'int'"):
        insert_sorted(lista, 'b')


def test_multiply_elements():
    # Caso 1: Lista com números inteiros positivos e fator de multiplicação 2
    lista = [1, 2, 3]
    resultado = multiply_elements(lista, 2)
    assert resultado == [2, 4, 6], f"Esperado [2, 4, 6], mas obteve {resultado}"

    # Caso 2: Lista com números negativos e fator de multiplicação 2
    lista = [-1, -2, -3]
    resultado = multiply_elements(lista, 2)
    assert resultado == [-2, -4, -6], f"Esperado [-2, -4, -6], mas obteve {resultado}"

    # Caso 3: Lista com mistura de números positivos e negativos e fator de multiplicação 3
    lista = [1, -2, 3]
    resultado = multiply_elements(lista, 3)
    assert resultado == [3, -6, 9], f"Esperado [3, -6, 9], mas obteve {resultado}"

    # Caso 4: Lista vazia e fator de multiplicação 5
    lista = []
    resultado = multiply_elements(lista, 5)
    assert resultado == [], f"Esperado [], mas obteve {resultado}"

    # Caso 5: Lista com um único elemento e fator de multiplicação 0
    lista = [7]
    resultado = multiply_elements(lista, 0)
    assert resultado == [0], f"Esperado [0], mas obteve {resultado}"

    # Caso 6: Lista com números flutuantes e fator de multiplicação 2
    lista = [1.5, 2.5, 3.5]
    resultado = multiply_elements(lista, 2)
    assert resultado == [3.0, 5.0, 7.0], f"Esperado [3.0, 5.0, 7.0], mas obteve {resultado}"

    # Caso 7: Lista com mistura de inteiros e flutuantes e fator de multiplicação 1
    lista = [1, 2.5, 3]
    resultado = multiply_elements(lista, 1)
    assert resultado == [1, 2.5, 3], f"Esperado [1, 2.5, 3], mas obteve {resultado}"

    # Caso 8: Lista com números inteiros positivos e fator de multiplicação -1
    lista = [1, 2, 3]
    resultado = multiply_elements(lista, -1)
    assert resultado == [-1, -2, -3], f"Esperado [-1, -2, -3], mas obteve {resultado}"

    # Caso 9: Lista com elementos mistos e fator de multiplicação não numérico (deve lançar TypeError)
    lista = [1, 'a', 3]
    with pytest.raises(TypeError, match="unsupported operand type(s) for *: 'int' and 'str'"):
        multiply_elements(lista, 2)

    # Caso 10: Lista com todos os elementos iguais e fator de multiplicação 10
    lista = [5, 5, 5]
    resultado = multiply_elements(lista, 10)
    assert resultado == [50, 50, 50], f"Esperado [50, 50, 50], mas obteve {resultado}"


def test_max_element():
    # Caso 1: Lista com números inteiros positivos
    lista = [1, 2, 3]
    resultado = max_element(lista)
    assert resultado == 3, f"Esperado 3, mas obteve {resultado}"

    # Caso 2: Lista com números inteiros negativos
    lista = [-1, -2, -3]
    resultado = max_element(lista)
    assert resultado == -1, f"Esperado -1, mas obteve {resultado}"

    # Caso 3: Lista com mistura de números positivos e negativos
    lista = [-1, 0, 1]
    resultado = max_element(lista)
    assert resultado == 1, f"Esperado 1, mas obteve {resultado}"

    # Caso 4: Lista com apenas um elemento
    lista = [5]
    resultado = max_element(lista)
    assert resultado == 5, f"Esperado 5, mas obteve {resultado}"

    # Caso 5: Lista vazia (deve lançar um erro)
    lista = []
    with pytest.raises(ValueError, match="max() arg is an empty sequence"):
        max_element(lista)

    # Caso 6: Lista com números flutuantes positivos
    lista = [1.1, 2.2, 3.3]
    resultado = max_element(lista)
    assert resultado == 3.3, f"Esperado 3.3, mas obteve {resultado}"

    # Caso 7: Lista com números flutuantes negativos
    lista = [-1.1, -2.2, -3.3]
    resultado = max_element(lista)
    assert resultado == -1.1, f"Esperado -1.1, mas obteve {resultado}"

    # Caso 8: Lista com mistura de inteiros e flutuantes positivos
    lista = [1, 2.5, 3]
    resultado = max_element(lista)
    assert resultado == 3, f"Esperado 3, mas obteve {resultado}"

    # Caso 9: Lista com tipos mistos (não suportados pelo max())
    lista = [1, "2", 3]
    with pytest.raises(TypeError, match="unorderable types: str() > int()"):
        max_element(lista)

    # Caso 10: Lista com todos os elementos iguais
    lista = [7, 7, 7]
    resultado = max_element(lista)
    assert resultado == 7, f"Esperado 7, mas obteve {resultado}"


def test_all_positive():
    # Caso 1: Todos os elementos são positivos
    lista = [1, 2, 3]
    assert all_positive(lista) is True, f"Esperado True, mas obteve {all_positive(lista)}"

    # Caso 2: Lista contém um elemento negativo
    lista = [1, -2, 3]
    assert all_positive(lista) is False, f"Esperado False, mas obteve {all_positive(lista)}"

    # Caso 3: Lista com todos os elementos negativos
    lista = [-1, -2, -3]
    assert all_positive(lista) is False, f"Esperado False, mas obteve {all_positive(lista)}"

    # Caso 4: Lista contendo zero
    lista = [0, 1, 2]
    assert all_positive(lista) is False, f"Esperado False, mas obteve {all_positive(lista)}"

    # Caso 5: Lista vazia
    lista = []
    assert all_positive(lista) is True, f"Esperado True, mas obteve {all_positive(lista)}"  # Lista vazia deve ser considerada como True para todos positivos

    # Caso 6: Lista com apenas um elemento positivo
    lista = [5]
    assert all_positive(lista) is True, f"Esperado True, mas obteve {all_positive(lista)}"

    # Caso 7: Lista com apenas um elemento negativo
    lista = [-5]
    assert all_positive(lista) is False, f"Esperado False, mas obteve {all_positive(lista)}"

    # Caso 8: Lista com elementos flutuantes positivos
    lista = [1.5, 2.3, 3.4]
    assert all_positive(lista) is True, f"Esperado True, mas obteve {all_positive(lista)}"

    # Caso 9: Lista com elementos flutuantes negativos
    lista = [1.5, -2.3, 3.4]
    assert all_positive(lista) is False, f"Esperado False, mas obteve {all_positive(lista)}"

    # Caso 10: Lista com elementos mistos (inteiros e flutuantes, todos positivos)
    lista = [1, 2.5, 3]
    assert all_positive(lista) is True, f"Esperado True, mas obteve {all_positive(lista)}"


def test_add_matrices_2d():
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    resultado = add_matrices_2d(mat1, mat2)
    assert resultado == [[6, 8], [10, 12]], f"Esperado [[6, 8], [10, 12]], mas obteve {resultado}"

    # Testando com matrizes de diferentes dimensões
    mat1 = [[1, 2]]
    mat2 = [[3, 4]]
    resultado = add_matrices_2d(mat1, mat2)
    assert resultado == [[4, 6]], f"Esperado [[4, 6]], mas obteve {resultado}"

    # Testando com matrizes que contêm zero
    mat1 = [[0, 0], [0, 0]]
    mat2 = [[1, 2], [3, 4]]
    resultado = add_matrices_2d(mat1, mat2)
    assert resultado == [[1, 2], [3, 4]], f"Esperado [[1, 2], [3, 4]], mas obteve {resultado}"


def test_transpose_matrix_2d():
    matrix = [[1, 2, 3], [4, 5, 6]]
    resultado = transpose_matrix_2d(matrix)
    assert resultado == [[1, 4], [2, 5], [3, 6]], f"Esperado [[1, 4], [2, 5], [3, 6]], mas obteve {resultado}"

    # Testando com uma matriz quadrada
    matrix = [[1, 2], [3, 4]]
    resultado = transpose_matrix_2d(matrix)
    assert resultado == [[1, 3], [2, 4]], f"Esperado [[1, 3], [2, 4]], mas obteve {resultado}"

    # Testando com uma matriz de uma única linha
    matrix = [[1, 2, 3]]
    resultado = transpose_matrix_2d(matrix)
    assert resultado == [[1], [2], [3]], f"Esperado [[1], [2], [3]], mas obteve {resultado}"


def test_max_value_2d():
    matrix = [[1, 2, 3], [4, 5, 6]]
    resultado = max_value_2d(matrix)
    assert resultado == 6, f"Esperado 6, mas obteve {resultado}"

    # Testando com uma matriz com todos os valores iguais
    matrix = [[7, 7, 7], [7, 7, 7]]
    resultado = max_value_2d(matrix)
    assert resultado == 7, f"Esperado 7, mas obteve {resultado}"

    # Testando com uma matriz contendo valores negativos
    matrix = [[-1, -2, -3], [-4, -5, -6]]
    resultado = max_value_2d(matrix)
    assert resultado == -1, f"Esperado -1, mas obteve {resultado}"

    # Testando com uma matriz contendo apenas zeros
    matrix = [[0, 0], [0, 0]]
    resultado = max_value_2d(matrix)
    assert resultado == 0, f"Esperado 0, mas obteve {resultado}"


def test_add_matrices_3d():
    mat1 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    mat2 = [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]
    resultado = add_matrices_3d(mat1, mat2)
    assert resultado == [[[10, 12], [14, 16]], [[18, 20], [22,
                                                           24]]], f"Esperado [[[10, 12], [14, 16]], [[18, 20], [22, 24]]], mas obteve {resultado}"

    # Testando com matrizes 3D onde os valores são zeros
    mat1 = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
    mat2 = [[[1, 1], [1, 1]], [[1, 1], [1, 1]]]
    resultado = add_matrices_3d(mat1, mat2)
    assert resultado == [[[1, 1], [1, 1]],
                         [[1, 1], [1, 1]]], f"Esperado [[[1, 1], [1, 1]], [[1, 1], [1, 1]]], mas obteve {resultado}"

    # Testando com matrizes 3D com diferentes dimensões
    mat1 = [[[1, 2]], [[3, 4]]]
    mat2 = [[[5, 6]], [[7, 8]]]
    resultado = add_matrices_3d(mat1, mat2)
    assert resultado == [[[6, 8]], [[10, 12]]], f"Esperado [[[6, 8]], [[10, 12]]], mas obteve {resultado}"


def test_max_2d_layer_3d():
    matrix = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    resultado = max_2d_layer_3d(matrix)
    assert resultado == 8, f"Esperado 8, mas obteve {resultado}"

    # Testando com todas as camadas contendo o mesmo valor máximo
    matrix = [[[5, 5], [5, 5]], [[5, 5], [5, 5]]]
    resultado = max_2d_layer_3d(matrix)
    assert resultado == 5, f"Esperado 5, mas obteve {resultado}"

    # Testando com valores negativos
    matrix = [[[-1, -2], [-3, -4]], [[-5, -6], [-7, -8]]]
    resultado = max_2d_layer_3d(matrix)
    assert resultado == -1, f"Esperado -1, mas obteve {resultado}"


def test_transpose_matrix_3d():
    matrix = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    resultado = transpose_matrix_3d(matrix)
    assert resultado == [[[1, 5], [3, 7]],
                         [[2, 6], [4, 8]]], f"Esperado [[[1, 5], [3, 7]], [[2, 6], [4, 8]]], mas obteve {resultado}"

    # Testando com matrizes 3D onde cada camada tem uma única linha
    matrix = [[[1, 2, 3]], [[4, 5, 6]]]
    resultado = transpose_matrix_3d(matrix)
    assert resultado == [[[1, 4]], [[2, 5]],
                         [[3, 6]]], f"Esperado [[[1, 4]], [[2, 5]], [[3, 6]]], mas obteve {resultado}"

    # Testando com uma matriz 3D com todas as camadas sendo iguais
    matrix = [[[1, 1], [1, 1]], [[1, 1], [1, 1]]]
    resultado = transpose_matrix_3d(matrix)
    assert resultado == [[[1, 1], [1, 1]],
                         [[1, 1], [1, 1]]], f"Esperado [[[1, 1], [1, 1]], [[1, 1], [1, 1]]], mas obteve {resultado}"


def test_filter_even_numbers():
    # Testa uma lista normal
    assert filter_even_numbers([1, 2, 3, 4, 5]) == [2, 4], "Esperado [2, 4]"

    # Testa uma lista com apenas números ímpares
    assert filter_even_numbers([1, 3, 5, 7]) == [], "Esperado []"

    # Testa uma lista com apenas números pares
    assert filter_even_numbers([2, 4, 6, 8]) == [2, 4, 6, 8], "Esperado [2, 4, 6, 8]"


def test_square_numbers():
    # Testa uma lista normal
    assert square_numbers([1, 2, 3]) == [1, 4, 9], "Esperado [1, 4, 9]"

    # Testa uma lista com apenas um número
    assert square_numbers([5]) == [25], "Esperado [25]"

    # Testa uma lista com números negativos
    assert square_numbers([-1, -2, -3]) == [1, 4, 9], "Esperado [1, 4, 9]"


def test_combine_lists():
    # Testa duas listas de mesmo comprimento
    assert combine_lists([1, 2, 3], [4, 5, 6]) == [5, 7, 9], "Esperado [5, 7, 9]"

    # Testa listas de diferentes comprimentos
    assert combine_lists([1, 2], [3, 4, 5]) == [4, 6], "Esperado [4, 6]"

    # Testa com listas vazias
    assert combine_lists([], []) == [], "Esperado []"


def test_flatten_list():
    # Testa uma lista de listas normal
    assert flatten_list([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5], "Esperado [1, 2, 3, 4, 5]"

    # Testa uma lista de listas vazias
    assert flatten_list([[], [], []]) == [], "Esperado []"

    # Testa uma lista de listas com uma sublista vazia
    assert flatten_list([[], [1, 2], [3]]) == [1, 2, 3], "Esperado [1, 2, 3]"


def test_extract_names():
    # Testa uma lista de dicionários com alguns dicionários sem 'name'
    people = [{'name': 'Alice'}, {'name': 'Bob'}, {'age': 30}]
    assert extract_names(people) == ['Alice', 'Bob'], "Esperado ['Alice', 'Bob']"

    # Testa uma lista de dicionários sem 'name'
    people = [{'age': 25}, {'age': 30}]
    assert extract_names(people) == [], "Esperado []"

    # Testa uma lista de dicionários com 'name' vazio
    people = [{'name': ''}, {'name': 'Bob'}, {'name': 'Alice'}]
    assert extract_names(people) == ['', 'Bob', 'Alice'], "Esperado ['', 'Bob', 'Alice']"


def test_get_odd_indices():
    # Testa uma lista normal
    assert get_odd_indices([10, 20, 30, 40, 50]) == [20, 40], "Esperado [20, 40]"

    # Testa uma lista com apenas um elemento
    assert get_odd_indices([10]) == [], "Esperado []"

    # Testa uma lista com apenas elementos em índices ímpares
    assert get_odd_indices([10, 20, 30, 40, 50]) == [20, 40], "Esperado [20, 40]"


def test_filter_even_numbers_empty():
    # Testa uma lista vazia
    assert filter_even_numbers([]) == [], "Esperado []"


def test_square_numbers_empty():
    # Testa uma lista vazia
    assert square_numbers([]) == [], "Esperado []"


def test_combine_lists_different_lengths():
    # Testa listas de comprimentos diferentes
    assert combine_lists([1, 2], [3, 4, 5]) == [4, 6], "Esperado [4, 6]"


def test_flatten_list_empty_sublist():
    # Testa lista de listas com sublistas vazias
    assert flatten_list([[], [1, 2], []]) == [1, 2], "Esperado [1, 2]"


def test_extract_names_no_names():
    # Testa uma lista de dicionários sem 'name'
    people = [{'age': 25}, {'age': 30}]
    assert extract_names(people) == [], "Esperado []"


def test_get_odd_indices_empty():
    # Testa uma lista vazia
    assert get_odd_indices([]) == [], "Esperado []"
