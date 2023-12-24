class CifradoCesar:
    def __init__(self, shift) -> None:
        caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

        codificador = [None] * len(caracteres)
        decodificador = [None] * len(caracteres)

        for i, char in enumerate(caracteres):
            codificador[i] = caracteres[(i + shift) % len(caracteres)]
            decodificador[i] = caracteres[(i - shift) % len(caracteres)]

        self.encriptado = "".join(codificador)
        self.desencriptado = "".join(decodificador)

    def encriptar(self, mensaje):
        return self.transformar(mensaje, self.encriptado, invertir=False)

    def desencriptar(self, secreto):
        return self.transformar(secreto, self.desencriptado, invertir=True)

    def transformar(self, original, codigo, invertir=False):
        mensajeTexto = list(original)
        for i in range(len(mensajeTexto)):
            if mensajeTexto[i] in codigo:
                j = codigo.index(mensajeTexto[i])
                if invertir:
                    mensajeTexto[i] = codigo[(j - 1) % len(codigo)]
                else:
                    mensajeTexto[i] = codigo[(j + 1) % len(codigo)]
        return "".join(mensajeTexto)


if __name__ == "__main__":
    cifrado = CifradoCesar(5)
    mensaje = "C4EA UN MENSAJE CI-RA0O C@N CE-AR"
    codificado = cifrado.encriptar(mensaje)
    print("Secreto:", codificado)
    respuesta = cifrado.desencriptar(codificado)
    print("Mensaje:", respuesta)
