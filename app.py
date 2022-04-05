import flask
import Operations
# app.py class to execute flask server endpoints with Operations methods:
# > python –m flask run.

app = flask.Flask(__name__)

@app.route('/suma', methods=['POST'])
def suma_service():
    v1 = flask.request.json['v1']
    v2 = flask.request.json['v2']
    return {'result': Operations.Operations.suma(v1, v2)}

@app.route('/resta', methods=['POST'])
def resta_service():
    v1 = flask.request.json['v1']
    v2 = flask.request.json['v2']
    return {'result': Operations.Operations.resta(v1, v2)}

@app.route('/mult', methods=['POST'])
def mult_service():
    v1 = flask.request.json['v1']
    v2 = flask.request.json['v2']
    return {'result': Operations.Operations.mult(v1, v2)}

@app.route('/divis', methods=['POST'])
def divis_service():
    v1 = flask.request.json['v1']
    v2 = flask.request.json['v2']
    return {'result': Operations.Operations.divis(v1, v2)}
