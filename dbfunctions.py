import dbconn2
import MySQLdb
import os
import sys
import re
from flask import (Flask, render_template, make_response,
                    url_for, request, flash, redirect)

DATABASE = 'houseit_db'
DEST_DIR = '/home/cs304/public_html/images/'
DEST_URL = '/~cs304/images/'
IN_DB    = False                # false means store in dest_dir
MAX_FILE_SIZE = 100000          # 100 KB

#Establish the connection with the database                            
def cursor(database=DATABASE):
        DSN = dbconn2.read_cnf()
        DSN['db'] = database
        conn = dbconn2.connect(DSN)
        return conn.cursor(MySQLdb.cursors.DictCursor)

#returns whether the user that just logged in is in the database
def userInDB(username):
	curs = cursor()
	#checking the student table by the username that was entered
	curs.execute('select * from student where username=%s',(username,))
	row = curs.fetchone()
	return (row is not None)

#inserts student into the student table
def insertStud(username,nm):
        curs = cursor()
        curs.execute('insert into student(username, nm) values (%s,%s)', (username,nm,))
        print 'Done inserting new student user'

def updateDorms(choice1,choice2,choice3,choice4,choice5,username):
	curs = cursor()
	curs.execute('UPDATE student SET dormChoice1=%s, dormChoice2=%s, dormChoice3=%s where username=%s', (choice1,choice2,choice3,username,))
	print 'Done updating dorm rankings'

#update the student table with the given parameters
def updateStud(username,roomType,roomMates,blockMates,nuts,pets,hardwood,acc):
	print 'In updateStud'
	print nuts
        curs = cursor()
	curs.execute('UPDATE student SET roomMates=%s, blockMates=%s,room_type=%s, nuts=%s, pets=%s, hardwood=%s, acc=%s where username=%s', (roomMates, blockMates, roomType, nuts, pets, hardwood, acc, username))

#get list of rooms that match the parameters exactly
#Need to expand this to return list of rooms that account for all the rooms students can use
#Example: If a student doesn't need a hardwood room, the hardwood rooms should still be displayed. Right now, they are not being displyed
def getRooms(dorm,roomType,nuts,pets,hardwood,acc):
	print 'in getRooms'
	curs = cursor()
        curs.execute('select * from room where dorm=%s and room_type=%s and nuts=%s and hardwood=%s and pets=%s and acc=%s and available=%s',(dorm,roomType,nuts,pets,hardwood,acc,'1'))
	return curs.fetchall()

#inserts or updates picture blob for a student
def storePicInDB(username,client_filename,file_data):
    curs = cursor()
    ## Test if the file was uploaded
    if not client_filename:
        return 'No file uploaded (yet)'
    try:
        curs.execute('UPDATE student SET pic=%s where username = %s',(file_data,username))
    except Exception as e:
        print e
        return 'Failure to store picture data into database: '+str(e)
    return 'Successfully uploaded picture data for username='+str(username)

def getPic(username):
    curs = cursor()
    curs.execute('SELECT pic FROM student WHERE username=%s',(username,))
    return curs.fetchone()
