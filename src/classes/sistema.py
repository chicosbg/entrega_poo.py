from gerenciadorDeVeiculos import GerenciadorDeVeiculos
from gerenciadorDePedidos import GerenciadorDePedidos
import requests
from cliente import Cliente
from pedido import Pedido
from coordenada import Coordenada
import csv
import re
from typing import List, Optional

class Sistema:
    def __init__(self):
        self._clientes: List[Cliente] = []
        self._pedidos: List[Pedido] = []
        self._veiculos = []
        self._gerenciadorDeVeiculos = GerenciadorDeVeiculos()
        self._gerenciadorDePedidos = GerenciadorDePedidos(None)
        
    def setGerenciadorVeiculos(self, gerenciadorVeiculos: GerenciadorDeVeiculos):
        self._gerenciadorDeVeiculos = gerenciadorVeiculos

    def lerCSV(self):
        with open("assets/csvs/dados_entregas.csv", mode='r', encoding='utf-8') as file:
            conteudo = csv.reader(file, delimiter=',')
            linhas = 0
            print("Iniciando a leitura do csv")
            for coluna in conteudo:
                print(f"lendo a linha {linhas+1}")
                if linhas == 0:
                    linhas += 1
                    continue
                try:
                    cliente = Cliente()
                    cliente.setNome(nome=coluna[0])
                    cliente.setCpf(cpf=coluna[1])
                    cliente.setEndereco(endereco=coluna[2])
                    cliente.setTelefone(telefone=coluna[3])
                    cliente.setEmail(email=coluna[4])
                    
                    pedido = Pedido()
                    list_cor = self.stringToCoordenadas(coluna[5].replace("\n", " ").split("/")[0])

                    coor = ""
                    if list_cor:
                        coor = Coordenada()
                        coor.setLatitude(list_cor[0])
                        coor.setLongitude(list_cor[1])
                    pedido.setLocalDeColeta(localDeColeta=coor)
                    
                    list_cor = self.stringToCoordenadas(coluna[6].replace("\n", " ").split("/")[0])
                    coor = ""
                    if list_cor:
                        coor = Coordenada()
                        coor.setLatitude(list_cor[0])
                        coor.setLongitude(list_cor[1])
                    pedido.setLocalDeEntrega(localDeEntrega=coor)
                    
                    pedido.setPesoDaCarga(pesoDaCarga=int(coluna[7]))
                    pedido.setSolicitante(solicitante=cliente)
                    
                    self._clientes.append(cliente)
                    self._pedidos.append(pedido)
                except:
                    print(f"a linha {linhas} não pode ser inserida")
                linhas += 1
                
            self._gerenciadorDePedidos.defineVeiculosTransporte(listaPedidos=self._pedidos)
            
    def stringToCoordenadas(self, string: str) -> Optional[List[str]]:
        response = requests.get(f"https://www.google.com/maps/search/{string.replace(' ', '+')}")
        return self.extract_coordinates(html_content=response.text)
            
    def extract_coordinates(self, html_content: str) -> Optional[List[str]]:
        match = re.search(r'\?center=(.*?)&amp;zoom', html_content)
        if match:
            coordinates = match.group(1).replace('%2C', ' ').split(" ")
            return coordinates
        return None
    
if __name__ == "__main__":
    teste = Sistema()
    teste.lerCSV()
