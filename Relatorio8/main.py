from database import Database
from game_database import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://54.89.40.208:7687", "neo4j", "limitations-shower-feed")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
game_db = GameDatabase(db)

# Criando alguns jogadores
game_db.create_player("João")
game_db.create_player("Caio")
game_db.create_player("José")

# Criando algumas partidas
game_db.create_match(1,90)
game_db.create_match(2,50)


# Associando as partidas aos jogadores
game_db.insert_player_match("João", 1)
game_db.insert_player_match("Caio", 1)
game_db.insert_player_match("José", 2)

# Atualizando o nome de um jogador
game_db.update_player("João", "Pedro")


# Deletando um jogador e uma partida
game_db.delete_player("Caio")
game_db.delete_match(2)

# Imprimindo todas as informações do banco de dados
print("Jogadores:")
print(game_db.get_players())
print("Partidas:")
print(game_db.get_matches())



# Fechando a conexão com o banco de dados
db.close()