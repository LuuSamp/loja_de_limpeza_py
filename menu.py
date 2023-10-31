from inventario import Inventario
from produtos import Produto
from detergente import Detergente
from amaciante import Amaciante
from marca import Marca
from alcool import Alcool

def exibir_inventario(inventario):
    print("------- Inventário -------")
    produtos_dict = inventario.lista_produtos()
    for produto in produtos_dict.keys():
        print(produto, ":", produtos_dict[produto])
    print()

def retirar_do_inventario(inventario):

    codigo = input("Codigo de Barras: ")
    quantidade = int(input("Quantidade: "))
    inventario.retira_produto(codigo, quantidade)
    
def adicionar_produto(inventario):
    marca = input("Marca do Produto (VEJA, YPE ou OMO): ")
    nome = input("Nome do Produto: ")
    codigo = input("Codigo de Barras: ")
    especificacao = input("Tipo de produto (Detergente, Amaciante ou Alcool): ")

    if especificacao == "Detergente": 
        tipo = input("Tipo de Detergente: ")
        inventario.adiciona_produto(Detergente(nome, codigo, marca, tipo))

    elif especificacao == "Amaciante": 
        odor = input("Odor do amaciante: ")
        inventario.adiciona_produto(Detergente(nome, codigo, marca, odor))
    
    elif especificacao == "Alcool":
        concentracao = input("Concentração de alcool: ")
        inventario.adiciona_produto(Detergente(nome, codigo, marca, concentracao))


def menu(inventario):
    exibir_inventario(inventario)
    print("Escolha uma opção:")
    print("1 - Adicionar produto ao inventário")
    print("2 - Remover produto do inventário")
    print("3 - Sair")
    opcao = int(input())
    if opcao == 1: adicionar_produto(inventario)
    elif opcao == 2: retirar_do_inventario(inventario)
    else: exit()