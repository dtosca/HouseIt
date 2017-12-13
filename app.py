#Diana Tosca and Jacqueline Young
import sys
import dbconn2
import dbfunctions
import MySQLdb
import os
import imghdr
from flask import (Flask, render_template, make_response, request, redirect, url_for,session, flash, send_from_directory)
from flask_cas import CAS

app = Flask(__name__)
app.secret_key = 'b@n@N@'

CAS(app)
app.config['CAS_SERVER'] = 'https://login.wellesley.edu:443'
app.config['CAS_AFTER_LOGIN'] = 'logged_in'
app.config['CAS_LOGIN_ROUTE'] = '/module.php/casserver/cas.php/login'
#app.config['CAS_LOGOUT_ROUTE'] = '/module.php/casserver/cas.php/logout'
app.config['CAS_AFTER_LOGOUT'] = 'https://cs.wellesley.edu:1942/scott'
app.config['CAS_VALIDATE_ROUTE'] = '/module.php/casserver/serviceValidate.php'

@app.route('/logged_in/')
def logged_in():
    flash('successfully logged in!')
    return redirect( url_for('index') )
 
@app.route('/')
def index():
    print session.keys()
    for k in session.keys():
        print k,' => ',session[k]
    if '_CAS_TOKEN' in session:
        token = session['_CAS_TOKEN']
    if 'CAS_ATTRIBUTES' in session:
        attribs = session['CAS_ATTRIBUTES']
        for k in attribs:
            print k,' => ',attribs[k]
    if 'CAS_USERNAME' in session:
        is_logged_in = True
        username = session['CAS_USERNAME']
        print('CAS_USERNAME is: ',username)
    else:
        is_logged_in = False
        username = None
        print('CAS_USERNAME is not in the session')
    return render_template('login.html', username=username, is_logged_in=is_logged_in)
 
 
@app.route('/scott/')
def logged_out():
    flash('successfully logged out!')
    return redirect( url_for('index') )


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
            #Get the information from the housing form
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
            #Combine blockmates and roommates into one string
            roomMate = str(roomMate1)+' '+str(roomMate2)+' '+str(roomMate3)
            blockMate = str(blockMate1)+' '+str(blockMate2)+' '+str(blockMate3)
            dbfunctions.formInfo(bnum,roomMate,blockMate)
            #Render the index.html tempates with information filled out
            return render_template('index.html',name=name,bnum=bnum,roomMate=roomMate,blockMate=blockMate,roomType=roomType)
    except Exception as err:
        print 'Exception', str(err)
    return render_template('preferences.html')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=os.getuid()
    app.debug = True
    app.run('0.0.0.0',port)
