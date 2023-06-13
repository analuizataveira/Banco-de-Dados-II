from database import Database
from gameCRUD import GameCRUD
from cli import SimpleCLI
from cli import GameCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.201.90.110:7687", "neo4j", "airport-ideals-card")
db.drop_all()

game_db = GameCRUD(db)

gameCLI = GameCLI(game_db)
gameCLI.run()

db.close()