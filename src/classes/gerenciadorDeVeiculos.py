from veiculo import Veiculo
from caminhonete import Caminhonete
from carro import Carro
from caminhao import Caminhao
from coordenada import Coordenada

class GerenciadorDeVeiculos:
    def __init__(self):
        self._veiculos_ativos = []
        
    def getVeiculosAtivos(self):
        pass

    def adicionarVeiculo(self, veiculo):
        self._veiculos_ativos.append(veiculo)

    def adicionarVeiculos(self, numeroChassi, modelo, localizacao):
        veiculo = Veiculo()
        try:
            veiculo.setIsAtivo(True)
            veiculo.setLocalizacao(localizacao)
            veiculo.setModelo(modelo)
            veiculo.setNumeroChassi(numeroChassi)
        except:
            print("Algo não saiu como esperado.")
            return False

    def adicionarVeiculos(self, numeroChassi, modelo, localizacao, anoFabricaocao):
        veiculo = Veiculo()
        try:
            veiculo.setIsAtivo(True)
            veiculo.setLocalizacao(localizacao)
            veiculo.setModelo(modelo)
            veiculo.setNumeroChassi(numeroChassi)
        except:
            print("Algo não saiu como esperado.")
            return False
        
        self._veiculos_ativos.append(veiculo)
        return True

    def adicionarVeiculos(self, veiculo):
        self._veiculos_ativos.append(veiculo)

    def adicionarVeiculos(self, tipo, numeroChassi, modelo, localizacao, isAtivo, anoFabricacao, capacidadeDeCarga):
        veiculo = Veiculo()
        if(tipo == "Caminhonete"):
            veiculo = Caminhonete()
        if(tipo == "Carro"):
            veiculo = Carro()
        if(tipo == "Caminhao"):
            veiculo = Caminhao()
            
        veiculo.setNumeroChassi(numeroChassi=numeroChassi)
        veiculo.setModelo(modelo=modelo)
        veiculo.setLocalizacao(localizacao=localizacao)
        veiculo.setIsAtivo(isAtivo=isAtivo)
        veiculo.setAnoFabricaocao(anoFabricaocao=anoFabricacao)
        veiculo.setCapacidadeDeCarga(capacidadeDeCarga=capacidadeDeCarga)
        self.veiculos_ativos.append(veiculo)
    
    def removerVeiculo(self, veiculo):
        self._veiculos_ativos.remove(veiculo)

    def buscaVeiculo(self, numeroChassi):
        for v in self._veiculos_ativos:
            if (v.getNumeroChassi() == numeroChassi):
                return v
        return None


    def buscaVeiculoByLocalizacao(self, localizacao:Coordenada):    
        for v in self._veiculos_ativos:
            if (localizacao.getLatitude() == v.getLocalizacao().getLatitude() and localizacao.getLongitude() == v.getLocalizacao().getLatitude()):
                return v
        return None


    def obterVeiculosAtivos(self):
        return self._veiculos_ativos

