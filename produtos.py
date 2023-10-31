from marca import Marca
from excecoes import MarcaNaoEncontradaError

class Produtos():
    """
    """

    numero_de_produtos = 0

    def __init__(self, nome:str, codigo_de_barras:str, marca:str) -> None:
        """
        """
        lista_de_marcas = [str(cada_marca.name) for cada_marca in Marca]
        try:
            if marca.upper() not in lista_de_marcas:
                raise MarcaNaoEncontradaError
            
            else:
                self.marca = marca
                self.nome = nome
                self.codigo_de_barras = codigo_de_barras
                Produtos.numero_de_produtos += 1

        except MarcaNaoEncontradaError:
            print("A marca inserida foi inválida.")

        except:
            print("Algo deu errado na criação do produto. Tente novamente.")

    def get_codigo_de_barras(self):
        """
        """
        return self.codigo_de_barras

    def __str__(self) -> str:
        return f"Nome: {self.nome} - Marca: {self.marca} - Código de Barras: {self.codigo_de_barras}."

