class Veiculo:
    def __init__(self, anoFabricaocao = None, capacidadeDeCarga = None, isAtivo = None, numeroChassi = None, modelo = None, localizacao = None) -> None:
        self._anoFabricaocao = anoFabricaocao
        self._capacidadeDeCarga = capacidadeDeCarga
        self._capacidadeDeCarga  = capacidadeDeCarga
        self._isAtivo = isAtivo
        self._numeroChassi = numeroChassi
        self._modelo = modelo
        self._localizacao = localizacao
        self.tipo = __class__
        if(__class__ == "Veiculo"):
            self.tipo = "Veiculo não definido."
            
    def getTipo(self):
        return self.tipo

    def getCapacidadeDeCarga(self):
        return self._capacidadeDeCarga
    
    def setCapacidadeDeCarga(self, capacidadeDeCarga):
        self._capacidadeDeCarga = capacidadeDeCarga
    
    def getAnoFabricaocao(self):
        return self._anoFabricaocao
    
    def setAnoFabricaocao(self, anoFabricaocao):
        self._anoFabricaocao = anoFabricaocao

    def getNumeroChassi(self):
        return self._numeroChassi

    def setNumeroChassi(self, numeroChassi):
        self._numeroChassi = numeroChassi

    def getModelo(self):
        return self._modelo

    def setModelo(self, modelo):
        self._modelo = modelo

    def getLocalizacao(self):
        return self._localizacao

    def setLocalizacao(self, localizacao):
        self._localizacao = localizacao

    def getIsAtivo(self):
        return self._isAtivo
    
    def setIsAtivo(self, isAtivo):
        self._isAtivo = isAtivo
