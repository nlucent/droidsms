#! /usr/bin/env python

import sys
import urllib
import android
from datetime import datetime


def main():
	serverurl = ''
	droid = android.Android()

	new_message = {}

	try:
		new_message['sender'] = droid.getIntent().result[u'extras'][u'%SMSRN']
	except:
		droid.makeToast('Sender is missing')
		sys.exit(1)

	try:
		new_message['number'] = droid.getIntent().result[u'extras'][u'%SMSRF']
		# droid.makeToast(number)
	except:
		droid.makeToast('Number is missing')
		sys.exit(1)

	try:
		new_message['message'] = droid.getIntent().result[u'extras'][u'%SMSRB']
		# droid.makeToast(message)
	except:
		droid.makeToast("Message is missing")
		sys.exit(1)

	try:
		new_message['date'] = droid.getIntent().result[u'extras'][u'%SMSRD']
		# droid.makeToast(date)
	except:
		droid.makeToast("Date is missing")
		sys.exit(1)

	try:
		new_message['time'] = droid.getIntent().result[u'extras'][u'%SMSRT']
		# droid.makeToast(time)
	except:
		droid.makeToast("Time is missing")
		sys.exit(1)

	try:
		new_message['apikey'] = droid.getIntent().result[u'extras'][u'%APIKEY']
		# droid.makeToast(apikey)
	except:
		droid.makeToast("APIKEY is missing")
		sys.exit(1)

	new_message = urllib.urlencode(new_message)
	f = urllib.urlopen(serverurl, new_message)

	if 'Success' in f.read():
		droid.makeToast("Success")
	else:
		droid.makeToast("Sms2Server Error")


if __name__ == '__main__':
	main()



