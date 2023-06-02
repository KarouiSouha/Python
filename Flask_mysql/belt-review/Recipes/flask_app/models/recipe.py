from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import user


class RECIPE :
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instructions=data['instructions']
        self.date=data['date']
        self.under_30=data['under_30']
        self.user_id=data['user_id']
        self.posted=user.USER.get_by_id({'id':self.user_id})
    @classmethod
    def create_recipe(cls,data):
        query="""
        INSERT INTO  recipes (name,description,instructions,date,under_30,user_id)
        VALUES (%(name)s,%(description)s,%(instructions)s,%(date)s,%(under_30)s,%(user_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def show_recipe(cls):
        query="""
        SELECT * FROM recipes;
        """
        results=connectToMySQL(DATABASE).query_db(query)
        recipes=[]
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
    
    @classmethod
    def get_one(cls,data):  # JOIN user 
            # ON recipes.user_id = user.id
            query  = """SELECT * FROM recipes
            WHERE id = %(id)s;"""
            result = connectToMySQL(DATABASE).query_db(query,data)
            return cls(result[0])
            # all_recipes = []

            # for row in result:
            #     this_recipe = cls(row)
            #     user_data = {
            #         "id": row["user.id"],
            #         "first_name": row["first_name"],
            #         "last_name": row["last_name"],
            #         "email": row["email"],
            #         "password": row["password"],
            #         "created_at": row["user.created_at"],
            #         "updated_at": row["user.updated_at"],
            #     }
            #     this_user = user.USER(user_data)
            #     this_recipe.posted = this_user
            #     all_recipes.append(this_recipe)
            # return all_recipes
        



    @classmethod
    def get_all(cls):
            query = """
                        SELECT * FROM recipes
                            JOIN user
                            ON recipes.user_id = user.id ;
                    """
            results = connectToMySQL(DATABASE).query_db(query)

            all_recipes = []

            for row in results:
                this_recipe = cls(row)


                user_data = {
                    "id": row["user.id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "email": row["email"],
                    "password": row["password"],
                    "created_at": row["user.created_at"],
                    "updated_at": row["user.updated_at"],
                }

                this_user = user.USER(user_data)
                this_recipe.posted = this_user
                all_recipes.append(this_recipe)
            return all_recipes
        
        
        
    @classmethod
    def update(cls,data):
            query = """
            UPDATE recipes
            SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,date=%(date)s,under_30=%(under_30)s,user_id=%(user_id)s
            WHERE id = %(id)s;"""
            return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete(cls,data):
            query  = """DELETE FROM recipes 
            WHERE id = %(id)s;"""
            return connectToMySQL(DATABASE).query_db(query,data)