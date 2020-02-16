from tuto13.application import create_app

if __name__ == '__main__':
    flask_app = create_app('dev')
    flask_app.run()
