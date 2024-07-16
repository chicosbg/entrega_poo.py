from veiculo import Veiculo
from cliente import Cliente
from coordenada import Coordenada
class Pedido:
    def __init__(self, veiculoDeTransporte=None, solicitante=None, localDeColeta=None, localDeEntrega=None, pesoDaCarga=None):
        self._veiculoDeTransporte = veiculoDeTransporte
        self._solicitante = solicitante
        self._localDeColeta = localDeColeta
        self._localDeEntrega = localDeEntrega
        self._pesoDaCarga = pesoDaCarga
        self._numeroPedido = 0
    
    def getNumeroPedido(self):
        return self._numeroPedido
    
    def setNumeroPedido(self, numeroPedido):
        if(numeroPedido <= 0):
            raise Exception("Numero do pedido invalido.")
        self._numeroPedido = numeroPedido

    def getVeiculoDeTransporte(self):
        return self._veiculoDeTransporte
    
    def setVeiculoDeTransporte(self, veiculoDeTransporte: Veiculo):
        if veiculoDeTransporte.getIsAtivo():
            raise Exception("Nao sao permitido veiculos nao ativos.")
        self._veiculoDeTransporte = veiculoDeTransporte
        
    def getSolicitante(self):
        return self._solicitante
    
    def setSolicitante(self, solicitante: Cliente):
        if (solicitante == None):
            raise Exception("Eh obrigatorio passar um solicitante.")
        self._solicitante = solicitante

    def getLocalDeColeta(self):
        return self._localDeColeta
    
    def setLocalDeColeta(self, localDeColeta: Coordenada):
        if (localDeColeta == None):
            raise Exception("Eh obrigatorio informar um local de coleta.")
        self._localDeColeta = localDeColeta

    def getLocalDeEntrega(self):
        return self._localDeEntrega
    
    def setLocalDeEntrega(self, localDeEntrega: Coordenada):
        if (localDeEntrega == None):
            raise Exception("Eh obrigatorio informar um local de entrega.")
        self.localDeEntrega = localDeEntrega

    def getPesoDaCarga(self):
        return self._pesoDaCarga
    
    def setPesoDaCarga(self, pesoDaCarga):
        if (pesoDaCarga <= 0):
            raise Exception("peso de carga invalido.")
        self._pesoDaCarga = pesoDaCarga
    
