from gerenciadorDeVeiculos import GerenciadorDeVeiculos
from pedido import Pedido

class GerenciadorDePedidos:
    def __init__(self, veiculos: GerenciadorDeVeiculos):
        self._veiculos = veiculos
        self._pedidos = []
        
    def defineVeiculosTransport(self, listaPedidos):
        veiculosAtivos = self._veiculos.getVeiculosAtivos()
        indicesAdicionados = []
        
        for veiculo in veiculosAtivos:
            capacidadeTotalDoVeiculo = veiculo.getCapacidadeDeCarga()
            contagemAtual = 0
            for pedido in listaPedidos:
                if (pedido.getPesoDaCarga() > capacidadeTotalDoVeiculo):
                    continue

                if (not indicesAdicionados[contagemAtual]):
                    continue

                pedido.setVeiculoDeTransporte(veiculo)

                self._pedidos.append(pedido)

                indicesAdicionados[contagemAtual] = contagemAtual

                capacidadeTotalDoVeiculo = capacidadeTotalDoVeiculo - pedido.getPesoDaCarga()
                
    def defineVeiculosTransport(self, pedido: Pedido):
        veiculosAtivos = self._veiculos.getVeiculosAtivos()
        for veiculo in veiculosAtivos:  
            if(pedido.getPesoDaCarga() > veiculo.getCapacidadeDeCarga()): 
                continue 
            pedido.setVeiculoDeTransporte(veiculo)
            self._pedidos.append(pedido)
            return True
        
        return False
    
    def realizarEntrega(self):
        for pedido in self._pedidos:
            pedido.getVeiculoDeTransporte().setLocalizacao(pedido.getLocalDeEntrega())