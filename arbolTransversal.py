def preorden(tree):
    if tree:
        print(tree.getRoot())
        preorden(tree.getHijoIzq())
        preorden(tree.getHijoDer())


def inorder(tree):
    if tree != None:
        inorder(tree.getHijoIzq())
        print(tree.getRoot())
        inorder(tree.getHijoDer())


def portorder(tree):
    if tree != None:
        portorder(tree.getHijoIzq())
        portorder(tree.getHijoDer())
        print(tree.getRoot())
