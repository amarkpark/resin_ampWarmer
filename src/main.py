from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Purple Unicorns RULE THE WORLD!!!"

@app.route('/on')
def on():
	return "Warmer ON"

@app.route('/off')
def off():
	return "Warmer OFF"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
