from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
    
app = Flask(__name__)

@app.route("/rahul")
def rahul_2():
    return "welcome, rahul"

app.run(debug = True)

# harry code

# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

# @app.route("/harry")
# def harry():
#     return "Hello harry bhai4!"
# app.run(debug=True)
