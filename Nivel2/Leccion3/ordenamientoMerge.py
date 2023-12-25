def ordenamientoMerge(lista):
    print("Dividiendo", lista)
    if len(lista) > 1:
        mitad = len(lista) // 2
        mitadIzq = lista[:mitad]
        mitadDer = lista[mitad:]
        ordenamientoMerge(mitadIzq)
        ordenamientoMerge(mitadDer)

        i = 0
        j = 0
        k = 0

        while i < len(mitadIzq) and j < len(mitadDer):
            if mitadIzq[i] < mitadDer[j]:
                lista[k] = mitadIzq[i]
                i += 1
                k += 1
            else:
                lista[k] = mitadDer[j]
                j += 1
                k += 1

        while i < len(mitadIzq):
            lista[k] = mitadIzq[i]
            i += 1
            k += 1

        while j < len(mitadDer):
            lista[k] = mitadDer[j]
            j += 1
            k += 1
    print("uniendo", lista)


lista = [33, 5, 67, 1, 56, 9, 0, 78, 6, 12, 21, 30]
ordenamientoMerge(lista)
print(lista)
