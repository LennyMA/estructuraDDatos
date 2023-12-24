class CircularQueue:
    class Node:
        __slots__ = "_elemento", "_siguiente"

        def __init__(self, elemento, siguiente) -> None:
            self._elemento = elemento
            self._siguiente = siguiente

    def __init__(self) -> None:
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def estaVacia(self):
        return self._size == 0

    def first(self):
        if self.estaVacia():
            raise Empty("Cola vacia")
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.estaVacia():
            raise Empty("Cola vacia")
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.estaVacia():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next


# Agregando una clase Empty para manejar excepciones
class Empty(Exception):
    pass
