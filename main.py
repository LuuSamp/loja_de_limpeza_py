from menu import *
from collections import Counter
from excecoes import *
from marca import Marca
from inventario import Inventario
from produtos import Produto
from detergente import Detergente
from amaciante import Amaciante
from alcool import Alcool

inventario = Inventario()
while True:
    menu(inventario)