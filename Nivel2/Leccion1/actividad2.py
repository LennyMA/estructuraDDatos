# I. Usa arreglos (normal y dinámico), listas y tuplas para:

# a. Crear una agenda de datos personales

agenda = [
    {
        "nombre": "Juan",
        "edad": 25,
        "celular": "0987654321",
        "correo": "juan@example.com",
    },
    {
        "nombre": "Maria",
        "edad": 27,
        "celular": "0912345678",
        "correo": "maria@example.com",
    },
]
contacto1 = agenda[0]
contacto2 = agenda[1]
print(
    "Contactos:\n",
    contacto1["nombre"],
    ":",
    contacto1["celular"],
    "\n",
    contacto2["nombre"],
    ":",
    contacto2["celular"],
)
tupla = (
    {
        "nombre": "Juan",
        "correo": "juan@example.com",
    },
    {
        "nombre": "Maria",
        "correo": "maria@example.com",
    },
)

print(tupla)

# b. Crear una lista de productos
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
c.append("Leche")
c.append("Huevos")
c.append("Cereal")
c.append("Pan")
c.append("Agua")
c.append("Queso")
c.append("Cafe")
print(c.__len__())

for i in range(len(c)):
    print(c._obtenerElemento_(i))

# II. Usa arreglos para construir una clase de pilas, otra de colas normal, y
# otra con deque, después, con base en la información del inciso I:


# a. Utiliza los métodos para crear un almacén de productos
# b. Edita el contenido usando los métodos para reacomodar los
# elemento
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


print("\nPila de productos:")
p = Pila()
print("La pila esta vaica?", p.estaVacia())
p.push("Leche")
p.push("Pan")
p.push("Huevos")
p.push("Cafe")
p.pop()
print(p.verUltimoElementoIngresado())
print(p.dimension())

from cifradoCesar import CifradoCesar
cifrado = CifradoCesar(10)
clave = "claveSegura123$%"
codificado = cifrado.encriptar(clave)
print("Secreto:", codificado)
respuesta = cifrado.desencriptar(codificado)
print("Clave:", respuesta)