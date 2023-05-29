from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE
class USER:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    @classmethod
    def create_user(cls,data):
        query="""
        INSERT INTO  users(first_name,last_name,email)
        VALUES (%(first_name)s,%(last_name)s,%(email)s);
        """
        return MySQLConnection('users_flask').query_db(query,data)
    
    @classmethod
    def show_users(cls):
        query="""
        SELECT * FROM users_flask.users;
        """
        results=MySQLConnection('users_flask').query_db(query)
        userdict=[]
        for user in results:
            userdict.append(cls(user))
        return userdict
    
    @classmethod
    def get_one(cls,id):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        data = {'id':id}
        result = MySQLConnection('users_flask').query_db(query,data)
        print(result)
        return result[0]

    @classmethod
    def update(cls,data):
        query = """
        UPDATE users
        SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() 
        WHERE id = %(id)s;"""
        return MySQLConnection('users_flask').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = """DELETE FROM users 
        WHERE id = %(id)s;"""
        return MySQLConnection('users_flask').query_db(query,data)
