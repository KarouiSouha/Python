from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
class PARTY :
    def __init__(self,data):
        self.id=data['id']
        self.what=data['what']
        self.location=data['location']
        self.date=data['date']
        self.all_ages=data['all_ages']
        self.user_id=data['user_id']
        self.description=data['description']
    
    @classmethod
    def create_partie(cls,data):
        query="""
        INSERT INTO  parties (what,location,date,all_ages,user_id,description)
        VALUES (%(what)s,%(location)s,%(date)s,%(all_ages)s,%(user_id)s,%(description)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def show_parties(cls):
        query="""
        SELECT * FROM party.parties;
        """
        results=connectToMySQL(DATABASE).query_db(query)
        parties=[]
        for party in results:
            parties.append(cls(party))
        return parties
    
    @classmethod
    def get_one(cls,id):
        query  = "SELECT * FROM parties WHERE id = %(id)s;"
        data = {'id':id}
        result = connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        return result[0]
   