from database import Database
from query import Query
from teacherCRUD import TeacherCRUD
from cli import SimpleCLI
from cli import TeacherCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.214.134.69:7687", "neo4j", "cab-circuit-entrance")
db.drop_all()

query_db = Query(db)
teacher_db = TeacherCRUD(db)

# QUESTAO 1
print(query_db.get_teacher_renzo())
print(query_db.get_teacher_m())
print(query_db.get_school())


# Questão 2
print(query_db.yougest_oldest())
print(query_db.avarege_city())
print(query_db.teachers())
print(query_db.city_name())

# Questão 3
teacherCLI = TeacherCLI(teacher_db)
teacherCLI.run()

db.close()