from produtos import Produtos

class Detergente(Produtos):
    """
    """
    numero_de_detergentes = 0
    def __init__(self, nome: str, codigo_de_barras: str, marca:str, tipo:str) -> None:
        """
        """
        super().__init__(nome, codigo_de_barras, marca) 
        self.tipo = tipo
        Detergente.numero_de_detergentes += 1

    def __str__(self) -> str:
        return f"Nome: {self.nome} - Marca: {self.marca} - Código de Barras: {self.codigo_de_barras} - Tipo: {self.tipo}."