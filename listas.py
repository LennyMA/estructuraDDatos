lista = [12, False, "string", [1, 2, 3], True, 0.33]
valor = lista[2]
valor2 = lista[3]
print(valor)
print(valor2)
valor3 = lista[3][2]
print(valor3)
lista[3][2] = 4
print(lista[3])
valor4 = lista[0:3]
valor5 = lista[0:5:2]
print(valor4)
print(valor5)
tupla = ("string",)
print(type(tupla))
print(tupla)
tupla = (12, False, "string", [1, 2, 3])
valor6 = tupla[::3]
print(type(tupla))
print(valor6)
