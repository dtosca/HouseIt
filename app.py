# Diana Tosca and Jacqueline Young
import sys
import dbconn2
import houseit
import MySQLdb
import os
from flask import (Flask, render_template, make_response,
                    url_for, request, flash, redirect)

app = Flask(__name__)
app.secret_key = 'b@n@N@'

@app.route('/', methods= ['GET','POST'])
def index():
    ''' Index page
    ''' 
    print "********************************************"
    return render_template('index.html')

@app.route('/reshalls/', methods= ['GET','POST'])
def dorms():
    ''' Dorms page
    ''' 
    return render_template('reshalls.html')

@app.route('/faq/', methods= ['GET','POST'])
def faq():
    ''' FAQ page
    ''' 
    return render_template('faq.html')

@app.route('/preferences/', methods= ['GET','POST'])
def pref():
    ''' Preferences page
    '''
    print "in PREF"
    try:
        print "IN TRY"
        if request.method == 'POST':
            print "IN POST"
            firstName = request.form['first-name']
            print "firstname: "+str(firstName)
            return render_template('index.html')
    except Exception as err:
        print 'Exception', str(err)
    return render_template('preferences.html')

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0',os.getgid())
