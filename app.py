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
app.config['CAS_LOGOUT_ROUTE'] = '/module.php/casserver/cas.php/logout'
app.config['CAS_AFTER_LOGOUT'] = 'https://cs.wellesley.edu:1942/scott'
app.config['CAS_VALIDATE_ROUTE'] = '/module.php/casserver/serviceValidate.php'

@app.route('/logged_in/')
def logged_in():
    flash('successfully logged in!')
    return redirect( url_for('home') )

@app.route('/home/')
def home():
    if 'CAS_ATTRIBUTES' in session:
        attribs = session['CAS_ATTRIBUTES']
        name = attribs['cas:givenName']+' '+attribs['cas:sn']
        username = session['CAS_USERNAME']
        userInDB = dbfunctions.userInDB(username)
        print "Is the user in DB? :"+str(userInDB)
        if(not userInDB):
            dbfunctions.insertStud(username,name)
    return render_template('index.html',name=name,username=username)

@app.route('/')
def index():
    name = ""
    username = ""
    print session.keys()
    for k in session.keys():
        print k,' => ',session[k]
    if '_CAS_TOKEN' in session:
        token = session['_CAS_TOKEN']
    if 'CAS_ATTRIBUTES' in session:
        attribs = session['CAS_ATTRIBUTES']
        name = attribs['cas:givenName']+' '+attribs['cas:sn']
        username = session['CAS_USERNAME']
    if 'CAS_USERNAME' in session:
        is_logged_in = True
        username = session['CAS_USERNAME']
        print('CAS_USERNAME is: ',username)
    else:
        is_logged_in = False
        username = None
        print('CAS_USERNAME is not in the session')    
    return render_template('login.html',name=name,username=username, is_logged_in=is_logged_in)
 
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
    name = ""
    username = ""
    try:
        if 'CAS_ATTRIBUTES' in session:
            attribs = session['CAS_ATTRIBUTES']
            name = attribs['cas:givenName']+' '+attribs['cas:sn']
            username = session['CAS_USERNAME']
        if request.method == 'POST':
            print "IN REQUEST POST"
            #Get the information from the housing form
            print "GETTINGS RANKINGS"
            ranking1 = request.form['ranking1']
            ranking2 = request.form['ranking2']
            ranking3 = request.form['ranking3']
            ranking4 = request.form['ranking4']
            ranking5 = request.form['ranking5']
            print "ROOM TYPE"
            roomType1 = request.form['rt1']
            roomType2 = request.form['rt2']
            roomType3 = request.form['rt3']
            print "PRINTING ROOMATES"
            roomMate1 = request.form['roommate1']
            roomMate2 = request.form['roommate2']
            roomMate3 = request.form['roommate3']
            print "BLOCKMATES"
            blockMate1 = request.form['blockmate1']
            blockMate2 = request.form['blockmate2']
            blockMate3 = request.form['blockmate3']
            blockMate4 = request.form['blockmate4']
            print "NEEDY"
            needsList = request.form.getlist('needs')
            needs = {'nuts':'0', 'pets':'0', 'hardwood':'0', 'accessible':'0'}
            for need in needs:
                if need in needsList:
                    needs[need] = '1'
                    
            #Combine blockmates and roommates into one string
            rankings = str(ranking1)
            roomType = str(roomType1)
            roomMate = str(roomMate1)+' '+str(roomMate2)+' '+str(roomMate3)
            blockMate = str(blockMate1)+' '+str(blockMate2)+' '+str(blockMate3)+' '+str(blockMate4)
            dbfunctions.updateStud(username,rankings,roomType,roomMate,blockMate,needs['nuts'],needs['pets'],needs['hardwood'],needs['accessible'])
            okRooms = dbfunctions.getRooms(rankings,roomType,needs['nuts'],needs['pets'],needs['hardwood'],needs['accessible'])
            print okRooms
            #Render the index.html tempates with information filled out
            return render_template('index.html',name=name,username=username,dorms=rankings,roomMate=roomMate,blockMate=blockMate,room_type=roomType,nuts=str(needs['nuts']),pets=str(needs['pets']),hardwood=str(needs['hardwood']),acc=str(needs['accessible']),rooms=okRooms,lottery_num='365')
    except Exception as err:
        print "IN EXCEPTIONS*********************************************************"
        print 'Exception', str(err)
    return render_template('preferences.html')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=os.getuid()
    app.debug = True
    app.run('0.0.0.0',port)
