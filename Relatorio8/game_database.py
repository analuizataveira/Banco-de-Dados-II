class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, id,score):
        query = "CREATE (:Match {id:$id,score:$score})"
        parameters = {"id": id, "score":score}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_matches(self):
        query = "MATCH (m:Match) RETURN m.id AS id, m.score AS score"
        results = self.db.execute_query(query)
        return [result["id", "score"] for result in results]

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def insert_player_match(self, player_name, match_id):
        query = "MATCH (p:Player {name: $player_name}) MATCH (m:Match {id: $match_id}) CREATE (p)-[:PARTICIPA]->(m)"
        parameters = {"player_name": player_name, "match_id": match_id}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)


    def delete_match(self, id):
        query = "MATCH (m:Match {id: $id}) DETACH DELETE m"
        parameters = {"id": id}
        self.db.execute_query(query, parameters)


