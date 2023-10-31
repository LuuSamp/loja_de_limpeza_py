from produtos import Produtos

class Amaciante(Produtos):
    """
    """
    numero_de_amaciantes = 0
    def __init__(self, nome: str, codigo_de_barras: str, marca:str, cheiro:str) -> None:
        """
        """
        super().__init__(nome, codigo_de_barras, marca) 
        self.cheiro = cheiro
        Amaciante.numero_de_amaciantes += 1

    def __str__(self) -> str:
        return f"Nome: {self.nome} - Marca: {self.marca} - Código de Barras: {self.codigo_de_barras} - Cheiro: {self.cheiro}."