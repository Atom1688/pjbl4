from models.db import db
from models.user.roles import Role
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__= "users"
    id = db.Column("id", db.Integer(), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    @staticmethod
    def save_user(role_type_, username, email, password):
        role = Role.get_single_role(role_type_)
        user = User(role_id=role.id, username=username, email=email, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def update_user(user_id, role_name, username, email, password):
        user = User.query.get(user_id)
        if user:
            user.role_id = Role.get_single_role(role_name).id
            user.username = username
            user.email = email
            user.password = generate_password_hash(password)
            db.session.commit()

    @staticmethod
    def delete_user(username):
        user = User.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
