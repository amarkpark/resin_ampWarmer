from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	print("Purple Unicorns RULE THE WORLD!!! \n")
    return "<a href='/on'>Turn Warmer ON</a> or <a href='/off'>Turn Warmer OFF</a>"

@app.route('/on')
def get_on():
	return "Warmer ON <a href='/off'>Turn Warmer OFF</a> <a href='/''>Return to Main</a>"

@app.route('/off')
def get_off():
	return "Warmer OFF <a href='/on'>Turn Warmer ON</a> <a href='/''>Return to Main</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
