from mysqlconnection import connectToMySQL
class USER:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    @classmethod
    def creat(cls, data):
        query ="""
        INSERT INTO users( first_name , last_name , email ) 
        VALUES ( %(first_name)s , %(last_name)s , %(email)s);"""
        return connectToMySQL('users_flask').query_db( query, data )
    @classmethod
    def show_users(cls):
        query="""
        SELECT * FROM users_flask.users;
        """
        raw_user=connectToMySQL('users_flask').query_db( query)
        u=[]
        for x in raw_user:
            u.append(cls(x))
        print(raw_user)
        return u