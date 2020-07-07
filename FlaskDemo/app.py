# coding=utf-8
# python -m flask run
# --host=0.0.0.0
# --port=8000

from flask import Flask, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


# @app.route('/hello')
@app.route('/hello/<name>')
def hello_user(name='User'):
    return '<h1>Hello {}</h1>'.format(name)


@app.route('/hi')
@app.route('/hi/<first_name>/<second_name>')
def hi_user(first_name='a', second_name='aa'):
    return '<h1>Hi {}, {}</h1>'.format(first_name, second_name)


@app.route('/foo/<name>')
def foo(name):
    return '<h1>Foo Page of {}</h1><a href="{}">hello</a>'.format(name, url_for('hello_user', name=name))
