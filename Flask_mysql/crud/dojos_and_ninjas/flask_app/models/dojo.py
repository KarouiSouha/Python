from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE
from flask_app.models.ninja import NINJA
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
        VALUES(%(name)s);
        """
        results=MySQLConnection(DATABASE).query_db(query,data)
        return results
    #show all dojos
    @classmethod
    def show_dojos(cls):
        query="""
        SELECT * FROM dojos ;
        """
        results_dojo=MySQLConnection(DATABASE).query_db(query)
        all_dojo=[]
        for row in results_dojo:
            all_dojo.append(cls(row))
        return all_dojo
    #read one ninja from ninjas
    @classmethod
    def show_ninja_in_dojo(cls,data):
        query="""
        SELECT * FROM dojos 
        JOIN ninjas
        ON dojos.id=ninjas.dojo_id
        WHERE dojo.id=%(id)s;
        """
        result=MySQLConnection(DATABASE).query_db(query,data)
        ninjas=[]
        if result:
            this_dojo=cls(result[0])
            for row in result :
                data_test={
                    'id':row['ninjas.id'],
                    'first_name':row['first_name'],
                    'alt_name':row['alt_name'],
                    'created_at':row['ninjas.created_at'],
                    'updated_at':row['ninjas.updated_at']
                }
                ninjas.append(NINJA(data_test))
                this_dojo.ninjas_list=ninjas
                return ninjas
        return []