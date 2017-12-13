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
	curs = cursor()
	curs.execute('insert into student(username, nm) values (%s,%s)', (username,nm,))
	print 'Done inserting new student user'

def updateStud(dorm,roomType,roomMates,blockMates,nuts,pets,carpet,accessible):
	curs = cursor()

def getRooms(dorm,roomType,roomMates,blockMates,nuts,pets,carpet,accessible):
	print 'wow'

#gets infomration from the forms to call other functions
def formInfo(rankings,roomType,roomMates,blockMates,nuts,pets,carpet,accessible):
	updateStud(rankings,roomType,nuts,pets,carpet,accessible);
	getRooms(rankings,roomType,nuts,pets,carpet,accessible);
