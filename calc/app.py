import operations
from flask import Flask, request

app = Flask(__name__)
# Put your app in here.

@app.route('/add')
operations.add(request.args['a'],request.args['b'])

@app.route('/sub')
operations.sub(request.args['a'],request.args['b'])

@app.route('/mult')
operations.mult(request.args['a'],request.args['b'])

@app.route('/div')
operations.div(request.args['a'],request.args['b'])