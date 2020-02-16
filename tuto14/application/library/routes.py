from application.library import library


@library.route('/')
def hello():
    return 'hello world!'
