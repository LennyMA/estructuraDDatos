class ArbolBinario:
    def __init__(self, root) -> None:
        self.key = root
        self.hijoIzq = None
        self.hijoDer = None

    def insertarIzq(self, nuevoNode):
        if self.hijoIzq == None:
            self.hijoIzq = ArbolBinario(nuevoNode)
        else:
            t = ArbolBinario(nuevoNode)
            t.hijoIzq = self.hijoIzq
            self.hijoIzq = t

    def insertarDer(self, nuevoNode):
        if self.hijoDer == None:
            self.hijoDer = ArbolBinario(nuevoNode)
        else:
            t = ArbolBinario(nuevoNode)
            t.hijoDer = self.hijoDer
            self.hijoDer = t

    def getHijoDer(self):
        return self.hijoDer

    def getHijoIzq(self):
        return self.hijoIzq

    def setRootVal(self, ob):
        self.key = ob

    def getRoot(self):
        return self.key

r = ArbolBinario(5)
print(r.getRoot())
print(r.getHijoDer())
print(r.getHijoIzq())
r.insertarIzq(4)
print(r.getHijoIzq().getRoot())
r.insertarDer(6)
print(r.getHijoDer().getRoot())
r.getHijoDer().setRootVal(8)
print(r.getHijoDer().getRoot())