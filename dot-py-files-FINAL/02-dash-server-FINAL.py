# Hello World super-basic dash server:
# 0. import flask server module
from dash import Dash, html

# 1. instantiate dash app
app = Dash()

# 2. say Hello 
print("Hello World from my cool Dash app!!") # print goes to the terminal command line; when app is launched, the message will print

# 3. output msg to the browser
app.layout = html.H1("My first Dash app at Noble!")

# 4. run app
app.run(debug=True)

# L@@K: to run app, quit old server if running: ctrl-C
# then, type in terminal: python 00-flask-server-dash.py