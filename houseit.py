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

def updatePref():
        curs = cursor()
        curs.execute()
