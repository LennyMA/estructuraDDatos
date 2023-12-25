class linkedStack:
    class Node:
        __slots__ = "_element", "_next"

        def __init__(self, elemento, siguiente) -> None:
            self._element = elemento
            self._next = siguiente

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def estaVacia(self):
        return self.size == 0

    def push(self, e):
        self.head = self.Node(e, self.head)
        self.size += 1

    def top(self):
        if self.estaVacia():
            raise Empty("Pila vacia")
        return self.head._element

    def pop(self):
        if self.estaVacia():
            raise Empty("Pila vacia")
        answer = self.head._element
        self.head = self.head._next
        self.size -= 1
        return answer

# Agregando una clase Empty para manejar excepciones
class Empty(Exception):
    pass
