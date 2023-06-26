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

    #Cria um relacionamento
    def create_avaliacao(self, game_name, jurado_name, nota, horas):
        query = "MATCH(j: Jurado{nome: $jurado_name}), (g:Game{titulo:$game_name}) CREATE(j)-[:JOGOU{nota: $nota, horas: $horas}]->(g);"
        parameters = {"game_name": game_name, "jurado_name": jurado_name, "nota":nota, "horas":horas}
        self.db.execute_query(query, parameters)

    #Mostrar o nome dos Jogos
    def get_game(self, titulo):
        query = "MATCH (g:Game{titulo: $titulo}) RETURN g.ano AS ano, g.genero AS genero;"
        parameters = {"titulo": titulo}
        results = self.db.execute_query(query, parameters)
        return [(result["genero"], result["ano"]) for result in results]


    #Deletar jurado
    def delete_jurado(self, titulo):
        query = "MATCH (g:Game{titulo: $titulo}) RETURN g.ano AS ano, g.genero AS genero;"
        parameters = {"titulo": titulo}
        results = self.db.execute_query(query, parameters)
        return [(result.get("ano"), result.get("genero")) for result in results]

    #Deletar jogo
    def delete_game(self, titulo):
        query = "MATCH (g:Game {titulo: $titulo}) DETACH DELETE g"
        parameters = {"titulo": titulo}
        self.db.execute_query(query, parameters)

    #Atualizando o relaciomnamento
    def update_avaliacao(self, jurado_name, game_name, new_nota, new_hora):
        query = "MATCH (j:Jurado {nome: $jurado_name})-[p:JOGOU]->(g:Game {titulo: $game_name})SET p.nota = $new_nota, p.horas = $new_hora"
        parameters = {"jurado_name": jurado_name, "game_name": game_name, "new_nota":new_nota, "new_hora":new_hora}
        self.db.execute_query(query, parameters)


