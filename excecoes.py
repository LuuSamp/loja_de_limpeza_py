class MarcaNaoEncontradaError(KeyError):
    """
    """
    def __init__(self, message="Marca inexistente."):
        self.message = message
        super().__init__(self.message)

class ProdutoFaltante(KeyError):
    """
    """
    def __init__(self, message="Estamos sem esse produto no momento."):
        self.message = message
        super().__init__(self.message)
