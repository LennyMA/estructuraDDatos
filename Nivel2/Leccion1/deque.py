class Deque:
    def __init__(self) -> None:
        self.elementos = []

    def listaVacia(self):
        return self.elementos == []

    def agregarAlFrente(self, item):
        self.elementos.append(item)

    def agregarAlFinal(self, item):
        self.elementos.insert(0, item)

    def eliminarAlFrente(self):
        return self.elementos.pop()

    def eliminarAlFinal(self):
        return self.elementos.pop(0)

    def verFrente(self):
        return self.elementos[len(self.elementos) - 1]

    def verFinal(self):
        return self.elementos[0]

    def dimension(self):
        return len(self.elementos)


d = Deque()
d.agregarAlFrente(1)
d.agregarAlFrente(2)
d.agregarAlFrente(3)
d.agregarAlFinal(4)
d.agregarAlFinal(5)

print("\nAgregando:")
print("Dimension: ", d.dimension())
print("Valor en frente:", d.verFrente())
print("Valor al final:", d.verFinal())

d.eliminarAlFrente()
d.eliminarAlFinal()

print("\nEliminando:")
print("Dimension: ", d.dimension())
print("Valor en frente:", d.verFrente())
print("Valor al final:", d.verFinal())
