def busquedaSecuencial(lista, elemento):
    posicion = 0
    encontrado = False
    while posicion < len(lista) and not encontrado:
        if lista[posicion] == elemento:
            encontrado = True
        else:
            posicion += 1
    return encontrado, posicion


lista = [1, 2, 3, 445, 6, 25, 74, 28, 35, 13]
print(busquedaSecuencial(lista, 5))
print(busquedaSecuencial(lista, 13))
