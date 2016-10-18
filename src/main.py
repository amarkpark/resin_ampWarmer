import sys
import os
from flask import Flask, url_for
app = Flask(__name__)
# app.config['WORKDIR'] = WORKDIR

# ALLOWED_EXTENSIONS = set('txt')

# # Grab the contents of a file
# def get_status(filename)
# 	with open(WORKDIR/filename, 'rU') as f:
# 		status = f.read()
# 		f.close()	

@app.route('/')
def index():
	print url_for('on')
	print url_for('off')
	return url_for('static', filename='status.txt')

@app.route('/on')
def on():
	return "Warmer ON"

@app.route('/off')
def off():
	return "Warmer OFF"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)