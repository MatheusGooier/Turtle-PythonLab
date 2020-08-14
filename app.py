from flask import Flask, request, json
from pymongo import MongoClient


client = MongoClient()
db = client.turtle
registros = db.contatos

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Home page'


@app.route('/consultaregistros')
def consultaregistros():
    resultados = registros.find()
    retorno = []
    for reg in resultados:
        reg.pop('_id')
        retorno.append(reg)        
    return json.jsonify(retorno)


@app.route('/consultaregistrosemail')
def consultaregistrosemail():
    email = request.args.get('email')
    resultados = registros.find({"email": email})    
    retorno = [] 
    
    if(resultados.count() == 0):
        return 'Nenhum registro encontrado com este e-mail'
    
    for reg in resultados:
        reg.pop('_id')
        retorno.append(reg)        
    
    return json.jsonify(retorno)


app.run()     	