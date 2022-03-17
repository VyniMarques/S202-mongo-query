from db.database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
# db.resetDatabase()

"""
pokemons = db.collection.find({"type": {"$size": 1}})
writeAJson(pokemons, "pokemons")
"""

"""
pokemons = db.collection.find({"next_evolution": None})
writeAJson(pokemons, "pokemons")
"""

"""
pokemons = db.executeQuery({"spawn_chance": {"$lt": 0.009}})
writeAJson(pokemons, "pokemons")
"""

"""
tipos = ["Ice", "Fire"]
fraquezas = ["Eletric", "Metal"]
pokemons = db.collection.find({"$or": [{"type": {"$in": tipos}}, {"weaknesses": {"$in": fraquezas}}]})
writeAJson(pokemons, "pokemons")
"""

"""
tipos = ["Metal", "Fighting"]
pokemons = db.executeQuery({"type": {"$in": tipos}, "spawn_chance": {"$gt": 0.1}, "multipliers": {"$exists": True}})
writeAJson(pokemons, "pokemons")
"""

