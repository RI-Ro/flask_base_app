from app import app
from flask_restful import Api, Resource
from flask import render_template
from app import db
from .models import User

@app.route('/')
def index():
    return render_template("index.html")


### flask_restful
api = Api(app)

class UsersListShow(Resource):
    def get(self):
        usersFromDB = User.query.all()
        users = [user.serialize for user in usersFromDB]
        return {
                "users" :   users
                }

class UsersListAdd(Resource):
    def get(self):
        import random
        randomID = random.randint(1000, 100000)
        u = User(username=f"username № {randomID}")
        db.session.add(u)
        db.session.commit()
        return {
                "add new user id"   :   u.id
                }

api.add_resource(UsersListShow, "/api/users/")
api.add_resource(UsersListAdd, "/api/users/add/")