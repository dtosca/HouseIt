#Diana Tosca and Jacqueline Young
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
    try:
        if request.method == 'POST':
            firstName = request.form['first-name']
            lastName = request.form['last-name']
            bnum = request.form['bnum']
            roomMate1 = request.form['roommate1']
            roomMate2 = request.form['roommate2']
            roomMate3 = request.form['roommate3']
            roomType = request.form['dropdown1']
            blockMate1 = request.form['blockmate1']
            blockMate2 = request.form['blockmate2']
            blockMate3 = request.form['blockmate3']
            name = str(firstName) + ' ' + str(lastName)
            roomMate = str(roomMate1)+' '+str(roomMate2)+' '+str(roomMate3)
            blockMate = str(blockMate1)+' '+str(blockMate2)+' '+str(blockMate3) 
            return render_template('index.html',name=name,bnum=bnum,roomMate=roomMate,blockMate=blockMate,roomType=roomType)
    except Exception as err:
        print 'Exception', str(err)
    return render_template('preferences.html')

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0',os.getgid())
