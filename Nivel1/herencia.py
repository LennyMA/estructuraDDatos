class Acuatico:
    def nada(self):
        print("El animal nada")


class Terrestre:
    def camina(slef):
        print("El animal camina")


class Cocodrilo(Acuatico, Terrestre):
    pass


c = Cocodrilo()
c.nada()
c.camina()
