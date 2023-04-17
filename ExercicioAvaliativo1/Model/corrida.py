from Model.passageiro import Passageiro

class Corrida():
    def __init__(self, nota:int, distancia: float, valor:float, passageiro: Passageiro):
        self.nota=nota
        self.distancia=distancia
        self.valor=valor
        self.passageiro = passageiro