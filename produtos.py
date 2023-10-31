from marca import Marca
from excecoes import MarcaNaoEncontradaError

class Produtos():
    """
    """

    numero_de_produtos = 0

    def __init__(self, nome:str, codigo_de_barras:str, marca:str) -> None:
        """
        """
        #todas as marcas cadastradas
        lista_de_marcas = [str(cada_marca.name) for cada_marca in Marca]

        try:
            #verifica se a marca fornecida existe
            if marca.upper() not in lista_de_marcas:
                raise MarcaNaoEncontradaError
            
            #se tiver tudo certo, cria a instância e configura os atributos
            else:
                self.marca = marca
                self.nome = nome
                self.codigo_de_barras = codigo_de_barras

                #editando o atributo estático de contagem
                Produtos.numero_de_produtos += 1

        except MarcaNaoEncontradaError:
            print("A marca inserida foi inválida.")

        except:
            print("Algo deu errado na criação do produto. Tente novamente.")

    def get_codigo_de_barras(self):
        """
        """
        #acessa o código de barras
        return self.codigo_de_barras

    def __str__(self) -> str:
        """
        """
        #descrição do produto
        return f"Nome: {self.nome} - Marca: {self.marca} - Código de Barras: {self.codigo_de_barras}."

