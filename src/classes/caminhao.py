from veiculo import Veiculo 
class Caminhao(Veiculo):
    def __init__(self, anoFabricaocao=None, capacidadeDeCarga=None, isAtivo=None, numeroChassi=None, modelo=None, localizacao=None) -> None:
        super().__init__(anoFabricaocao, capacidadeDeCarga, isAtivo, numeroChassi, modelo, localizacao)
        self.tipo
        self._capacidadeDeCarga = 1000 