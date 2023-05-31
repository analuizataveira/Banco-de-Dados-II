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


class TeacherCLI(SimpleCLI):
    def __init__(self, teacher_model):
        super().__init__()
        self.teacher_model = teacher_model
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)


    def create_teacher(self):
        name = input("Nome: ")
        ano_nasc = int(input("Ano de nascimento: "))
        cpf = input("Cpf: ")
        self.teacher_model.create_teacher(name, ano_nasc, cpf)

    def read_teacher(self):
        name = input("Nome: ")
        teacher = self.teacher_model.read_teacher(name)
        if teacher:
            print(f"Nome: {teacher['name']}")
            print(f"Ano nascimento: {teacher['ano_nasc']}")
            print(f"CPF: {teacher['cpf']}")


    def update_teacher(self):
        name = input("Nome ")
        new_cpf = input("Novo cpf: ")
        self.teacher_model.update_teacher(name, new_cpf)


    def delete_teacher(self):
        name = input("Entre com o nome do professor que deseja deletar: ")
        self.teacher_model.delete_teacher(name)

    def run(self):
        print("Welcome to the Inatel")
        print("Available commands: create, read, update, delete, quit")
        super().run()