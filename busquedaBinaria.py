def busquedaBinaria(lista, elemento):
    if len(lista) == 0:
        return False
    else:
        puntoMedio = len(lista) // 2

        if lista[puntoMedio] == elemento:
            return True
        elif elemento < lista[puntoMedio]:
            return busquedaBinaria(lista[:puntoMedio], elemento)
        else:
            return busquedaBinaria(lista[puntoMedio + 1 :], elemento)


lista = [1, 2, 3, 4, 54, 65, 76, 86, 97, 100]
print(busquedaBinaria(lista, 1))
print(busquedaBinaria(lista, 445))
