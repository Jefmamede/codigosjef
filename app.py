from flask import Flask
app = Flask(__name__)
@app.route('/') #Este comando cria uma página 
def index(): # Mostrando um texto na página criada
	return "Hello World"
