from flask import Flask, session
import os

app=Flask(__name__)
app.secret_key=os.urandom(24)

@app.route('/')
def index():
	return "Root route for sesh example"

@app.route('/session/write/<name>/')
def write(name=None):
	session['name'] = name
	return "Wrote %s into 'name' key of session" % name

@app.route('/session/read/')
def read():
	try:
		if(session['name']):
			return str(session['name'])
	except KeyError:
            pass
	return "No session var set for 'name key"

@app.route('/session/remove/')
def remove():
	session.pop('name',None)
	return "Removed key 'name from sesh"

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
