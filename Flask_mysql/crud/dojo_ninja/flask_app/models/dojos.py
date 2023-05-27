from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE
from flask_app.models.ninjas import NINJA
class DOJO:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.ninjas_list=[]
    @classmethod
    #create dojo
    def create_dojo(cls,data):
        query="""
        INSERT INTO dojos (name)
        VALUES (%(name)s);
        """
        results=MySQLConnection(DATABASE).query_db(query,data)
        return results
    @classmethod
    #show dojo
    def show_dojos(cls):
        query="""
        SELECT * FROM dojos;
        """
        results_dojo=MySQLConnection(DATABASE).query_db(query)
        all_dojo=[]
        for row in results_dojo:
            all_dojo.append(cls(row))
        return all_dojo
    #create one ninja
    @classmethod
    def show_ninja_in_dojo(cls,data):
        query="""
        SELECT * FROM dojos
        JOIN ninjas
        ON dojos.id=ninjas.dojo_id
        WHERE dojo.id=%(id)s;
        """
        results=MySQLConnection(DATABASE).query_db(query,data)
        ninjas=[]
        if results:
            this_dojo=cls(results[0])
            for row in results:
                data_test={
                    'id':row['ninjas.id'],
                    'first_name':row['first_name'],
                    'last_name':row['last_name'],
                    'created_at':row['ninjas.created_at'],
                    'updated_at':row['ninjas.updated_at']
                }
                ninjas.append(NINJA(data_test))
                this_dojo.ninjas_list=ninjas
                return ninjas
        return []
        