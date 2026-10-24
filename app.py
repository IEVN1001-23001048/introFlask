from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    titulos:"PWA"
    listas(6)
    return render_template("index.html")

@app.route('/hola')
def func():
    return"hola otra vez"

@app.route('/user/<string:user>')
def pepe(user):
    return"hola: " + user

@app.route('/user/<int:n>')
def numero(n):
    return"numero: {}".format(n) 

@app.route('/user/<int:id>/<string:username>')
def username(id,username):
    return"ID: {} Nombre: {}".format(id,username) 

@app.route('/suma/<int:n1>/<int:n2>')
def suma(n1,n2):
    return"La suma es: {}".format(n1+n2)
     

if __name__=="__main__":
        app.run(debug=True)