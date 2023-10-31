from produtos import Produtos

class Alcool(Produtos):
    """
    """
    numero_de_alcool = 0
    def __init__(self, nome: str, codigo_de_barras: str, marca:str, porcentagem:str) -> None:
        """
        """
        super().__init__(nome, codigo_de_barras, marca) 
        self.porcentagem = porcentagem
        Alcool.numero_de_alcool += 1

    def __str__(self) -> str:
        return f"Nome: {self.nome} - Marca: {self.marca} - Código de Barras: {self.codigo_de_barras} - Porcentagem: {self.porcentagem}."