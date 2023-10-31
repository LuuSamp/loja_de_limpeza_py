class MarcaNaoEncontradaError(KeyError):
    """
    """
    def __init__(self, message="Marca inexistente."):
        """
        """
        #configura a mensagem da exceção
        self.message = message

        #cria a exceção com base na classe mãe
        super().__init__(self.message)

class ProdutoFaltante(KeyError):
    """
    """
    def __init__(self, message="Estamos sem esse produto no momento."):
        """
        """
        #configura a mensagem da exceção
        self.message = message

        #cria a exceção com base na classe mãe
        super().__init__(self.message)
