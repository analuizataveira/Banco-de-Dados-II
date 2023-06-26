from database import Database
from gameCRUD import GameCRUD
from cli import SimpleCLI
from cli import GameCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.193.198.110:7687", "neo4j", "realinements-cuffs-missiles")
db.drop_all()

game_db = GameCRUD(db)

game_db.create_game("Devour","Terror",2020)
game_db.create_game("Minecraft","Sandbox",2011)
game_db.create_game("Warzone","Shooter",2019)

game_db.create_jurado("Ana")
game_db.create_jurado("Bruno")
game_db.create_jurado("Davi")


game_db.create_avaliacao("Devour","Ana",10,1000)
game_db.create_avaliacao("Warzone","Bruno",9,1500)


gameCLI = GameCLI(game_db)
gameCLI.run()

db.close()