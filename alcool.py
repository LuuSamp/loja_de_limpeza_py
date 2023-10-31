from produtos import Produtos

class Alcool(Produtos):
    """
    """
    numero_de_alcool = 0
    def __init__(self, nome: str, codigo_de_barras: str, marca:str, porcentagem:str) -> None:
        """
        """
        #utilizando métodos da classe mãe
        super().__init__(nome, codigo_de_barras, marca) 

        #configurando atributo próprio
        self.porcentagem = porcentagem

        #editando o atributo estático de contagem
        Alcool.numero_de_alcool += 1

    def __str__(self) -> str:
        """
        """
        #descrição do produto
        return f"Nome: {self.nome} - Marca: {self.marca} - Código de Barras: {self.codigo_de_barras} - Porcentagem: {self.porcentagem}."