from collections import Counter
from excecoes import *

class Inventario():

    def __init__(self):
        self.produtos = []

    def adiciona_produto(self, produto):
        self.produtos.append(produto)
    
    def retira_produto(self, produto_id, quantidade):
        codigos_de_barras = [produto.get_codigo_de_barras() for produto in self.produtos]
        # Se o codigo do produto não está na lista do inventário, levanta um erro
        if produto_id not in codigos_de_barras:
            raise ProdutoFaltante()
        
        # Confirmando se há tal quantidade e armazenando seus indices
        ultimo_index = 0
        indexes = []
        for numero_produto in range(quantidade):
            try:
                index = codigos_de_barras.index(produto_id, ultimo_index)
            except ValueError:
                raise ProdutoFaltante("Não há essa quantidade no inventario")
            
            ultimo_index = index
            indexes.append(index)
        
        # Removendo os produtos da lista.
        for cada_index in sorted(indexes, reverse=True):
            self.produtos.pop(cada_index)

    def lista_produtos(self):
        nomes_produtos = [str(produto) for produto in self.produtos]
        dicionario_produtos = dict(Counter(nomes_produtos))
        return dicionario_produtos
    
