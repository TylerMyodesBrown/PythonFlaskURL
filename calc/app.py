import operations
from flask import Flask, request

app = Flask(__name__)
# Put your app in here.

@app.route('/add')
def add_oper():
    operations.add(request.args['a'],request.args['b'])

@app.route('/sub')
def sub_oper():
    operations.sub(request.args['a'],request.args['b'])

@app.route('/mult')
def mult_oper():
    operations.mult(request.args['a'],request.args['b'])

@app.route('/div')
def div_oper():
    operations.div(request.args['a'],request.args['b'])