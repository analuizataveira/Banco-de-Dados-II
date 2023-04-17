from Model.motorista import Motorista
from Model.passageiro import Passageiro
from Model.corrida import Corrida

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        corridas = ()
        aux = 1
        while (aux == 1):

            #Criando um passageiro
            nome = input("Digite o nome do passageiro: ")
            documento = input("Informe o documento do passageiro: ")

            #Criando objeto tipo passageiro com os valores de entrada
            passageiro = Passageiro(nome, documento)

            #Criando uma corrida
            nota_corrida = int(input("Como voce avalia a corrida? (Entre 0 e 5): "))
            distancia = float(input("Informe com a distancia da corrida: "))
            valor = float(input("Informe o valor da corrida: "))

            #Criando objeto tipo corrida com os valores de entrada
            corrida = Corrida(nota_corrida, distancia, valor, passageiro)

            #Adiciona a corrida criada na list corrida
            corridas += (corrida,)

            aux = int(input("Deseja adicionar outra corrida para esse motorista? (0 - Não, 1 - Sim): "))

        nota_motorista = int(input("Como voce avalia esse motorista? (Entre 0 e 5): "))

        #Criando um motorista com os parametros de entrada e a corrida já criada
        motorista = Motorista(nota_motorista, corridas)

        #Adicionado no banco de dados
        self.motorista_model.create_motorista(motorista)

    #Método read por um ID
    def read_motorista(self):
        id = input("Enter the id: ")
        motorista = self.motorista_model.read_motorista_by_id(id)

        print(f'Nota do motorista: {motorista.nota_motorista}')
        for corrida in motorista.corridas:
            print(f'Nota da corrida: {corrida.nota_corrida}')
            print(f'Distancia da corrida: {corrida.distancia}')
            print(f'Valor da corrida: {corrida.valor}')
            print(f'Nome do passageiro: {corrida.passageiro.nome}')
            print(f'Documento do passageiro: {corrida.passageiro.documento}')

    #Atualizar o valor de motorista por um ID
    def update_motorista(self):
        id = input("Enter the id: ")
        corridas = ()
        aux = 1
        while (aux == 1):
            nome = input("Entre com o nome do passageiro: ")
            documento = input("Entre com o documento do passageiro: ")
            passageiro = Passageiro(nome, documento)

            nota_corrida = int(input("Entre com a nota da corrida: "))
            distancia = float(input("Entre com a distancia da corrida: "))
            valor = float(input("Entre com o valor da corrida: "))
            corrida = Corrida(nota_corrida, distancia, valor, passageiro)
            corridas += (corrida,)

            aux = int(input("Deseja atualizar outra corrida para esse motorista? (0 - Não, 1 - Sim): "))

        nota_motorista = int(input("Como voce avalia esse motorista? (Entre 0 e 5): "))
        motorista = Motorista(nota_motorista, corridas)
        self.motorista_model.update_motorista(id, motorista)

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motorista_model.delete_motorista(id)

    def run(self):
        print("Welcome to the InaCar")
        print("Available commands: create, read, update, delete, quit")
        super().run()