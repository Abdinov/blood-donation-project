# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from model import location
from model import destination

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        query = request.form['location']
        coordinates = location(query)
        lst = destination(coordinates)
        # print(lst)
        # print(query)
        address = location(query)
        # print(address)
    return render_template('results.html', lst = lst)
