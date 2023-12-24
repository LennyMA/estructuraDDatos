class Cola:
    def __init__(self) -> None:
        self.elementos = []

    def estaVacia(self):
        return self.elementos == []

    def encolar(self, item):
        self.elementos.insert(0, item)

    def desencolar(self):
        return self.elementos.pop()

    def verFrente(self):
        return self.elementos[len(self.elementos) - 1]

    def verRetaguardia(self):
        return self.elementos[0]

    def dimension(self):
        return len(self.elementos)


c = Cola()
c.encolar("Gato")
c.encolar("Perro")
c.encolar(10)
print(c.dimension())
print(c.verFrente())
print(c.verRetaguardia())
c.desencolar()
print(c.verFrente())
print(c.verRetaguardia())
