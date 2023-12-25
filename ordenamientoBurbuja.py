def busquedaBurbuja(lista):
    for num_paso in range(len(lista) - 1, 0, -1):
        for i in range(num_paso):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux


lista = [33, 5, 67, 1, 56, 9, 0, 78, 6, 12, 21, 30]
busquedaBurbuja(lista)
print(lista)
