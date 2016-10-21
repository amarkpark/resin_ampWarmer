import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return os.getenv('TFTD', 'Purple Unicorns RULE THE WORLD!!!')

@app.route('/on')
def on():
	return "Warmer ON"

@app.route('/off')
def off():
	return "Warmer OFF"

@app.route('/whoami')
def whoami():
	return os.getenv('DEVID', 'Please set a device ID')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)