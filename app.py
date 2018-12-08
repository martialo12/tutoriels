from flask import Flask, request, render_template

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)



