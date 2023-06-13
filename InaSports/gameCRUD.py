class GameCRUD:
    def __init__(self, database):
        self.db = database

    def create_game(self, titulo, genero, ano):
        query = "CREATE (:Game {titulo: $titulo ,genero: $genero ,ano:$ano})"
        parameters = {"titulo": titulo, "genero": genero,"ano": ano }
        self.db.execute_query(query, parameters)


    def create_jurado(self, nome):
        query = "CREATE (:Jurado {nome: $nome})"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)


    def create_avaliacao(self, game_name, jurado_name, nota, horas):
        query = "MATCH(j: Jurado{nome: $jurado_name}), (g:Game{titulo:$game_name}) CREATE(j)-[:JOGOU{nota: $nota, horas: $horas}]->(g);"
        parameters = {"game_name": game_name, "jurado_name": jurado_name, "nota":nota, "horas":horas}
        self.db.execute_query(query, parameters)


    def get_jurados(self):
        query = "MATCH (j:Jurado) RETURN j.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def get_games(self):
        query = "MATCH (g:Game) RETURN g.titulo AS titulo"
        results = self.db.execute_query(query)
        return [result["titulo"] for result in results]


    def update_jurado(self, old_name, new_name):
        query = "MATCH (j:Jurado {nome: $old_name}) SET j.nome = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def delete_jurado(self, nome):
        query = "MATCH (j:Jurado {nome: $nome}) DETACH DELETE j"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    def delete_game(self, titulo):
        query = "MATCH (g:Game {titulo: $titulo}) DETACH DELETE g"
        parameters = {"titulo": titulo}
        self.db.execute_query(query, parameters)

