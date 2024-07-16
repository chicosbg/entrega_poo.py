from veiculo import Veiculo
from caminhonete import Caminhonete
from carro import Carro
from caminhao import Caminhao

class GerenciadorDeVeiculos:
    def __init__(self):
        self.veiculos_ativos = []
        
    def getVeiculosAtivos(self):
        pass

    def adicionarVeiculo(self, veiculo):
        pass

    def adicionarVeiculos(self, numeroChassi, modelo, localizacao):
        pass

    def adicionarVeiculos(self, numeroChassi, modelo, localizacao, anoFabricaocao):
        pass

    def adicionarVeiculos(self, veiculo):
        self.veiculos_ativos.append(veiculo)

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
        self.veiculos_ativos.remove(veiculo)

    def buscaVeiculo(self, numeroChassi):
        pass

    def buscaVeiculoByLocalizacao(self, localizacao):
        pass

    def obterVeiculosAtivos(self):
        return self.veiculos_ativos
