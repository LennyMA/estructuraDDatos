import ctypes


class ArregloDinamico:
    def __init__(self) -> None:
        self.n = 0
        self.capacidad = 1
        self.A = self._crearArreglo_(self.capacidad)

    def __len__(self):
        return self.n

    def _obtenerElemento_(self, i):
        if not 0 <= i < self.n:
            raise IndexError("Indice no valido")
        return self.A[i]

    def append(self, ob):
        if self.n == self.capacidad:
            self._redimensiona_(2 * self.capacidad)
        self.A[self.n] = ob
        self.n += 1

    def _redimensiona_(self, c):
        B = self._crearArreglo_(c)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacidad = c

    def _crearArreglo_(self, c):
        return (c * ctypes.py_object)()


c = ArregloDinamico()
print(c.__len__())
c.append(5)
print(c.__len__())
print(c._obtenerElemento_(0))
