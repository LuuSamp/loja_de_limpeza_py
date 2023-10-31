from collections import Counter

class Inventario():

    def __init__(self):
        self.produtos = []

    def adiciona_produto(self, produto):
        self.produtos.append(produto)
    
    def retira_produto(self, produto):
        index = self.produtos.index(produto)
        self.pop(index)

    def lista_produtos(self):
        nomes_produtos = [str(produto) for produto in self.produtos]
        dicionario_produtos = dict(Counter(nomes_produtos))
        return dicionario_produtos
    

