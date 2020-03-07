from flask import render_template

from application.library import library
from application.library.models import Book, Publication


@library.route('/')
def display_books():
    books = Book.query.all()
    return render_template('home.html', books=books)


@library.route('/display/publisher/<publisher_id>')
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Book.query.filter_by(pub_id=publisher.id).all()
    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)



