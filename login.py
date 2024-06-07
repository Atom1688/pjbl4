from flask import render_template, request, Blueprint

users = {
    'admin': 'admin',
    'rafael': '12345',
    'matheus': '54321'
}

current_user = ''

login = Blueprint("login", __name__)

@login.route('/')
def index():
    return render_template("login/login.html")

@login.route('/home')
def home():
    if current_user == 'admin':
        return render_template("admin_home.html", user=current_user)
    else:
        return render_template("user_home.html", user=current_user)


@login.route('/validated_user', methods=['POST'])
def validated_user():
    global current_user
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        if user in users and users[user] == password:
            current_user = user
            if user == 'admin':
                return render_template('admin_home.html', user=current_user)
            else:
                return render_template('user_home.html', user=current_user)
        else:
            return render_template('login/invalid_credentials.html')
    else:
        return render_template('login/login.html')