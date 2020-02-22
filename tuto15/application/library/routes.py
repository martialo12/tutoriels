from flask import render_template

from application.library import library
from application.library.models import Book


@library.route('/')
def home():
    books = Book.query.all()
    return render_template('home.html', books=books)
