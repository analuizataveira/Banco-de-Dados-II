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
                print("Comando inválido.Tente novamente!")


class GameCLI(SimpleCLI):
    def __init__(self, game_model):
        super().__init__()
        self.game_model = game_model
        self.add_command("create jurado", self.create_jurado)
        self.add_command("create game", self.create_game)
        self.add_command("create avaliacao", self.create_avaliacao)
        self.add_command("read", self.read_games)
        self.add_command("update", self.update_jurado)
        self.add_command("delete", self.delete_game)


    def create_jurado(self):
        nome = input("Nome: ")
        self.game_model.create_jurado(nome)

    def create_game(self):
        titulo = input("Titulo: ")
        genero = input("Genero: ")
        ano = int(input("Ano: "))
        self.game_model.create_game(titulo,genero,ano)


    def create_avaliacao(self):
        nome_jurado = input("Nome do jurado: ")
        nome_jogo = input("Nome do Jogo avaliado: ")
        nota = int(input("Nota: "))
        horas = int(input("Horas jogadas: "))
        self.game_model.create_avaliacao(nome_jurado,nome_jogo,nota,horas)

    def read_games(self):
        titulo = input("Titulo: ")
        game = self.game_model.read_games(titulo)
        if game:
            print(f"Titulo: {game['titulo']}")
            print(f"Genero: {game['genero']}")
            print(f"Ano: {game['ano']}")


    def update_jurado(self):
        nome = input("Nome ")
        novo_nome = input ("Novo nome: ")
        self.game_model.update_jurado(nome, novo_nome)


    def delete_game(self):
        titulo = input("Entre com o nome do jogo que deseja deletar: ")
        self.game_model.delete_game(titulo)

    def run(self):
        print("Welcome to the InaE-Sports")
        print("Available commands: create jurado, create game, create avaliacao, read , update, delete, quit")
        super().run()