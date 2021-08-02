from project_app import db

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(), nullable=False)
    num = db.Column(db.String(), nullable=False)


    def __repr__(self):
        return f"<User('{self.id}')>"
