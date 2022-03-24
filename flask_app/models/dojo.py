from flask_app.config.mysqlconnection import connectToMySQL

class Dojos:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def add_dojo(cls, data):
        query = 'INSERT INTO dojos (id), (name) values (%(id)s), (%(name)s;'
        mysql = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return mysql

    @classmethod
    #don't forget to put cls and data
    def save(cls, data):
        #query adds users into data based off user input
        query = 'INSERT INTO dojos (name) values (%(name)s);'
        mysql = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return mysql

    @classmethod
    def Get_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        all_dojos = []
        for dict in results:
            all_dojos.append( cls(dict) )
        return results

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return cls(result[0])

    @classmethod
    def show_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return results