from flask import Blueprint, request, render_template, redirect, url_for, flash
from models.user.roles import Role
from models.user.users import User
from werkzeug.security import generate_password_hash
from models.db import db

User_ = Blueprint("User_", __name__, template_folder="views")

@User_.route('/register_user')
def register_user():
    roles = Role.get_role()
    return render_template("register_user.html", roles=roles)

@User_.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        role_name = request.form['role_type_']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        User.save_user(role_name, username, email, password)
        return redirect(url_for('User_.list_users'))

@User_.route('/list_users')
def list_users():
    users = User.query.all()
    return render_template("users.html", devices=users)

@User_.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        role_name = request.form['role_type_']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user.role_id = Role.get_single_role(role_name).id
        user.username = username
        user.email = email
        user.password = generate_password_hash(password)
        db.session.commit()
        return redirect(url_for('User_.list_users'))
    roles = Role.get_role()
    return render_template("edit_user.html", user=user, roles=roles)

@User_.route('/del_user', methods=['GET'])
def del_user():
    username = request.args.get('username')
    user = User.query.filter_by(username=username).first()
    if user:
        role = Role.query.get(user.role_id)
        if role.name == 'Admin':
            flash('Não é possível deletar usuários administradores.')
        else:
            db.session.delete(user)
            db.session.commit()
    return redirect(url_for('User_.list_users'))