#!/usr/bin/env python
#
# SMS recording web service
# Receive and log encrypted SMS messages from phone clients
# adding comment for proxy test

import webbrowser
from flask import Flask, app, request, render_template, redirect, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

logging.basicConfig(format='localhost - - [%(asctime)s] %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

connection = pymongo.Connection()
db = connection["sms_messages"]
collection = db['sms_messages']

@app.route('/login', methods=['POST'])
def login():
	username = request['user']
	password = request['passwd']

@app.route('/login', methods=['GET'])
def loginpage():
	return render_template('login.html')

@app.route('/logout')
def logout():
	pass

@app.route('/register', methods=['GET'])
def registerpage():
	return render_template('register.html')

@app.route('/register', methods=['POST'])
def adduser():
	new_user = request.form['username']
	new_passwd = request.form['password']
	new_email = request.form['email']

@app.route('/')
@app.route('/all')
def index():
	posts = collection.find()

	if posts:
		return render_template('show_messages.html', rows=posts)
	return HTTPError(404, "Page not found")

# @app.route('/new', methods=['GET'])
# def newrecord():
# 	return render_template('new_record.html')

# @app.route('/new', methods=['POST'])	
# def addrecord():
# 	new_post = {
# 		"date" : request.form['newdate'],
# 		"time" : request.form['newtime'],
# 		"sender" : request.form['newsender'],
# 		"number" : request.form['newnumber'],
# 		"message" : request.form['newmessage'],
# 	}

# 	collection.insert(new_post)
# 	return redirect('/all')

@app.route('/delete/<number>')
def remove(number):
	collection.remove({'_id': ObjectId(number)})
	return redirect('/all')

@app.route('/date/<date>', methods=['GET'])
def bydate(date):
	docs = collection.find({"date": date})
	return render_template('bydate.html', date=date, docs=docs)

@app.route('/number/<number>', methods=['GET'])
def bynumber(number):
	rows = db.sms_messages.find({"number": number})
	return render_template('bynumber.html', number=number, rows=rows)

@app.route('/sender/<sender>', methods=['GET'])
def bysender(sender):
	rows = db.sms_messages.find({"sender": sender})
	return render_template('bysender.html', sender=sender, rows=rows)

@app.route('/api', methods=['POST'])
def api():
	try:
		new_post = {
			"api_key" : request.form['apikey'],
			"date" : request.form['date'],
			"time" : request.form['time'],
			"sender" : request.form['sender'],
			"number" : request.form['number'],
			"message" : request.form['message']
		}
		
		val = collection.insert(new_post)
		if isinstance(val, ObjectId):
			return jsonify(action="Success")
		else:
			return jsonify(action="Error")
	except(KeyError):
		return "Invalid request"

if __name__ == '__main__':
	app.run(debug=True)
