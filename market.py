from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# To install the application: pip install flask
# To run the application successfully, we are required to set up some environment variables: set FLASK_APP=market.py
# To activate the debug mode, which allows your file to be automatically updated: set FLASK_DEBUG=1

app = Flask(__name__)                               #name of db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'                       # In other for Flask to recognize the db, we need to add some configurations

db = SQLAlchemy(app) #This is basically to initialize the sqlalchemy and connect it to our flaskapp


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(), nullable=False, unique=True)
    description= db.Column(db.String(length=1024), nullable=False, unique=True)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

                    #Dynamic Routes
@app.route('/about/<username>')
def aboutPage(username):
    return f'<h1>This is about the about page of {username}</h1>'

# Styling and Templates
@app.route("/market")
def market_page():
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
]
    return render_template('market.html', item=items) 
# In order for our html file to access this data we are accessing, we have to use something called a templating engine called jinja Template, this basically just involves adding double curly bracees and the name of the variable you want to access

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
