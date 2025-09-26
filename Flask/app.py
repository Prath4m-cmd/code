from flask import Flask
'''
It creates an instance of the Flask class,
which will be your WSGI (web server gateway interface) application.
'''
### WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the best flask program. This is a Home page"

@app.route("/index")
def index():
    return "Welcome to index page"

if __name__=="__main__":
    app.run(debug=True)
