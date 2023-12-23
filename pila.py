class Pila:
    def __init__(self) -> None:
        self.elementos = []

    def estaVacia(self):
        return self.elementos == []

    def push(self, item):
        self.elementos.append(item)

    def pop(self):
        return self.elementos.pop()

    def verUltimoElementoIngresado(self):
        return self.elementos[len(self.elementos) - 1]

    def dimension(self):
        return len(self.elementos)


p = Pila()
print(p.estaVacia())
p.push(4)
p.push("perro")
p.pop()
print(p.verUltimoElementoIngresado())
print(p.dimension())

