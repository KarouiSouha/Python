from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
class DOJO:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    @classmethod
    #create dojo
    def create_dojo(cls,data):
        query="""
        INSERT INTO dojos (name)
        VALUES(%(name)s);
        """
        result=connectToMySQL(DATABASE).query_db(query,data)
        
        