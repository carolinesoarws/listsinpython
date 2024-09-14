class Node:

    def __init__(self, data=None):
        self.data = data  # Dado armazenado no nó
        self.next = None  # Referência para o próximo nó


class LinkedList:
    def __init__(self):
        self.head = None  # Inicialmente, a lista está vazia

    # Método para adicionar um nó ao final da lista
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Método para imprimir a lista
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
            print(None)

    # Método para inserir um nó no início da lista
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Método para remover um nó pelo valor
    def delete(self, key):
        current = self.head

        # Se o nó a ser removido é o nó cabeça
        if current is not None:
            if current.data == key:
                self.head = current.next
            current = None
            return current

        # Procurar o nó a ser removido, mantendo a referência ao nó anterior
        prev = None
        while current is not None:
            if current.data == key:
                break
            prev = current
            current = current.next

        # Se o nó não foi encontrado
        if current is None:
            return

        # Desvincular o nó da lista
        prev.next = current.next
        current = None
