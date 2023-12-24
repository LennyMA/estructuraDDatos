class DoubleLinkedBase:
    class Node:
        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev, next) -> None:
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self) -> None:
        self._header = self.Node(None, None, None)  # Corregido aquí
        self._trailer = self.Node(None, None, None)  # Corregido aquí
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def length(self):
        return self._size

    def estaVacia(self):
        return self._size == 0

    def insertarEnMedio(self, e, predecessor, successor):
        newest = self.Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def deleteNode(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next
        return element
