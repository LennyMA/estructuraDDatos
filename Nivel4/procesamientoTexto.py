ubicacion = "./texto.txt"
filename = open(ubicacion)
completo = filename.read()
escribirSobre = open(ubicacion, "a")
for i in range(10):
    c = str(i)
    escribir = escribirSobre.write(c + "\n")
    filename = open(ubicacion)
    completo = filename.read()

print(completo)
