from app import app, db, login, admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(256))

    # setup password hash methods
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # setup password check method
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# add user loader; finds correct user to login when login_user is called
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
