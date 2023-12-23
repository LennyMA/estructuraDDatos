def contar(dato, objetivo):
    n = 0
    for i in dato:
        if i == objetivo:
            n += 1
    return n


lista = ["a", "a", "b", "c", "a", "d"]
cuenta = contar(lista, "a")
print(cuenta)
