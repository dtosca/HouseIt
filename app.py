#Diana Tosca and Jacqueline Young
import sys
import dbconn2
import dbfunctions
import MySQLdb
import os
import imghdr
from flask import (Flask, render_template, make_response, request, redirect, url_for,session, flash, send_from_directory)
from flask_cas import CAS
from werkzeug import secure_filename

app = Flask(__name__)
app.secret_key = 'b@n@N@'

#CAS routes
CAS(app)
app.config['CAS_SERVER'] = 'https://login.wellesley.edu:443'
app.config['CAS_AFTER_LOGIN'] = 'logged_in'
app.config['CAS_LOGIN_ROUTE'] = '/module.php/casserver/cas.php/login'
app.config['CAS_LOGOUT_ROUTE'] = '/module.php/casserver/cas.php/logout'
app.config['CAS_AFTER_LOGOUT'] = 'https://cs.wellesley.edu:1942/scott'
app.config['CAS_VALIDATE_ROUTE'] = '/module.php/casserver/serviceValidate.php'

#url route for after logging in, redirects to "home"
@app.route('/logged_in/')
def logged_in():
    flash('successfully logged in!')
    return redirect( url_for('home'))

#home page that displays main information. After user logs in with CAS, their username and full name is displayed. 
#Varibles retrieved through session.
@app.route('/home/')
def home():
    if 'CAS_ATTRIBUTES' in session:
        attribs = session['CAS_ATTRIBUTES']
        name = attribs['cas:givenName']+' '+attribs['cas:sn']
        username = session['CAS_USERNAME']
	#checks if the user that logged is in our database
        userInDB = dbfunctions.userInDB(username)
        print "Is the user in DB? :"+str(userInDB)
	#if the user is not the database, insert them into the student table
        if(not userInDB):
            dbfunctions.insertStud(username,name)
    return render_template('index.html',name=name,username=username)

#Renders template for login, redirecting to Wellesley login.
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
    ''' Dorms page, information for all of the dorms.
    ''' 
    return render_template('reshalls.html')

@app.route('/faq/', methods= ['GET','POST'])
def faq():
    ''' FAQ page, page with fill in  FAQ information.
    ''' 
    return render_template('faq.html')

@app.route('/uploader/', methods = ['GET','POST'])
def uploader():
    name = ""
    username = ""
    #get the username and full name from session
    if 'CAS_ATTRIBUTES' in session:
        attribs = session['CAS_ATTRIBUTES']
        name = attribs['cas:givenName']+' '+attribs['cas:sn']
        username = session['CAS_USERNAME']
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        print 'file uploaded successfully'
        dbfunctions.storePicInDB(username,f.filename,f)
        pic = dbfunctions.getPic(username)
        return redirect(url_for('home',picture=str(pic)))

@app.route('/preferences/', methods= ['GET','POST'])
def pref():
    ''' Preferences page, page to fill out preferences, which store the information in the database and sends it back to front end.
    '''
    if not 'CAS_USERNAME' in session:
        return redirect(url_for('index'))
    else:
        #initializing name and username to display on the home.html page
        name = ""
        username = ""
        try:
	    #get the username and full name from session
            if 'CAS_ATTRIBUTES' in session:
                attribs = session['CAS_ATTRIBUTES']
                name = attribs['cas:givenName']+' '+attribs['cas:sn']
                username = session['CAS_USERNAME']

	    #get all the information from the form once it is submitted
            if request.method == 'GET':
                print "IN REQUEST GET"
            if request.method == 'POST':
                print "IN REQUEST POST"

                #Gets information from the dorm rankings section of form
                ranking1 = request.form['ranking1']
                ranking2 = request.form['ranking2']
                ranking3 = request.form['ranking3']
                ranking4 = request.form['ranking4']
                ranking5 = request.form['ranking5']

	        #Gets information from the room type (single,double,etc) section of form
                roomType1 = request.form['rt1']
                roomType2 = request.form['rt2']
                roomType3 = request.form['rt3']

                #Gets information from request roommates section.
                roomMate1 = request.form['roommate1']
                roomMate2 = request.form['roommate2']
                roomMate3 = request.form['roommate3']

                #Gets infomation for requested blockmakes sections
                blockMate1 = request.form['blockmate1']
                blockMate2 = request.form['blockmate2']
                blockMate3 = request.form['blockmate3']
                blockMate4 = request.form['blockmate4']

                #Gets list of necessary room attributes from the room checkboxes in the form
                needsList = request.form.getlist('needs')

	        #created a dictionary for the room attributes filled out in the form
                needs = {'nuts':'0', 'pets':'0', 'hardwood':'0', 'accessible':'0'}

	        #Go through the needs list and update the need dictionary
                for need in needs:
                    if need in needsList:
                        needs[need] = '1'
                    
                #Combine blockmates and roommates into one string for display purposes
                rankings = str(ranking1)
                roomType = str(roomType1)
                roomMate = str(roomMate1)+' '+str(roomMate2)+' '+str(roomMate3)
                blockMate = str(blockMate1)+' '+str(blockMate2)+' '+str(blockMate3)+' '+str(blockMate4)

                #call function to update dorm choices in student db
                dbfunctions.updateDorms(ranking1,ranking2,ranking3,ranking4,ranking5,username)

	        #call function to update student table, given the parameters filled out in the form
                dbfunctions.updateStud(username,roomType,roomMate,blockMate,needs['nuts'],needs['pets'],needs['hardwood'],needs['accessible'])

	        #call function to get the list of rooms that fit the criteria filled out in the form
                okRooms = dbfunctions.getRooms(rankings,roomType,needs['nuts'],needs['pets'],needs['hardwood'],needs['accessible'])
                print okRooms

                #Render the index.html tempates with information filled out
                return render_template('index.html',name=name,username=username,dorms=rankings,roomMate=roomMate,blockMate=blockMate,room_type=roomType,nuts=str(needs['nuts']),pets=str(needs['pets']),hardwood=str(needs['hardwood']),acc=str(needs['accessible']),rooms=okRooms,lottery_num='365')
        except Exception as err:
            print "IN EXCEPTIONS"
            print 'Exception', str(err)
        #if an error occurs, stay on the preferences.html page
        return render_template('preferences.html')

@app.route('/bates/')
def bates():
    return render_template('bates.html')
@app.route('/beebe/')
def beebe():
    return render_template('beebe.html')
@app.route('/casacervantes/')
def casacervantes():
    return render_template('casacervantes.html')
@app.route('/cazenove/')
def cazenove():
    return render_template('cazenove.html')
@app.route('/claflin/')
def claflin():
    return render_template('claflin.html')
@app.route('/dower/')
def dower():
    return render_template('dower.html')
@app.route('/freeman/')
def freeman():
    return render_template('freeman.html')
@app.route('/frenchhouse/')
def frenchhouse():
    return render_template('frenchhouse.html')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=os.getuid()
    app.debug = True
    app.run('0.0.0.0',port)
