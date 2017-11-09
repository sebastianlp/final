from flask import Flask, render_template, session, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from wtforms import Form, StringField, PasswordField, validators
from users.user import UserModel
from data.sale import SaleModel
import json
from Forms.client import ClientForm
from Forms.Product import ProductForm

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
    clients = []
    client = ''
    error = False
    form = ClientForm(request.form)
    
    try:
        S = SaleModel()
        clients = list(S.clients())

        if request.method == 'POST' and form.validate():
            client = form.clientName.data
            clientProducts = S.byClient(client)
    except FileNotFoundError:
        error = True
        
    return render_template('client.html', form=form, clients=json.dumps(clients), client=client, products=clientProducts, error=error)

@app.route("/product", methods=['GET', 'POST'])
def product_view():
    if check_user_logged() is False:
        return redirect(url_for('login'))
    
    productsClient = []
    clients = []
    product = ''
    error = False
    form = ProductForm(request.form)

    try:
        S = SaleModel()
        products = list(S.products())

        if request.method == 'POST' and form.validate():
            product = form.productName.data
            productsClient = S.byProduct(product)
    except FileNotFoundError:
        error = True
        
    return render_template('product.html', form=form, products=json.dumps(products), product=product,clients=productsClient, error=error)


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

if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=80, debug=True)