class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente!")


class GameCLI(SimpleCLI):
    def __init__(self, game_model):
        super().__init__()
        self.game_model = game_model
        self.add_command("create game", self.create_game)
        self.add_command("create jurado", self.create_jurado)
        self.add_command("create avaliacao", self.create_avaliacao)
        self.add_command("get game", self.get_game)
        self.add_command("update avaliacao", self.update_avaliacao)
        self.add_command("delete game", self.delete_game)
        self.add_command("delete jurado", self.delete_jurado)

    def create_game(self):
        titulo = input("Titulo: ")
        genero = input("Genero: ")
        ano = int(input("Ano: "))
        self.game_model.create_game(titulo,genero,ano)

    def create_jurado(self):
        nome = input("Nome: ")
        self.game_model.create_jurado(nome)


    def create_avaliacao(self):
        game_name = input("Nome do Jogo avaliado: ")
        jurado_name = input("Nome do jurado: ")
        nota = int(input("Nota: "))
        horas = int(input("Horas jogadas: "))
        self.game_model.create_avaliacao(game_name,jurado_name,nota,horas)

    def get_game(self):
        titulo = input("Titulo: ")
        game = self.game_model.get_game(titulo)
        if game:
            print(f"Genero: {game[0][0]}")
            print(f"Ano:{game[0][1]}")


    def update_avaliacao(self):
        jurado_name = input("Nome do jurado: ")
        game_name = input("Nome do game: ")
        new_nota = int(input("Nova nota: "))
        new_hora = int(input("Novas horas jogadas: "))
        self.game_model.update_avaliacao(jurado_name,game_name,new_nota,new_hora)


    def delete_game(self):
        titulo = input("Entre com o nome do jogo que deseja deletar: ")
        self.game_model.delete_game(titulo)

    def delete_jurado(self):
        nome = input("Entre com o nome do jurado que deseja deletar: ")
        self.game_model.delete_jurado(nome)

    def run(self):
        print("Bem vindo ao Ina-ESports")
        print(f"Comandos disponíveis: ")
        print(f"create jurado")
        print(f"create game")
        print(f"create avaliacao")
        print(f"get game")
        print(f"update avaliacao")
        print(f"delete jurado")
        print(f"delete game")
        super().run()