class Query:
    def __init__(self, database):
        self.db = database

    def get_teacher_renzo(self):
        query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        results = self.db.execute_query(query)
        return [(result["ano_nascimento"], result["cpf"]) for result in results]

    def get_teacher_m(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
        results = self.db.execute_query(query)
        return [(result["name"], result["cpf"]) for result in results]

    def get_school(self):
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS school_name, s.address AS address, s.number AS number"
        results = self.db.execute_query(query)
        return [(result["name"], result["endereco"], result["numero"]) for result in results]

    def yougest_oldest(self):
        query ="MATCH(t: Teacher) RETURN MIN(t.ano_nasc) AS OldestTeacher, MAX(t.ano_nasc) AS YoungestTeacher"
        results = self.db.execute_query(query)
        return [(result["OldestTeacher"], result["YoungestTeacher"]) for result in results]

    def avarege_city(self):
        query = "MATCH (c:City) RETURN AVG(c.population) AS mediaHabitantes"
        results = self.db.execute_query(query)
        return [result["mediaHabitantes"] for result in results]

    def city_name(self):
        query = "MATCH(c: City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name, 'a', 'A') AS nomeModificado"
        results = self.db.execute_query(query)
        return [result["nomeModificado"] for result in results]

    def teachers(self):
        query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1) AS third"
        results = self.db.execute_query(query)
        return [result["third"] for result in results]
