from veiculo import Veiculo 
class Carro(Veiculo):
    def __init__(self, anoFabricaocao=None, capacidadeDeCarga=None, isAtivo=None, numeroChassi=None, modelo=None, localizacao=None) -> None:
        super().__init__(anoFabricaocao, capacidadeDeCarga, isAtivo, numeroChassi, modelo, localizacao)
        self._capacidadeDeCarga = 350
        self.tipo