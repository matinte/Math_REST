# > python –m flask run.
# Para que este commando funcione, el archivo ha de llamarse app.py y localizarse donde se ejecuta
# el comando.

import flask

# import math.operations

app = flask.Flask(__name__)


@app.route('/suma', methods=['POST'])
def suma():
    v1 = flask.request.json['v1']
    v2 = flask.request.json['v2']
    return {'result': sum(v1, v2)}

@app.route('/resta', methods=['POST'])
def resta():
    v1 = flask.request.json['v1']
    v2 = flask.request.json['v2']
    return {'result': sum(v1, v2)}

@app.route('/mult', methods=['POST'])
def mult():
    v1 = flask.request.json['v1']
    v2 = flask.request.json['v2']
    return {'result': sum(v1, v2)}

@app.route('/divis', methods=['POST'])
def divis():
    v1 = flask.request.json['v1']
    v2 = flask.request.json['v2']
    return {'result': sum(v1, v2)}
