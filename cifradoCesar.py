class CifradoCesar:
    def __init__(self, shift) -> None:
        codificador = [None] * 26
        decodificador = [None] * 26
        for i in range(26):
            codificador[i] = chr((i + shift) % 26 + ord("A"))
            decodificador[i] = chr((i - shift) % 26 + ord("A"))
        self.encriptado = "".join(codificador)
        self.desencriptado = "".join(decodificador)

    def encriptar(self, mensaje):
        return self.transformar(mensaje, self.encriptado)

    def desencriptar(self, secreto):
        return self.transformar(secreto, self.desencriptado)

    def transformar(self, original, codigo):
        mensajeTexto = list(original)
        for i in range(len(mensajeTexto)):
            if mensajeTexto[i].isupper():
                j = ord(mensajeTexto[i]) - ord("A")
                mensajeTexto[i] = codigo[j]
        return "".join(mensajeTexto)


if __name__ == "__main__":
    cifrado = CifradoCesar(5)
    # mensaje = "CREA UN MENSAJE CIFRADO CON CESAR"
    mensaje = "0998857553"
    codificado = cifrado.encriptar(mensaje)
    print("Secreto:", codificado)
    respuesta = cifrado.desencriptar(codificado)
    print("Mensaje:", respuesta)

