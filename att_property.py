class Produto():

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco  = preco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if valor == "" or valor == None:
            print("Nome vazio")
        else:
            self.__nome = valor

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            print("Valor incorreto")
        else:
            self.__preco = valor

p1 = Produto("Celular", 800)

print(p1.nome , p1.preco)

p1.preco = -50
p1.nome = None


print(p1.nome , p1.preco)
