from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()



#pokemons sem evolução e pre evolução
pokemons = db.collection.find({"prev_evolution": {"$exists": False}, "next_evolution": {"$exists": False}})
writeAJson(pokemons, "pokemons_semEvolucao_e_preEvolucao")


#pokemons com avg spawn > 10
pokemons = db.collection.find({"spawn_chance": {"$gt": 10}})
writeAJson(pokemons, "pokemons_avgSpawn_maior_10")


#pokemons avg spawns = 0
pokemons = db.collection.find({"avg_spawns": 0})
writeAJson(pokemons, "pokemons_avg_spawns_0")

# pokemons tipo gelo ou voador com fraqueza a eletrico ou metal
tipos = ["Ice", "Flying"]
fraquezas = ["Electric", "Steel"]
pokemons = db.collection.find({"type": {"$in": tipos}, "weaknesses": {"$in": fraquezas}})
fraquezas = ["Psychic", "Ice"]
pokemons = db.collection.find({"weaknesses": {"$all": fraquezas}})
writeAJson(pokemons,"pokemons_tipoGeloOuVoadorComFraquezaEEletricoOuMetal")