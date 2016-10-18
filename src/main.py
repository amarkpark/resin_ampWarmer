from flask import Flask, url_for
app = Flask(__name__)

# Grab the contents of a file
f = open('./status.txt', 'rU')
status = f.read()
f.close()

@app.route('/')
def index():
	print url_for('on')
	print url_for('off')
	return status

@app.route('/on')
def on():
	return "Warmer ON"

@app.route('/off')
def off():
	return "Warmer OFF"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)