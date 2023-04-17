from pymongo import MongoClient
import database
from Model.passageiro import  Passageiro
from Model.corrida import Corrida
from Model.motorista import Motorista
from bson.objectid import ObjectId

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    #Método create para o motorista
    def create_motorista(self, motorista):
        try:
            #Dicionário, ou seja, documento do tipo motorista
            motorista_dict = {
                "Nota": motorista.nota,
                "Corridas":[
                    {
                        "Nota": corrida.nota,
                        "Distancia": corrida.distancia,
                        'valor': corrida.valor,
                        'passageiro':{
                            'nome': corrida.passageiro.nome,
                            'documento': corrida.passageiro.documento
                        }
                    } for corrida in motorista.corridas

                ]
            }
            res = self.db.collection.insert_one(motorista_dict)
            print(f"Driver created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating driver: {e}")
            return None

    #Método search
    def read_motorista_by_id(self, id: str):
        try:
            motorista_dict = self.db.collection.find_one({"_id": ObjectId(id)})
            if(motorista_dict):
                notas = motorista_dict['Nota']
                corridas_dict = motorista_dict['Corridas']
                corridas = [Corrida(corrida_dict['Nota'], corrida_dict['Distancia'], corrida_dict['valor'], Passageiro(corrida_dict['passageiro']['nome'], corrida_dict['passageiro']['documento'])) for corrida_dict in corridas_dict]
            print(f"Driver found: {motorista_dict}")
            return Motorista(notas, corridas)
        except Exception as e:
            print(f"An error occurred while reading driver: {e}")
            return None

    #Método update
    def update_motorista(self, motorista_id, motorista):
        try:
            motorista_dict = {
                'Nota': motorista.nota,
                'Corridas': [
                    {
                        'Nota': corrida.nota,
                        'Distancia': corrida.distancia,
                        'valor': corrida.valor,
                        'passageiro': {
                            'nome': corrida.passageiro.nome,
                            'documento': corrida.passageiro.documento
                        }
                    } for corrida in motorista.corridas
                ]
            }
            res = self.db.collection.update_one({"_id": ObjectId(motorista_id)}, {"$set": motorista_dict})
            print(f"Driver updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating driver: {e}")
            return None

    #Método delete
    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorista: {e}")
            return None