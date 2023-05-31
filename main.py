#from asyncio.windows_events import NULL
from dataclasses import replace
#from pynput import keyboard
from flask import Flask, render_template, request, make_response, redirect
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'
global m
m=""
@app.route('/')
def index():
    return render_template("home.html")
@app.route("/about")    
def about():
    return render_template("about.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
@app.route('/donate')
def donate():
    return render_template("donate.html")




        

        

            


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)

