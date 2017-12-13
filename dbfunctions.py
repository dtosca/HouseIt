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

def insertStud(username,nm):
	print 'In insertStud'
        curs = cursor()
        curs.execute('insert into student(username, nm) values (%s,%s)', (username,nm,))
        print 'Done inserting new student user'

def updateStud(dorm,roomType,roomMates,blockMates,nuts,pets,hardwood,accessible):
	print 'In updateStud'
        curs = cursor()
curs.execute('UPDATE student SET dorm=%s, room_type=%s, nuts=%s, pets=%s, hardwood=%s, acc=%s', (dorm, roomType, nuts, pets, hardwood, acc))

def getRooms(dorm,roomType,roomMates,blockMates,nuts,pets,hardwood,accessible):
	print 'in getRooms'
	curs = cursor()
        curs.execute('select * from room where dorm=%s and roomType=%s and nuts=% and hardwood=%s and pets_okay=%s and acc=%s and available=true',(dorm,roomType,nuts,pets,hardwood,acc))
row = curs.fetchall()
        return row
#gets infomration from the forms to call other functions               
def formInfo(rankings,roomType,roomMates,blockMates,nuts,pets,hardwood,accessible):
        updateStud(rankings,roomType,nuts,pets,hardwood,accessible)
        getRooms(rankings,roomType,nuts,pets,hardwood,accessible)
