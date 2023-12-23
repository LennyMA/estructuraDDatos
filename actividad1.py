# Práctica lo que aprendiste

# I. Crea una clase para representar el perfil de un cliente, los productos
# y un carrito de compra. Identifica lo siguiente:

# a. Nombre
# b. Atributos
# c. Funciones y métodos

# II. Usa las clases previas para realizar lo siguiente: 
 
# a. Obtener el nombre de los clientes 
# b. Obtener el precio de los productos 
# c. Obtener el valor de las compras


class Cliente:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def __str__(self) -> str:
        return f"Cliente: {self.nombre + " " + self.apellido}\nCorreo: {self.correo}"


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f"Producto: {self.nombre}, Precio: {self.precio}"


class Carrito:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def calcularTotal(self):
        return sum(producto.precio for producto in self.productos)

    def __str__(self) -> str:
        productosCarrito = "\n".join(str(producto) for producto in self.productos)
        return f"{self.cliente}\nProductos en el carrito:\n{productosCarrito}\nTotal: ${self.calcularTotal()}"


c1 = Cliente("Lenin", "Moreno", "lenin@gmail.com")
p1 = Producto("Laptop Asus ROG STRIG", 1000)
p2 = Producto("Teclado mecanico", 120)
p3 = Producto("Mouse havit", 30)

carritoC1 = Carrito(c1)
carritoC1.agregarProducto(p1)
carritoC1.agregarProducto(p2)
carritoC1.agregarProducto(p3)

print(carritoC1)
