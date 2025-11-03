# L@@K: IF your file name says START, do a Save As and remove the START part

# Setting up a flask server and outputting a simple message

# 0. import flask server module

# 1. instantiate flask app

# __name__ means current env and allows ap to find folders more easily

# 2. say Hello in the browser--browser requires a route

# "/" means home or index; it's this browser address: http://127.0.0.1:5000

# all routes require a function on next line; func runs when route addr is hit
# route functions must return a value to the browser

# print goes to the terminal command line; when app is launched, the message will print

# 3. make another route, this one called '/about' and link the two routes together w html 

# 4. instruct app to run via command line (terminal) only and to allow changes to code while app is running (w/o having to quit app)

# L@@K: to run app, type in terminal: python 01-flask-server.py