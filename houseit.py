import dbconn2
import MySQLdb
import os
import sys
from flask import (Flask, render_template, make_response,
                    url_for, request, flash, redirect)


DATABASE = 'dtosca_db'

#Establish the connection with the database
def cursor(database=DATABASE):
	DSN = dbconn2.read_cnf()
	DSN['db'] = database
	conn = dbconn2.connect(DSN)
	return conn.cursor(MySQLdb.cursors.DictCursor)



#Query that returns a specific movie by checking for matching tt in database
#def getMovie(tt):
#	''' Returns picked movie'''
#	curs = cursor()
#	curs.execute('select * from movie where tt=%s', (tt,))
#	row = curs.fetchone()
#	print 'Calling getMovie'
#	return row




