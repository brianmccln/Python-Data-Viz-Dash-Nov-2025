# L@@K: IF your file name says START, do a Save As and remove the START part

# Setting up a flask server and outputting a simple message

# 0. import flask server module
from flask import Flask

# 1. instantiate flask app
app = Flask(__name__)

# __name__ means current env and allows app to find folders more easily

# 2. say Hello in the browser--browser requires a route
@app.route("/")
def index():
    return """
        <h1>Home</h1>
        <h2>Hello World from Flask app running in the Browser!</h2>
        <h3><a href='/about'>About Me</a></h3>
        <h3><a href='/blog'>Blog</a></h3>
    """
        
# "/" means home or index; it's this browser address: http://127.0.0.1:5000

# all routes require a function on next line; func runs when route addr is hit
# route functions must return a value to the browser

# print goes to the terminal command line; when app is launched, the message will print
print("Hello World from Flask in the Terminal!")

# 3. make another route, this one called '/about' and link the two routes together w html 
@app.route("/about")
def about():
    return """
    <h1>About</h1>
    <h2>About Me: My name is Brian! I teach Python!</h2>
    <h3><a href='/'>Home</a></h3>
    <h3><a href='/blog'>Blog</a></h3>
    """

# LAB:
# make a new route called '/blog' and link to it from all pages -- link all 3 pages together so we can get from any page to the other 2 pages
# have the content be an h1 with the title of your fictitious blog post
# HELPFUL HINT: Wrap your return value tags in "triple-double quotes".. this allows you to hit enter within the text without breaking the code
@app.route("/blog")
def blog():
	return"""
        <h1>My HTML Blog and You</h1>
        <h2>Lets Talk about Blogging and how it affects you!</h2>
        <h3><a href="/">Home</a></h3>
        <h3><a href='/about'>About Me</a></h3>
    """
 
# 4. instruct app to run via command line (terminal) only and to allow changes to code while app is running (w/o having to quit app)
if __name__ == "__main__":
    app.run(debug=True)

# L@@K: to run app, type in terminal: 
# python 01-flask-server.py

# with app running, visit the home route:
# http://127.0.0.1:5000/
# visit the about route (in the browser)
# http://127.0.0.1:5000/about