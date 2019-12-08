from datetime import datetime

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(

    SECRET_KEY='topsecret',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:Seigneur1@localhost/catalog',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)


@app.route('/index/')
@app.route('/')
def test_flask():
    return "TEST FLASK"


# query strings
@app.route('/test')
def query_strings(voiture='BMW'):
    query_val = request.args.get('voiture', voiture)
    return '<h1> ma voiture est une : {} </h1>'.format(query_val)


# remove query strings
@app.route('/user/')
@app.route('/user/<name>')
def no_query_strings(name='Linda'):
    return '<h1> Bienvenue {} !</h1>'.format(name)


# STRINGS
@app.route('/text/<string:name>')
def working_with_string(name):
    return '<h1> the string you just passed is:' + name + '</h1>'


# NUMBERS
@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> the number you just passed is:' + str(num) + '</h1>'


# sum of 2 integers
@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1, num2):
    return '<h1> the sum is: {}'.format(num1+num2) + '</h1>'


# FLOAT
@app.route('/product/<float:num1>/<float:num2>')
def product_two_numbers(num1, num2):
    return '<h1> the product is: {}'.format(num1*num2) + '</h1>'


# USING TEMPLATE
@app.route('/template/')
def hello():
    return render_template('hello.html')


# using jinja template in html
@app.route('/films')
def films():
    films_dict = {
        'BLACK PANTHER': 2.5,
        'Avengers: Infinity War': 3.2,
        'Ready Player One': 2.14,
        'Les Indestructibles 2': 1.48,
        'Woman at War': 2.52,
        'The Guilty': 1.5,
        'Deadpool 2': 3.5,
        'Mission Impossible - Fallout': 1.7
    }
    return render_template('table_movies.html', films=films_dict, name='Sorelle')


@app.route('/macros')
def films_macros():
    films_dict = {
        'BLACK PANTHER': 2.5,
        'Avengers: Infinity War': 3.2,
        'Ready Player One': 2.14,
        'Les Indestructibles 2': 1.48,
        'Woman at War': 2.52,
        'The Guilty': 1.5,
        'Deadpool 2': 3.5,
        'Mission Impossible - Fallout': 1.7
    }
    return render_template('using_macros.html', films=films_dict)


# PUBLICATION TABLE
class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return ' Publisher  is {}'.format(self.name)


# BOOK TABLE
class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # ESTABLISH A RELATIONSHIP BETWEEN PUBLICATION AND BOOK TABLES
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):

        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return 'title of book is {} by {}'.format(self.title, self.author)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)




