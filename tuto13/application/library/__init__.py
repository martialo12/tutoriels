from flask import Blueprint

library = Blueprint('library', __name__, template_folder='templates')

from tuto13.application.library import routes