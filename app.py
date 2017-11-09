from flask import Flask, render_template, session, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from wtforms import Form, StringField, PasswordField, validators
from users.user import UserModel
from data.sale import SaleModel

S = SaleModel()
U = UserModel()

app = Flask(__name__)
Bootstrap(app)

def check_user_logged():
    if session.get('username') is None:
        return False

    return True

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
    if check_user_logged() is False:
        return redirect(url_for('login'))

    session.pop('username', None)
    return redirect(url_for('main'))

@app.route("/private")
def private_main():
    if check_user_logged() is False:
        return redirect(url_for('login'))

    return render_template('private.html')

@app.route("/client", methods=['GET', 'POST'])
def client_view():
    if check_user_logged() is False:
        return redirect(url_for('login'))

    clientProducts = []
    client = ''  
    
    if request.method == 'POST':
        client = request.form['client']
        clientProducts = S.byClient(client)
        
    return render_template('client.html', client=client, products=clientProducts)

# @app.route("/clientasd", methods=['GET', 'POST'])
# def client_view_():
#     app.logger.info(S.groupBy(S.byClient('pedo')))

@app.route("/product", methods=['GET', 'POST'])
def product_view():
    if check_user_logged() is False:
        return redirect(url_for('login'))
    
    clients = []
    product = ''

    if request.method == 'POST':
        product = request.form['product']
        clients = S.byProduct(product)

    return render_template('product.html', product=product,clients=clients)

if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=80, debug=True)