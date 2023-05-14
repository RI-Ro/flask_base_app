from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(64))

    def __repr__(self):
        return f"<User {self.username}>"

    @property    
    def serialize(self):
        return {
        "id"		:	self.id,
		"username"	:	self.username
		}