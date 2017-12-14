import dbconn2
import MySQLdb
import os
import sys
from flask import (Flask, render_template, make_response,
                    url_for, request, flash, redirect)

DATABASE = 'houseit_db'

#Establish the connection with the database                            
def cursor(database=DATABASE):
        DSN = dbconn2.read_cnf()
        DSN['db'] = database
        conn = dbconn2.connect(DSN)
        return conn.cursor(MySQLdb.cursors.DictCursor)

def userInDB(username):
	curs = cursor()
	curs.execute('select * from student where username=%s',(username,))
	row = curs.fetchone()
	print row
	return (row is not None)

def insertStud(username,nm):
	print 'In insertStud'
        curs = cursor()
        curs.execute('insert into student(username, nm) values (%s,%s)', (username,nm,))
        print 'Done inserting new student user'

def updateStud(username,dorm,roomType,roomMates,blockMates,nuts,pets,hardwood,acc):
	print 'In updateStud'
	print nuts
        curs = cursor()
	curs.execute('UPDATE student SET dorm=%s, room_type=%s, nuts=%s, pets=%s, hardwood=%s, acc=%s where username=%s', (dorm, roomType, nuts, pets, hardwood, acc,username))

def getRooms(dorm,roomType,nuts,pets,hardwood,acc):
	print 'in getRooms'
	curs = cursor()
        curs.execute('select * from room where dorm=%s and room_type=%s and nuts=%s and hardwood=%s and pets=%s and acc=%s and available=%s',(dorm,roomType,nuts,pets,hardwood,acc,'1'))
	row = curs.fetchall()
	return row
