def busquedaBinaria(lista, elemento):
    if len(lista) == 0:
        return False
    else:
        lista.sort()
        puntoMedio = len(lista) // 2

        if lista[puntoMedio] == elemento:
            return True
        elif elemento < lista[puntoMedio]:
            return busquedaBinaria(lista[:puntoMedio], elemento)
        else:
            return busquedaBinaria(lista[puntoMedio + 1 :], elemento)


lista = [1, 2, 3, 445, 6, 25, 74, 28, 35, 13]
print(busquedaBinaria(lista, 35))
print(busquedaBinaria(lista, 411))
