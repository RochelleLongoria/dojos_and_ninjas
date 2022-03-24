from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojos
class Ninjas:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['upated_at']
        self.dojo_id = data['dojo_id']
        
    # Now we use class methods to query our database


    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) 
                            values (%(first_name)s, %(last_name)s, %(age)s, Now(), Now() , %(dojo_id)s);
                """
        mysql = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return mysql

    @classmethod
    def view_ninja(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return results

    
    # @classmethod
    # def dojo_roster(cls, data):
    #     query = "Select * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        
    #     results = connectToMySQL('dojo_ninjas').query_db(query,data)
    #     print(results)
    #     dojo = cls(results[0])
    #     for row in results:
    #         d = {
    #             'id': row['ninjas.id'],
    #             'first_name': row['first_name'],
    #             'last_name': row['last_name'],
    #             'age': row['age'],
    #             'created_at': row['ninjas.created_at'],
    #             'updated_at': row['ninjas.updated_at']
    #         }
    #         dojo.ninjas.append(Ninjas(d))
    #         return dojo

    