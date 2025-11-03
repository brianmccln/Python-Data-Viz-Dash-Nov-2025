# Hello World super-basic flask server:
# 0. import flask server module
from flask import Flask

# 1. instantiate flask app
app = Flask(__name__) # __name__ means current env and allows ap to find folders more easily

# 2. say Hello in the browser--browser requires a route
@app.route("/") # "/" means home or index; it's this browser address: http://127.0.0.1:5000
def index(): # all routes require a function on next line; func runs when route addr is hit
    return "<h1>Hello World..!!!</h1><h2><a href='/about'>About Me</a></h2>" # route functions must return a value to the browser

print("Hello World") # print goes to the terminal command line; when app is launched, the message will print

# 3. make another route, this one called '/about' and link the two routes together w html 
@app.route("/about")
def about():
    return "<h1>About Me</h1><h2>Hi! I'm Brian! I teach Python!</h2><h3><a href='/'>Home</a></h3>"

# 4. instruct app to run via command line (terminal) only and to allow changes to code while app is running (w/o having to quit app)
if __name__ == "__main__":
    app.run(debug=True)

# L@@K: to run app, type in terminal: python 01-flask-server.py