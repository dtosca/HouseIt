# Diana Tosca and Jacqueline Young
import sys
import MySQLdb
import dbconn2
import hwk6
import os
from flask import (Flask, render_template, make_response,
                    url_for, request, flash, redirect)

app = Flask(__name__)
app.secret_key = 'b@n@N@'

@app.route('/', methods= ['GET','POST'])
def index():
    ''' Index page
    ''' 
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0',os.getgid())
