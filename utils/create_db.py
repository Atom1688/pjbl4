from flask import Flask
from models import *



def create_db(app:Flask):
    with app.app_context():
        db.drop_all()
        db.create_all()

def create_db(app:Flask):
    with app.app_context():
        db.drop_all()
        db.create_all()
        Role.save_role( "Admin", "Usuário full" )
        Role.save_role( "User", "Usuário com limitações")
        User.save_user("Admin","Admin", "admin","admin")

def get_single_role(name):
    role = Role.query.filter(Role.name == name).first()
    return role

def get_role():
    role = Role.query.all()
    return role


if __name__ == "__main__":
    from app import app  # Certifique-se de que 'app' seja a instância do Flask no seu arquivo 'app.py'
    create_db(app)
