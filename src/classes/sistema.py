from gerenciadorDeVeiculos import GerenciadorDeVeiculos
from gerenciadorDePedidos import GerenciadorDePedidos
import requests
from cliente import Cliente
from pedido import Pedido
from coordenada import Coordenada
import csv
import re

class Sistema:
    def __init__(self):
        self._clientes = []
        self._pedidos = []
        self._veiculos = []
        self._gerenciadorDeVeiculos = GerenciadorDeVeiculos()
        self._gerenciadorDePedidos = GerenciadorDePedidos(None)
        
    def setGerenciadorVeiculos(self, gerenciadorVeiculos: GerenciadorDeVeiculos):
        self.gerenciadorVeiculos = gerenciadorVeiculos

    def lerCSV(self):
        with open("assets/csvs/dados_entregas.csv", mode='r') as file:
            conteudo = csv.reader(file, delimiter=',')
            linhas = 0
            for coluna in conteudo:
                if linhas == 0:
                    linhas += 1
                    continue
                
                cliente = Cliente()
                cliente.setNome(nome=coluna[0])
                cliente.setCpf(cpf=coluna[1])
                cliente.setEndereco(endereco=coluna[2])
                cliente.setTelefone(telefone=coluna[3])
                cliente.setEmail(email=coluna[4])
                
                pedido = Pedido()
                list_cor = self.stringToCoordenadas(coluna[5].replace("\n", " ").split("/")[0])

                coor = ""
                if(list_cor):
                    coor = Coordenada()
                    coor.setLatitude(list_cor[0])
                    coor.setLongitude(list_cor[1])
                pedido.setLocalDeColeta(localDeColeta=coor)
                
                list_cor = self.stringToCoordenadas(coluna[6].replace("\n", " ").split("/")[0])
                coor = ""
                if(list_cor):
                    coor = Coordenada()
                    coor.setLatitude(list_cor[0])
                    coor.setLongitude(list_cor[1])
                pedido.setLocalDeEntrega(localDeEntrega=coor)
                
                pedido.setPesoDaCarga(pesoDaCarga=int(coluna[7]))

                pedido.setSolicitante(solicitante=pedido)
                
                self._clientes.append(cliente)
                self._pedidos.append(pedido)
                linhas += 1
                
            self._gerenciadorDePedidos.defineVeiculosTransporte(listaPedidos=self._pedidos)
            
    def stringToCoordenadas(self, string: str):
        response = requests.get(f"https://www.google.com/maps/search/{string.replace(" ", "+")}")
        return self.extract_coordinates(html_content=response.text)
            
    def extract_coordinates(self, html_content: str):
        match = re.search(r'\?center=(.*?)&amp;zoom', html_content)
        if match:
            coordinates = match.group(1).replace('%2C', ' ').split(" ")
            return coordinates
        return None
    
if __name__ == "__main__":
    teste = Sistema()
    teste.lerCSV()