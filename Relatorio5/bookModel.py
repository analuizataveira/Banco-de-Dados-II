from pymongo import MongoClient
from bson.objectid import ObjectId

class BookModel:
    def __init__(self, database):
        self.db = database

    def create_book(self, id:int, titulo: str, autor: str, ano:int, preco:float):
        try:
            res = self.db.collection.insert_one({"_id": id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
            print(f"Book created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating book: {e}")
            return None

    def read_book_by_id(self, id: int):
        try:
            res = self.db.collection.find_one({"_id": id})
            print(f"Book found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading book: {e}")
            return None

    def update_book(self, id: int, titulo: str, autor: str, ano:int, preco:float):
        try:
            res = self.db.collection.update_one({"_id": id}, {"$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}})
            print(f"Book updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating book: {e}")
            return None

    def delete_book(self, id: int):
        try:
            res = self.db.collection.delete_one({"_id": id})
            print(f"Book deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting book: {e}")
            return None