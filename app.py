from flask import Flask, render_template, session, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from wtforms import Form, StringField, PasswordField, validators
from users.user import UserModel
from data.sale import SaleModel

app = Flask(__name__)
Bootstrap(app)

def check_user_logged():
    if session.get('username') is None:
        return False

    return True

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = False

    try:
        U = UserModel()
        if request.method == 'POST':
            username = request.form['username']
            if U.authenticate(username=username, password=request.form['password']):
                session['username'] = request.form['username']
                return redirect(url_for('private_main'))
    except FileNotFoundError:
        error = True
    
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

    error = False

    try:
        S = SaleModel()
        data = S.data
        headers = S.headers
    except FileNotFoundError:
        error = True

    return render_template('private.html', data=data, headers=headers, error=error)

@app.route("/client", methods=['GET', 'POST'])
def client_view():
    if check_user_logged() is False:
        return redirect(url_for('login'))

    clientProducts = []
    client = ''
    error = False
    
    try:
        S = SaleModel()

        if request.method == 'POST':
            client = request.form['client']
            clientProducts = S.byClient(client)
    except FileNotFoundError:
        error = True
        
    return render_template('client.html', client=client, products=clientProducts, error=error)

@app.route("/client/best")
def best_clients_view():
    error = False
    bestClients = []

    try:
        S = SaleModel()
        bestClients = S.bestClients()
    except FileNotFoundError:
        error = True

    return render_template('best_clients.html', error=error, bestClients=bestClients)

@app.route("/product/most")
def most_products_view():
    error = False
    mostProducts = []

    try:
        S = SaleModel()
        mostProducts = S.mostSold()
    except FileNotFoundError:
        error = True

    return render_template('most_products.html', error=error, mostProducts=mostProducts)

# @app.route("/clientasd", methods=['GET', 'POST'])
# def client_view_():
#     app.logger.info(S.groupBy(S.byClient('pedo')))

@app.route("/product", methods=['GET', 'POST'])
def product_view():
    if check_user_logged() is False:
        return redirect(url_for('login'))
    
    clients = []
    product = ''
    error = False

    try:
        S = SaleModel()

        if request.method == 'POST':
            product = request.form['product']
            clients = S.byProduct(product)
    except FileNotFoundError:
        error = True
        
    return render_template('product.html', product=product,clients=clients, error=error)

if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=80, debug=True)