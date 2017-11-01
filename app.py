from flask import Flask, render_template, session, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from wtforms import Form, StringField, PasswordField, validators
from views.client import ClientView
from views.product import ProductView
from users.user import UserModel

U = UserModel()

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        if U.authenticate(username=username, password=request.form['password']):
            session['username'] = request.form['username']
            flash('Login exitoso')
            return redirect(url_for('private_main'))
        else:
            error = 'Credenciales invalidas'
    return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('main'))

@app.route("/private")
def private_main():
    return render_template('private.html')

app.add_url_rule('/client', view_func=ClientView.as_view('client_view'))

app.add_url_rule('/product', view_func=ProductView.as_view('product_view'))

if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=80, debug=True)